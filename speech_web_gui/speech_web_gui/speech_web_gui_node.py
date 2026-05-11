#!/usr/bin/env python3
import os
import threading
import time

from flask import Flask, render_template, request, jsonify

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SpeechWebGUINode(Node):
    def __init__(self):
        super().__init__("speech_web_gui_node")

        # ---------------- Parameters ----------------
        self.declare_parameter("topic_gui_event", "/gui_control/gui_event")
        self.declare_parameter("topic_gui_cmd", "/control/gui_cmd")
        self.declare_parameter("host", "0.0.0.0")
        self.declare_parameter("port", 5000)
        self.declare_parameter("debug", True)

        self.topic_gui_event = str(self.get_parameter("topic_gui_event").value)
        self.topic_gui_cmd = str(self.get_parameter("topic_gui_cmd").value)
        self.host = str(self.get_parameter("host").value)
        self.port = int(self.get_parameter("port").value)
        self.debug = bool(self.get_parameter("debug").value)

        # ---------------- ROS pub/sub ----------------
        self.gui_event_pub = self.create_publisher(String, self.topic_gui_event, 10)
        self.gui_cmd_sub = self.create_subscription(String, self.topic_gui_cmd, self.on_gui_cmd, 10)

        # ---------------- Shared UI state ----------------
        self.state = {
            "status": "🟦 Idle",
            "result": "Text: (none yet)",
            "last": "Last: (none)",
            "show_pos": False,
            "show_scroll": False,
            "show_rotate": False,
        }
        self._lock = threading.Lock()

        # ---------------- Flask app ----------------
        # หา templates แบบ robust มากที่สุด
        pkg_dir = os.path.dirname(os.path.abspath(__file__))
        src_template_dir = os.path.abspath(os.path.join(pkg_dir, "..", "templates"))

        # fallback เผื่อ install mode
        install_template_dir = os.path.abspath(
            os.path.join(pkg_dir, "..", "..", "..", "..", "share", "speech_web_gui", "templates")
        )

        if os.path.exists(os.path.join(src_template_dir, "index.html")):
            template_dir = src_template_dir
        elif os.path.exists(os.path.join(install_template_dir, "index.html")):
            template_dir = install_template_dir
        else:
            template_dir = src_template_dir  # fallback ไว้ก่อน

        self.app = Flask(__name__, template_folder=template_dir)

        self.get_logger().info(f"Web GUI ready | template_dir={template_dir}")

        # register routes
        self._setup_routes()

    # =========================================================
    # Flask Routes
    # =========================================================
    def _setup_routes(self):
        app = self.app

        @app.route("/", methods=["GET"])
        def index():
            return render_template("index.html")

        @app.route("/health", methods=["GET"])
        def health():
            return "ok", 200

        @app.route("/api/state", methods=["GET"])
        def api_state():
            with self._lock:
                return jsonify(self.state)

        @app.route("/api/send", methods=["POST"])
        def api_send():
            data = request.get_json(silent=True) or {}
            cmd = str(data.get("cmd", "")).strip()

            if not cmd:
                return jsonify({"ok": False, "error": "empty cmd"}), 400

            self._pub_event(cmd)

            with self._lock:
                self.state["last"] = f"Last: {cmd}"
                self.state["result"] = f"Text: {cmd}"

            return jsonify({"ok": True, "sent": cmd})

    # =========================================================
    # ROS callbacks
    # =========================================================
    def _pub_event(self, s: str):
        msg = String()
        msg.data = s
        self.gui_event_pub.publish(msg)

        if self.debug:
            self.get_logger().info(f"PUB -> {self.topic_gui_event}: {s}")

    def on_gui_cmd(self, msg: String):
        data = (msg.data or "").strip()

        if self.debug:
            self.get_logger().info(f"SUB <- {self.topic_gui_cmd}: {data}")

        with self._lock:
            if data.startswith("SET_STATUS:"):
                st = data.split(":", 1)[1]
                self.state["status"] = st if st else "🟦 Idle"

            elif data.startswith("SET_RESULT:"):
                res = data.split(":", 1)[1]
                self.state["result"] = res
                self.state["last"] = f"Last: {res[:36]}{'…' if len(res) > 36 else ''}"

            elif data == "SHOW_POS":
                self.state["show_pos"] = True
            elif data == "HIDE_POS":
                self.state["show_pos"] = False

            elif data == "SHOW_SCROLL":
                self.state["show_scroll"] = True
            elif data == "HIDE_SCROLL":
                self.state["show_scroll"] = False

            elif data == "SHOW_ROTATE":
                self.state["show_rotate"] = True
            elif data == "HIDE_ROTATE":
                self.state["show_rotate"] = False

    # =========================================================
    # Run
    # =========================================================
    def run(self):
        # ROS spin in background
        spin_thread = threading.Thread(target=self._spin_ros, daemon=True)
        spin_thread.start()

        # Flask serve
        self.app.run(host=self.host, port=self.port, debug=False, use_reloader=False)

    def _spin_ros(self):
        while rclpy.ok():
            rclpy.spin_once(self, timeout_sec=0.1)


def main(args=None):
    rclpy.init(args=args)
    node = SpeechWebGUINode()
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