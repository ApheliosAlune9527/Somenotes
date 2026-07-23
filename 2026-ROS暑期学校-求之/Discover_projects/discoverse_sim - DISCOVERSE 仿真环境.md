---
title: discoverse_sim - DISCOVERSE 仿真环境
tags:
  - DISCOVERSE
  - MuJoCo
  - 仿真
  - 3DGS
  - 机器人学习
created: 2026-07-23
---

# discoverse_sim - DISCOVERSE 仿真环境

> [!info] 路径
> `/home/aphelios/Discover_projects/discoverse_sim/`

## 简介

[DISCOVERSE](https://github.com/discoverse-dev/DISCOVERSE) 是基于 **3D Gaussian Splatting** 的统一、模块化、开源仿真框架，用于 **Real2Sim2Real 机器人学习**（IROS 2025 论文）。

- **论文**：[arXiv:2507.21981](https://arxiv.org/abs/2507.21981)
- **官网**：[air-discoverse.github.io](https://air-discoverse.github.io/)
- **许可证**：MIT

## 已安装的核心组件

| 组件 | 版本 | 说明 |
|------|------|------|
| DISCOVERSE | v1.9.0 | 框架本体 |
| MuJoCo | 3.10.0 | 物理仿真引擎 |
| NumPy | 2.2.6 | 数值计算 |
| OpenCV | 5.0.0 | 计算机视觉 |
| SciPy | 1.15.3 | 科学计算 |
| Matplotlib | 3.10.9 | 可视化 |

## 虚拟环境

```
/home/aphelios/Discover_projects/discoverse_sim/discoverse-venv/
```

激活方式：

```bash
cd /home/aphelios/Discover_projects/discoverse_sim
source discoverse-venv/bin/activate
```

> [!tip] 国内加速
> 3DGS 模型从 Hugging Face 下载，可设置镜像：
> ```bash
> export HF_ENDPOINT="https://hf-mirror.com"
> ```

---

## 目录结构

```
discoverse_sim/
├── discoverse/           ← [[#核心库 discoverse/]]
├── examples/             ← [[#示例 examples/]]
├── policies/             ← [[#策略 policies/]]
├── models/               ← [[#模型 models/]]
├── submodules/           ← [[#子模块 submodules/]]
├── scripts/              ← [[#工具脚本 scripts/]]
├── assets/               ← 资源文件
├── discoverse-venv/      ← Python 虚拟环境
├── discoverse.egg-info/  ← pip 安装元数据
├── logs/                 ← 运行日志
├── pyproject.toml        ← 项目配置
├── README.md             ← 英文文档
├── README_zh.md          ← 中文文档
└── LICENSE               ← MIT 许可证
```

---

## 核心库 discoverse/

| 子目录 | 说明 |
|--------|------|
| `envs/` | 仿真环境定义 |
| `robots/` | 机器人模型 |
| `robots_env/` | 机器人-环境绑定 |
| `task_base/` | 任务基类 |
| `configs/` | 配置文件 |
| `utils/` | 工具函数 |
| `aigc/` | AI 生成内容相关 |
| `universal_manipulation/` | 通用操作模块 |
| `gaussian_web_renderer/` | 3DGS Web 渲染器 |
| `docker/` | Docker 构建文件 |
| `doc/` | 文档 |

---

## 示例 examples/

共 **16 个示例目录**，按功能分类：

### 机器人任务（AIRBOT Play 相关）

| 示例 | 说明 |
|------|------|
| `tasks_airbot_play/` | AIRBOT Play 任务集（见下方详情） |
| `tasks_hand_arm/` | 灵巧手+手臂任务 |
| `tasks_mmk2/` | MMK2 机器人任务 |
| `universal_tasks/` | 通用任务 |

### 控制与感知

| 示例 | 说明 |
|------|------|
| `force_control/` | 力控制 |
| `force_control_data_collect_using_joy/` | 手柄力控数据采集 |
| `mocap_ik/` | 动作捕捉 + 逆运动学 |
| `3dmouse/` | 3D 鼠标遥操作 |

### 仿真与渲染

| 示例 | 说明 |
|------|------|
| `gsplat/` | 3D Gaussian Splatting 渲染 |
| `hardware_sim/` | 硬件在环仿真 |
| `sensor_lidar/` | 激光雷达仿真 |

### ROS 集成

| 示例 | 说明 |
|------|------|
| `ros1/` | ROS1 集成示例 |
| `ros2/` | ROS2 集成示例 |

### 其他

| 示例 | 说明 |
|------|------|
| `robots/` | 机器人模型示例 |
| `grasp_gen/` | 抓取姿态生成 |
| `active_slam/` | 主动 SLAM |

### tasks_airbot_play 详细任务列表

| 脚本 | 任务描述 |
|------|---------|
| `block_bridge_place.py` | 方块桥接放置 |
| `close_laptop.py` | 合上笔记本电脑 |
| `cover_cup.py` | 盖杯盖 |
| `open_drawer.py` | 打开抽屉 |
| `pick_jujube.py` | 拾取红枣 |
| `place_block.py` | 放置方块 |
| `place_coffeecup.py` | 放置咖啡杯 |
| `place_jujube_coffeecup.py` | 将红枣放入咖啡杯 |
| `place_jujube.py` | 放置红枣 |
| `place_kiwi_fruit.py` | 放置猕猴桃 |
| `push_mouse.py` | 推鼠标 |
| `stack_block.py` | 堆叠方块 |

---

## 策略 policies/

| 策略 | 说明 | 依赖 |
|------|------|------|
| `act/` | ACT（Action Chunking with Transformers）模仿学习 | `torch`、`einops`、`h5py` |
| `dp/` | Diffusion Policy | `torch`、`wandb`、`numba` |
| `Diffusion-Policy/` | Diffusion Policy（完整实现） | 同上 |
| `RDT/` | RDT 策略 | — |
| `openpi/` | OpenPI 策略 | — |
| `RL/` | 强化学习 | — |
| `train.py` | 通用训练脚本 | — |
| `infer.py` | 通用推理脚本 | — |

---

## 模型 models/

| 子目录 | 说明 |
|--------|------|
| `mjcf/` | MuJoCo XML 模型文件 |
| `urdf/` | URDF 机器人描述文件 |
| `meshes/` | 3D 网格文件（STL/OBJ） |

---

## 子模块 submodules/

| 子模块 | 说明 |
|--------|------|
| `MuJoCo-LiDAR/` | MuJoCo 激光雷达仿真 |
| `urdf2mjcf/` | URDF 到 MJCF 格式转换工具 |
| `XML-Editor/` | MuJoCo XML 场景编辑器 |
| `lerobot/` | LeRobot 机器人学习框架 |
| `ComfyUI/` | ComfyUI（AI 图像生成） |

---

## 工具脚本 scripts/

| 脚本 | 说明 |
|------|------|
| `check_installation.py` | 验证安装是否完整 |
| `check_mujoco_install.py` | 验证 MuJoCo 安装 |
| `setup_submodules.py` | 自动下载配置子模块 |
| `generate_3dgs.py` | 生成 3D Gaussian Splatting 模型 |
| `mesh2mjcf.py` | 网格文件转 MJCF 格式 |
| `mesh2mjcf_batch.py` | 批量网格转换 |
| `tasks_data_gen.py` | 任务数据生成 |
| `upload_to_huggingface.py` | 上传模型到 Hugging Face |

---

## 可选模块安装

| 模块 | 安装命令 | 用途 | 关键依赖 |
|------|---------|------|---------|
| 3DGS 渲染 | `pip install -e ".[gs]"` | Real2Sim 高保真渲染 | `torch>=2.0.0`、`gaussian_renderer` |
| LiDAR | `pip install -e ".[lidar]"` | 激光雷达仿真 | `taichi>=1.6.0` |
| ACT 模仿学习 | `pip install -e ".[act]"` | 策略学习 | `torch`、`einops`、`h5py` |
| Diffusion Policy | `pip install -e ".[diffusion-policy]"` | 扩散策略学习 | `torch`、`wandb`、`numba` |
| XML 场景编辑器 | `pip install -e ".[xml-editor]"` | 场景设计 | `PyQt5`、`PyOpenGL` |

> [!warning] 显存需求
> 可选模块需要 PyTorch（`pip install -e ".[gs]"` 会自动拉取）。
> RTX 3050 Laptop 只有 4GB 显存，3DGS 渲染可能吃紧，基础 MuJoCo 仿真没问题。
