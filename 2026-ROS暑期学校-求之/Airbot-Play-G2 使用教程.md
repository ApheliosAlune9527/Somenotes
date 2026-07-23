---
title: AIRBOT Play + G2 夹爪 使用教程
tags:
  - ROS2
  - 机械臂
  - AIRBOT
  - MoveIt
  - 教程
created: 2026-07-21
updated: 2026-07-23
---

# AIRBOT Play + G2 夹爪 使用教程

> [!info] 环境信息
> - **适用硬件**：AIRBOT Play 六轴机械臂 + G2 夹爪
> - **系统环境**：Ubuntu 22.04 + ROS2 Humble + Python 3.10
> - **最后更新**：2026-07-23
> - **离线安装包**：[[Airbot-Play-G2 安装包/]]
> - **旧版官方资料**：[[Airbot-Play-G2 安装包/AIRBOT Play V5.1.6 官方资料索引|V5.1.6 官方资料索引]]

---

## 目录

1. [[#1. 你电脑上装了什么]]
2. [[#2. 三条路径：选哪个？]]
3. [[#3. 路径 A：ROS2 仿真（不动真机）]]
4. [[#4. 路径 B：真机直控（arm-sdk 5.2.2）]]
5. [[#5. 路径 C：真机 + MoveIt2 规划控制]]
6. [[#6. 附：5.1.6 SDK 键盘控制（旧版）]]
7. [[#7. 认识你的机械臂]]
8. [[#8. 安全守则]]
9. [[#9. 常见问题排查]]
10. [[#10. API 速查表]]
11. [[#11. 关节限位参考]]
12. [[#附录 A：官方资源]]
13. [[#附录 B：DISCOVERSE Real2Sim 仿真环境]]

---

## 1. 你电脑上装了什么

### 软件清单

| 组件 | 版本 | 路径/说明 |
|------|------|----------|
| ROS2 Humble | Humble | `/opt/ros/humble/` |
| MoveIt2 | 2.5.9 | 随 ROS2 安装 · 源码包：[[Airbot-Play-G2 安装包/AIRBOT-Play-Hardware-with-Moveit2-feature-humble.zip\|MoveIt2 源码]] |
| arm-sdk（Python SDK） | 5.2.2 | 虚拟环境 `~/Discover_projects/arm-venvs/airbot-venv-5.2.2` · 安装包：[[Airbot-Play-G2 安装包/arm_sdk-5.2.2-py3-none-any.whl\|arm_sdk wheel]] |
| airbot-arm（控制服务） | 5.2.2 | `/usr/bin/airbot-arm` · 安装包：[[Airbot-Play-G2 安装包/airbot-arm_5.2.2_amd64.deb\|airbot-arm deb]] |
| airbot-configure（CAN 驱动） | 5.2.1.6-1 | 自动创建 `can0` 接口 · 安装包：[[Airbot-Play-G2 安装包/airbot-configure_5.2.1.6-1_all.deb\|airbot-configure deb]] |
| airbot_py（旧版 SDK） | 5.1.6 | 虚拟环境 `~/Discover_projects/arm-venvs/airbot-venv-5.1.6` · 安装包：[[Airbot-Play-G2 安装包/airbot_py-5.1.6-py3-none-any.whl\|airbot_py wheel]] |
| Docker 镜像 | 5.1.6 | `airbot-runtime:5.1.6` |
| ROS2 工作空间 | - | `~/Discover_projects/ros2_ws/airbot_play_moveit2/` · 源码包：[[Airbot-Play-G2 安装包/airbot_hardware_sdk_humble_AMD64.zip\|ROS2 HW SDK]] |

### ROS2 工作空间包含的包

| 包名 | 用途 |
|------|------|
| `airbot_play` | 核心功能包 |
| `airbot_play_description` | URDF 模型 |
| `airbot_play_movit_config` | MoveIt2 配置（含所有 launch 文件） |
| `airbot_play_msgs` | 消息定义 |

### 关键文件位置

| 文件 | 路径 |
|------|------|
| 本教程 | `~/Discover_projects/docs/AIRBOT-Play-G2-使用教程.md` |
| 老师 SOP（Jazzy 版） | `~/桌面/SOP.md` |
| 交接文档 | `~/Discover_projects/docs/HANDOFF.md` |
| ROS2 工作空间 | `~/Discover_projects/ros2_ws/airbot_play_moveit2/` |

---

## 2. 三条路径：选哪个？

```
┌──────────────────────────────────────────────────────┐
│                  你想做什么？                          │
├──────────────────┬──────────────────┬────────────────┤
│  路径 A：仿真     │ 路径 B：真机直控   │ 路径 C：真机+MoveIt │
│  (不动真机)       │ (arm-sdk)        │ (ROS2 规划)    │
├──────────────────┼──────────────────┼────────────────┤
│ 用途：            │ 用途：            │ 用途：          │
│ 学习 MoveIt2      │ 直接写 Python     │ 用 MoveIt2 做  │
│ 测试运动规划      │ 控制机械臂        │ 路径规划控制真机 │
│ 不怕撞坏东西      │ 键盘控制/示教     │ RViz 可视化    │
├──────────────────┼──────────────────┼────────────────┤
│ 需要：            │ 需要：            │ 需要：          │
│ ✅ ROS2 Humble    │ ✅ USB 连接       │ ✅ USB 连接     │
│ ✅ 工作空间       │ ✅ 24V 电源       │ ✅ 24V 电源     │
│ ❌ 不需要 USB     │ ✅ can0 接口      │ ✅ can0 接口    │
│ ❌ 不需要电源     │ ✅ airbot-arm     │ ✅ airbot-arm   │
│ ❌ 不需要airbot   │                  │ ✅ ROS2 Humble  │
│   -arm 服务       │                  │ ✅ 工作空间     │
├──────────────────┼──────────────────┼────────────────┤
│ 启动命令：        │ 启动命令：        │ 启动命令：      │
│ demo.launch.py    │ Python 脚本      │ movit_to_airbot│
│                   │ (arm_sdk)        │ .launch.py     │
└──────────────────┴──────────────────┴────────────────┘
```

### 快速判断

- **只想看看机械臂长什么样、学 MoveIt** → 路径 A
- **想用 Python 直接控制真机动** → 路径 B
- **想用 MoveIt 规划路径控制真机** → 路径 C

### SDK 版本说明

| SDK | 虚拟环境 | 启动方式 | 用途 |
|-----|---------|---------|------|
| arm-sdk 5.2.2（推荐） · [[Airbot-Play-G2 安装包/arm_sdk-5.2.2-py3-none-any.whl\|📦]] | `~/Discover_projects/arm-venvs/airbot-venv-5.2.2` | `sudo airbot-arm ...` | Python API 编程控制 |
| airbot_py 5.1.6（旧版） · [[Airbot-Play-G2 安装包/airbot_py-5.1.6-py3-none-any.whl\|📦]] | `~/Discover_projects/arm-venvs/airbot-venv-5.1.6` | `airbot_fsm ...`（Docker） | 键盘控制 |

> [!warning] 不要混用
> 5.2.2 用 `airbot-arm` 服务，5.1.6 用 `airbot_fsm` 服务，不能同时运行。

---

## 3. 路径 A：ROS2 仿真（不动真机）

这条路径用 `FakeSystem` 模拟机械臂，在 RViz 里可视化，**不需要连接真机**。

### 前提条件

- [x] ROS2 Humble 已安装
- [x] 工作空间已编译

### 启动步骤

```bash
# 终端：加载环境并启动仿真
source /opt/ros/humble/setup.bash
source ~/Discover_projects/ros2_ws/airbot_play_moveit2/install/setup.bash
ros2 launch airbot_play_movit_config demo.launch.py
```

### 启动后你会看到

- **RViz 窗口**：显示机械臂 3D 模型
- **终端日志**：显示 controller_manager、joint_state_broadcaster 等节点启动

### 在 RViz 里操作

1. 左侧面板 → **MotionPlanning**
2. **Planning** 标签页 → 选择 `manipulator` 规划组
3. 拖动机械臂模型到目标位置
4. 点击 **Plan** 预览路径
5. 点击 **Plan & Execute** 执行运动（仿真中执行）

### 可用的 ROS2 命令

```bash
# 查看节点
ros2 node list

# 查看控制器状态
ros2 control list_controllers

# 查看关节状态
ros2 topic echo /joint_states
```

### 已知问题

- 首次启动 RViz 可能闪退（rviz2 与 move_group 的启动竞争），重新运行即可

---

## 4. 路径 B：真机直控（arm-sdk 5.2.2）

> [!tip] 相关安装包
> - [[Airbot-Play-G2 安装包/arm_sdk-5.2.2-py3-none-any.whl\|arm-sdk 5.2.2 Python SDK]]
> - [[Airbot-Play-G2 安装包/airbot-arm_5.2.2_amd64.deb\|airbot-arm 5.2.2 控制服务]]

这条路径用 `arm-sdk 5.2.2` 的 Python API 直接控制真机，**不经过 ROS2**。

### 前提条件

- USB-2 Type-C 线连接电脑和机械臂底座
- 24V 电源已接通
- 灯带为白色呼吸（USB 已连接）

### 第 1 步：确认 CAN 接口

```bash
ip link show can0
```

应该看到 `state UP`。如果没有，检查 USB 连接或重启后再试。

### 第 2 步：启动控制服务

```bash
sudo airbot-arm -i can0 -t airbot_play_g2
```

等待日志出现 `gRPC server listening on 0.0.0.0:50051`，灯带变为**绿色常亮**。

> [!warning] 保持终端开启
> 不要关闭这个终端。

### 第 3 步：在新终端运行 Python 脚本

```bash
source ~/Discover_projects/arm-venvs/airbot-venv-5.2.2/bin/activate
python3 your_script.py
```

### 快速测试：查看状态（不动手）

```python
# test_status.py — 安全，不会让机械臂动
from arm_sdk import AirbotClient

with AirbotClient() as arm:
    # 服务状态
    state = arm.get_service_state()
    print("服务状态:", state.service_state)   # True = 正常
    print("状态机:", state.fsm_state)          # Idle = 空闲

    # 关节角度
    joints = arm.get_arm_joint_state()
    print("关节角度 (弧度):", joints.angles)
    print("关节速度:", joints.velocities)
    print("关节电流:", joints.efforts)

    # 末端位姿
    pose = arm.get_end_pose()
    print("位置 (x,y,z):", pose.position)
    print("姿态 (rx,ry,rz):", pose.orientation)

    # 电机状态
    motors = arm.get_arm_motor_state()
    print("电机温度:", motors.motor_temperatures)
    print("错误码:", motors.error_ids)  # 全 0 = 正常

    # 夹爪状态
    eef = arm.get_eef_joint_state()
    print("夹爪位置:", eef.angles)
```

### 快速测试：重力补偿（手动拖动）

```python
# gravity_comp.py — 关节变松，可以用手拖动
from arm_sdk import AirbotClient
import time

with AirbotClient() as arm:
    arm.acquire_control()
    arm.enter_gravity_compensation_mode()

    print("已进入重力补偿模式，可以手动拖动机械臂")
    print("按 Ctrl+C 退出")
    # 灯带会变成紫色呼吸

    try:
        while True:
            joints = arm.get_arm_joint_state()
            print(f"角度: {[f'{a:.3f}' for a in joints.angles]}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n退出")
```

### 快速测试：关节运动

```python
# move_test.py — 低速运动测试
from arm_sdk import AirbotClient, Controller, ArmControlOptions

with AirbotClient() as arm:
    arm.acquire_control()
    arm.switch_controller(Controller.planning_control)

    options = ArmControlOptions()
    options.velocity_scaling_factor = 0.1  # 非常慢，安全

    # 移动 J5 关节一个小角度
    arm.move_joint([0.0, 0.0, 0.0, 0.0, 0.3, 0.0], options)
    print("运动完成")
```

### 快速测试：夹爪控制

```python
# gripper_test.py — 打开/关闭夹爪
from arm_sdk import AirbotClient, Controller, ArmControlOptions
import time

with AirbotClient() as arm:
    arm.acquire_control()
    arm.switch_controller(Controller.direct_control)

    options = ArmControlOptions()
    options.eef_eff = 6.0  # 夹爪电流阈值
    arm.set_eef_speed(3.14)

    # 打开夹爪
    arm.move_eef(0.072, options)
    print("夹爪已打开")
    time.sleep(1)

    # 关闭夹爪
    arm.move_eef(0.0, options)
    print("夹爪已关闭")
```

### 运行官方例程

```bash
source ~/Discover_projects/arm-venvs/airbot-venv-5.2.2/bin/activate

# 查看所有例程
arm-sdk examples list

# 运行键盘控制
arm-sdk examples run airbot_example_keyboard_control_joint

# 运行重力补偿
arm-sdk examples run airbot_example_gravity_compensation

# 运行关节运动
arm-sdk examples run airbot_example_move_joint_PTP

# 运行末端运动
arm-sdk examples run airbot_example_move_end_pose_PTP
```

### 停止服务

在运行 `airbot-arm` 的终端按 `Ctrl+C`，机械臂会自动回零。

---

## 5. 路径 C：真机 + MoveIt2 规划控制

> [!tip] 相关安装包
> - [[Airbot-Play-G2 安装包/airbot-arm_5.2.2_amd64.deb\|airbot-arm 5.2.2 控制服务]]
> - [[Airbot-Play-G2 安装包/AIRBOT-Play-Hardware-with-Moveit2-feature-humble.zip\|MoveIt2 工作空间源码]]
> - [[Airbot-Play-G2 安装包/airbot_hardware_sdk_humble_AMD64.zip\|ROS2 Hardware SDK]]

这条路径结合 ROS2 MoveIt2 和真机，用 RViz 做可视化规划，控制真机运动。

### 前提条件

- USB-2 Type-C 线连接电脑和机械臂底座
- 24V 电源已接通
- `can0` 接口存在
- ROS2 Humble + 工作空间已编译

### 第 1 步：启动控制服务

```bash
sudo airbot-arm -i can0 -t airbot_play_g2
```

等待灯带变为绿色常亮。

> [!warning] 保持终端开启
> 不要关闭这个终端。

### 第 2 步：启动 MoveIt2 + 真机

```bash
# 新终端
source /opt/ros/humble/setup.bash
source ~/Discover_projects/ros2_ws/airbot_play_moveit2/install/setup.bash
ros2 launch airbot_play_movit_config movit_to_airbot.launch.py
```

### 启动后你会看到

- **RViz 窗口**：显示真机的实时状态
- **终端日志**：显示 MoveIt2 和 ros2_control 节点启动

### 在 RViz 里操作

1. 左侧面板 → **MotionPlanning**
2. **Planning** 标签页 → 选择 `manipulator` 规划组
3. 拖动机械臂模型到目标位置
4. 点击 **Plan** 预览路径（确认安全后）
5. 点击 **Plan & Execute** 控制真机运动

### 同时用 ROS2 命令监控

```bash
# 另开终端
source /opt/ros/humble/setup.bash
source ~/Discover_projects/ros2_ws/airbot_play_moveit2/install/setup.bash

# 查看控制器状态
ros2 control list_controllers

# 查看关节状态
ros2 topic echo /joint_states

# 查看节点
ros2 node list
```

---

## 6. 附：5.1.6 SDK 键盘控制（旧版）

> [!tip] 相关安装包
> - [[Airbot-Play-G2 安装包/airbot_py-5.1.6-py3-none-any.whl\|airbot_py 5.1.6 旧版 SDK]]
> - [[Airbot-Play-G2 安装包/airbot-configure_5.2.1.6-1_all.deb\|airbot-configure CAN 驱动]]
> - [[Airbot-Play-G2 安装包/AIRBOT Play V5.1.6 官方资料索引\|官方 PDF 归档]]

这是旧版 `airbot_py 5.1.6` 的键盘控制方式，使用 Docker 运行。与前面的 `arm-sdk 5.2.2` 是两套不同的 SDK，**不要混用**。

> [!warning] 版本边界
> 本节仅适用于 `airbot_py 5.1.6`、`airbot_fsm`/`airbot_server` 这套旧版工具。当前 `arm-sdk 5.2.2` 请使用第 4 节的 `airbot-arm` 流程。

| SDK | 虚拟环境 | 启动方式 |
|-----|---------|---------|
| arm-sdk 5.2.2（推荐） | `~/Discover_projects/arm-venvs/airbot-venv-5.2.2` | `sudo airbot-arm ...` |
| airbot_py 5.1.6（旧版） | `~/Discover_projects/arm-venvs/airbot-venv-5.1.6` | `airbot_fsm ...`（Docker） |

### 启动步骤

**终端 1** — 启动驱动（CAN 接口通常已由系统自动配置）：

```bash
airbot_fsm -i can0 -p 50051
```

> [!note] 关于 CAN 接口
> 你的系统已配置 udev 规则，USB CAN 适配器插入后会自动启动 `can0` 接口（波特率 1Mbps）。如果 `airbot_fsm` 报错找不到 can0，再手动执行：
> ```bash
> sudo ip link set can0 type can bitrate 1000000
> sudo ip link set up can0
> ```

首次启动会下载 Docker 镜像，等待出现：

```
All arm controllers are ready
Transition activate for sdk_server succeeded
```

**终端 2** — 键盘控制：

```bash
unset PYTHONPATH PYTHONHOME
source ~/Discover_projects/arm-venvs/airbot-venv-5.1.6/bin/activate
python -m airbot_examples.task_kbd_ctrl -p 50051
```

出现 `Press Enter to continue...` 时，确认机械臂周围无人、无障碍物后按回车。之后终端清屏是正常现象，程序已进入键盘输入模式。

### 键盘按键

| 按键 | 操作 |
|------|------|
| `Enter` | 切换 SLOW/DEFAULT 速度档 |
| `Space` | 切换关节速度/笛卡尔速度控制 |
| `Tab` | 移动到预设初始姿态；初次操作不要按 |
| `w`/`s` | X 轴前后平移 |
| `a`/`d` | Y 轴左右平移 |
| `q`/`e` | Z 轴上下平移 |
| `o`/`u` | 绕 X 轴旋转 |
| `i`/`k` | 绕 Y 轴旋转 |
| `j`/`l` | 绕 Z 轴旋转 |
| `[` / `]` | 闭合/打开夹爪 |
| `z` | 退出 |
| `Ctrl+C` | 立即停止 |

#### 关节速度控制（SERVO_JOINT_VEL）

按 `Space` 切换到关节速度模式后，以下按键分别控制对应关节的正向或反向运动：

| 按键 | 操作 |
|------|------|
| `1` / `2` | J1 正向 / 反向 |
| `3` / `4` | J2 正向 / 反向 |
| `5` / `6` | J3 正向 / 反向 |
| `7` / `8` | J4 正向 / 反向 |
| `9` / `0` | J5 正向 / 反向 |
| `-` / `=` | J6 正向 / 反向 |

### 停止

1. 键盘客户端按 `z` 或 `Ctrl+C`
2. `airbot_fsm` 终端按 `Ctrl+C`

---

## 7. 认识你的机械臂

### 硬件组成

```
       ┌─── J6（腕旋转）
       │ ┌─ J5（腕摆动）
       │ │ ┌ J4（前臂）
       │ │ │
    ┌──┴─┴─┴──┐
    │  末端板  │ ← G2 夹爪连接在这里
    └────┬────┘
         │ J3（肘部）
    ┌────┴────┐
    │  连杆2  │
    └────┬────┘
         │ J2（肩部）
    ┌────┴────┐
    │  连杆1  │
    └────┬────┘
         │ J1（底座旋转）
    ┌────┴────┐
    │  底座   │ ← USB-2 和电源在这里
    └─────────┘
```

### 关键接口

| 接口 | 用途 |
|------|------|
| **USB-2（Type-C）** | 控制通信，连接电脑 |
| **USB-1（Type-C）** | 末端相机数据（本教程不用） |
| **24V 电源** | 供电 |
| **底座按钮** | 零位校准用 |

### 灯带状态速查

| 灯效 | 含义 | 你需要做的 |
|------|------|-----------|
| 🟡 黄灯常亮 | 自检中 | 等待完成 |
| 🟡 黄灯闪烁 | 需要零位校准 | 长按底座按钮 3 秒 |
| 🔴 红灯常亮 | 自检失败/限位 | 急停-恢复解除（见第 8 节） |
| ⚪ 白灯常亮 | 等待 USB 连接 | 插上 USB-2 |
| ⚪ 白色呼吸 | USB 已连接，等待服务 | 启动 airbot-arm 或 airbot_fsm |
| 🟢 绿色波浪 | 服务初始化中 | 等待变成绿色常亮 |
| 🟢 绿色常亮 | **正常工作** | 可以开始控制 |
| 🟣 紫色呼吸 | 重力补偿模式 | 正常，可手动拖动 |

### 首次上电与零位校准

1. 固定机械臂底座，清空工作范围；连接 USB-2 和 24V 电源后，等待自检结束。
2. 仅当灯带黄色闪烁、提示零位丢失时，长按底座按钮约 3 秒，听到提示声后进入手动调整状态。
3. 缓慢对齐机械臂连杆上的零位标记；J4、J5、J6 可保持任意位置。
4. 再按一次底座按钮，听到提示声即完成校零。USB 已连接时，灯带应恢复为白色呼吸。

旧版操作图示与原文见 [[Airbot-Play-G2 安装包/AIRBOT Play V5.1.6 官方资料索引\|V5.1.6 官方资料索引]]。当前 V5.2.2 的控制服务仍应按第 4 节启动。

---

## 8. 安全守则

> [!danger] 必须遵守
> 1. **固定机械臂**：底座必须用夹具固定在桌面，不能悬空或手持
> 2. **清空工作空间**：机械臂最大工作半径 647mm 内不能有人和物品
> 3. **手指远离关节**：运动时不要把手放在关节或夹爪附近
> 4. **准备急停**：
>    - arm-sdk 5.2.2：`arm.set_arm_emergency_stop(True)`
>    - 5.1.6 键盘控制：按 `z` 或 `Ctrl+C`
>    - 通用：直接拔电源（最后手段）
> 5. **先慢后快**：第一次运行新脚本时，把速度设得很低（如 0.1）

> [!danger] 绝对不要
> - 在机械臂运动时触碰它
> - 在没有固定底座的情况下运行运动程序
> - 不理解参数含义就运行例程
> - 同时运行两个 SDK 客户端（会争夺控制权）
> - 同时运行 `airbot-arm` 和 `airbot_fsm`（会争夺 CAN 总线）
> - 在关节接近限位时继续往同方向运动

### 紧急情况

```python
# arm-sdk 5.2.2 急停
from arm_sdk import AirbotClient

with AirbotClient() as arm:
    arm.acquire_control()
    arm.set_arm_emergency_stop(True)  # 急停
```

急停后恢复：

```python
    arm.set_arm_emergency_stop(False)  # 恢复
```

红灯/限位恢复（标准方法）：

```python
from arm_sdk import AirbotClient
import time

with AirbotClient() as arm:
    arm.acquire_control()
    arm.set_arm_emergency_stop(True)   # 急停
    time.sleep(5.0)                    # 等待 5 秒
    arm.set_arm_emergency_stop(False)  # 恢复
```

---

## 9. 常见问题排查

### 通用问题

| 问题 | 原因 | 解决方法 |
|------|------|---------|
| `can0` 不存在 | USB 未连接 | 插上 USB-2，检查 `/dev/ttyCAN0` |
| 灯带白色呼吸 | USB 已连，服务未启动 | 启动 `airbot-arm` 或 `airbot_fsm` |
| 灯带黄色闪烁 | 需要零位校准 | 长按底座按钮 3 秒 |
| 灯带红色常亮 | 限位/状态异常 | 急停-恢复（见第 8 节） |
| `Connection refused` | 服务没启动 | 检查 `airbot-arm` 或 `airbot_fsm` 终端是否在运行 |

### 路径 A 问题（仿真）

| 问题 | 原因 | 解决方法 |
|------|------|---------|
| RViz 闪退 | rviz2 与 move_group 启动竞争 | 重新运行即可 |
| 控制器未加载 | 工作空间未 source | 确认 source 了 install/setup.bash |

### 路径 B 问题（arm-sdk 5.2.2）

| 问题 | 原因 | 解决方法 |
|------|------|---------|
| `arm-sdk: command not found` | 没激活 venv | `source ~/Discover_projects/arm-venvs/airbot-venv-5.2.2/bin/activate` |
| `No module named 'arm_sdk'` | PYTHONPATH 干扰 | `env -u PYTHONPATH -u PYTHONHOME python xxx.py` |
| `Failed to acquire control` | 控制权被占用 | 关闭其他 SDK 客户端 |
| 夹爪红灯 | 末端未识别 | 确认用 `airbot_play_g2` 启动服务 |

### 路径 C 问题（MoveIt2 + 真机）

| 问题 | 原因 | 解决方法 |
|------|------|---------|
| MoveIt 连接失败 | airbot-arm 未启动 | 先启动 airbot-arm 服务 |
| 规划失败 | 目标不可达 | 检查关节限位 |
| 执行不动 | 控制器未激活 | `ros2 control list_controllers` 检查状态 |

### 5.1.6 问题

| 问题 | 原因 | 解决方法 |
|------|------|---------|
| `airbot_fsm: 未找到命令` | 命令名错误 | 用下划线：`airbot_fsm` |
| `No module named 'airbot_examples'` | 未激活 5.1.6 环境 | 执行 `unset` + `source` 三行命令 |
| 键盘程序回车后终端空白 | 进入原始键盘输入模式 | 正常现象，直接按按键 |

---

## 10. API 速查表

### 连接与控制权

```python
from arm_sdk import AirbotClient, Controller, ArmControlOptions, CartesianPose

with AirbotClient(host="localhost", port=50051) as arm:
    arm.acquire_control()           # 获取控制权
    arm.release_control()           # 释放控制权
    arm.switch_controller(Controller.xxx)  # 切换控制模式
```

### 控制模式

| 模式 | 适用场景 |
|------|---------|
| `Controller.direct_control` | 直控电机，低延迟 |
| `Controller.servo_control` | 遥操作，250Hz 高频 |
| `Controller.planning_control` | 带轨迹规划（PTP/直线/圆弧） |
| `Controller.mit_control` | 力矩和位置混合控制 |

### 状态查询（不需要控制权）

```python
arm.get_service_state()     # 服务状态
arm.get_firmware_info()     # 固件信息
arm.get_arm_joint_state()   # 关节状态（角度/速度/电流）
arm.get_arm_motor_state()   # 电机状态（温度/错误码）
arm.get_end_pose()          # 末端位姿
arm.get_eef_joint_state()   # 夹爪关节状态
arm.get_eef_motor_state()   # 夹爪电机状态
```

### 运动控制（需要控制权）

```python
# 关节运动
arm.move_joint(pos, options)                    # 单点
arm.move_joint_waypoints(waypoints, options)    # 多点路径

# 末端运动
arm.move_end_pose(pose, options)                # 点到点
arm.move_end_pose_linear(start, target, options)    # 直线
arm.move_end_pose_circle(start, path, target, options)  # 圆弧

# 夹爪
arm.move_eef(0.072, options)  # 打开（0.072=全开，0.0=全关）

# 速度设置
arm.set_arm_speed([1.0]*6)    # 各关节最大速度
arm.set_eef_speed(3.14)       # 夹爪最大速度

# 特殊功能
arm.enter_gravity_compensation_mode()  # 重力补偿
arm.return_zero()                       # 回零
arm.set_arm_emergency_stop(True)        # 急停
```

### ArmControlOptions 参数

```python
options = ArmControlOptions()
options.velocity_scaling_factor = 0.3     # 速度比例（0.01~1.0）
options.acceleration_scaling_factor = 0.3 # 加速度比例
options.eef_eff = 6.0                     # 夹爪电流限制（0~20）
options.blocking = False                  # 是否阻塞等待完成
```

---

## 11. 关节限位参考

### 机械臂关节（弧度）

| 关节 | 最小值 | 最大值 | 说明 |
|------|--------|--------|------|
| J1 | -3.14 | 2.09 | 底座旋转 |
| J2 | -2.96 | 0.17 | 肩部 |
| J3 | -0.087 | 3.14 | 肘部 |
| J4 | -3.01 | 3.01 | 前臂旋转 |
| J5 | -1.76 | 1.76 | 腕摆动 |
| J6 | -3.01 | 3.01 | 腕旋转 |

### G2 夹爪

| 参数 | 值 | 说明 |
|------|-----|------|
| 最小值 | 0.0 | 完全关闭 |
| 最大值 | 0.072 | 完全打开 |

### 弧度与角度换算

```
角度 = 弧度 × (180 / π)
弧度 = 角度 × (π / 180)

常用值：
  0°    = 0.0 rad
  45°   = 0.785 rad
  90°   = 1.571 rad
  180°  = 3.142 rad
```

---

## 附录 A：官方资源

- 📦 **本地离线安装包**：[[Airbot-Play-G2 安装包/]]
- 📦 **SDK 安装配置指南**：[[Airbot-Play-G2 安装包/AIRBOT-PLAY-SDK-安装配置指南.zh-CN.md\|AIRBOT-PLAY-SDK-安装配置指南]]
- 📦 **V5.1.6 官方资料归档**：[[Airbot-Play-G2 安装包/AIRBOT Play V5.1.6 官方资料索引\|软件安装、初次运行与键盘控制]]
- 📖 官方文档：[airbot-play](https://docs.airbots.online/airbot-play/)
- 📖 SDK API 参考：[API Reference](https://docs.airbots.online/airbot-play/sdk/api/reference.html)
- 📖 **使用示例（推荐）**：[Examples](https://docs.airbots.online/airbot-play/sdk/api/examples.html)
- 📖 控制模式说明：[Control Modes](https://docs.airbots.online/airbot-play/sdk/concepts/control-modes.html)
- 📖 关节限位说明：[Joint Limits](https://docs.airbots.online/airbot-play/sdk/quickstart/joint-limits.html)
- 📖 灯带状态说明：[Arm Status LED](https://docs.airbots.online/airbot-play/sdk/concepts/arm-status-led.html)

---

## 附录 B：DISCOVERSE Real2Sim 仿真环境

### 简介

[DISCOVERSE](https://github.com/discoverse-dev/DISCOVERSE) 是基于 3D Gaussian Splatting 的统一仿真框架，用于 Real2Sim2Real 机器人学习（IROS 2025）。支持 `airbot_play` 等多种机器人。

### 安装位置

```
/home/aphelios/Discover_projects/discoverse_sim/
```

虚拟环境：

```
/home/aphelios/Discover_projects/discoverse_sim/discoverse-venv/
```

### 启动方式

```bash
cd /home/aphelios/Discover_projects/discoverse_sim
source discoverse-venv/bin/activate
```

### 已安装的核心组件

| 组件 | 版本 |
|------|------|
| DISCOVERSE | v1.9.0 |
| MuJoCo | 3.10.0 |
| NumPy | 2.2.6 |
| OpenCV | 5.0.0 |
| SciPy | 1.15.3 |
| Matplotlib | 3.10.9 |

### 可选模块（按需安装）

| 模块 | 安装命令 | 用途 |
|------|---------|------|
| 3DGS 渲染 | `pip install -e ".[gs]"` | Real2Sim 高保真渲染 |
| LiDAR | `pip install -e ".[lidar]"` | 激光雷达仿真 |
| ACT 模仿学习 | `pip install -e ".[act]"` | 策略学习 |
| XML 场景编辑器 | `pip install -e ".[xml-editor]"` | 场景设计 |

> [!warning] 关于可选模块
> 可选模块需要 PyTorch（`pip install -e ".[gs]"` 会自动拉取）。
> RTX 3050 Laptop 只有 4GB 显存，3DGS 渲染可能吃紧，基础 MuJoCo 仿真没问题。

### 国内加速

3DGS 模型从 Hugging Face 下载，国内可设置镜像：

```bash
export HF_ENDPOINT="https://hf-mirror.com"
```

### 官方文档

- 📖 GitHub：[DISCOVERSE](https://github.com/discoverse-dev/DISCOVERSE)
- 📖 中文 README：[README_zh.md](https://github.com/discoverse-dev/DISCOVERSE/blob/main/README_zh.md)

