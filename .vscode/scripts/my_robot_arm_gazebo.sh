#!/bin/bash
bash .vscode/scripts/build.sh

source install/setup.bash
ros2 launch my_robot_arm gazebo.launch.py
