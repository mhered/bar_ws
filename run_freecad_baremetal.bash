#!/bin/bash

source /opt/ros/jazzy/setup.bash
source /home/mhered/bar_ws/install/setup.bash

echo "Starting FreeCAD, please wait ..."
export ROS_DISTRO=jazzy
/home/mhered/Applications/FreeCAD_1.0.0-conda-Linux-x86_64-py311_762d03e714090fee85c2cd69af722050.AppImage --appimage-extract-and-run --module-path ${PYTHONPATH//:/' --module-path '} 
