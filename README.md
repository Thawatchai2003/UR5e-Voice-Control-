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

### Zimmer_HRC_03_configured

A pre-configured ROS2 package for integrating and operating the Zimmer HRC gripper within a robotic system environment.

#### Description

The `Zimmer_HRC_03_configured` package provides a ready-to-use configuration for the Zimmer HRC gripper. It contains predefined parameters, communication settings, launch files, and integration resources required for seamless deployment with ROS2-based robotic applications.

#### Features

* Pre-configured Zimmer HRC gripper setup
* ROS2-compatible package structure
* Ready-to-use launch configurations
* Gripper communication and control support
* Integration with Universal Robots (UR series)
* Simplified deployment and testing workflow

#### Purpose

This package reduces the setup time required for Zimmer HRC gripper integration by providing a validated configuration environment. It is designed to work alongside robot control packages and enables reliable gripper operation in ROS2 applications.

