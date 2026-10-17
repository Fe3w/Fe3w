# Abhishek Singh

**Compiler Engineering | CPU/GPU Performance | Systems Software | Robotics & Physical AI**

B.Tech student in Robotics & Automation Engineering, pursuing Honors in Embedded Systems at Symbiosis Institute of Technology, Pune. I focus on the relationship between compiler decisions, hardware architecture, and runtime performance, with practical work in CPU/GPU kernel optimization, profiling, LLVM-based tooling, ROS 2, and vision-guided robotic manipulation.

## Selected Engineering Projects

### Heterogeneous CPU/GPU Performance Analysis and Roofline Profiling

**Status:** Honors project — core benchmarks complete; ML-workload extension in progress.  
**Hardware:** Intel Core i7-13650HX CPU and NVIDIA RTX 4060 Laptop GPU.  
**Stack:** C++, OpenMP, AVX2/FMA, CUDA, WMMA, Intel VTune, NVIDIA Nsight Compute.

Investigated how baseline numerical kernels compare with hardware performance limits and used profiling and Roofline analysis to examine memory bandwidth, CPU utilization, register pressure, and GPU occupancy.

- **CPU work:** Benchmarked Vector Add, Dot Product, and GEMM; applied cache blocking, OpenMP, and AVX2/FMA optimizations. Validated outputs against reference implementations.
- **GPU work:** Optimized reduction behavior and implemented a TF32 WMMA Tensor Core GEMM; validated numerical output against a reference implementation.
- **Reported results:** CPU GEMM improved from **0.707 to 86.03 GFLOP/s (121.6×)**. CPU Vector Add improved **12.7×** and Dot Product **13.3×**. GPU TF32 GEMM reached **2,679 GFLOP/s (3.7× baseline)** with **0.0686% maximum relative error**.
- **Report:** [Project report (Google Drive)](https://drive.google.com/file/d/1XhWOYI6mYyLRbKIm25UFTFQibAgZOgr0/view?usp=sharing)

*Performance figures are reported in the project report; hardware, benchmark configuration, and comparison baselines should be consulted when interpreting the results.*

### Seminar Paper: CPU and GPU Architecture Evolution for Deep Learning Acceleration

**Status:** Honors seminar, 2026.

Examines how CPU/GPU architecture and compiler representations affect deep-learning performance. Covers LLVM IR, MLIR, SSA, control-flow graphs, alias and dependence analysis, code generation, loop transformations, fusion, and vectorization. Applies Roofline analysis to published NVIDIA A100 GEMM results.

- **Paper:** [Read seminar paper (Google Drive)](https://drive.google.com/file/d/1Iqg1ht8dw_D7Ud5cnDXnYjy3pSv4l__W/view)

### ROS 2 Green-Target Tracking and LiDAR Safety

**Status:** Public repository.

A TurtleBot3/Gazebo project that detects and follows a green target while using LiDAR to stop before a nearby obstacle.

- **Perception:** Converts camera frames to HSV, thresholds the target colour, filters noise, and estimates horizontal image-centre error from the target contour.
- **Control:** Uses proportional visual servoing to steer toward the target and rotates in place to reacquire it when it leaves the camera frame.
- **Safety:** Checks a forward LiDAR sector and commands zero velocity when the nearest valid range falls below a configurable threshold.
- **Stack:** Python, ROS 2, Gazebo, TurtleBot3, OpenCV, LiDAR.
- **Repository:** [Pepermint task — ROS 2 target tracking](https://github.com/Fe3w/Pepermint_task1_abhishek)

### Neuro-Symbolic Robotic Sorting System — Vision-Language Model Pipeline

**Status:** B.Tech Honors project — in progress.  
**Stack:** Python, NVIDIA Isaac Sim, Dobot Magician, Qwen2.5-VL, InternVL3.5.

Building a vision-language-guided object-sorting pipeline with a focus on reducing dependence on hosted APIs and evaluating open-weight models for manipulation tasks.

- Connects VLM predictions to segmentation masks, depth measurements, 3D target coordinates, and inverse-kinematics commands for object manipulation.
- Tests the pipeline in Isaac Sim and develops a synthetic-data workflow with consistency filtering.
- Fine-tuning open-weight VLMs for the task is in progress.
- **Code repository:** Not yet linked publicly.

### LLVM Loop Optimization Advisor

**Status:** In progress.  
**Stack:** C++, LLVM, CMake.

Developing an **analysis-only LLVM new-pass-manager plugin** to make loop structure and potential optimization constraints visible at the IR level without modifying the IR.

- Reports loop structure, memory accesses, and control-flow properties.
- Regression-test coverage is being developed for simple and nested loops, reductions, unknown trip counts, and access patterns that may introduce dependencies.
- **Code repository:** Not yet linked publicly.

### Mini C-Like Compiler with an LLVM IR Backend

**Status:** In progress.  
**Stack:** C++, LLVM.

Building a small compiler to explore the path from a defined C-like source language to native code.

- Frontend scope includes a lexer, parser, abstract syntax tree, symbol table, and semantic checks.
- The planned backend generates LLVM IR for arithmetic, `if/else` statements, and `while` loops, then uses the LLVM verifier, existing optimization passes, and code generation to produce native executables.
- **Code repository:** Not yet linked publicly.

### Robotic Arm Manipulation — Dobot Magician Integration

**Status:** In progress as part of the neuro-symbolic sorting project.

Working on the manipulation stage that connects depth-derived 3D target coordinates to inverse-kinematics commands for object handling. Simulation and pipeline testing are being conducted in Isaac Sim. This is an integration component of the Physical AI project rather than a separately published repository.

## Additional Robotics and Engineering Experience

### Team Robominds — Design Lead & Co-Head, DD Robocon 2026

- Contributed to cross-functional team coordination and the design of an obstacle-clearing robot chassis.
- Team Robominds earned a Stage I score of **90/100**.
- References: [event update on LinkedIn](https://www.linkedin.com/posts/abhishek-singh-a2003b287_robocon2026-teamrobominds-automation-ugcPost-7438862846412771328-uZSR) · [competition media](https://github.com/user-attachments/assets/18fe45f4-467c-4aaa-97d2-063ad31eb409)

### EMG- and Computer-Vision-Controlled Robotic Hand

Worked on a 3D-printed hand prototype combining EMG input and computer-vision-based control, with an ESP32 and MQTT used in the control and communication path. [Project media](https://github.com/user-attachments/assets/1f63cb8e-624d-42df-a676-d73537d68324)

### Drone CAD for Robofest

Designed a drone assembly in Siemens NX, focusing on packaging, structural layout, and aerodynamic balance. [Assembly view 1](https://github.com/user-attachments/assets/4cfe013f-7190-41ad-a7d0-d2e637cecb79) · [Assembly view 2](https://github.com/user-attachments/assets/b2e3c0e5-843c-44f1-af15-eaf6705dd7a5)

## Technical Skills

- **Programming and systems:** C, C++, Python, Linux-based development.
- **Compiler and performance:** LLVM/Clang, LLVM IR, compiler-optimization fundamentals, CPU/GPU architecture, CUDA, OpenMP, AVX2/FMA, WMMA, benchmarking, Roofline analysis, NVIDIA Nsight Compute, Intel VTune.
- **Robotics and embedded:** ROS 2 (Jazzy), Gazebo, OpenCV, STM32, ESP32, ARM ISA, UART/SPI/I²C/CAN, RTOS concepts.
- **Machine learning and numerical tools:** Qwen2.5-VL, InternVL3.5, NumPy, Pandas, Matplotlib, Keras, MediaPipe.
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

I am interested in internships and engineering roles involving compiler optimization, CPU/GPU performance engineering, systems software, accelerated computing, and semiconductor technologies.
