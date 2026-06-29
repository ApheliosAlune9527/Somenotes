---
title: "Python 路径拼接：os.path vs pathlib"
author: Alune
created: 2026-06-29
tags: [Python, 基础, 路径, pathlib]
---

## 为什么要学路径拼接？

> [!tip] 核心原则
> **永远不要硬编码绝对路径**（如 `"E:/All_Projects/..."`）。用下面的模板，让代码自动定位自己所在的文件夹，在任何电脑上都能运行。

---

## 写法一：os.path（经典）

```python
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, "attachments", "Ellie.png")
```

### 第一行：剥洋葱 —— 定位当前脚本所在的文件夹

```python
script_dir = os.path.dirname(os.path.abspath(__file__))
```

从最内层往外剥：

#### 🧅 第一层（最核心）：`__file__`

*   **它是什么**：Python 的一个**内置变量（Built-in Variable）**。
*   **它的值**：代表**当前正在运行的这个 `.py` 文件的名字**（带有相对路径）。
*   **举例**：此时 `__file__` 的值就是 `"Opencv\04_basic.py"`。

#### 🧅 第二层：`os.path.abspath(...)`

*   **函数全称**：`abspath` = **Absolute Path（绝对路径）**。
*   **作用**：把一个相对路径，_强行补全_ 为从盘符开始的完整路径。
*   **输入**：`"Opencv\04_basic.py"`（相对路径）
*   **输出**：`"E:\All_Projects\pycharm_project\Data _analysis_study\Opencv\04_basic.py"`（绝对路径）

#### 🧅 第三层：`os.path.dirname(...)`

*   **函数全称**：`dirname` = **Directory Name（文件夹名）**。
*   **动作**：这是一个**纯字符串裁剪函数**。它在字符串里从右往左找，找到第一个斜杠 \（或 /），然后把斜杠右边的所有字（04_basic.py）强行切掉，只返回左边的文本。
*   **作用**：**砍掉路径最后的文件名，只留下它所在的文件夹路径**。
*   **输入**：`"E:\...\Opencv\04_basic.py"`（完整文件路径）
*   **输出**：`"E:\All_Projects\pycharm_project\Data _analysis_study\Opencv"`（尾巴的 `\04_basic.py` 被砍掉了）

**最终结果**：变量 `script_dir` 精准拿到了当前代码文件所在的物理文件夹的绝对路径。

---

### 第二行：智能胶水 —— 跨平台安全拼接

```python
path = os.path.join(script_dir, "attachments", "Ellie.png")
```

#### ⚙️ 零件：os.path.join(...)
- **它是什么**：os 库里的一个路径拼接函数。
- **运作机制（智能强力胶）**：
    1. 它拿到三个孤立的字符串：
        
        - `"E:\All_Projects\...\Opencv"`
            
        - `"attachments"`
            
        - `"Ellie.png"`
            
    2. 它检测当前电脑的操作系统是 **Windows**。
        
    3. 它自动在三个字符串之间，强行插上 Windows 的路径分隔符反斜杠 **\**。
        
    4. 最后，拼成一个完整的大字符串：  
        `"E:\All_Projects\...\Opencv\attachments\Ellie.png"`

#### 为什么不用加号 `+` 拼接？

比如 `script_dir + "\attachments\" + "Ellie.png"`，在你的 Windows 电脑上可能运行正常。但是，**当你把代码移到机器人的 Ubuntu（Linux）系统上运行时，程序会瞬间崩溃！**

因为不同的操作系统，**路径分隔符（Path Separator）** 不一样：
*   **Windows**：使用反斜杠 **`\`**（例如 `Opencv\attachments`）
*   **Linux / macOS**：使用正斜杠 **`/`**（例如 `Opencv/attachments`）

#### `os.path.join()` 的智能之处（跨平台兼容性）

它是一个 **"智能胶水"**，拼接路径时会自动检测你的操作系统：

| 操作系统 | `os.path.join()` 自动生成 |
|:---:|------|
| **Windows** | `E:\...\Opencv\attachments\Ellie.png`（反斜杠 `\`） |
| **Linux / macOS** | `/home/.../Opencv/attachments/Ellie.png`（正斜杠 `/`） |

而且，它还会自动处理多余的斜杠，绝对不会拼出像 `Opencv//attachments` 这种畸形路径。

> [!info] 两行代码的潜台词
> "不管我是被谁调用的，不管我在哪个目录下运行。先找到我（`04_basic.py`）自己住在哪个文件夹里（`script_dir`），然后用符合当前操作系统的分隔符，安全地把子文件夹 `attachments` 和图片 `Ellie.png` 贴在我屁股后面。"

记住这个模板，未来任何涉及读写本地文件的 Python 脚本都可以直接套用。

---

## 写法二：pathlib（推荐，更 Pythonic）

```python
from pathlib import Path
path = Path(__file__).parent / "attachments" / "Ellie.png"
```

一行顶两行，`/` 就是拼路径，不是除法。`Path(__file__).parent` 等价于 `os.path.dirname(os.path.abspath(__file__))`。

### 常用属性（不加括号）

```python
p = Path("E:/Projects/Opencv/attachments/Ellie.png")

p.name       # "Ellie.png"        → 文件名（含扩展名）
p.stem       # "Ellie"            → 文件名（不含扩展名）
p.suffix     # ".png"             → 扩展名
p.parent     # "E:/.../attachments" → 所在文件夹
```

### 常用方法

```python
p.exists()          # True/False  → 文件存不存在
p.is_file()         # True/False  → 是不是文件
p.is_dir()          # True/False  → 是不是文件夹
p.read_text()       # 读取文本内容（一行搞定，不用 open）
p.write_text("hi")  # 写入文本内容
```

### 遍历文件夹

```python
folder = Path("attachments")

for f in folder.glob("*.png"):      # 找所有 .png
    print(f.name)

for f in folder.rglob("*.png"):     # 递归找（包含子文件夹）
    print(f.name)
```

---

## 对照表：os.path vs pathlib

| 你想做的事 | `os.path` 写法 | `pathlib` 写法 |
|-----------|---------------|---------------|
| 拼路径 | `os.path.join(a, b, c)` | `a / b / c` |
| 取文件名 | `os.path.basename(p)` | `p.name` |
| 取文件夹 | `os.path.dirname(p)` | `p.parent` |
| 取扩展名 | `os.path.splitext(p)[1]` | `p.suffix` |
| 判断存在 | `os.path.exists(p)` | `p.exists()` |
| 取绝对路径 | `os.path.abspath(p)` | `p.resolve()` |

> [!info] 结论
> 新项目一律用 `pathlib`，老项目维护才用 `os.path`。
