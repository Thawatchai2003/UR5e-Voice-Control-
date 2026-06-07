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

## 3. Clone UR5e Control Repository

Move to the project folder and clone the UR5e Control repository from GitHub.

### Command

```bash
cd ~/UR5e_ws/src

mkdir -p UR5e_Control

cd UR5e_Control

git clone https://github.com/Thawatchai2003/Ur5e_Control.git
```

### Description

- `cd ~/UR5e_ws/src` : Move to the ROS2 source folder
- `mkdir -p UR5e_Control` : Create the UR5e Control project folder
- `cd UR5e_Control` : Move into the UR5e Control folder
- `git clone` : Download repository from GitHub
- `Ur5e_Control.git` : ROS2 package repository for UR5e voice control and robot operation

### Expected Directory Structure

```text
UR5e_ws/
└── src/
    ├── Zimmer_HRC_03/
    ├── Zimmer_HRC_03_configured/
    └── UR5e_Control/
        └── Ur5e_Control/
```
