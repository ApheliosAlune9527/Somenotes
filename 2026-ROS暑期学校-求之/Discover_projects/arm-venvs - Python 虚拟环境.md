---
title: arm-venvs - Python 虚拟环境
tags:
  - AIRBOT
  - Python
  - venv
created: 2026-07-23
---

# arm-venvs - Python 虚拟环境

> [!info] 路径
> `/home/aphelios/Discover_projects/arm-venvs/`

## 环境列表

| 虚拟环境 | Python 版本 | SDK 版本 | 用途 |
|---------|------------|---------|------|
| `airbot-venv-5.2.2` | 3.10 | arm-sdk 5.2.2（推荐） | Python API 编程控制 |
| `airbot-venv-5.1.6` | 3.10 | airbot_py 5.1.6（旧版） | 键盘控制（Docker） |

## airbot-venv-5.2.2

### 激活方式

```bash
source ~/Discover_projects/arm-venvs/airbot-venv-5.2.2/bin/activate
```

### 已安装的核心包

| 包名 | 版本 | 说明 |
|------|------|------|
| `arm_sdk` | 5.2.2 | AIRBOT Python SDK |
| `grpcio` | — | gRPC 通信 |
| `protobuf` | — | Protocol Buffers |
| `typer` | — | CLI 工具 |
| `loguru` | — | 日志 |

### 对应安装包

- [[Airbot-Play-G2 安装包/arm_sdk-5.2.2-py3-none-any.whl|arm_sdk wheel]]
- [[Airbot-Play-G2 安装包/airbot-arm_5.2.2_amd64.deb|airbot-arm deb]]

---

## airbot-venv-5.1.6

> [!warning] 旧版环境
> 5.1.6 使用 Docker 容器运行 `airbot_fsm` 服务，与 5.2.2 的 `airbot-arm` 服务**不能同时运行**。

### 激活方式

```bash
unset PYTHONPATH PYTHONHOME
source ~/Discover_projects/arm-venvs/airbot-venv-5.1.6/bin/activate
```

### 已安装的核心包

| 包名 | 版本 | 说明 |
|------|------|------|
| `airbot_py` | 5.1.6 | 旧版 Python SDK |
| `airbot_proto` | — | Protobuf 定义 |
| `airbot_examples` | — | 官方例程（含键盘控制） |

### 对应安装包

- [[Airbot-Play-G2 安装包/airbot_py-5.1.6-py3-none-any.whl|airbot_py wheel]]

---

## 使用场景对照

| 场景 | 使用哪个环境 |
|------|------------|
| [[Airbot-Play-G2 使用教程#4. 路径 B：真机直控（arm-sdk 5.2.2）\|路径 B：真机直控]] | `airbot-venv-5.2.2` |
| [[Airbot-Play-G2 使用教程#6. 附：5.1.6 SDK 键盘控制（旧版）\|5.1.6 键盘控制]] | `airbot-venv-5.1.6` |
| [[Airbot-Play-G2 使用教程#10. API 速查表\|API 编程]] | `airbot-venv-5.2.2` |
