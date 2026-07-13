1. 创建工作空间
![[Pasted image 20260710150130.png]]

2. 构建工作空间所有功能包
![[Pasted image 20260710150258.png]]
3. 构建单独功能包
![[Pasted image 20260710150314.png]]

4. 这个package.xml是控制包的依赖关系的
![[Pasted image 20260710150337.png]]

## 二、pkg 功能包的建立

# 🔍 ROS 2 2.2节「使用功能包组织 Python 节点」全景深度学习手册

本指南基于鱼香ROS（小鱼）的《ROS 2 机器人开发从入门到实践》第 2.2 节视频教程（B站视频 BV1ky411e7hp）进行深度提炼，融入了官方标准实践与高频避坑指南。

## 🎬 视频精华时间戳索引 (Video Timeline Index)

| 视频时间戳 | 章节名称 | 核心学习要点与实操指引 |
|---|---|---|
| 00:00 - 01:25 | 功能包核心概念引入 | 理解 Package 的存在意义：统一管理、松耦合、方便复用与社区分享 |
| 01:25 - 04:30 | ROS 2 包指令探秘 | 学习 ros2 pkg 体系，深入阅读 --help 掌握功能包构建选项的用法 |
| 04:30 - 07:15 | 创建 ament_python 包 | 实操 ros2 pkg create --build-type ament_python 并解读默认生成的文件 |
| 07:15 - 10:45 | 编写 Python 节点脚本 | ⭐ 避坑重灾区： 解析「双层同名文件夹」地雷，编写规范 of Python 节点代码 |
| 10:45 - 13:50 | 核心配置文件 | 配置修改 setup.py 的 entry_points 注册节点可执行入口，并在 package.xml 声明依赖 |
| 13:50 - 17:10 | colcon 编译机制 | 详解 colcon build 及产生的 build/、install/、log/ 三大目录的底层作用 |
| 17:10 - 20:30 | 环境加载与节点运行 | 深入理解 source 命令对 AMENT_PREFIX_PATH 的修改，并用 ros2 run 跑通节点 |
| 20:30 - 22:58 | 总结与课后进阶 | 知识梳理、关于在新终端中重新 source 的重要提示 |

## ⏳ ROS 2 功能包生命周期：这些文件是什么时候出现的？

初学者最容易混淆哪些文件是"生来就有"的，哪些是"编译出来"的。请看以下四个阶段的演变：

**【阶段一：空的工作空间】**

```
📁 chapt2_ws/
└── 📁 src/                     <--- 手动创建，此时里面空空如也
```

▼ 执行创建命令：`ros2 pkg create --build-type ament_python demo_python_pkg`

**【阶段二：功能包骨架生成】**（⭐ 你的问题：这些文件就是这一步生成的！）

```
📁 chapt2_ws/
└── 📁 src/
    └── 📁 demo_python_pkg/
        ├── 📄 package.xml       <--- 自动生成！功能包身份证
        ├── 📄 setup.py          <--- 自动生成！Python安装/入口配置文件
        ├── 📄 setup.cfg         <--- 自动生成！构建辅助文件
        ├── 📁 resource/         <--- 自动生成！
        └── 📁 demo_python_pkg/  <--- 自动生成！内层同名文件夹（目前只有一个空 __init__.py）
```

▼ 执行手动编写：你在内层同名文件夹下新建并编写节点代码

**【阶段三：手工编写代码】**

```
📁 chapt2_ws/
└── 📁 src/
    └── 📁 demo_python_pkg/
        └── 📁 demo_python_pkg/
            ├── 📄 __init__.py
            └── 📄 python_node.py <--- 手动新建！你的 Python 核心代码
```

▼ 执行编译命令：`colcon build`

**【阶段四：编译产物登场】**

```
📁 chapt2_ws/
├── 📁 src/                      <--- 这里的源码和配置文件依然保持原样
├── 📁 build/                    <--- 编译产生！编译过程的临时草稿纸
├── 📁 install/                  <--- 编译产生！系统运行真正去读取的最终成果区
└── 📁 log/                      <--- 编译产生！编译日志，报错了来这里查
```

## 🧠 核心概念剖析

### 1. 什么是 ROS 2 功能包 (Package)？

功能包是 ROS 2 中组织、编译和分享代码的最小单元。 在第 2.1 节中，我们直接编写了独立的 `.py` 文件运行，但在实际大型项目中，这样做无法实现工程化管理。功能包的核心优势在于：

- **松耦合设计**：将雷达驱动、路径规划、控制算法拆分为不同的包，修改其中一个不会影响其他。
- **统一构建**：通过统一指令（如 `colcon build`）一键编译、打包、定位所有关联的节点。
- **生态分享**：别人只需要下载你的功能包并将其放入工作空间，即可无缝编译和使用。

### 2. 构建类型：Python 包 vs C++ 包

不同于 ROS 1 混合使用 CMake 构建，ROS 2 为不同语言提供了专属的构建类型：

- **ament_python**：针对 Python 节点的构建系统。基于 Python 的 setuptools，无需编写 `CMakeLists.txt`，只需通过 `setup.py` 声明入口。
- **ament_cmake**：针对 C++ 节点的构建系统。基于标准的 CMake 流程，核心配置文件为 `CMakeLists.txt`。

## 📂 详细的图解流向与目录架构

### ⚠️ 新手致命地雷："双层同名文件夹" ASCII 图解

通过命令创建功能包时，ROS 2 默认会生成一个带有双层同名文件夹的工程结构。新手极易将节点写 in 第一层，导致编译后运行报错 `ModuleNotFoundError`。请严格按照下方图解放置你的 Python 脚本：

```
demo_python_pkg/                           <--- [外层] 功能包根目录
├── package.xml                            <--- 功能包清单文件（配置依赖）
├── setup.py                               <--- Python 构建脚本（配置节点注册入口）
├── setup.cfg                              <--- 构建配置文件
├── resource/                              <--- 资源文件夹（保存包索引，无需手动改动）
│   └── demo_python_pkg
├── test/                                  <--- 自动化测试用例目录
└── demo_python_pkg/                       <--- [内层] ⭐ 真正的 Python 模块目录 ⭐
    ├── __init__.py                        <--- Python 包初始化文件（留空，勿删！）
    └── python_node.py                     <--- ⭐ 开发者编写的代码必须且只能放在这里！
```

## 🔁 编译到运行的环境变量映射流程

ROS 2 不是通过文件路径直接查找节点的，而是依赖环境变量。以下是整个构建流程及变量变迁：

```
[ 编写源码 ]  -->  [ 运行 colcon build ] 
                         │
                         ├──> 生成 build/   (临时编译文件)
                         ├──> 生成 install/ (包含最终可执行文件和环境配置脚本)
                         └──> 生成 log/     (编译与调试日志)
                         │
[ 运行 source install/setup.bash ] 
                         │
                         └──> 将本地的 install/ 路径注入系统环境变量 AMENT_PREFIX_PATH
                         │
[ 运行 ros2 run demo_python_pkg python_node ]
                         │
                         └──> ROS 2 顺利在 AMENT_PREFIX_PATH 指向的路径中搜寻到该节点并运行
```

## 🛠️ colcon build 编译产物全景拆解（新手解惑）

运行 `colcon build` 后，工作空间中多出的 `build/`、`install/`、`log/` 目录以及里面密密麻麻的文件，它们在底层发挥着各自的作用：

### 1. build/ 目录：临时中转站（厨房的配菜区）

- **本质**：这里存放编译过程中的中间临时文件。
- **对于 Python 项目**：这里存储的是通过 Python setuptools 转化代码时的缓存（例如编译出的 `easy_install` 临时配置、各种 `.egg-info` 元数据）。
- **重要结论**：你完全不需要碰这个文件夹！ 如果你修改了代码但编译报错、或者想彻底重来，可以直接使用 `rm -rf build` 删掉它。它在下一次编译时会被重新自动创建。

### 2. install/ 目录：最终成果区（做好的菜，准备上桌）

这是最关键的文件夹。ROS 2 运行程序时，不是去读你写代码的那个工作空间（src），而是来这里寻找可执行程序。对于我们的 `demo_python_pkg` 而言，`install/` 下的目录树及核心文件作用如下：

```
install/
├── demo_python_pkg/                         # 👈 你的功能包最终生成的部署版本
│   ├── lib/
│   │   └── demo_python_pkg/
│   │       └── python_node                  # ⭐ 最终生成的可执行文件（其实是个加载你的 Python 代码的 Shell 脚本）
│   └── share/
│       ├── demo_python_pkg/
│       │   └── package.xml                  # 拷贝过来的包配置文件
│       └── ament_index/resource_index/packages/
│           └── demo_python_pkg              # 🌟 零字节文件（ROS 2 的"路标"，用来快速识别系统中安装了哪些包）
│
├── local_setup.bash                         # 👈 核心脚本：仅导入当前这一个工作空间的环境变量
├── setup.bash                               # 👈 核心脚本：全局环境配置脚本（最常用）
├── setup.sh / local_setup.sh                # 兼容通用 Shell 终端的环境脚本
└── setup.zsh / local_setup.zsh              # 兼容 Mac/Ubuntu 的 Zsh 终端的环境脚本
```

### 🔍 常见困惑：setup.bash 与 local_setup.bash 有什么区别？

- **`local_setup.bash`**：只会把当前工作空间（这个 `install/` 目录里）的所有功能包路径写进系统环境变量。
- **`setup.bash`**：不仅会导入当前工作空间，还会顺藤摸瓜，自动把"当前空间依赖的其他工作空间"（比如 ROS 2 官方系统目录 `/opt/ros/humble/`）的环境变量一并 source 进来。

> 💡 **黄金定律**：在日常开发中，永远执行 `source install/setup.bash`，最省心、最不容易报错。

### 3. log/ 目录：黑匣子日志（排查报错神器）

每次执行 `colcon build`，都会在这个目录下留下脚印。

- **latest_build**：这是一个软链接，永远指向你最新一次运行 `colcon build` 的日志文件夹。
- **build_\<timestamp\>**：以时间戳命名的历史日志目录。
- **内部文件**：里面包含各个功能包编译过程中的 `stdout.log`（输出日志）和 `stderr.log`（错误日志）。当编译提示失败、控制台输出信息不全时，你可以打开这个目录下的日志文件，查看具体的报错细节。

## 🛠️ 完整的命令深度解析

### 1. ros2 pkg create 创建功能包

```bash
ros2 pkg create --build-type ament_python --license Apache-2.0 --dependencies rclpy --node-name my_node demo_python_pkg
```

#### 📌 参数矩阵表 (Flags Reference)

| 参数名 | 默认值 | 作用说明 | 视频推荐设置 |
|---|---|---|---|
| `--build-type` | ament_cmake | 指定包的构建系统（ament_cmake/ament_python） | 必须显式指定为 ament_python |
| `--license` | 无 | 指定开源协议（如 Apache-2.0, MIT, GPLv3 等） | 推荐使用 Apache-2.0 |
| `--dependencies` | 无 | 自动导入依赖包（在 package.xml 和 setup.py 中预声明） | 推荐直接声明 rclpy |
| `--node-name` | 无 | 自动生成该名称的代码模板（不指定则不生成模板文件） | 初学者可指定以获取模板，或手动新建 |

## 🔑 核心解密：setup.py 中的 entry_points 到底在操作谁？为什么必须配置它？

在 `setup.py` 中，有这样一段看似天书的代码：

```python
entry_points={
    'console_scripts': [
        'python_node = demo_python_pkg.python_node:main'
    ],
}
```

### 1. 拆解：等号两边分别是谁？ (Who?)

这行配置的通用语法是：

$$\text{'可执行文件名'} = \text{'内层文件夹名（包名）}.\text{Python文件名}:\text{入口函数名'}$$

具体到我们的项目：

- **python_node** (等号左边)：这是你给这个节点起的"终端呼叫绰号"。一旦配置好，你就能通过 `ros2 run demo_python_pkg python_node` 来启动它。
- **demo_python_pkg.python_node** (等号右边前半部分)：定位到你的 Python 脚本。系统会去 `src/demo_python_pkg/demo_python_pkg/python_node.py` 寻找。
- **:main** (等号右边后半部分)：指定在这个脚本里哪一个函数是程序的起点。

### 2. 底层原理：为什么必须配置它？ (Why?)

你可能会想："Python 代码直接用 `python3 python_node.py` 就能跑，为什么 ROS 2 还要搞得这么麻烦？"原因有三个：

**原因①：Linux 无法直接"无脑执行"普通的 .py 文件**

在 Linux 系统中，普通的文本文件（比如 `.py`）如果没有可执行权限（`chmod +x`），且第一行没有声明解释器路径（`#!/usr/bin/env python3`），系统是无法直接把它当成程序来调用的。

**原因②：colcon build 会为你自动生成"代理人"（可执行文件）**

当你在 `setup.py` 注册了这一行后，执行 `colcon build` 时，编译系统会读取这个配置，并在 `install/demo_python_pkg/lib/demo_python_pkg/` 目录下，自动为你生成一个名为 `python_node` 的可执行文件（它本质上是一个微型的 Shell 脚本）。

**原因③：ros2 run 依靠"代理人"间接运行你的 Python 代码**

当你在终端敲下 `ros2 run demo_python_pkg python_node` 时：

1. ROS 2 去 `install/` 目录下搜索名为 `python_node` 的可执行程序。
2. 找到后，运行这个由系统生成的"代理人"程序。
3. 这个"代理人"会在后台默默执行：`from demo_python_pkg.python_node import main; main()`。

因此，如果不写 `entry_points`，编译时就不会产生这个"代理人"可执行文件，`ros2 run` 就会报错提示 `No executable found`。

## 📝 核心配置文件完美写法模板

### ① 节点文件：demo_python_pkg/demo_python_pkg/python_node.py

遵循标准面向过程或面向对象的规范写法：

```python
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args) # 初始化 ROS 2 客户端
    node = Node("python_node") # 创建节点对象，指定节点名称为 python_node
    node.get_logger().info("Hello, ROS 2 Python Node inside Package!") # 打印日志
    
    try:
        rclpy.spin(node) # 循环运行节点，保持其活性
    except KeyboardInterrupt:
        pass
        
    node.destroy_node() # 销毁节点对象
    rclpy.shutdown() # 关闭 ROS 2 客户端

# ⭐ 强烈推荐保留此入口！方便不需要 colcon 编译时直接用 python3 调试
if __name__ == '__main__':
    main()
```

### ② 构建文件：demo_python_pkg/setup.py

配置 `entry_points` 是让 `ros2 run` 能够找到你程序的唯一钥匙：

```python
from setuptools import find_packages, setup

package_name = 'demo_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='YourName',
    maintainer_email='your_email@example.com',
    description='ROS2 Python study demo',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # ⭐ 核心映射：声明 ros2 run 命令调用的可执行程序
            # 格式：'可执行程序名 = 包名.文件名:入口函数名'
            'python_node = demo_python_pkg.python_node:main'
        ],
    },
)
```

### ③ 清单文件：demo_python_pkg/package.xml

告诉 ROS 2 你的包需要哪些底层运行支持：

```xml
<?xml version="1.0"?>
<?model-ypath-format 3?>
<package format="3">
  <name>demo_python_pkg</name>
  <version>0.0.0</version>
  <description>ROS 2 Python package demo</description>
  <maintainer email="your_email@example.com">YourName</maintainer>
  <license>Apache-2.0</license>

  <!-- ⭐ 必须添加 rclpy 依赖声明，否则编译部署后可能无法运行 -->
  <depend>rclpy</depend>

  <test_depend>ament_copyright</test_depend>
  <test_depend>ament_flake8</test_depend>
  <test_depend>ament_pep257</test_depend>
  <test_depend>python3-pytest</test_depend>

  <export>
    <build_type>ament_python</build_type>
  </export>
</package>
```

## 🛠️ 实战操作四步走

### 运行环境准备

每次编译前，请确保你在工作空间根目录中（例如 `~/chapt2_ws/` 目录下）：

```bash
# 1. 编译当前工作空间下所有的包
colcon build

# 2. 刷新、载入本地工作空间的环境变量
source install/setup.bash

# 3. 运行你的节点
ros2 run demo_python_pkg python_node
```

## 💡 终极实战技巧：Python 专属的 --symlink-install（免反复编译）

由于 Python 是解释型语言，每次改动代码都要重新执行 `colcon build` 简直是灾难。为此，ROS 2 提供了一个终极黑科技：软链接安装。

### 1. 什么是软链接编译？

如果你在编译时加入参数：

```bash
colcon build --symlink-install
```

底层变化：ROS 2 在 `install/` 目录中创建的不再是 `src/` 中 Python 文件的物理副本，而是一个指向你 `src/` 源码文件的软链接（快捷方式）！

### 2. 带来的巨大优势

- **一次编译，实时生效**：你只需要在第一次创建好包、修改好 `setup.py` 和 `package.xml` 配置文件后，执行一次带有该参数的编译。
- **后期改动免编译**：之后你任何时候在 `src/` 里修改 `python_node.py` 中的 Python 逻辑代码，都不需要再次执行 `colcon build`！直接再次 `ros2 run` 即可运行最新改动的代码！

> 注意：如果你修改了 `setup.py` 的可执行文件名映射或 `package.xml` 的依赖，依然需要重新编译一遍刷新软链接。

## 🚨 高频报错与排错 FAQ 字典

### Q1: ModuleNotFoundError: No module named 'demo_python_pkg.xxxx'

- **可能原因**：你把 `python_node.py` 建在外层目录了。
- **解决办法**：用 `mv` 将脚本移动到内层 `demo_python_pkg/demo_python_pkg/` 文件夹下，并重新运行 `colcon build`。

### Q2: 提示 No executable found 或者 Package 'demo_python_pkg' not found

- **可能原因**：你可能打开了新的终端却忘记执行 `source install/setup.bash`，或者 `setup.py` 里的 `entry_points` 名字拼写错误。
- **解决办法**：
  - 检查新终端是否执行了 `source install/setup.bash`。
  - 确认 `entry_points` 里等号左右两侧名字完全正确（没有拼写错误 or 多余的空格）。

---

## 三、话题


1. ![[Pasted image 20260712203319.png]]
2. ![[Pasted image 20260712203337.png]]
3. 详细接口定义查看方法：![[Pasted image 20260712203407.png]]
4. 发布话题需要知道：话题名字 `/turtle1/cmd_vel` 和 话题接口 `geometry_msgs/msg/Twist
![[Pasted image 20260712203440.png]]

### 1. 通过话题来发布小说
> *任务：*
![[Pasted image 20260712223534.png]]

1.  功能包创建 ：`ros2 pkg create demo_py_topic --build-type ament_python --dependencies rclpy example_interfaces --license Apache-2.0 `