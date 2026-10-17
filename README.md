# Abhishek Singh

B.Tech student in Robotics & Automation Engineering & Honors in Embedded Systems
I am building toward compiler engineering and CPU/GPU performance optimization. My work centers on LLVM IR analysis, hardware-aware kernel optimization, and profiling-driven performance work. I apply the same systems focus to robotics and Physical AI projects.

---

## Engineering Focus

- **Compilers:** LLVM IR, new-pass-manager analysis passes, frontend-to-IR code generation, optimization concepts (loop analysis, SSA, alias and dependence analysis).
- **CPU/GPU performance:** Benchmarking, Roofline modeling, bottleneck analysis with Intel VTune and NVIDIA Nsight Compute, cache blocking, SIMD, CUDA, Tensor Core kernels.
- **Systems and embedded software:** C/C++ on Linux, STM32/ESP32 firmware, communication buses, real-time constraints.
- **Physical AI:** Vision-language-model pipelines, depth-based 3D localization, and inverse kinematics on robot manipulators.

---

## Selected Projects

### Heterogeneous CPU/GPU Performance Analysis and Roofline Profiling
**Status:** Honors project. Core benchmarks complete; ML-workload extension in progress.
**Stack:** C++, OpenMP, AVX2/FMA, CUDA, WMMA, Intel VTune, Nsight Compute

- **Problem:** Quantify how far naive kernels sit from hardware limits on an Intel Core i7-13650HX and an NVIDIA RTX 4060 Laptop GPU, and explain why.
- **Work:** Benchmarked Vector Add, Dot Product, and GEMM, with outputs validated against reference implementations. CPU: cache blocking, OpenMP, AVX2/FMA. GPU: reduction optimization and a TF32 WMMA Tensor Core GEMM. Used VTune, Nsight Compute, and Roofline analysis to investigate memory bandwidth, core utilization, register pressure, and occupancy.
- **Results (from project report):** CPU GEMM 0.707 to 86.03 GFLOP/s (121.6x). CPU Vector Add 12.7x and Dot Product 13.3x. GPU TF32 GEMM reached 2,679 GFLOP/s (3.7x baseline) at 0.0686% maximum relative error.
- **Links:** <!-- TODO: add repository link --> <!-- TODO: add project report link -->

### LLVM Loop Optimization Advisor
**Status:** In progress.
**Stack:** C++, LLVM, CMake

- **Problem:** Make loop structure and optimization-blocking properties visible at the IR level.
- **Work:** An analysis-only LLVM new-pass-manager plugin that reports loop structure, memory accesses, and control-flow properties without modifying the IR. Building regression tests for simple and nested loops, reductions, unknown trip counts, and access patterns that may introduce dependencies.
- **Link:** <!-- TODO: add repository link -->

### Mini C-Like Compiler with an LLVM IR Backend
**Status:** In progress.
**Stack:** C++, LLVM

- **Problem:** Understand the full path from source language to native code.
- **Work:** C++ frontend for a defined C-like subset: lexer, parser, AST, symbol table, semantic checks. LLVM IR generation for arithmetic, if/else, and while loops, then LLVM's verifier, existing optimization passes, and code generation to produce native executables.
- **Link:** <!-- TODO: add repository link -->

### Neuro-Symbolic Robotic Sorting System (VLM Pipeline)
**Status:** B.Tech project, in progress.
**Stack:** Python, NVIDIA Isaac Sim, Dobot Magician, Qwen2.5-VL, InternVL3.5

- **Problem:** Reduce reliance on hosted APIs for vision-language-guided manipulation.
- **Work:** Pipeline mapping VLM-predicted image coordinates to segmentation masks, converting depth measurements to 3D coordinates, and issuing inverse-kinematics commands. Tested in Isaac Sim. Built a synthetic-data pipeline with consistency filtering and am fine-tuning open-weight VLMs for the task.
- **Link:** <!-- TODO: add repository link -->

### Seminar Paper: CPU and GPU Architecture Evolution for Deep Learning Acceleration
**Status:** Honors seminar, 2026.

- Examines how compiler representations and analyses (LLVM IR, MLIR, SSA, CFGs, alias and dependence analysis) affect code generation, loop transformations, fusion, and vectorization. Applies Roofline analysis to published NVIDIA A100 GEMM results.
- **Link:** <!-- TODO: add paper link -->

---

## Robotics and Mechatronics

**Team Robominds, DD Robocon 2026 (Design Lead and Co-Head)**
Led a 30-member cross-functional team. Scored 90/100 in the preliminary round and advanced to the National Finals at IIT Delhi. Owned component selection, structural load analysis, and actuation design under weight and geometry constraints.

https://github.com/user-attachments/assets/18fe45f4-467c-4aaa-97d2-063ad31eb409

[LinkedIn post](https://www.linkedin.com/posts/abhishek-singh-a2003b287_robocon2026-teamrobominds-automation-ugcPost-7438862846412771328-uZSR)

**EMG and Computer Vision Controlled Prosthetic Hand**
3D-printed hand with EMG control and a vision-based control mode, using ESP32, MQTT, and real-time computer vision.

https://github.com/user-attachments/assets/1f63cb8e-624d-42df-a676-d73537d68324

**Drone Design for Robofest**
Full drone assembly modeled in Siemens NX.

<p align="center">
  <img src="https://github.com/user-attachments/assets/4cfe013f-7190-41ad-a7d0-d2e637cecb79" width="48%" />
  <img src="https://github.com/user-attachments/assets/b2e3c0e5-843c-44f1-af15-eaf6705dd7a5" width="48%" />
</p>

---

## Technical Skills

| Domain | Skills |
|---|---|
| Languages | C++, C, Python, CUDA, PTX, SystemVerilog |
| Compilers | LLVM IR, new pass manager, code generation, GCC fundamentals |
| Performance | Intel VTune, NVIDIA Nsight Compute, Roofline modeling, cache blocking, memory coalescing, SIMD, microbenchmarking |
| Embedded | STM32, ESP32, UART/SPI/I2C/CAN, ARM ISA, RTOS concepts |
| Robotics | ROS 2 (Jazzy), Gazebo, Isaac Sim, MATLAB/Simulink |
| ML and vision | OpenCV, MediaPipe, NumPy, Keras, VLM fine-tuning |
| Tooling | Linux, CMake, Git, Siemens NX, Fusion 360 |

---

## Learning (independent study)

- Advanced Compilers (Cornell CS 6120), course materials: LLVM IR, analysis, optimization
- Accelerated Computing, course materials: CUDA, parallel computing
- Advanced VLSI Design (Compcarta): SystemVerilog, digital design, testability

---

## Contact

- Email: abhishekp135531@gmail.com
- [LinkedIn](https://www.linkedin.com/in/abhishek-singh-a2003b287/)
- [LeetCode](https://leetcode.com/u/Abhishek_P_S_/)
- [X / Twitter](https://x.com/Fe3ws_)
