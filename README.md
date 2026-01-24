# Auto Aim Turret System using ROS2

## About This Project

This project implements a ROS2-based auto aim turret system that performs real-time target detection and tracking using computer vision. The system captures live video from a camera, processes each frame to detect a target, computes the required pan and tilt angles, and controls servo motors to keep a laser aligned with the target. The entire system runs on a Raspberry Pi and demonstrates real-time control, modular software design, and hardware integration using ROS2. The project is designed using multiple ROS2 nodes, each responsible for a specific task. These nodes communicate using ROS2 topics with a publisher–subscriber mechanism. Continuous data such as image frames, target coordinates, and control commands are exchanged through topics to support real-time tracking.

ROS2 Humble plays a central role in this project by providing a stable and real-time capable robotics framework. It enables modular node development, efficient inter-node communication, and reliable execution on embedded hardware like the Raspberry Pi. ROS2 Humble’s improved DDS-based communication, Python support, and long-term stability make it well-suited for real-time robotics applications such as this auto aim turret system.

The project is designed using multiple ROS2 nodes, each responsible for a specific task. These nodes communicate using ROS2 topics with a publisher–subscriber mechanism. Continuous data such as image frames, target coordinates, and control commands are exchanged through topics to support real-time tracking. No ROS services or actions are used, as the system requires continuous, non-blocking data flow rather than request-response communication.

The hardware used in this project includes a Raspberry Pi as the main controller, a USB camera for visual input, a pan–tilt mechanism driven by servo motors, and a laser module for visual alignment. A breadboard and jumper wires are used for hardware connections. The Raspberry Pi runs the ROS2 nodes and directly interfaces with the servo motors using GPIO and PWM signals.

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
