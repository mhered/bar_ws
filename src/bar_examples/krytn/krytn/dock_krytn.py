#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
import time

rclpy.init()

# Create node and setup
node = Node("krytn_docker")

pub = node.create_publisher(PoseStamped, '/goal_pose', qos_profile=1)

current_pose = None

def callback(msg):
    """ Callback function for the subscriber. """
    global current_pose
    current_pose = msg.pose.pose  # Extract only the pose
    logger.info(f"Updated Pose: position=({current_pose.position.x}, {current_pose.position.y})")

sub = node.create_subscription(PoseWithCovarianceStamped, '/pose', callback, qos_profile=1)

clock = node.get_clock()
logger = node.get_logger()

ApproachPose = PoseStamped()
ApproachPose.pose.position.x = 0.0
ApproachPose.pose.position.y = 0.0
ApproachPose.pose.orientation.z = 0.9
ApproachPose.pose.orientation.w = -0.4

DockedPose = PoseStamped()
DockedPose.pose.position.x = 0.259
DockedPose.pose.position.y = 0.542
DockedPose.pose.orientation.z = 0.9
DockedPose.pose.orientation.w = -0.4

# Construct a new message goal pose
point = PoseStamped()
point.pose.position.x = ApproachPose.pose.position.x
point.pose.position.y = ApproachPose.pose.position.y
point.pose.orientation.z = ApproachPose.pose.orientation.z
point.pose.orientation.w = ApproachPose.pose.orientation.w
point.header.frame_id = 'map'
point.header.stamp = clock.now().to_msg()

# Publish the message and log it
pub.publish(point)
logger.info("Moving Krtyn to Approach position...")
logger.info(f"Published Pose: position=({point.pose.position.x}, {point.pose.position.y}, {point.pose.position.z}), orientation=({point.pose.orientation.x}, {point.pose.orientation.y}, {point.pose.orientation.z}, {point.pose.orientation.w})")

# time.sleep(1.0)

while True:
    if current_pose is not None:
      logger.info(f"Current Pose: x={current_pose.position.x}, y={current_pose.position.y} | Target: x={ApproachPose.pose.position.x}, y={ApproachPose.pose.position.y}")
      if abs(current_pose.position.x - ApproachPose.pose.position.x) < 0.02 and \
         abs(current_pose.position.y - ApproachPose.pose.position.y) < 0.02:
        logger.info("Approach position reached!")
        break
    rclpy.spin_once(node)
    pub.publish(point)
    time.sleep(0.1)

logger.info("Approach position reached! Moving to Docked position...")

# Update new message goal pose
point.pose.position.x = DockedPose.pose.position.x
point.pose.position.y = DockedPose.pose.position.y
point.pose.orientation.z = DockedPose.pose.orientation.z
point.pose.orientation.w = DockedPose.pose.orientation.w
point.header.frame_id = 'map'
point.header.stamp = clock.now().to_msg()

# Publish the Docked position
pub.publish(point)
logger.info(f"Published Docked Pose: position=({point.pose.position.x}, {point.pose.position.y}), orientation=({point.pose.orientation.z}, {point.pose.orientation.w})")

time.sleep(1)
rclpy.shutdown()

