---
title: ros2_ws - ROS2 工作空间
tags:
  - ROS2
  - MoveIt2
  - AIRBOT
  - 工作空间
created: 2026-07-23
---

# ros2_ws - ROS2 工作空间

> [!info] 路径
> `/home/aphelios/Discover_projects/ros2_ws/airbot_play_moveit2/`

## 工作空间结构

```
airbot_play_moveit2/
├── src/                  ← 源码包
│   ├── airbot_play/      ← [[#airbot_play — 核心功能包]]
│   ├── airbot_play_description/   ← [[#airbot_play_description — URDF 模型]]
│   ├── airbot_play_movit_config/  ← [[#airbot_play_movit_config — MoveIt2 配置]]
│   └── airbot_play_msgs/          ← [[#airbot_play_msgs — 消息定义]]
├── build/                ← colcon 编译产物
├── install/              ← 安装产物（source install/setup.bash）
├── log/                  ← 编译日志
└── scripts/              ← 辅助脚本
    ├── install_ros2_humble_deps.bash  ← ROS2 Humble 依赖安装
    └── setup_humble_ws.bash           ← 工作空间初始化
```

## 环境加载

```bash
source /opt/ros/humble/setup.bash
source ~/Discover_projects/ros2_ws/airbot_play_moveit2/install/setup.bash
```

---

## ROS2 包详情

### airbot_play — 核心功能包

| 属性 | 值 |
|------|-----|
| 类型 | Python（ament_python） |
| 版本 | 0.0.0 |
| 许可证 | MIT |
| 维护者 | junjie (contact@discover-robotics.com) |

**依赖**：`rclpy`、`std_msgs`、`sensor_msgs`、`trajectory_msgs`、`control_msgs`、`std_srvs`

**核心节点**：`airbot_play_node.py`

**Launch 文件**：`play.launch.py`

---

### airbot_play_description — URDF 模型

| 属性 | 值 |
|------|-----|
| 类型 | CMake（ament_cmake） |
| 版本 | 0.0.0 |
| 许可证 | Apache-2.0 |
| 说明 | 由 SolidWorks 生成的 URDF 模型包 |

**依赖**：`robot_state_publisher`、`joint_state_publisher`、`joint_state_publisher_gui`、`rviz2`、`xacro`

---

### airbot_play_movit_config — MoveIt2 配置

| 属性 | 值 |
|------|-----|
| 类型 | CMake（ament_cmake） |
| 版本 | 0.3.0 |
| 许可证 | BSD-3-Clause |
| 说明 | MoveIt2 运动规划配置（含所有 launch 文件） |

**Launch 文件**：

| Launch 文件 | 用途 |
|------------|------|
| `demo.launch.py` | 仿真模式（FakeSystem） |
| `movit_to_airbot.launch.py` | 真机 + MoveIt2 |
| `move_group.launch.py` | MoveIt2 规划组 |
| `moveit_rviz.launch.py` | RViz 可视化 |
| `bringup.launch.py` | 完整启动 |
| `spawn_controllers.launch.py` | 控制器加载 |
| `rsp.launch.py` | Robot State Publisher |
| `setup_assistant.launch.py` | MoveIt Setup Assistant |
| `warehouse_db.launch.py` | 运动规划数据库 |
| `static_virtual_joint_tfs.launch.py` | 虚拟关节变换 |

**配置文件**：

| 配置文件 | 说明 |
|---------|------|
| `ros2_controllers.yaml` | ros2_control 控制器配置 |
| `moveit_controllers.yaml` | MoveIt2 控制器配置 |
| `kinematics.yaml` | 运动学求解器配置 |
| `joint_limits.yaml` | 关节限位 |
| `initial_positions.yaml` | 初始关节位置 |
| `pilz_cartesian_limits.yaml` | 笛卡尔空间限位 |

---

### airbot_play_msgs — 消息定义

| 属性 | 值 |
|------|-----|
| 类型 | CMake（ament_cmake） |
| 版本 | 0.0.0 |
| 许可证 | Apache-2.0 |
| 说明 | 自定义消息和服务定义 |

**依赖**：`rosidl_default_generators`、`std_msgs`、`builtin_interfaces`

---

## 使用场景

| 场景 | Launch 文件 | 说明 |
|------|------------|------|
| [[Airbot-Play-G2 使用教程#3. 路径 A：ROS2 仿真（不动真机）\|路径 A：仿真]] | `demo.launch.py` | FakeSystem，不需要真机 |
| [[Airbot-Play-G2 使用教程#5. 路径 C：真机 + MoveIt2 规划控制\|路径 C：真机]] | `movit_to_airbot.launch.py` | 需要 airbot-arm 服务 |

## 安装包

- [[Airbot-Play-G2 安装包/AIRBOT-Play-Hardware-with-Moveit2-feature-humble.zip|MoveIt2 工作空间源码]]
- [[Airbot-Play-G2 安装包/airbot_hardware_sdk_humble_AMD64.zip|ROS2 Hardware SDK]]
