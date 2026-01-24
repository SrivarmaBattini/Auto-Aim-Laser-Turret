# Auto Aim Turret System using ROS2

## About This Project

This project implements a ROS2-based auto aim turret system that performs real-time target detection and tracking using computer vision. The system captures live video from a camera, processes each frame to detect a target, computes the required pan and tilt angles, and controls servo motors to keep a laser aligned with the target. The entire system runs on a Raspberry Pi and demonstrates real-time control, modular software design, and hardware integration using ROS2. The project is designed using multiple ROS2 nodes, each responsible for a specific task. These nodes communicate using ROS2 topics with a publisher–subscriber mechanism. Continuous data such as image frames, target coordinates, and control commands are exchanged through topics to support real-time tracking.

ROS2 Humble plays a central role in this project by providing a stable and real-time capable robotics framework. It enables modular node development, efficient inter-node communication, and reliable execution on embedded hardware like the Raspberry Pi. ROS2 Humble’s improved DDS-based communication, Python support, and long-term stability make it well-suited for real-time robotics applications such as this auto aim turret system.

A camera node captures live video using OpenCV and publishes image frames to a ROS2 topic. The detection node subscribes to these frames and applies classical image processing techniques such as color conversion, segmentation, and contour detection to identify the target and extract its position. The tracking node receives the target coordinates and applies tracking logic to ensure smooth and stable motion while handling target loss. The control node converts the computed pan and tilt angles into PWM signals to drive the servo motors and control the laser module. A web streaming node publishes annotated video frames, allowing real-time monitoring through a browser without interfering with the control pipeline.

In this project, classical image processing techniques are used to detect and track the target in real time. Live video frames captured from the camera are processed using OpenCV, where color space conversion and noise reduction are applied to simplify the image and improve stability. The processed frames are segmented to isolate the target from the background, and contour detection is used to identify the target region. The centroid of the detected contour is then calculated to obtain the target’s position, which is continuously updated and used for tracking and control.

---

## Technologies Used
- Python  
- ROS2 (Robot Operating System)  
- OpenCV  
- Raspberry Pi  
- Servo Motor Control (PWM/GPIO)  

---

## Hardware Used
- Raspberry Pi  
- USB Camera  
- Servo Motors (for Pan–Tilt Mechanism) 
- Laser Module  
- Breadboard  
- Jumper Wires  

---

## How to Run the Project
1. Set up the ROS2 environment (source /opt/ros/humble/setup.bash)
2. Create and build the workspace (colcon build)
3. Source the workspace (source install/setup.bash)
4. Connect the hardware
5. Launch the system (ros2 launch auto_turret turret_launch.py)
