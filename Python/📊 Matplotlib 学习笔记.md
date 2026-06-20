
> 📚 本笔记整理自 YouTube Matplotlib 教程，系统涵盖 Matplotlib 从基础图表到 Pandas 实战的核心知识点。

---

## 目录

- [[#一、Matplotlib 简介与安装配置|一、简介与安装]]
- [[#二、折线图基础与 NumPy 整合|二、折线图基础]]
- [[#三、折线与数据标记的个性化定制|三、Markers 定制]]
- [[#四、高级标签、标题与刻度定制|四、标签与刻度]]
- [[#五、参考网格线的配置|五、网格线]]
- [[#六、条形图与水平条形图|六、条形图]]
- [[#七、饼图深度定制|七、饼图]]
- [[#八、散点图与相关性分析|八、散点图]]
- [[#九、直方图与分布可视化|九、直方图]]
- [[#十、画布与多子图网格|十、子图]]
- [[#十一、Pandas 综合实战|十一、Pandas 实战]]

---

## 一、Matplotlib 简介与安装配置 `[00:00:00 - 00:02:09]`

1. **什么是 Matplotlib**：Python 中最流行、最基础的可视化库。它可以将生硬的数据转化为直观的折线图、条形图、散点图、直方图及饼图等。
	<br>
2. **Pyplot 模块**：`matplotlib.pyplot` 是整个库中最核心的交互接口，它提供了一个类似于 MATLAB 的绘图框架，极大简化了各类图表的创建和展示流程。

**绘图基础工作流**

```
【输入数据】           【创建/配置图表】                【渲染输出】
X 轴 / Y 轴 数据  ───►  plt.plot(x, y) / plt.bar(...) ───►  plt.show() 
(List 或 Array)          (设置标记、颜色、标签等)             (弹出图形窗口)
```

> [!example] 安装与导入
> ```python
> # 安装指令
> pip install matplotlib
> ```
> ```python
> import matplotlib
> import matplotlib.pyplot as plt
>
> # 验证安装版本 (视频演示版本为 3.10.6)
> print(matplotlib.__version__)
> ```


## 二、折线图 (Line Plot) 基础与 NumPy 整合 `[00:02:09 - 00:07:05]`

1. **数据对称性约束**：传入 `plot` 函数的 $X$ 和 $Y$ 轴坐标数据集，其**元素数量必须完全相等**（一一映射）。
	<br>
2. **单参数默认行为**：若只向 `plt.plot(y)` 传入单组数据，Matplotlib 会默认该数组为 $Y$ 轴坐标，而 $X$ 轴将自动从 `0` 开始，每次自增 `1`。
	<br>
3. **NumPy 强力支持**：虽然 Python 基础 `list` 可直接画图，但在真实数据科学场景中，**NumPy Array** 因为连续内存存储和底层向量化计算，速度极快，是更标准和推荐的数据载体。

> [!example]- 基础折线图画法（原生 List）
> ```python
> import matplotlib.pyplot as plt
>
> # 1. 准备数据 (年份与对应的学生数量)
> years = [2023, 2024, 2025, 2026]
> class_sizes = [15, 25, 30, 20]
>
> # 2. 映射坐标点
> plt.plot(years, class_sizes)
>
> # 3. 必须调用 show() 才能唤起独立窗口渲染图表
> plt.show()
> ```

> [!example]- NumPy 数组加速版实现
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
>
> # 将原生列表转换为更高效的 NumPy 数组
> x_arr = np.array([2023, 2024, 2025, 2026])
> y_arr = np.array([15, 25, 30, 20])
>
> plt.plot(x_arr, y_arr)
> plt.show()
> ```

---
    

## 三、折线与数据标记 (Markers) 的个性化定制 `[00:07:05 - 00:16:22]`

1. **数据标记 (Marker)**：图表中折线上每个具体的坐标点符号（如圆圈、星号、点）。
	<br>
2. **线条样式 (Line Style)**：控制折线的物理形态（实线、虚线、点线）。
	<br>
3. **样式打包优化 (Dictionary Unpacking)**：当需要绘制多条折线且共享一套复杂的自定义外观属性时，将样式属性写入 Python `dict` 并通过解包传入，可以大幅减少代码冗余并便于集中维护。

**折线属性结构图解**

```
                 [markerfacecolor (点内部填充色)]
                         │
                         ▼
        O─────────────►  ●  ◄─────────────── [markeredgecolor (点边缘颜色)]
        │                │
        └───────┬────────┘
                ▼
        [line_style / ls (线条样式: solid / dashed / dotted / none)]
```

**高频配置参数表 (plot 参数)**：

| 完整参数名 | 缩写 | 可选参数值举例 | 说明 |
|---|---|---|---|
| `marker` | — | `'.'`(点), `'o'`(圆), `'v'`(倒三角), `'*'`(星) | 数据节点的符号标记 |
| `markersize` | `ms` | 整数（如 `10`, `30`） | 标记点大小 |
| `markerfacecolor` | `mfc` | `'cyan'`, Hex颜色代码 `'#0088ff'` | 标记点内部填充颜色 |
| `markeredgecolor` | `mec` | `'black'`, Hex颜色代码 | 标记点外部边缘颜色 |
| `linestyle` | `ls` | `'solid'`, `'dashed'`, `'dotted'`, `'none'` | 折线类型 (`'none'` 时只显示散点) |
| `linewidth` | `lw` | 数值（如 `1`, `4`） | 线条粗细 |
| `color` | `c` | 颜色名、RGB元组、十六进制代码 | 折线的整体颜色 |

> [!example] 字典解包实战：统一多条折线的外观样式
> ```python
> import matplotlib.pyplot as plt
> import numpy as np
> x = np.array([2023, 2024, 2025, 2026])
> y1 = np.array([15, 25, 1000, 20])
> y2 = np.array([10, 20, 800, 10])
> y3 = np.array([5, 15, 500, 5])
> # 这里使用dict()来创建字典,当然花括号也行
> line_style = dict(
>     marker=".",
>     markersize=20,
>     mfc="#1cd3fc",
>     mec="#1cd3fc",
>     linestyle="solid",
>     linewidth="4",
> )
>
> plt.plot(x, y1, color="#1cfca2", **line_style)
> plt.plot(x, y2, color="#1c5bfc", **line_style)
> plt.plot(x, y3, color="#fc491c", **line_style)
> plt.show()
> ```

---
    

## 四、高级标签、标题与刻度定制 `[00:16:22 - 00:21:12]`

1. **字体统一性**：通过设置 `family` 参数（如 `'Arial'`) 可以大幅提升报表的专业度和统一感。
	<br>
2. **X 轴强制硬刻度 (Ticks)**：Matplotlib 默认会对数据轴刻度进行平滑估算（例如输出 `2023.5` 等小数刻度）。使用 `plt.xticks()` 可以指定**仅在精确的数据坐标点**上显示刻度标签。
	<br>
3. **刻度全局修改 (`tick_params`)**：不仅可以调节坐标系外圈的标签，还可以快速对两轴的物理刻度线颜色、粗细进行整顿。

> [!example] 轴文字修饰与刻度精准约束实战
> ```python
> plt.title("Class Size",
>           fontsize=20,
>           family="Arial",
>           fontweight="bold",
>           color="#1c5bfc",)
> plt.xlabel("Year",
>            fontsize=15,
>            family="Arial",
>            fontweight="bold",
>            color="#1c5bfc",)
>
> plt.ylabel("Students",
>            fontsize=15,
>            family="Arial",
>            fontweight="bold",
>            color="#1c5bfc",)
>
> # 自定义刻度
> plt.tick_params(axis="both",
>                 colors="#1c5bfc",)
>
> plt.xticks(x)  # 强制让x轴的刻度只显示在特定数值上
>
> plt.plot(x, y1)
> plt.plot(x, y2)
> plt.plot(x, y3)
> plt.show()
> ```

---
    

## 五、参考网格线 (Grid Lines) 的配置 `[00:21:12 - 00:23:58]`

1. **网格辅助线**：用于提高图表纵深可读性的强力手段，常用于金融图表和密集科学图表。
	<br>
2. **方向隔离控制**：支持通过 `axis` 参数控制网格线仅水平生成 (`'y'`) 或是仅垂直生成 (`'x'`)。

**网格方向控制**

```
【axis='x'】 仅垂直网格线           【axis='y'】 仅水平网格线
     │     │     │                      ─────── ─────── ───────
     │     │     │                      ─────── ─────── ───────
     │     │     │                      ─────── ─────── ───────
```

> [!example] 网格线配置实战
> ```python
> x = [1, 2, 3, 4, 5]
> y = [5, 10, 15, 20, 25]
>
> plt.grid(axis="y",
>          color="lightgray",
>          linestyle="dashed",
>          linewidth=2,)
> plt.plot(x, y)
> plt.show()
> ```

---

## 六、条形图 (Bar Chart) 与水平条形图 `[00:23:58 - 00:27:57]`

1. **应用场景**：条形图是对比**离散的类别型数据**（如食物类型、班级名称、品牌）最适合的工具。
	<br>
2. **水平条形图 (`barh`)**：适合类别名称文字非常长、或是类别数量很多时的展示，可以有效防止 $X$ 轴文字发生拥挤重叠。

> [!example] 垂直和水平条形图代码实战
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
>
> # 离散类别与服务数值数据
> categories = ["Grains", "Vegetables", "Fruits", "Dairy", "Meat", "Sweets"]
> values = [20, 15, 30, 10, 25, 5]
>
> plt.bar(categories, values)
> # plt.barh(categories, values) # 水平柱状图
> plt.title("Daily Consumption")
> plt.xlabel("Food")
> plt.ylabel("Quantity")
> plt.show()
> ```

---
    

## 七、饼图 (Pie Chart) 深度定制 `[00:27:57 - 00:34:12]`

1. **主要用途**：用于展示各部分在整体（100%）中所占的百分比和分布比例。
	<br>
2. **爆破效果 (Explode)**：通过让某一块或几块切片在径向方向往外凸出，能够极好地聚焦观众视线。
	<br>
3. **格式说明符 `autopct`**：通过控制特定的 C 语言风格格式化占位符，控制切片上百分比小数点的保留位数（如 `%0.1f%%` 表示保留一位小数且尾部附带 `%` 符号）。

**饼图定制元素**

```
                          Title: College Classes
                                  /
                                 /
                         .-'""'-. 
                       .'   \    '. 
                      / Red  \ Yell\
                     | Fresh  \ Soph|
                      \ Blue  / /  /
                       '.  Jun_.-'   ◄─── [Explode] (Seniors Green 切片凸出)
                         '-..-' ______/
                             \ \ \
                              '-'-' (带 Drop Shadow 阴影立体感)
```

> [!example] 多维度个性化饼图实战
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
>
> categories = np.array(["Freshman",
>                        "Sophomore", "Junior", "Senior"])
> values = np.array([150, 375, 800, 650])
> colors = ["#1c5bfc", "#1cfca2", "#fc491c", "#1cd3fc"]
> plt.title("Bro Code Class")
> plt.pie(values, labels=categories,
>         autopct="%1.1f%%", startangle=90,
>         colors=colors,
>         shadow=True,
>         explode=[0, 0.1, 0, 0],)
> plt.show()
> ```

---
    

## 8. 散点图 (Scatter Plot) 与相关性分析 `[00:34:12 - 00:40:58]`

### 💡 核心概念

- **作用**：探究和展示两个连续变量之间的关联规律（如：正相关、负相关、不相关）。
    
- **透明度 (Alpha)**：通过控制 `alpha` 的取值区间 `[0.0, 1.0]`，可以极好地解决因数据点过于密集导致的“数据点重叠覆盖”问题。
    
- **图例 (Legend)**：当一个坐标系内包含两个不同的群体点集（如 A 班和 B 班）时，使用标签标记并通过 `plt.legend()` 将其显示出来，实现多维对比。
    

### 💻 完整命令与代码解析

- **双班级对比散点图实战**：
    
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])
    y1 = np.array([55, 60, 65, 62, 68,  70, 75, 78, 82, 85, 87])

    x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8])
    y2 = np.array([50, 58, 65, 70, 72,  78, 83, 88, 92, 95, 98])

    plt.scatter(x1, y1,
                color="skyblue",
                alpha=0.5,
                s=200,
                label="Student A")
    plt.scatter(x2, y2,
                color="pink",
                alpha=0.5,
                s=200,
                label="Student B")
    plt.title("Test Scores")
    plt.xlabel("Hours Studied")
    plt.ylabel("Grade")
    plt.legend()

    plt.show()
    ```
    

## 9. 直方图 (Histogram) 与分布可视化 `[00:40:58 - 00:47:13]`

### 💡 核心概念

- **直方图 vs 条形图**：
    
    - **条形图**：展示定性分类数据（如品牌、城市）。
        
    - **直方图**：展示定量连续分布数据（如年龄分布、考试得分区间），它通过自动或者指定的 **区间桶 (Bins)** 将数值分组并统计其频数。
        
- **高斯/正常分布生成 (`np.random.normal`)**：
    
    - `loc`：均值（正态分布中心）。
        
    - `scale`：标准差（越小分布越陡峭，越大越分散）。
        
- **边界约束 (`np.clip`)**：用于对异常数据进行约束。在模拟考试分数时，通过 `np.clip` 可以将计算产生的低于 `0` 分或大于 `100` 分的极端随机值规整到合理范围内。
    
- **`plt.hist()` 的返回值**：
    
    - 一个包含每个柱子高度的数组（即每个柱子里有多少数据）
    - 一个柱子边界的数组（注意边界要比柱子数量多 1 个）
    - 一个包含每个柱子对象的列表（每个柱子都是一个矩形对象，可以单独更改其属性）
    
- **柱子数值标注技巧**：利用 `plt.hist()` 的返回值，配合 `plt.text()` 和 `zip()` 循环，可以在每个柱子上方标注频数。
    

### 📊 正常分布 Bins 划分示意

```
 频数 (Y轴)
    ▲
 15 │              ┌───┐
 10 │          ┌───┤   ├───┐
  5 │      ┌───┤   │   │   ├───┐
    └──────┴───┴───┴───┴───┴───┴──────► 数值区间 (X轴: Bins=10)
          50  60  70  80  90  100
```

### 💻 完整命令与代码解析

- **基础直方图与数据约束**：
    
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    # 生成100个平均值为75，标准差为10的正态分布数据
    score = np.random.normal(loc=75, scale=10, size=100)
    # 如果标准差不当可能会出现不合适的数,此时我们可以使用.clip()函数来限制数据的范围,比如限制在0到100之间
    score = np.clip(score, 0, 100)

    # plt.hist(score, bins=10,
    #                 color="lightgreen",
    #                 edgecolor="black",
    #                 )
    counts, bins = plt.hist(score, bins=10,
                            color="lightgreen",
                            edgecolor="black",
                            )
    ```
    
- **柱子上方标注频数值**：
    
    > `plt.hist()` 会返回三个值：`counts`（每个柱子的高度/频数）、`bins`（柱子的边界数组）。利用这两个返回值，配合 `plt.text()` 可以在每个柱子上方精确标注数值。
    
    ```python
    for count, bin_edge in zip(counts, bins[:-1]):
        plt.text(bin_edge + (bins[1] - bins[0]) / 2, count + 0.3,
                 str(int(count)), ha="center", fontsize=9)
    plt.title("Exam Scores")
    plt.xlabel("Score")
    plt.ylabel("# of Students")
    plt.tight_layout()  # 调整布局以避免标签重叠
    plt.show()
    ```
    
    > **标注逻辑解析**：
    > 1. **写什么数字？** → 柱子的高度，正好 `.hist` 函数返回的第一个参数就是柱子的高度，定义变量 `counts` 接收即可
    > 2. **写在哪里？** → 柱子的中间位置。水平坐标 `x = bin_edge + (bins[1] - bins[0]) / 2`（左边界 + 柱子宽度的一半），垂直坐标 `y = count + 0.3`（柱子高度 + 小偏移量）
    > 3. **如何配对？** → 使用 `zip()` 函数将 `counts` 和 `bins[:-1]` 两个数组内的元素进行配对，确保每个数值正确显示到对应的柱子上
    > 4. `str(int(count))` → 将高度转换为字符串类型，因为 `.text()` 函数要求文本参数是字符串；`ha="center"` → 水平居中对齐

## 10. 画布与多子图网格 (Figure & Subplots) `[00:47:13 - 00:54:09]`

### 💡 核心概念

- **画布 (Figure)**：底层的全局图像窗口容器（也就是空白纸张）。
    
- **轴域/子图 (Axes/Subplot)**：Figure 画布内部承载单个独立图表坐标系的最小单元。
    
- **多维网格解包 (Tuple Unpacking)**：`plt.subplots(nrows, ncols)` 会返回 Figure 对象和一整组 Axes 子图对象。通过 2D 数组索引定位（如 `axes[row, col]`）便能分别操作每一张子图。
    
- **排版紧凑化布局 (`plt.tight_layout`)**：Matplotlib 的默认排版容易导致各子图的 X 轴标签与上一行子图的 Title 重合。执行 `tight_layout()` 可以自适应紧凑自适应调整，彻底消除重叠现象。
    

### 📊 2x2 子图网格坐标图解

```
 ┌─────────────────────────────────────────────────────┐
 │ Figure (画布)                                        │
 │  ┌───────────────────────┐  ┌───────────────────────┐│
 │  │ axes[0, 0] (左上)      │  │ axes[0, 1] (右上)      ││
 │  └───────────────────────┘  └───────────────────────┘│
 │  ┌───────────────────────┐  ┌───────────────────────┐│
 │  │ axes[1, 0] (左下)      │  │ axes[1, 1] (右下)      ││
 │  └───────────────────────┘  └───────────────────────┘│
 └─────────────────────────────────────────────────────┘
```

### 💻 完整命令与代码解析

- **2x2 网格多维科学曲线排版实战**：
    
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    # 子图
    figure, axes = plt.subplots(2, 2)
    # subplot()函数会返回一个包含所有子图的Figure对象和一个包含每个子图的Axes对象的数组
    # 所以我们要操作子图 就是操作axes这个数组
    # axes[0, 0]表示第一行第一列的子图, axes[0, 1]表示第一行第二列的子图, 以此类推
    x = np.array([1, 2, 3, 4, 5])

    axes[0, 0].plot(x, x * 2, color="red")
    axes[0, 0].set_title("x*2")

    axes[0, 1].plot(x, x ** 2, color="blue")
    axes[0, 1].set_title("x**2")

    axes[1, 0].plot(x, x ** 3, color="green")
    axes[1, 0].set_title("x**3")

    axes[1, 1].plot(x, x ** 4, color="orange")
    axes[1, 1].set_title("x**4")
    plt.tight_layout()  # 调整布局以避免子图重叠
    plt.show()
    ```
    

## 11. Pandas 与 Matplotlib 综合实战项目 (宝可梦数据分析) `[00:54:09 - 00:59:51]`

### 💡 实战场景

我们将复现教程中的终极综合实战项目：导入包含前 **150 只初代宝可梦各项属性** 的 `data.csv` 文件，利用 **Pandas** 提取并统计初代宝可梦的**主要属性（Type 1）分布数量**，随后使用 **Matplotlib** 绘制一张具有极高可读性的水平排名分布条形图。

### 💻 初代宝可梦属性数量统计全栈实现

- **数据清洗及可视化代码**：
    
    ```
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # 1. 利用 Pandas 读取宝可梦属性 CSV 报表
    # 确保你的本地运行环境下包含该 data.csv 文件
    df = pd.read_csv("data.csv")
    
    # 2. 提取 'Type 1' (主要属性) 列，并利用 value_counts 计算各属性出现的次数
    # ascending=True 表示升序排序，使出现频率最高的属性位于图表顶部
    type_count = df["Type 1"].value_counts(ascending=True)
    
    # 3. 创建高质感水平条形图 (Horizontal Bar Chart)
    # X轴传入具体的宝可梦数量 (type_count.values)
    # Y轴传入对应的索引属性名称，如 Grass, Fire 等 (type_count.index)
    plt.barh(
        type_count.index, 
        type_count.values, 
        color="#3282b8", 
        edgecolor="black"
    )
    
    # 4. 精细化图表标注
    plt.title("Distribution of Pokemon by Primary Type (Original 150)", fontsize=16, fontweight="bold")
    plt.xlabel("Total Count", fontsize=12)
    plt.ylabel("Primary Type (Type 1)", fontsize=12)
    
    # 5. 应用布局紧凑化优化，确保所有文字均完整包含在生成的图片画幅内
    plt.tight_layout()
    
    # 6. 渲染图形
    plt.show()
    ```
    

_祝您 Matplotlib 可视化进阶愉快！用精美的图表去讲述数据背后的真实故事！_