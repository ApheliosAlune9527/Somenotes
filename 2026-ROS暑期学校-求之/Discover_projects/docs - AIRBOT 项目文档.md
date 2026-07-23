---
title: docs - AIRBOT 项目文档
tags:
  - AIRBOT
  - 文档
  - SOP
created: 2026-07-23
---

# docs - AIRBOT 项目文档

> [!info] 路径
> `/home/aphelios/Discover_projects/docs/`

## 文件清单

| 文件 | 大小 | 说明 |
|------|------|------|
| `AIRBOT-Play-G2-使用教程.md` | 24K | 完整使用教程（路径 A/B/C、API 速查表等） |
| `AIRBOT-PLAY-SDK-安装配置指南.zh-CN.md` | 34K | 官方 SDK 安装配置指南（中文版） |
| `HANDOFF.md` | 18K | 任务交接文档（安装过程全记录） |
| `SOP.md` | 18K | 课程操作 SOP（Ubuntu 24.04 + Jazzy 版） |

## 各文件简介

### AIRBOT-Play-G2-使用教程.md

已同步至 Obsidian 笔记：[[Airbot-Play-G2 使用教程]]

覆盖内容：
- 软件清单与路径说明
- 三条使用路径（仿真 / 真机直控 / MoveIt2 真机）
- arm-sdk 5.2.2 Python API 速查
- 关节限位、安全守则、常见问题排查
- DISCOVERSE Real2Sim 仿真环境简介

### AIRBOT-PLAY-SDK-安装配置指南.zh-CN.md

官方中文安装指南，覆盖：
- 系统环境检查
- `airbot-arm` deb 包安装
- arm-sdk Python wheel 安装
- CAN 接口配置（udev + systemd）
- 真机验证步骤

> [!tip] 离线备份
> 安装包目录下有一份副本：[[Airbot-Play-G2 安装包/AIRBOT-PLAY-SDK-安装配置指南.zh-CN.md]]

### HANDOFF.md

任务交接文档，记录了从零开始安装的完整过程：

1. **环境盘点** — 确认 Ubuntu 22.04、Python 3.10、无旧版 AIRBOT 软件
2. **基础依赖安装** — can-utils、Python venv
3. **SDK 安装** — `airbot-arm_5.2.2_amd64.deb` + `arm_sdk-5.2.2-py3-none-any.whl`
4. **真机连接验证** — slcan 内核模块、gRPC 服务启动
5. **夹爪问题修复** — 确认 G2 型号，以 `airbot_play_g2` 模式启动
6. **CAN 自动配置** — `airbot-configure` deb 包，udev 规则 + systemd 服务

### SOP.md

课程标准操作流程，适用于 **Ubuntu 24.04 + ROS2 Jazzy** 环境（老师原版）：
- 仿真环境安装
- MoveIt2 Demo 操作（Plan / Plan & Execute）
- 真机模式操作
- 常见问题

> [!note] 环境差异
> 本机已适配为 Ubuntu 22.04 + ROS2 Humble，与 SOP 原始环境（Jazzy）不同。
