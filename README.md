# Gesture-controlled-robotic-arm
This project develops a Raspberry Pi–based gesture-controlled robotic arm that uses computer vision to track hand movements in real time. Detected gestures are translated into servo commands, enabling the robotic arm and hand to mimic human motion accurately and responsively


## Overview
This repository contains the design and implementation of a **gesture-controlled robotic arm** powered by Raspberry Pi 4 and ROS 2 Humble.  
Using computer vision (MediaPipe Hands & Pose) and real-time communication, the system captures human hand movements and translates them into precise robotic arm and hand motions.

The solution integrates hardware, software, and networking components to deliver a responsive, low-latency, and intuitive control experience.

---

## Features
- **Real-Time Tracking** – Detects and processes 2D/3D hand landmarks using MediaPipe.
- **Wireless Communication** – ROS 2 publishes joint commands from the laptop to the Raspberry Pi over Wi-Fi.
- **Multi-Servo Control** – 10 servo motors controlled via PCA9685 (5 arm joints, 5 robotic hand fingers).
- **Orientation Feedback** – MPU6050 IMU provides motion and angle data for stability.
- **Simulation & Visualization** – Supports RViz2 and Gazebo for testing.
- **Independent Power Systems** – Separate supply for Pi and servos to prevent interference.

---

## Hardware Components
- **Raspberry Pi 4** – Central processing unit for servo control and ROS 2 communication.
- **PCA9685 Servo Driver** – PWM control for up to 16 servos.
- **MG996R Servos** – High-torque motors for joints.
- **LFD-01 Servos** – Finger movement control.
- **MPU6050 IMU Sensor** – Orientation and motion detection.
- **11.1V LiPo Battery (4200 mAh)** – Servo power source.
- **DC-DC Buck Converter** – Voltage regulation for servos.

---

## Software Stack
- **Ubuntu 22.04 LTS** – Operating system for both Raspberry Pi and laptop.
- **Python 3** – Primary programming language for control logic.
- **ROS 2 Humble** – Middleware for communication and data handling.
- **MediaPipe** – Hand and pose landmark detection.
- **RViz2 & Gazebo** – Visualization and simulation tools.
- **VirtualBox** – For hosting Ubuntu on laptop (optional).

---



