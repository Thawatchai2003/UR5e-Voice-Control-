# UR5e Voice Control

Voice-controlled system for controlling the UR5e collaborative robot using ROS2, MoveIt2, and Speech Recognition.

---

# System Requirements

Before starting the installation, make sure the following software and tools are installed on your system.

- Ubuntu 22.04
- ROS2 Humble
- Python 3
- MoveIt2
- UR5e Robot

---

# Prerequisites Installation

## 1. Update Ubuntu Packages

Update and upgrade all Ubuntu packages before installation.

### Command
```bash
sudo apt update
sudo apt upgrade -y
```

### Description
- `sudo` : Execute command with administrator privileges
- `apt update` : Update package lists
- `apt upgrade` : Upgrade installed packages
- `-y` : Automatically confirm installation

---

## 2. Install Python3 and pip

Install Python3 and pip package manager.

### Command
```bash
sudo apt install python3 python3-pip -y
```

### Description
- `python3` : Python programming language
- `python3-pip` : Python package manager
- `-y` : Automatically confirm installation

---

## 3. Install Colcon Build Tool

Install colcon build tools for ROS2 workspace compilation.

### Command
```bash
sudo apt install python3-colcon-common-extensions -y
```

### Description
- `python3-colcon-common-extensions` : ROS2 build tool extensions

---

## 4. Install Git

Install Git for cloning repositories from GitHub.

### Command
```bash
sudo apt install git -y
```

### Description
- `git` : Version control system for downloading repositories

---

## 5. Install ROS2 Humble

Install ROS2 Humble Desktop version.

### Command
```bash
sudo apt install ros-humble-desktop -y
```

### Description
- `ros-humble-desktop` : Full ROS2 Humble desktop installation

---

## 6. Source ROS2 Environment

Load the ROS2 environment setup.

### Command
```bash
source /opt/ros/humble/setup.bash
```

### Description
- `source` : Load environment variables
- `/opt/ros/humble/setup.bash` : ROS2 Humble setup file

---

## 7. Add ROS2 Environment Automatically

Automatically source ROS2 setup when opening terminal.

### Command
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### Description
- `echo` : Write command into `.bashrc`
- `>>` : Append text to file
- `~/.bashrc` : Bash configuration file
- `source ~/.bashrc` : Reload bash configuration

---

# Workspace Installation

## 1. Create a ROS2 Workspace

Create a ROS2 workspace for the UR5e Voice Control project.

### Command
```bash
mkdir -p UR5e_ws/src
```

### Description
- `mkdir` : Create a new folder
- `-p` : Create nested folders automatically
- `~/UR5e_ws/src` : Workspace and source folder location
  
---

## 2. Clone Repository into Source Folder

Move to the source folder and clone the required Zimmer_HRC_03 repositories from GitHub.

### Command
```bash
cd ur5e_ws/src

git clone https://github.com/Thawatchai2003/Zimmer_HRC_03.git

git clone https://github.com/Thawatchai2003/Zimmer_HRC_03_configured.git
```

### Description
- `cd ur5e_ws/src` : Move to the ROS2 source folder
- `git clone` : Download repository from GitHub
- `Zimmer_HRC_03.git` : ROS2 package repository for Zimmer HRC gripper control
- `Zimmer_HRC_03_configured.git` : Configured ROS2 package for Zimmer HRC system setup

## 3. Create UR5e Control Package

Create a ROS2 Python package named `UR5e_Control` inside the workspace source folder.

### Command

```bash
cd ~/UR5e_ws/src

ros2 pkg create --build-type ament_python UR5e_Control
```

### Description

- `cd ~/UR5e_ws/src` : Move to the ROS2 source folder
- `ros2 pkg create` : Create a new ROS2 package
- `--build-type ament_python` : Create a Python-based ROS2 package
- `UR5e_Control` : Package name for the UR5e Voice Control system

### Expected Directory Structure

```text
UR5e_ws/
└── src/
    └── UR5e_Control/
        ├── package.xml
        ├── setup.py
        ├── setup.cfg
        ├── resource/
        │   └── UR5e_Control
        ├── test/
        └── UR5e_Control/
            └── __init__.py
```

### Purpose

The `UR5e_Control` package serves as the main ROS2 package for the UR5e Voice Control system. It contains voice processing nodes, robot control nodes, gripper interfaces, launch files, configuration files, and graphical monitoring tools.

## 4. Replace the Generated Package with the Repository Version

Replace the default ROS2 package template with the official UR5e Control repository.

### Command

```bash
cd ~/UR5e_ws/src

rm -rf UR5e_Control

git clone https://github.com/Thawatchai2003/Ur5e_Control.git UR5e_Control
```

### Description

* `cd ~/UR5e_ws/src` : Navigate to the ROS2 workspace source directory.
* `rm -rf UR5e_Control` : Remove the previously generated package template.
* `git clone` : Clone the repository from GitHub.
* `Ur5e_Control.git` : Repository containing the complete UR5e Voice Control System.
* `UR5e_Control` : Local package directory name inside the workspace.

### Expected Directory Structure

```text
UR5e_ws/
└── src/
    ├── Zimmer_HRC_03/
    ├── Zimmer_HRC_03_configured/
    └── UR5e_Control/
        ├── package.xml
        ├── setup.py
        ├── setup.cfg
        ├── config/
        ├── launch/
        ├── resource/
        └── UR5e_Control/
```

### Purpose

The UR5e Control repository provides the complete implementation of the voice-controlled robotic manipulation framework. It includes speech processing, command interpretation, robot motion control, gripper integration, graphical monitoring tools, and system configuration files required for operating a UR5e robot within a ROS2 environment.

## 5. Replace Launch Files

Remove the default launch directory and replace it with the latest launch configuration from the GitHub repository.

### Command

```bash
cd ~/UR5e_ws/src/UR5e_Control

rm -rf launch

git clone https://github.com/Thawatchai2003/launch.git launch
```

### Description

* `cd ~/UR5e_ws/src/UR5e_Control` : Navigate to the UR5e Control package directory.
* `rm -rf launch` : Remove the existing launch directory.
* `git clone` : Clone the repository from GitHub.
* `launch.git` : Repository containing the launch files for the UR5e Voice Control System.
* `launch` : Clone the repository using `launch` as the local directory name.

### Expected Directory Structure

```text
UR5e_ws/
└── src/
    └── UR5e_Control/
        ├── package.xml
        ├── setup.py
        ├── setup.cfg
        ├── config/
        ├── launch/
        │   ├── ur5_real.launch.py
        │   └── ...
        ├── resource/
        └── UR5e_Control/
```

### Purpose

This step installs the latest launch files required to start and manage the UR5e Voice Control System. These launch files define how ROS2 nodes, robot drivers, gripper interfaces, speech processing modules, and monitoring tools are initialized and executed within the system.

## 6. Configure Initial Joint Positions

Create the initial joint position configuration file for the UR5e robot.

### Command

```bash
cd ~/UR5e_ws/src/UR5e_Control/config

nano initial_positions.yaml
```

### Description

* `cd ~/UR5e_ws/src/UR5e_Control/config` : Navigate to the configuration directory.
* `nano initial_positions.yaml` : Create and edit the initial joint position configuration file.

### File Content

Paste the following joint values into `initial_positions.yaml`:

```yaml
shoulder_pan_joint: 0.0
shoulder_lift_joint: -1.57
elbow_joint: 0.0
wrist_1_joint: -1.57
wrist_2_joint: 0.0
wrist_3_joint: 0.0
```

### Purpose

This configuration file defines the default joint positions of the UR5e robot at startup. These values are commonly used as an initial home position for robot initialization, motion planning, and testing.

## 7. Configure UR5e Executor Parameters

Create the executor parameter configuration file for the UR5e Control System.

### Command

```bash
cd ~/UR5e_ws/src/UR5e_Control/config

nano ur5e_executor_params.yaml
```

### Description

* `cd ~/UR5e_ws/src/UR5e_Control/config` : Navigate to the configuration directory.
* `nano ur5e_executor_params.yaml` : Create and edit the UR5e executor parameter file.

### File Content

Paste the following configuration into `ur5e_executor_params.yaml`:

```yaml
ur5e_executor_node:
  ros__parameters:
    speed_mode: "normal"
```

### Purpose

This configuration file defines runtime parameters for the `ur5e_executor_node`. The `speed_mode` parameter controls the robot execution behavior and can be adjusted depending on the application requirements.

### Parameter Description

| Parameter    | Value      | Description                                           |
| ------------ | ---------- | ----------------------------------------------------- |
| `speed_mode` | `"normal"` | Execute robot motions at the default operating speed. |

### Expected Directory Structure

```text
UR5e_ws/
└── src/
    └── UR5e_Control/
        ├── config/
        │   ├── initial_positions.yaml
        │   └── ur5e_executor_params.yaml
        ├── launch/
        ├── resource/
        ├── package.xml
        ├── setup.py
        └── setup.cfg
```
## 8. Configure Package Installation

Update the `setup.py` file to register all ROS2 nodes, launch files, and configuration files required by the UR5e Voice Control System.

### File

```text
UR5e_ws/
└── src/
    └── UR5e_Control/
        └── setup.py
```

### setup.py

```python
from glob import glob
from setuptools import setup

package_name = 'UR5e_Control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],

    # Install shared files (ROS2)
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        (
            'share/' + package_name,
            ['package.xml']
        ),

        (
            'share/' + package_name + '/launch',
            glob('launch/*.launch.py')
        ),

        (
            'share/' + package_name + '/config',
            [
                'config/initial_positions.yaml',
                'config/ur5e_executor_params.yaml',
            ]
        ),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='thawatchai',
    maintainer_email='example@example.com',
    description='UR5e Voice Control System',
    license='Apache License 2.0',
    tests_require=['pytest'],

    entry_points={
        'console_scripts': [

            # Speech & Voice
            'speech_to_text_node = UR5e_Control.speech_to_text_node:main',
            'tts_node_gtts = UR5e_Control.tts_node_gtts:main',
            'speech_gui_node = UR5e_Control.speech_gui_node:main',
            'nlu_parser_node = UR5e_Control.nlu_parser_node:main',
            'beep_node = UR5e_Control.beep_node:main',
            'voice_logger_node = UR5e_Control.voice_logger_node:main',
            'dialog_fsm_node = UR5e_Control.dialog_fsm_node:main',
            'audio_monitor_gui = UR5e_Control.audio_monitor_gui:main',

            # UR5e Control
            'ur5_cmd_mapper_node = UR5e_Control.ur5_cmd_mapper_node:main',
            'control_position_node = UR5e_Control.control_position_node:main',
            'ur5_executor_node = UR5e_Control.ur5_executor_node:main',
            'gripper_bridge_node = UR5e_Control.gripper_bridge_node:main',
            'audio_receiver_node = UR5e_Control.audio_receiver_node:main',
        ],
    },
)
```

### Purpose

The `setup.py` file defines how the UR5e Control package is installed within ROS2. It registers launch files, configuration files, and executable nodes, allowing them to be discovered and executed after building the workspace.

### Registered Configuration Files

```text
config/
├── initial_positions.yaml
└── ur5e_executor_params.yaml
```

### Registered ROS2 Nodes

* speech_to_text_node
* tts_node_gtts
* speech_gui_node
* nlu_parser_node
* beep_node
* voice_logger_node
* dialog_fsm_node
* audio_monitor_gui
* ur5_cmd_mapper_node
* control_position_node
* ur5_executor_node
* gripper_bridge_node
* audio_receiver_node

```
```
### Purpose

This file ensures that all components of the UR5e Voice Control System are properly installed and accessible within ROS2 after building the workspace with `colcon build`.

## 9. Create ReSpeaker Microphone Array Package

Create a ROS2 package for integrating and managing the ReSpeaker Microphone Array.

### Command

```bash
cd ~/UR5e_ws/src

ros2 pkg create --build-type ament_python Respeaker_mic_array
```

### Description

* `cd ~/UR5e_ws/src` : Move to the ROS2 source folder.
* `ros2 pkg create` : Create a new ROS2 package.
* `--build-type ament_python` : Create a Python-based ROS2 package.
* `Respeaker_mic_array` : Package name for ReSpeaker microphone array integration.

### Expected Directory Structure

```text
UR5e_ws/
└── src/
    ├── Zimmer_HRC_03/
    ├── Zimmer_HRC_03_configured/
    ├── UR5e_Control/
    └── Respeaker_mic_array/
        ├── package.xml
        ├── setup.py
        ├── setup.cfg
        ├── resource/
        │   └── Respeaker_mic_array
        ├── test/
        └── Respeaker_mic_array/
            └── __init__.py
```

### Purpose

The `Respeaker_mic_array` package provides the software framework for integrating the ReSpeaker Microphone Array with ROS2. It is responsible for audio acquisition, microphone array management, voice activity detection, and audio streaming for speech recognition systems.

## 10. Replace the Generated ReSpeaker Package with the Repository Version

Remove the automatically generated package and replace it with the latest ReSpeaker Microphone Array source code from the GitHub repository.

### Command

```bash
cd ~/UR5e_ws/src/Respeaker_mic_array

rm -rf Respeaker_mic_array

git clone https://github.com/Thawatchai2003/Respeaker_mic_array.git
```

### Description

* `cd ~/UR5e_ws/src/Respeaker_mic_array` : Move to the ReSpeaker package directory.
* `rm -rf Respeaker_mic_array` : Remove the previously generated Python package directory.
* `git clone` : Download the repository from GitHub.
* `Respeaker_mic_array.git` : Repository containing the ReSpeaker Microphone Array source code.

### Expected Directory Structure

```text
UR5e_ws/
└── src/
    └── Respeaker_mic_array/
        ├── package.xml
        ├── setup.py
        ├── setup.cfg
        ├── config/
        ├── launch/
        ├── resource/
        └── Respeaker_mic_array/
```

### Purpose

This step replaces the default ROS2 package template with the complete ReSpeaker Microphone Array implementation from the GitHub repository. The package provides audio acquisition, microphone array management, voice activity detection, and audio streaming capabilities for speech recognition and voice-controlled robotic applications.

## 11. Create ReSpeaker Launch File

Create a launch file for starting the ReSpeaker microphone array nodes and audio processing pipeline.

### Command

```bash
cd ~/UR5e_ws/src/Respeaker_mic_array/launch

nano respeaker.launch.py
```

### Description

* `cd ~/UR5e_ws/src/Respeaker_mic_array/launch` : Move to the launch directory.
* `nano respeaker.launch.py` : Create and edit the ReSpeaker launch file.

### File Content

Paste the following code into `respeaker.launch.py`:

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='respeaker_mic_array',
            executable='audio_node',
            name='audio_node',
            output='screen'
        ),

        Node(
            package='respeaker_mic_array',
            executable='graph_node',
            name='graph_node',
            output='screen'
        ),

        Node(
            package='respeaker_mic_array',
            executable='audio_listener_node',
            name='audio_listener_node',
            output='screen',
            parameters=[{
                "sample_rate": 16000,
                "chunk_size": 1024,
                "use_channel": 0,
                "debug_log": True,

                "mode": 2,
                "auto_scan_interval_sec": 0.5,
                "auto_switch_threshold_rms": 300.0,
                "switch_margin_ratio": 1.15,
                "normalize_output": False,
            }]
        ),
    ])
```

### Purpose

This launch file starts all core nodes required for the ReSpeaker Microphone Array system. It initializes audio acquisition, audio visualization, and audio monitoring components used by the voice-controlled robotic platform.

### Launched Nodes

| Node                  | Description                                                                |
| --------------------- | -------------------------------------------------------------------------- |
| `audio_node`          | Captures audio data from the ReSpeaker microphone array.                   |
| `graph_node`          | Displays real-time audio visualization and monitoring information.         |
| `audio_listener_node` | Processes incoming audio streams and manages microphone channel selection. |

### Usage

```bash
ros2 launch Respeaker_mic_array respeaker.launch.py
```

### Notes

* The audio sample rate is configured to 16 kHz.
* Audio is processed in chunks of 1024 samples.
* Channel 0 is selected by default.
* Automatic microphone monitoring and channel management are enabled.
* Debug logging is enabled for troubleshooting and system verification.

## 12. Configure Package Installation

Create the `setup.py` file for the ReSpeaker Microphone Array package.

### Command

```bash
cd ~/UR5e_ws/src/Respeaker_mic_array

nano setup.py
```

### Description

* `cd ~/UR5e_ws/src/Respeaker_mic_array` : Move to the package root directory.
* `nano setup.py` : Create and edit the package installation script.

### File Content

Paste the following code into `setup.py`:

```python
from setuptools import setup, find_packages

package_name = 'respeaker_mic_array'

### setup.py

```python
from setuptools import setup, find_packages

package_name = 'respeaker_mic_array'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            'share/' + package_name + '/launch',
            ['launch/respeaker.launch.py']
        ),
    ],

    package_data={
        package_name: [
            'usb_4_mic_array/*.bin',
            'usb_4_mic_array/*.cfg',
        ],
    },

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='thawatchai',
    maintainer_email='thawatchai@todo.todo',
    description='ReSpeaker USB 4-Mic Array ROS2 Driver',
    license='MIT',

    entry_points={
        'console_scripts': [
            'doa_node = respeaker_mic_array.doa_node:main',
            'vad_node = respeaker_mic_array.vad_node:main',
            'audio_node = respeaker_mic_array.audio_node:main',
            'full_dsp_tuning_node = respeaker_mic_array.full_dsp_tuning_node:main',
            'graph_node = respeaker_mic_array.graph_node:main',
            'audio_listener_node = respeaker_mic_array.audio_listener_node:main',
            'google_stt = respeaker_mic_array.google_stt_node:main',
        ],
    },
)
```

### Purpose

The `setup.py` file defines how the ReSpeaker Microphone Array package is installed and registered within the ROS2 environment. It installs launch files, DSP resources, and registers executable nodes for audio capture, voice activity detection, direction-of-arrival estimation, and speech recognition.

```

### Purpose

The `setup.py` file defines how the ReSpeaker Microphone Array package is installed and registered within the ROS2 environment. It installs launch files, DSP configuration resources, and registers executable ROS2 nodes used for audio acquisition, voice activity detection, speech recognition, and microphone array processing.

### Registered Launch Files

```text
launch/
└── respeaker.launch.py
```

### Included DSP Resources

```text
usb_4_mic_array/
├── *.bin
└── *.cfg
```

### Registered ROS2 Nodes

#### Audio Processing

* `audio_node`
* `audio_listener_node`
* `graph_node`

#### Microphone Array Processing

* `doa_node`
* `vad_node`
* `full_dsp_tuning_node`

#### Speech Recognition

* `google_stt`

### Purpose of Each Node

| Node                   | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| `audio_node`           | Captures audio from the ReSpeaker microphone array.                   |
| `audio_listener_node`  | Receives and processes audio streams.                                 |
| `graph_node`           | Displays real-time audio monitoring data.                             |
| `doa_node`             | Estimates the Direction of Arrival (DOA) of sound sources.            |
| `vad_node`             | Performs Voice Activity Detection (VAD).                              |
| `full_dsp_tuning_node` | Configures and tunes DSP parameters of the microphone array.          |
| `google_stt`           | Converts speech audio into text using Google Speech-to-Text services. |

## 13. Configure DSP Parameters

Create the DSP configuration file for the ReSpeaker Microphone Array.

### Command

```bash
cd ~/UR5e_ws/src/Respeaker_mic_array/config

nano dsp_params.yaml
```

### Description

* `cd ~/UR5e_ws/src/Respeaker_mic_array/config` : Move to the configuration directory.
* `nano dsp_params.yaml` : Create and edit the DSP parameter configuration file.

### File Content

Paste the following configuration into `dsp_params.yaml`:

```yaml
graph_node:
  ros__parameters:

    # ===== CORE =====
    AGCONOFF: 1
    ECHOONOFF: 1
    STATNOISEONOFF: 1
    NONSTATNOISEONOFF: 1
    TRANSIENTONOFF: 1
    RT60ONOFF: 1
    CNIONOFF: 1
    NLATTENONOFF: 1
    HPFONOFF: 1

    # ===== AGC =====
    AGCMAXGAIN: 20
    AGCDESIREDLEVEL: 0.02
    AGCTIME: 0.5

    # ===== NOISE =====
    GAMMA_NS: 1.5
    GAMMA_NN: 1.3
    MIN_NS: 0.15
    MIN_NN: 0.10

    # ===== ASR =====
    GAMMA_NS_SR: 1.4
    GAMMA_NN_SR: 1.4
    MIN_NS_SR: 0.20
    MIN_NN_SR: 0.20

    # ===== BEAMFORMING =====
    GAMMA_E: 1.5
    GAMMA_ETAIL: 1.3
    GAMMA_ENL: 2.0
    AECNORM: 1.0
```

### Purpose

The `dsp_params.yaml` file defines Digital Signal Processing (DSP) parameters used by the ReSpeaker microphone array. These settings control automatic gain control, echo cancellation, noise suppression, speech enhancement, and beamforming performance.

### Parameter Groups

#### Core DSP Features

* `AGCONOFF` : Automatic Gain Control (AGC)
* `ECHOONOFF` : Acoustic Echo Cancellation (AEC)
* `STATNOISEONOFF` : Stationary Noise Suppression
* `NONSTATNOISEONOFF` : Non-Stationary Noise Suppression
* `TRANSIENTONOFF` : Transient Noise Reduction
* `RT60ONOFF` : Reverberation Suppression
* `CNIONOFF` : Comfort Noise Insertion
* `NLATTENONOFF` : Non-Linear Echo Attenuation
* `HPFONOFF` : High-Pass Filter

#### Automatic Gain Control (AGC)

* `AGCMAXGAIN` : Maximum gain level
* `AGCDESIREDLEVEL` : Target output level
* `AGCTIME` : AGC response time

#### Noise Suppression

* `GAMMA_NS`
* `GAMMA_NN`
* `MIN_NS`
* `MIN_NN`

#### Speech Recognition Optimization

* `GAMMA_NS_SR`
* `GAMMA_NN_SR`
* `MIN_NS_SR`
* `MIN_NN_SR`

#### Beamforming and Echo Control

* `GAMMA_E`
* `GAMMA_ETAIL`
* `GAMMA_ENL`
* `AECNORM`

### Expected Directory Structure

```text
Respeaker_mic_array/
├── config/
│   └── dsp_params.yaml
├── launch/
├── resource/
├── package.xml
├── setup.py
└── setup.cfg
```
