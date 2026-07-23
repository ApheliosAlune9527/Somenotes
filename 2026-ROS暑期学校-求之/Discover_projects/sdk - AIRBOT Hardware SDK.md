---
title: sdk - AIRBOT Hardware SDK
tags:
  - AIRBOT
  - SDK
  - ROS2
created: 2026-07-23
---

# sdk - AIRBOT Hardware SDK

> [!info] 路径
> `/home/aphelios/Discover_projects/sdk/`

## 文件清单

| 文件 | 大小 | 说明 |
|------|------|------|
| `airbot_hardware_sdk_humble_AMD64.zip` | 3.0M | ROS2 Humble 硬件 SDK（AMD64 架构） |

## 说明

这是 AIRBOT Play 的 **ROS2 硬件接口 SDK**，用于将 AIRBOT 机械臂接入 ROS2 的 `ros2_control` 框架。

### 与 arm-sdk 的区别

| 包 | 用途 | 使用场景 |
|----|------|---------|
| **arm-sdk 5.2.2**（Python wheel） | 直接用 Python API 控制机械臂 | [[Airbot-Play-G2 使用教程#4. 路径 B：真机直控（arm-sdk 5.2.2）\|路径 B：真机直控]] |
| **ROS2 Hardware SDK**（此包） | 接入 `ros2_control`，配合 MoveIt2 | [[Airbot-Play-G2 使用教程#5. 路径 C：真机 + MoveIt2 规划控制\|路径 C：MoveIt2 真机]] |

### 安装包位置

> [!tip] 离线备份
> [[Airbot-Play-G2 安装包/airbot_hardware_sdk_humble_AMD64.zip]]
