#!/usr/bin/env python3
import os
import threading
import tempfile
import subprocess

from flask import Flask, request, jsonify, render_template

import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt8MultiArray, String


class PhoneAudioBridgeNode(Node):
    def __init__(self):
        super().__init__("phone_audio_bridge_node")

        # =========================================================
        # Parameters
        # =========================================================
        self.declare_parameter("audio_topic", "/phone/audio_raw")
        self.declare_parameter("event_topic", "/gui_control/gui_event")
        self.declare_parameter("host", "0.0.0.0")
        self.declare_parameter("port", 5050)
        self.declare_parameter("debug", True)

        # HTTPS cert paths (optional)
        self.declare_parameter("cert_path", os.path.expanduser("~/ur5_ws/certs/cert.pem"))
        self.declare_parameter("key_path", os.path.expanduser("~/ur5_ws/certs/key.pem"))

        self.audio_topic = str(self.get_parameter("audio_topic").value)
        self.event_topic = str(self.get_parameter("event_topic").value)
        self.host = str(self.get_parameter("host").value)
        self.port = int(self.get_parameter("port").value)
        self.debug = bool(self.get_parameter("debug").value)

        self.cert_path = str(self.get_parameter("cert_path").value)
        self.key_path = str(self.get_parameter("key_path").value)

        # =========================================================
        # ROS publishers
        # =========================================================
        self.audio_pub = self.create_publisher(UInt8MultiArray, self.audio_topic, 10)
        self.event_pub = self.create_publisher(String, self.event_topic, 10)

        # =========================================================
        # Flask app + template directory detection
        # =========================================================
        pkg_dir = os.path.dirname(os.path.abspath(__file__))

        # source layout:
        #   src/phone_audio_bridge/phone_audio_bridge/phone_audio_bridge_node.py
        #   src/phone_audio_bridge/templates/index.html
        src_template_dir = os.path.abspath(os.path.join(pkg_dir, "..", "templates"))

        # install layout (ament_python + --symlink-install may vary)
        install_candidate_1 = os.path.abspath(
            os.path.join(pkg_dir, "..", "..", "..", "..", "share", "phone_audio_bridge", "templates")
        )

        # build layout (during dev, symlink-install sometimes resolves here)
        build_candidate = os.path.abspath(
            os.path.join(pkg_dir, "..", "..", "templates")
        )

        template_dir = None
        for d in [src_template_dir, install_candidate_1, build_candidate]:
            if os.path.exists(os.path.join(d, "index.html")):
                template_dir = d
                break

        if template_dir is None:
            template_dir = src_template_dir

        self.app = Flask(__name__, template_folder=template_dir)
        self._setup_routes()

        self.get_logger().info(f"Phone Audio Bridge ready | template_dir={template_dir}")
        self.get_logger().info(f"Audio publish topic = {self.audio_topic}")
        self.get_logger().info(f"Event publish topic = {self.event_topic}")
        self.get_logger().info(f"HTTPS cert = {self.cert_path}")
        self.get_logger().info(f"HTTPS key  = {self.key_path}")

    # =========================================================
    # Flask routes
    # =========================================================
    def _setup_routes(self):
        app = self.app

        @app.route("/", methods=["GET"])
        def index():
            return render_template("index.html")

        @app.route("/health", methods=["GET"])
        def health():
            return "ok", 200

        @app.route("/api/send_cmd", methods=["POST"])
        def send_cmd():
            data = request.get_json(silent=True) or {}
            cmd = str(data.get("cmd", "")).strip()

            if not cmd:
                return jsonify({"ok": False, "error": "empty cmd"}), 400

            try:
                msg = String()
                msg.data = cmd
                self.event_pub.publish(msg)

                if self.debug:
                    self.get_logger().info(f"CMD -> {self.event_topic}: {cmd}")

                return jsonify({"ok": True, "sent": cmd})

            except Exception as e:
                self.get_logger().error(f"/api/send_cmd failed: {e}")
                return jsonify({"ok": False, "error": str(e)}), 500

        @app.route("/api/audio_chunk", methods=["POST"])
        def audio_chunk():
            """
            รับ audio chunk เป็น webm/mp4 จาก browser (MediaRecorder)
            แล้วแปลงเป็น raw PCM s16le, 16kHz, mono
            จากนั้น publish เป็น UInt8MultiArray
            """
            raw_bytes = request.get_data()

            if not raw_bytes:
                return jsonify({"ok": False, "error": "empty audio"}), 400

            try:
                pcm_bytes = self._convert_media_to_pcm(raw_bytes)

                if not pcm_bytes:
                    return jsonify({"ok": False, "error": "ffmpeg returned empty pcm"}), 500

                msg = UInt8MultiArray()
                msg.data = list(pcm_bytes)
                self.audio_pub.publish(msg)

                if self.debug:
                    self.get_logger().info(
                        f"MEDIA -> {self.audio_topic}: input={len(raw_bytes)} bytes | pcm={len(pcm_bytes)} bytes"
                    )

                return jsonify({
                    "ok": True,
                    "input_bytes": len(raw_bytes),
                    "pcm_bytes": len(pcm_bytes)
                })

            except Exception as e:
                self.get_logger().error(f"/api/audio_chunk failed: {e}")
                return jsonify({"ok": False, "error": str(e)}), 500

        @app.route("/api/audio_chunk_pcm", methods=["POST"])
        def audio_chunk_pcm():
            """
            รับ raw PCM 16-bit little-endian, mono, 16kHz จาก WebAudio fallback
            แล้ว publish ตรงเข้า ROS เลย
            """
            raw_bytes = request.get_data()

            if not raw_bytes:
                return jsonify({"ok": False, "error": "empty pcm"}), 400

            try:
                msg = UInt8MultiArray()
                msg.data = list(raw_bytes)
                self.audio_pub.publish(msg)

                if self.debug:
                    self.get_logger().info(f"PCM -> {self.audio_topic}: {len(raw_bytes)} bytes")

                return jsonify({
                    "ok": True,
                    "pcm_bytes": len(raw_bytes)
                })

            except Exception as e:
                self.get_logger().error(f"/api/audio_chunk_pcm failed: {e}")
                return jsonify({"ok": False, "error": str(e)}), 500

    # =========================================================
    # Convert media bytes (webm/mp4/etc) -> PCM s16le 16k mono
    # =========================================================
    def _convert_media_to_pcm(self, media_bytes: bytes) -> bytes:
        """
        ใช้ ffmpeg แปลง media container จาก browser เป็น:
          - pcm_s16le
          - mono
          - 16kHz
        """
        with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as fin:
            fin.write(media_bytes)
            in_path = fin.name

        with tempfile.NamedTemporaryFile(suffix=".pcm", delete=False) as fout:
            out_path = fout.name

        try:
            cmd = [
                "ffmpeg",
                "-y",
                "-i", in_path,
                "-f", "s16le",
                "-acodec", "pcm_s16le",
                "-ac", "1",
                "-ar", "16000",
                out_path
            ]

            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )

            with open(out_path, "rb") as f:
                pcm = f.read()

            return pcm

        except subprocess.CalledProcessError as e:
            stderr = ""
            try:
                stderr = e.stderr.decode("utf-8", errors="ignore")
            except Exception:
                pass

            raise RuntimeError(f"ffmpeg failed: {stderr[:1000]}")

        finally:
            try:
                os.remove(in_path)
            except Exception:
                pass
            try:
                os.remove(out_path)
            except Exception:
                pass

    # =========================================================
    # Run
    # =========================================================
    def run(self):
        # ROS spin in background thread
        spin_thread = threading.Thread(target=self._spin_ros, daemon=True)
        spin_thread.start()

        ssl_context = None
        if os.path.exists(self.cert_path) and os.path.exists(self.key_path):
            ssl_context = (self.cert_path, self.key_path)
            self.get_logger().info(f"HTTPS enabled | cert={self.cert_path}")
        else:
            self.get_logger().warning(
                "HTTPS cert/key not found -> fallback to HTTP (mobile mic may not work)"
            )

        self.app.run(
            host=self.host,
            port=self.port,
            debug=False,
            use_reloader=False,
            ssl_context=ssl_context
        )

    def _spin_ros(self):
        while rclpy.ok():
            rclpy.spin_once(self, timeout_sec=0.1)


def main(args=None):
    rclpy.init(args=args)
    node = PhoneAudioBridgeNode()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        try:
            rclpy.shutdown()
        except Exception:
            pass


if __name__ == "__main__":
    main()