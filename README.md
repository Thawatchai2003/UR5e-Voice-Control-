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

## 2. Go to Workspace Folder

Move to the workspace directory.

### Command
```bash
cd ~/ur5e_ws
```

### Description
- `cd` : Change directory
- `~/ur5e_ws` : Workspace location

---

## 3. Build Workspace

Build the ROS2 workspace.

### Command
```bash
colcon build
```

### Description
- `colcon build` : Compile all ROS2 packages in the workspace

---

## 4. Source Workspace

Load the ROS2 workspace environment.

### Command
```bash
source install/setup.bash
```

### Description
- `source` : Load environment variables
- `install/setup.bash` : Setup file generated after build

---

## 5. Go to Source Folder

Move to the source folder.

### Command
```bash
cd ~/ur5e_ws/src
```

### Description
- Used for cloning or adding ROS2 packages into the workspace

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
cd ~/ur5e_ws
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

# ROS2 Useful Commands

## Show ROS2 Topics

### Command
```bash
ros2 topic list
```

### Description
- Display all active ROS2 topics

---

## Monitor Joint States

### Command
```bash
ros2 topic echo /joint_states
```

### Description
- Display real-time joint state information

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

---

# Author

UR5e Voice Control Project using ROS2 and Speech Recognition.
