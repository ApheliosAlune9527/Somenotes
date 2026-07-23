---
title: Discover_projects 项目总览
tags:
  - AIRBOT
  - ROS2
  - DISCOVERSE
  - 项目结构
created: 2026-07-23
---

# Discover_projects 项目总览

> [!info] 路径
> `/home/aphelios/Discover_projects/`

## 目录结构

```
Discover_projects/
├── docs/              ← [[docs - AIRBOT 项目文档|项目文档]]（教程、SOP、交接文档）
├── sdk/               ← [[sdk - AIRBOT Hardware SDK|硬件 SDK 安装包]]
├── arm-venvs/         ← [[arm-venvs - Python 虚拟环境|Python 虚拟环境]]（5.2.2 & 5.1.6）
├── ros2_ws/           ← [[ros2_ws - ROS2 工作空间|ROS2 工作空间]]（MoveIt2 + AIRBOT）
└── discoverse_sim/    ← [[discoverse_sim - DISCOVERSE 仿真环境|DISCOVERSE 仿真环境]]
```

## 各模块关系

```
                    ┌──────────────┐
                    │  docs/       │ 教程 & 文档
                    └──────┬───────┘
                           │ 参考
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
  ┌───────────────┐ ┌────────────┐ ┌────────────────┐
  │ arm-venvs/    │ │ ros2_ws/   │ │ discoverse_sim/│
  │ Python SDK    │ │ MoveIt2    │ │ MuJoCo 仿真    │
  │ 真机直控      │ │ 真机/仿真   │ │ Real2Sim       │
  └───────┬───────┘ └─────┬──────┘ └───────┬────────┘
          │               │                │
          └───────┬───────┘                │
                  ▼                        ▼
           ┌──────────┐            ┌──────────────┐
           │ AIRBOT   │            │ DISCOVERSE   │
           │ 真机控制  │            │ 仿真学习      │
           └──────────┘            └──────────────┘
```

## 快速导航

| 子目录 | 说明 | 关键文件 |
|--------|------|---------|
| [[docs - AIRBOT 项目文档\|docs/]] | 安装教程、SOP、交接文档 | 4 个 Markdown 文件 |
| [[sdk - AIRBOT Hardware SDK\|sdk/]] | ROS2 硬件 SDK 安装包 | `airbot_hardware_sdk_humble_AMD64.zip` |
| [[arm-venvs - Python 虚拟环境\|arm-venvs/]] | arm-sdk 5.2.2 & airbot_py 5.1.6 环境 | 两个 Python venv |
| [[ros2_ws - ROS2 工作空间\|ros2_ws/]] | AIRBOT Play MoveIt2 工作空间 | 4 个 ROS2 包 |
| [[discoverse_sim - DISCOVERSE 仿真环境\|discoverse_sim/]] | 3DGS 仿真框架（IROS 2025） | 16 个示例 + 5 个策略 |
