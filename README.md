# Abhishek Singh

**Compiler Engineering | CPU/GPU Performance | Systems Software | Robotics**

B.Tech student in Robotics & Automation Engineering, pursuing Honors in Embedded Systems at Symbiosis Institute of Technology, Pune. My technical focus is low-level software and the relationship between compiler decisions, hardware architecture, and runtime performance. I am building depth in LLVM/Clang, LLVM IR, hardware-aware optimization, CUDA, profiling, and benchmarking, alongside practical work in ROS 2, computer vision, and embedded systems.

## Technical Focus

- **Compiler engineering:** LLVM/Clang, LLVM IR, optimization passes, compiler fundamentals, lowering, and code-generation concepts.
- **CPU/GPU performance:** CPU and GPU architecture, CUDA, numerical-kernel optimization, benchmarking, bottleneck analysis, and profiling with NVIDIA Nsight Compute and Intel VTune.
- **Systems and embedded software:** C/C++, Linux development, ARM architecture, microcontrollers, peripheral interfaces, and real-time systems concepts.
- **Physical AI and robotics:** computer vision, ROS 2, simulation, perception-to-control pipelines, and intelligent robotic manipulation.

## Selected Public Project

### [ROS 2 Green-Target Tracking and LiDAR Safety](https://github.com/Fe3w/Pepermint_task1_abhishek)

A TurtleBot3/Gazebo project that detects and follows a green target while using LiDAR to stop before a nearby obstacle.

- **Perception:** converts camera frames to HSV, thresholds the target colour, filters noise, and estimates the target's horizontal image-centre error from its contour.
- **Control:** uses a proportional visual-servoing controller to steer toward the target and rotates in place to reacquire it when it leaves the camera frame.
- **Safety:** checks a forward LiDAR sector and commands zero velocity when the nearest valid range falls below a configurable threshold.
- **Technologies:** Python, ROS 2, Gazebo, TurtleBot3, OpenCV, and LiDAR.

The repository documents the node architecture and configurable control parameters. No performance figures are claimed here because the repository does not publish a reproducible benchmark.

## Robotics and Engineering Experience

### Team Robominds — Design Lead & Co-Head, DD Robocon 2026

- Contributed to cross-functional team coordination and the design of an obstacle-clearing robot chassis.
- Team Robominds earned a Stage I score of **90/100** (see the linked event update).
- References: [event update on LinkedIn](https://www.linkedin.com/posts/abhishek-singh-a2003b287_robocon2026-teamrobominds-automation-ugcPost-7438862846412771328-uZSR) · [competition media](https://github.com/user-attachments/assets/18fe45f4-467c-4aaa-97d2-063ad31eb409)

### EMG- and Computer-Vision-Controlled Hand

Worked on a 3D-printed hand concept combining EMG input and computer-vision control, with an ESP32 and MQTT used in the control/communication path. [Project media](https://github.com/user-attachments/assets/1f63cb8e-624d-42df-a676-d73537d68324)

### Drone CAD for Robofest

Designed a drone assembly in Siemens NX, with attention to packaging, structure, and aerodynamic layout. [Assembly view 1](https://github.com/user-attachments/assets/4cfe013f-7190-41ad-a7d0-d2e637cecb79) · [Assembly view 2](https://github.com/user-attachments/assets/b2e3c0e5-843c-44f1-af15-eaf6705dd7a5)

## Technical Skills

- **Programming and systems:** C, C++, Python, Linux-based development.
- **Compiler and performance focus:** LLVM/Clang, LLVM IR, compiler-optimization fundamentals, CPU/GPU architecture, CUDA, NVIDIA Nsight Compute, Intel VTune.
- **Robotics and embedded:** ROS 2 (Jazzy), Gazebo, OpenCV, STM32, ESP32, ARM ISA, UART/SPI/I²C/CAN, RTOS concepts.
- **Machine learning and numerical tools:** NumPy, Pandas, Matplotlib, Keras, MediaPipe.
- **Control and design:** MATLAB, Simulink, Stateflow, Siemens NX, Autodesk Fusion 360.

## Education

**B.Tech — Robotics & Automation Engineering, Honors in Embedded Systems**  
Symbiosis Institute of Technology, Pune

## Contact

- Email: [abhishekp135531@gmail.com](mailto:abhishekp135531@gmail.com)
- LinkedIn: [abhishek-singh-a2003b287](https://www.linkedin.com/in/abhishek-singh-a2003b287/)
- GitHub: [Fe3w](https://github.com/Fe3w)
- LeetCode: [Abhishek_P_S_](https://leetcode.com/u/Abhishek_P_S_/)
- X: [@Fe3ws_](https://x.com/Fe3ws_)

---

I am especially interested in internships and engineering roles involving compiler optimization, CPU/GPU performance, systems software, accelerated computing, and semiconductor technologies.
