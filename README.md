<!--
  Videos: a bare https://github.com/user-attachments/assets/<id> URL on its own
  line (blank line above and below) renders as GitHub's video player.
  Graphics: python tools/gen_assets.py → python tools/make_hero_gif.py (banner)
            python tools/make_results_png.py (GPU-project result charts)
-->

<div align="center">

<picture><source media="(prefers-color-scheme: light)" srcset="assets/light/hero.gif" /><img src="assets/hero.gif" width="100%" alt="Abhishek Singh — compilers, CPU/GPU performance, autonomous systems, with an animated GPU warp scheduler" /></picture>

<a href="https://github.com/Fe3w">
  <picture><source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&pause=1400&color=7C3AED&center=true&vCenter=true&width=760&lines=Making+code+fast+%E2%80%94+then+proving+why+it%27s+fast.;LLVM+passes+%C2%B7+CUDA+kernels+%C2%B7+Roofline+analysis;From+autonomous+systems+down+to+Tensor+Cores." /><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&pause=1400&color=C4A7FF&center=true&vCenter=true&width=760&lines=Making+code+fast+%E2%80%94+then+proving+why+it%27s+fast.;LLVM+passes+%C2%B7+CUDA+kernels+%C2%B7+Roofline+analysis;From+autonomous+systems+down+to+Tensor+Cores." alt="Typing headline" /></picture>
</a>

</div>

<p align="center">
  <a href="#whoami"><code>01 WHOAMI</code></a> ·
  <a href="#stack"><code>02 STACK</code></a> ·
  <a href="#performance"><code>03 PERFORMANCE</code></a> ·
  <a href="#compilers"><code>04 COMPILERS</code></a> ·
  <a href="#autonomy"><code>05 AUTONOMY</code></a> ·
  <a href="#builds"><code>06 BUILDS</code></a> ·
  <a href="#contact"><code>07 CONTACT</code></a>
</p>

<p align="center">
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Pune,_IN-efeafb?style=flat-square&logo=googlemaps&logoColor=7c3aed" /><img src="https://img.shields.io/badge/Pune,_IN-0e0a18?style=flat-square&logo=googlemaps&logoColor=c4a7ff" alt="Pune, India" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/B.Tech-class_of_2027-efeafb?style=flat-square" /><img src="https://img.shields.io/badge/B.Tech-class_of_2027-0e0a18?style=flat-square" alt="B.Tech class of 2027" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Honors-Embedded_Systems-efeafb?style=flat-square" /><img src="https://img.shields.io/badge/Honors-Embedded_Systems-0e0a18?style=flat-square" alt="Honors in Embedded Systems" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/DD_Robocon_2026-National_Finalist-efeafb?style=flat-square" /><img src="https://img.shields.io/badge/DD_Robocon_2026-National_Finalist-0e0a18?style=flat-square" alt="DD Robocon 2026 National Finalist" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/open_to-compiler_%2F_perf_internships-efeafb?style=flat-square" /><img src="https://img.shields.io/badge/open_to-compiler_%2F_perf_internships-0e0a18?style=flat-square" alt="Open to compiler and performance internships" /></picture>
</p>

<img src="assets/terminal.svg" width="100%" alt="Terminal: whoami, current projects, benchmark results" />

---

<a id="whoami"></a>

### `01 — WHOAMI`

Final-year Robotics & Automation student (Honors in Embedded Systems) at Symbiosis Institute of Technology, Pune, **working my way down the stack**. I started with autonomous systems that perceive, decide and act. Now most of my time goes to what sits underneath them: the kernels, the compilers and the hardware that decide how fast any of it runs.

- 🔭 **Currently building:** an LLVM loop-analysis pass, a C-like compiler with an LLVM IR backend, and an ML-workload extension to my roofline study
- 🎯 **Looking for:** internships in compiler optimization, CPU/GPU performance engineering, systems software and accelerated computing
- 💬 **Ask me about:** roofline models, why a GEMM is memory-bound until it isn't, LLVM's new pass manager, perception-to-control pipelines in ROS 2
- 🏁 **Off-keyboard:** led design for Team Robominds to the DD Robocon 2026 National Finals at IIT Delhi

---

<a id="stack"></a>

### `02 — STACK`

<picture><source media="(prefers-color-scheme: light)" srcset="assets/light/stack.svg" /><img src="assets/stack.svg" width="100%" alt="The stack: autonomy, kernels, compilers, silicon" /></picture>

<p>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/C++-efeafb?style=for-the-badge&logo=cplusplus&logoColor=7c3aed" /><img src="https://img.shields.io/badge/C++-0e0a18?style=for-the-badge&logo=cplusplus&logoColor=c4a7ff" alt="C++" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/C-efeafb?style=for-the-badge&logo=c&logoColor=7c3aed" /><img src="https://img.shields.io/badge/C-0e0a18?style=for-the-badge&logo=c&logoColor=c4a7ff" alt="C" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/CUDA-efeafb?style=for-the-badge&logo=nvidia&logoColor=7c3aed" /><img src="https://img.shields.io/badge/CUDA-0e0a18?style=for-the-badge&logo=nvidia&logoColor=c4a7ff" alt="CUDA" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/LLVM-efeafb?style=for-the-badge&logo=llvm&logoColor=7c3aed" /><img src="https://img.shields.io/badge/LLVM-0e0a18?style=for-the-badge&logo=llvm&logoColor=c4a7ff" alt="LLVM" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Python-efeafb?style=for-the-badge&logo=python&logoColor=7c3aed" /><img src="https://img.shields.io/badge/Python-0e0a18?style=for-the-badge&logo=python&logoColor=c4a7ff" alt="Python" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Linux-efeafb?style=for-the-badge&logo=linux&logoColor=7c3aed" /><img src="https://img.shields.io/badge/Linux-0e0a18?style=for-the-badge&logo=linux&logoColor=c4a7ff" alt="Linux" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/CMake-efeafb?style=for-the-badge&logo=cmake&logoColor=7c3aed" /><img src="https://img.shields.io/badge/CMake-0e0a18?style=for-the-badge&logo=cmake&logoColor=c4a7ff" alt="CMake" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Intel_VTune-efeafb?style=for-the-badge&logo=intel&logoColor=7c3aed" /><img src="https://img.shields.io/badge/Intel_VTune-0e0a18?style=for-the-badge&logo=intel&logoColor=c4a7ff" alt="Intel VTune" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/ROS_2-efeafb?style=for-the-badge&logo=ros&logoColor=7c3aed" /><img src="https://img.shields.io/badge/ROS_2-0e0a18?style=for-the-badge&logo=ros&logoColor=c4a7ff" alt="ROS 2" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/OpenCV-efeafb?style=for-the-badge&logo=opencv&logoColor=7c3aed" /><img src="https://img.shields.io/badge/OpenCV-0e0a18?style=for-the-badge&logo=opencv&logoColor=c4a7ff" alt="OpenCV" /></picture>
  <picture><source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Git-efeafb?style=for-the-badge&logo=git&logoColor=7c3aed" /><img src="https://img.shields.io/badge/Git-0e0a18?style=for-the-badge&logo=git&logoColor=c4a7ff" alt="Git" /></picture>
</p>

| Compilers & performance | Parallel & GPU | Autonomy & embedded | ML & vision |
|---|---|---|---|
| LLVM / Clang · LLVM IR | CUDA · PTX · WMMA | ROS 2 (Humble / Jazzy) · Gazebo | Qwen2.5-VL · InternVL3.5 fine-tuning |
| New-pass-manager plugins | OpenMP · AVX2 / FMA | NVIDIA Isaac Sim · Dobot Magician | Synthetic data pipelines |
| Roofline · arithmetic intensity | TF32 Tensor Cores | STM32 · ESP32 · RTOS concepts | OpenCV · MediaPipe |
| Nsight Compute · Intel VTune | Cache blocking · shared-memory tiling | UART / SPI / I²C / CAN · MQTT | Keras · NumPy · Pandas |
| GCC · micro-benchmarking | Ampere / Hopper SM architecture | MATLAB · Simulink · Stateflow | SystemVerilog · Intel Quartus |

---

<a id="performance"></a>

### `03 — PERFORMANCE ENGINEERING`

#### ⚡ Heterogeneous CPU/GPU Performance Analysis & Roofline Profiling
<sub><code>Honors project · 2026</code> · core benchmarks ✅ · ML-workload extension in progress · <code>C++ · OpenMP · AVX2/FMA · CUDA · WMMA · VTune · Nsight Compute</code></sub>

📄 [**Project report**](https://drive.google.com/file/d/1XhWOYI6mYyLRbKIm25UFTFQibAgZOgr0/view?usp=sharing) · 📜 [**Seminar paper**](https://drive.google.com/file/d/1Iqg1ht8dw_D7Ud5cnDXnYjy3pSv4l__W/view?usp=sharing)

How far are textbook kernels from what the hardware can actually do, and *why*? I benchmarked baseline kernels on an **Intel Core i7-13650HX** and an **NVIDIA RTX 4060 Laptop GPU**, optimized them step by step, and used profiling plus Roofline analysis to explain each gap: memory bandwidth, core utilization, register pressure, occupancy.

<img src="assets/media/results-speedup.png" width="100%" alt="Speedup per kernel, log scale: vector add CPU 12.7x GPU 1.0x; dot product CPU 13.3x GPU 28.7x; GEMM CPU 121.6x GPU 3.7x. GEMM throughput: CPU 0.707 to 86.03 GFLOP/s, GPU 730 to 934 to 2,679 GFLOP/s" />

| Kernel | Arithmetic intensity | CPU speedup | GPU speedup | What limits the GPU (Nsight Compute) |
|---|---|---|---|---|
| Vector add | 0.083 FLOP/byte | **12.7×** | **1.0×** | DRAM 92% busy → memory-bound |
| Dot product | 0.25 FLOP/byte | **13.3×** | **28.7×** | tree reduction removes the serial chain |
| GEMM | 170.7 FLOP/byte | **121.6×** · 0.707 → 86.03 GFLOP/s | **3.7×** · 730 → 2,679 GFLOP/s | naive: SM 99% (FP32 pipe) · Tensor Cores: starved of data |

<sub>CPU: cache blocking · OpenMP · AVX2/FMA. GPU: coalescing · block reduction · shared-memory tiling · TF32 WMMA Tensor Cores. Every output validated against a reference implementation · TF32 GEMM max relative error <b>0.0686%</b>.</sub>

<img src="assets/media/results-profiler.png" width="100%" alt="Nsight Compute utilisation: vector add SM 11% DRAM 92%, memory-bound; naive GEMM SM 99% DRAM 1%, compute-bound; Tensor Core GEMM SM 50% DRAM 8%, starved of data" />

**▶ Real-time race on the GPU** · every kernel version runs against one shared clock until the slowest (the dot-product baseline) has finished three times; playback is slowed so the race is visible. In this run, block reduction takes the dot product from 227.48 ms to 6.50 ms (**34.98×**), GEMM goes 14.55 → 9.98 → 3.85 ms (tiled **1.46×**, TF32 Tensor Cores **3.78×**, 2,987 GFLOP/s), and coalescing leaves the memory-bound vector add unchanged (0.99×).

https://github.com/user-attachments/assets/59c39e98-2050-4bd9-8ce8-9170273fc229

<sub>A separate run from the report table above, so the figures differ slightly.</sub>

**▶ CPU vs GPU, explained with my measurements** · a 103-second walkthrough: where the silicon goes, how work flows through each processor, the memory hierarchy, the optimisation techniques, the measured results and which workloads suit which processor.

https://github.com/user-attachments/assets/b8438f65-99d4-4611-a12c-56aaf073b32a

<details open>
<summary><b>Architecture diagrams</b> · i7-13650HX vs RTX 4060 Laptop</summary>
<br>

<img src="assets/media/arch-cpu-vs-gpu.png" width="100%" alt="CPU vs GPU: where the silicon goes. CPU: 6 P-cores, 8 E-cores, 24 MB L3, DDR5 76.8 GB/s. GPU: 24 SMs, 3,072 lanes, shared L2, GDDR6 256 GB/s" />

<img src="assets/media/arch-work-flow.png" width="100%" alt="How work flows: a pipelined CPU thread versus GPU warps taking turns to hide memory latency" />

<img src="assets/media/arch-memory-hierarchy.png" width="100%" alt="Memory hierarchy of the i7-13650HX and RTX 4060 Laptop, from execution units down to DRAM, VRAM and storage" />

</details>

**Next:** extending the study to ML workloads (in progress).

#### 📜 Seminar paper · Breaking the Compute Bottleneck
<sub><code>Honors seminar · 2026</code></sub> · 📜 [**Read the paper**](https://drive.google.com/file/d/1Iqg1ht8dw_D7Ud5cnDXnYjy3pSv4l__W/view?usp=sharing)

How CPU, GPU and TPU/NPU architectures evolved for deep learning, and how the compiler stack (LLVM IR, MLIR, SSA, control-flow graphs, alias and dependence analysis) shapes code generation, loop transformations, fusion and vectorization. Applies Roofline analysis to published NVIDIA A100 GEMM results.

---

<a id="compilers"></a>

### `04 — COMPILERS` <sub>in progress</sub>

Building the compiler side from both ends: a tool that **reads** optimized IR, and a compiler that **writes** it.

| Project | What it does | Stack |
|---|---|---|
| 🔍 **LLVM Loop Optimization Advisor** | Analysis-only new-pass-manager plugin that reports loop structure, memory accesses and control-flow properties, without modifying the IR. Regression tests cover nested loops, reductions, unknown trip counts and dependent accesses. | C++ · LLVM · CMake |
| 🛠️ **Mini C-like compiler** | Lexer → parser → AST → semantic checks → LLVM IR for arithmetic, `if/else` and `while`, then the LLVM verifier, optimization passes and native codegen. | C++ · LLVM |

---

<a id="autonomy"></a>

### `05 — AUTONOMOUS SYSTEMS`

#### 🤖 Neuro-Symbolic Autonomous Sorting · VLM pipeline
<sub><code>B.Tech project · 2026</code> · in progress · <code>Python · Isaac Sim · Dobot Magician · Qwen2.5-VL · InternVL3.5</code></sub>

A vision-language-guided sorting system for autonomous manipulation that turns *"put the red parts in the left bin"* into arm motion, and explains each decision. Model predictions become segmentation masks, depth turns them into 3D targets, rule-based symbolic logic makes the sort decision, and inverse kinematics drives a Dobot Magician. Each task is validated in NVIDIA Isaac Sim, then run on the physical arm. To cut API dependence and latency, I'm fine-tuning smaller open-weight VLMs on synthetic data filtered for consistency.

**▶ Simulation: language-conditioned pick-and-place in NVIDIA Isaac Sim** · task: *"pick up the green cube and place it next to the cylinder"*. The VLM interprets the scene, the planner avoids the remaining objects, and the arm executes the placement.

https://github.com/user-attachments/assets/113927a2-1523-44bc-97b1-f1e8f54ed114

**🔧 On the real Dobot Magician** · phone camera, ArUco markers that map pixels to the robot frame, and live object detection with pick coordinates in mm, checked against the arm's reach envelope

<table>
  <tr>
    <td width="50%" align="center"><img src="assets/media/dobot-lab-setup.jpg" width="100%" alt="Dobot Magician on the lab bench with ArUco markers and test objects" /><br><sub><b>Bench setup</b> · Dobot Magician, ArUco markers, test objects</sub></td>
    <td width="50%" align="center"><img src="assets/media/dobot-aruco-calibration.jpg" width="100%" alt="Numbered ArUco calibration markers detected in the camera image" /><br><sub><b>Calibration</b> · numbered ArUco markers link camera pixels to robot coordinates</sub></td>
  </tr>
</table>

<p align="center"><img src="assets/media/dobot-detection-1.jpg" width="100%" alt="Height map and live camera view with detected objects and their robot-frame coordinates" /><br><img src="assets/media/dobot-detection-2.jpg" width="100%" alt="The same detection after the objects are rearranged" /><br><sub><b>Live detection</b> · height map (left) and camera view (right): each object is labelled with its x / y in mm and checked against the dashed reach rings. The second frame shows a rearranged scene.</sub></p>

```mermaid
flowchart LR
  CAM[RGB-D camera] --> VLM[fine-tuned VLM<br/>Qwen2.5-VL / InternVL3.5]
  VLM --> PX[pixel coordinates] --> M[segmentation mask]
  M --> D[depth → 3D target]
  VLM --> R[symbolic rules<br/>explainable decision]
  D --> IK[inverse kinematics] --> ARM[Dobot Magician]
  R --> IK
  SYN[synthetic data<br/>multi-model + consistency filter] -.fine-tune.-> VLM
```

#### 🎯 Vision-Based Target Tracking with LiDAR Collision Avoidance (ROS 2)
<sub><code>Python · ROS 2 Humble · Gazebo · TurtleBot3 · OpenCV</code> · [**repo →**](https://github.com/Fe3w/Pepermint_task1_abhishek)</sub>

A two-node ROS 2 package: HSV segmentation and contour centroids feed a proportional visual-servoing controller; the robot spins to reacquire a lost target, and a LiDAR check (0.5 m in a 20° frontal cone) stops it before a collision. All gains and thresholds are ROS 2 parameters, with a one-command launch file.

**▶ Target search, acquisition and pursuit** · the TurtleBot3 rotates in place to locate the target, then follows it using proportional visual servoing on the image-centre error.

https://github.com/user-attachments/assets/8b71ba75-8a89-4cfd-ae5a-b8ca14dbee04

**▶ LiDAR-based collision avoidance** · as the robot closes in, the frontal-cone range check commands zero velocity before contact.

https://github.com/user-attachments/assets/fcea9351-c6b0-4003-a7d3-23be096ce114

---

<a id="builds"></a>

### `06 — MORE BUILDS & LEADERSHIP`

#### ✋ EMG + Computer-Vision Robotic Hand
3D-printed hand driven by EMG input and a real-time OpenCV/MediaPipe gesture tracker; commands stream over MQTT to an ESP32 with **<100 ms** actuator response. I wrote the ESP32 subscriber firmware and made CAD changes for mechanical alignment.

https://github.com/user-attachments/assets/1f63cb8e-624d-42df-a676-d73537d68324

#### 🏁 Team Robominds · DD Robocon 2026 — Design Lead & Co-Head
<sub>Jan – Jun 2026</sub>

Led a **30-member** cross-functional team through rapid design iterations: **90/100** in the preliminary round and a place in the **National Finals (Stage 3) at IIT Delhi**. Owned planning and technical decisions on component selection, structural load analysis and actuation design under strict weight and geometry limits, following a V-Model lifecycle. [Event update on LinkedIn →](https://www.linkedin.com/posts/abhishek-singh-a2003b287_robocon2026-teamrobominds-automation-ugcPost-7438862846412771328-uZSR)

https://github.com/user-attachments/assets/18fe45f4-467c-4aaa-97d2-063ad31eb409

#### 🚁 Drone CAD for Robofest
Drone assembly in Siemens NX, focused on packaging, structural layout and balance.

<table>
  <tr>
    <td width="50%"><img src="https://github.com/user-attachments/assets/4cfe013f-7190-41ad-a7d0-d2e637cecb79" width="100%" alt="Drone assembly, view 1" /></td>
    <td width="50%"><img src="https://github.com/user-attachments/assets/b2e3c0e5-843c-44f1-af15-eaf6705dd7a5" width="100%" alt="Drone assembly, view 2" /></td>
  </tr>
</table>

<details>
<summary><b>🐍 Python tooling</b></summary>
<br>

- OCR-based PDF retrieval (PyMuPDF, pytesseract): scans nested folders, falls back to OCR on scanned pages, finds PDFs by keyword
- Face-similarity search integrated with the Google Drive API (OAuth)
- Automated image-dataset preprocessing and splitting for CNN training
- Scripted Gazebo simulation runs; used the data to fine-tune bipedal robot control models

</details>

<details>
<summary><b>🎓 Education, coursework & certifications</b></summary>
<br>

- **B.Tech, Robotics & Automation Engineering** · Honors in Embedded & Automotive Systems · Symbiosis Institute of Technology, Pune · CGPA 7.65 · expected June 2027
- **Independent study:** Cornell CS 6120 Advanced Compilers (LLVM IR, analysis, optimization) · MIT 6.S894 Accelerated Computing (GPU programming, CUDA)
- **Advanced VLSI Design** (Compcarta): SystemVerilog, digital design, testing
- **NPTEL:** Deep Learning for Computer Vision (IIT Hyderabad) · Advanced Robotics (IIT Kanpur)
- **MathWorks:** MATLAB, Simulink, Stateflow Onramps

</details>

#### `LIVE FROM GITHUB`

<!-- Needs .github/workflows/snake.yml in this repo. Run it once from the Actions tab. -->
<p align="center">
  <picture><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Fe3w/Fe3w/output/snake-light.svg" /><img src="https://raw.githubusercontent.com/Fe3w/Fe3w/output/snake-dark.svg" width="100%" alt="Contribution snake" /></picture>
</p>

---

<a id="contact"></a>

### `07 — CONTACT`

<div align="center">

**Working on compilers, GPU performance or autonomous systems that need to run faster? Say hello.**

<a href="mailto:abhishekp135531@gmail.com"><img src="https://img.shields.io/badge/Email-0e0a18?style=for-the-badge&logo=gmail&logoColor=c4a7ff" alt="Email" /></a>
<a href="https://www.linkedin.com/in/abhishek-singh-a2003b287/"><img src="https://img.shields.io/badge/LinkedIn-0e0a18?style=for-the-badge&logo=linkedin&logoColor=c4a7ff" alt="LinkedIn" /></a>
<a href="https://github.com/Fe3w"><img src="https://img.shields.io/badge/GitHub-0e0a18?style=for-the-badge&logo=github&logoColor=c4a7ff" alt="GitHub" /></a>
<a href="https://leetcode.com/u/Abhishek_P_S_/"><img src="https://img.shields.io/badge/LeetCode-0e0a18?style=for-the-badge&logo=leetcode&logoColor=c4a7ff" alt="LeetCode" /></a>
<a href="https://x.com/Fe3ws_"><img src="https://img.shields.io/badge/@Fe3ws__-0e0a18?style=for-the-badge&logo=x&logoColor=c4a7ff" alt="X" /></a>

`COMPILERS · GPU PERFORMANCE · AUTONOMOUS SYSTEMS` · Pune, Maharashtra, IN

<br>

<a href="https://x.com/Ki11_5trike" title="Umbrella art by @Ki11_5trike"><img src="assets/media/art-umbrella.gif" width="260" alt="Animated glitch-art figure under an umbrella by @Ki11_5trike" /></a>

<sub>🎨 hourglass &amp; umbrella art by <a href="https://x.com/Ki11_5trike"><b>@Ki11_5trike</b></a></sub>

<picture><source media="(prefers-color-scheme: light)" srcset="assets/light/footer.svg" /><img src="assets/footer.svg" width="100%" alt="" /></picture>

</div>
