# UR5e Voice Control

Voice-controlled system for controlling the UR5e collaborative robot using ROS2, MoveIt2, and Speech Recognition.

---

# System Requirements

- Ubuntu 22.04
- ROS2 Humble
- Python 3 
- MoveIt2
- UR5e Robot

---

# Installation

## 1. Create a ROS2 Workspace

Create a ROS2 workspace for the project.

### Command
```bash
mkdir -p ~/ur5e_ws/src
```

### Description
- `mkdir` : Create a new folder
- `-p` : Create nested folders automatically
- `~/ur5e_ws/src` : Workspace and source folder location

---

## 2. Go to Source Folder

Move to the source folder inside the workspace.

### Command
```bash
cd ~/ur5e_ws/src
```

### Description
- `cd` : Change directory
- `~/ur5e_ws/src` : Source folder location for ROS2 packages

---

## Option A : Clone Existing Repository

Clone the UR5e Voice Control package from GitHub.

### Command
```bash
git clone https://github.com/your_username/ur5e_voice_control.git
```

### Description
- `git clone` : Download repository from GitHub
- `ur5e_voice_control.git` : Voice control package repository

---

## Option B : Create a New ROS2 Package

Create a new ROS2 Python package manually.

### Command
```bash
ros2 pkg create ur5e_voice_control --build-type ament_python --dependencies rclpy std_msgs geometry_msgs
```

### Description
- `ros2 pkg create` : Create a new ROS2 package
- `ur5e_voice_control` : Package name
- `--build-type ament_python` : Create Python-based ROS2 package
- `--dependencies` : Add required ROS2 dependencies

---

## 3. Go to Workspace Folder

Move back to the workspace directory.

### Command
```bash
cd ~/ur5e_ws
```

### Description
- `~/ur5e_ws` : Main ROS2 workspace location

---

## 4. Build Workspace

Build the ROS2 workspace.

### Command
```bash
colcon build
```

### Description
- `colcon build` : Compile all ROS2 packages in the workspace

---

## 5. Source Workspace

Load the ROS2 workspace environment.

### Command
```bash
source install/setup.bash
```

### Description
- `source` : Load environment variables
- `install/setup.bash` : Setup file generated after build

---

## 6. Clone Universal Robots Driver

Clone the UR ROS2 driver package.

### Command
```bash
git clone -b humble https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver.git
```

### Description
- `git clone` : Download repository from GitHub
- `-b humble` : Select ROS2 Humble branch
- `Universal_Robots_ROS2_Driver.git` : UR5e ROS2 driver package

---

## 7. Clone MoveIt2

Clone MoveIt2 package.

### Command
```bash
git clone -b humble https://github.com/ros-planning/moveit2.git
```

### Description
- `moveit2.git` : Motion planning framework for ROS2

---

## 8. Install Dependencies

Install all required dependencies.

### Command
```bash
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

### Description
- `rosdep update` : Update ROS dependency database
- `rosdep install` : Install missing ROS dependencies
- `--from-paths src` : Check packages inside src folder
- `--ignore-src` : Ignore source packages
- `-r` : Continue installing even if errors occur
- `-y` : Automatically confirm installation

---

## 9. Build All Packages

Build all ROS2 packages.

### Command
```bash
colcon build --symlink-install
```

### Description
- `--symlink-install` : Create symbolic links for easier development

---

## 10. Source Workspace Again

Reload the workspace environment.

### Command
```bash
source install/setup.bash
```

### Description
- Reload ROS2 workspace environment after build

---

# Running the System

## 1. Launch UR Driver

### Command
```bash
ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur5e robot_ip:=192.168.1.102
```

### Description
- `ros2 launch` : Launch ROS2 launch file
- `ur_type:=ur5e` : Specify robot model
- `robot_ip:=192.168.1.102` : IP address of UR5e robot

---

## 2. Launch MoveIt2

### Command
```bash
ros2 launch ur_moveit_config ur_moveit.launch.py ur_type:=ur5e
```

### Description
- Launch MoveIt2 motion planning system

---

## 3. Run Voice Control Node

### Command
```bash
ros2 run ur5e_voice_control voice_command_node
```

### Description
- Run voice command recognition node

---

# Voice Commands

| Voice Command | Action |
|---|---|
| "Move home" | Move robot to home position |
| "Move left" | Move robot to the left |
| "Pick object" | Pick an object |
| "Stop robot" | Stop robot movement |

---

# Project Structure

```bash
ur5e_ws/
 ├── src/
 │   ├── Universal_Robots_ROS2_Driver/
 │   ├── moveit2/
 │   ├── ur5e_voice_control/
 │
 ├── build/
 ├── install/
 └── log/
```
