
## 目录

1. [Matplotlib 简介与安装配置](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#1-matplotlib-%E7%AE%80%E4%BB%8B%E4%B8%8E%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE-000000---000705 "null")
    
2. [折线图 (Line Plot) 基础与 NumPy 整合](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#2-%E6%8A%98%E7%BA%BF%E5%9B%BE-line-plot-%E5%9F%BA%E7%A1%80%E4%B8%8E-numpy-%E6%95%B4%E5%90%88-000209---000705 "null")
    
3. [折线与数据标记 (Markers) 的个性化定制](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#3-%E6%8A%98%E7%BA%BF%E4%B8%8E%E6%95%B0%E6%8D%AE%E6%A0%87%E8%AE%B0-markers-%E7%9A%84%E4%B8%AA%E6%80%A7%E5%8C%96%E5%AE%9A%E5%88%B6-000705---001622 "null")
    
4. [高级标签、标题与刻度定制](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#4-%E9%AB%98%E7%BA%A7%E6%A0%87%E7%AD%BE%E6%A0%87%E9%A2%98%E4%B8%8E%E5%88%BB%E5%BA%A6%E5%AE%9A%E5%88%B6-001622---002112 "null")
    
5. [参考网格线 (Grid Lines) 的配置](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#5-%E5%8F%82%E8%80%83%E7%BD%91%E6%A0%BC%E7%BA%BF-grid-lines-%E7%9A%84%E9%85%8D%E7%BD%AE-002112---002358 "null")
    
6. [条形图 (Bar Chart) 与水平条形图](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#6-%E6%9D%A1%E5%BD%A2%E5%9B%BE-bar-chart-%E4%B8%8E%E6%B0%B4%E5%B9%B3%E6%9D%A1%E5%BD%A2%E5%9B%BE-002358---002757 "null")
    
7. [饼图 (Pie Chart) 深度定制](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#7-%E9%A5%BC%E5%9B%BE-pie-chart-%E6%B7%B1%E5%BA%A6%E5%AE%9A%E5%88%B6-002757---003412 "null")
    
8. [散点图 (Scatter Plot) 与相关性分析](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#8-%E6%95%A3%E7%82%B9%E5%9B%BE-scatter-plot-%E4%B8%8E%E7%9B%B8%E5%85%B3%E6%80%A7%E5%88%86%E6%9E%90-003412---004058 "null")
    
9. [直方图 (Histogram) 与分布可视化](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#9-%E7%9B%B4%E6%96%B9%E5%9B%BE-histogram-%E4%B8%8E%E5%88%86%E5%B8%83%E5%8F%AF%E8%A7%86%E5%8C%96-004058---004713 "null")
    
10. [画布与多子图网格 (Figure & Subplots)](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#10-%E7%94%BB%E5%B8%83%E4%B8%8E%E5%A4%9A%E5%AD%90%E5%9B%BE%E7%BD%91%E6%A0%BC-figure--subplots-004713---005409 "null")
    
11. [Pandas 与 Matplotlib 综合实战项目 (宝可梦数据分析)](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#11-pandas-%E4%B8%8E-matplotlib-%E7%BB%BC%E5%90%88%E5%AE%9E%E6%88%98%E9%A1%B9%E7%9B%AE-%E5%AE%9D%E5%8F%AF%E6%A2%A6%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90-005409---005951 "null")
    

## 1. Matplotlib 简介与安装配置 `[00:00:00 - 00:02:09]`

### 💡 核心概念

- **什么是 Matplotlib**：Python 中最流行、最基础的可视化库。它可以将生硬的数据转化为直观的折线图、条形图、散点图、直方图及饼图等。
    
- **Pyplot 模块**：`matplotlib.pyplot` 是整个库中最核心的交互接口，它提供了一个类似于 MATLAB 的绘图框架，极大简化了各类图表的创建和展示流程。
    

### 📊 绘图基础工作流

```
【输入数据】           【创建/配置图表】                【渲染输出】
X 轴 / Y 轴 数据  ───►  plt.plot(x, y) / plt.bar(...) ───►  plt.show() 
(List 或 Array)          (设置标记、颜色、标签等)             (弹出图形窗口)
```

### 💻 完整命令与代码解析

- **安装指令**：
    
    ```
    pip install matplotlib
    ```
    
- **模块导入与版本验证**：
    
    ```
    import matplotlib
    import matplotlib.pyplot as plt
    
    # 验证安装版本 (视频演示版本为 3.10.6)
    print(matplotlib.__version__)
    ```
    

## 2. 折线图 (Line Plot) 基础与 NumPy 整合 `[00:02:09 - 00:07:05]`

### 💡 核心概念

- **数据对称性约束**：传入 `plot` 函数的 $X$ 和 $Y$ 轴坐标数据集，其**元素数量必须完全相等**（一一映射）。
    
- **单参数默认行为**：若只向 `plt.plot(y)` 传入单组数据，Matplotlib 会默认该数组为 $Y$ 轴坐标，而 $X$ 轴将自动从 `0` 开始，每次自增 `1`。
    
- **NumPy 强力支持**：虽然 Python 基础 `list` 可直接画图，但在真实数据科学场景中，**NumPy Array** 因为连续内存存储和底层向量化计算，速度极快，是更标准和推荐的数据载体。
    

### 💻 完整命令与代码解析

- **基础折线图画法（原生 List）**：
    
    ```
    import matplotlib.pyplot as plt
    
    # 1. 准备数据 (年份与对应的学生数量)
    years = [2023, 2024, 2025, 2026]
    class_sizes = [15, 25, 30, 20]
    
    # 2. 映射坐标点
    plt.plot(years, class_sizes)
    
    # 3. 必须调用 show() 才能唤起独立窗口渲染图表
    plt.show()
    ```
    
- **NumPy 数组加速版实现**：
    
    ```
    import numpy as np
    import matplotlib.pyplot as plt
    
    # 将原生列表转换为更高效的 NumPy 数组
    x_arr = np.array([2023, 2024, 2025, 2026])
    y_arr = np.array([15, 25, 30, 20])
    
    plt.plot(x_arr, y_arr)
    plt.show()
    ```
    

## 3. 折线与数据标记 (Markers) 的个性化定制 `[00:07:05 - 00:16:22]`

### 💡 核心概念

- **数据标记 (Marker)**：图表中折线上每个具体的坐标点符号（如圆圈、星号、点）。
    
- **线条样式 (Line Style)**：控制折线的物理形态（实线、虚线、点线）。
    
- **样式打包优化 (Dictionary Unpacking)**：当需要绘制多条折线且共享一套复杂的自定义外观属性时，将样式属性写入 Python `dict` 并通过 解包传入，可以大幅减少代码冗余并便于集中维护。
    

### 📊 折线属性结构图解

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

### 💻 完整命令与代码解析

- **高频配置参数表 (plot 参数)**：
    
    |   |   |   |   |
    |---|---|---|---|
    |**完整参数名**|**缩写缩短版**|**可选参数值举例**|**说明**|
    |`marker`|-|`'.'`(点), `'o'`(圆), `'v'`(倒三角), `'*'`(星)|数据节点的符号标记|
    |`markersize`|`ms`|整数（如 `10`, `30`）|标记点大小|
    |`markerfacecolor`|`mfc`|`'cyan'`, Hex颜色代码 `'#0088ff'`|标记点内部填充颜色|
    |`markeredgecolor`|`mec`|`'black'`, Hex颜色代码|标记点外部边缘颜色|
    |`linestyle`|`ls`|`'solid'`, `'dashed'`, `'dotted'`, `'dashdot'`, `'none'`|折线类型 (为 `'none'` 时只显示散点)|
    |`linewidth`|`lw`|数值（如 `1`, `4`）|线条粗细|
    |`color`|`c`|颜色名、RGB元组、十六进制代码|折线的整体颜色|
    
- **字典解包实战：统一多条折线的外观样式**：
    
    ```
    import numpy as np
    import matplotlib.pyplot as plt
    
    x = np.array([2023, 2024, 2025, 2026])
    y1 = np.array([15, 25, 30, 20])
    y2 = np.array([17, 23, 38, 5])
    y3 = np.array([13, 15, 20, 30])
    
    # 统一的外观配置字典
    shared_style = {
        'marker': '.',
        'markersize': 20,
        'markerfacecolor': '#00dfff',
        'markeredgecolor': '#00dfff',
        'linestyle': 'dashed',
        'linewidth': 3
    }
    
    # 通过 ** 快速解包，单独传入差异化的颜色参数
    plt.plot(x, y1, color='#1e3d59', **shared_style)
    plt.plot(x, y2, color='#ff6e40', **shared_style)
    plt.plot(x, y3, color='#17b978', **shared_style)
    
    plt.show()
    ```
    

## 4. 高级标签、标题与刻度定制 `[00:16:22 - 00:21:12]`

### 💡 核心概念

- **字体统一性**：通过设置 `family` 参数（如 `'Arial'`) 可以大幅提升报表的专业度和统一感。
    
- **X 轴强制硬刻度 (Ticks)**：Matplotlib 默认会对数据轴刻度进行平滑估算（例如输出 `2023.5` 等小数刻度）。使用 `plt.xticks()` 可以指定**仅在精确的数据坐标点**上显示刻度标签。
    
- **刻度全局修改 (`tick_params`)**：不仅可以调节坐标系外圈的标签，还可以快速对两轴的物理刻度线颜色、粗细进行整顿。
    

### 💻 完整命令与代码解析

- **轴文字修饰与刻度精准约束实战**：
    
    ```
    import numpy as np
    import matplotlib.pyplot as plt
    
    years = np.array([2023, 2024, 2025, 2026])
    students = np.array([15, 25, 30, 20])
    
    plt.plot(years, students)
    
    # 1. 标题高级设置 (大小、字体族、粗细、十六进制颜色)
    plt.title("Class Size Distribution", fontsize=25, family="Arial", fontweight="bold", color="#111d5e")
    
    # 2. X、Y 轴标签设置
    plt.xlabel("Year", fontsize=18, family="Arial", fontweight="bold", color="#c70039")
    plt.ylabel("Students", fontsize=18, family="Arial", fontweight="bold", color="#c70039")
    
    # 3. 强制限制 X 轴刻度：仅显示定义的年份，清除模糊自动生成的点（如 2023.5）
    plt.xticks(years)
    
    # 4. 坐标轴刻度线与标签颜色全局调节
    plt.tick_params(axis="both", colors="#111d5e")
    
    plt.show()
    ```
    

## 5. 参考网格线 (Grid Lines) 的配置 `[00:21:12 - 00:23:58]`

### 💡 核心概念

- **网格辅助线**：用于提高图表纵深可读性的强力手段，常用于金融图表和密集科学图表。
    
- **方向隔离控制**：支持通过 `axis` 参数控制网格线仅水平生成 (`'y'`) 或是仅垂直生成 (`'x'`)。
    

### 📊 网格方向控制

```
【axis='x'】 仅垂直网格线           【axis='y'】 仅水平网格线
     │     │     │                      ─────── ─────── ───────
     │     │     │                      ─────── ─────── ───────
     │     │     │                      ─────── ─────── ───────
```

### 💻 完整命令与代码解析

```
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 10, 15, 20, 25])

plt.plot(x, y)

# 配置半透明的网格辅助线 (axis='y' 表示只显示横向参考线)
plt.grid(axis='y', linewidth=1.5, color='lightgray', linestyle='dashed')

plt.show()
```

## 6. 条形图 (Bar Chart) 与水平条形图 `[00:23:58 - 00:27:57]`

### 💡 核心概念

- **应用场景**：条形图是对比**离散的类别型数据**（如食物类型、班级名称、品牌）最适合的工具。
    
- **水平条形图 (`barh`)**：适合类别名称文字非常长、或是类别数量很多时的展示，可以有效防止 $X$ 轴文字发生拥挤重叠。
    

### 💻 完整命令与代码解析

- **垂直和水平条形图代码实战**：
    
    ```
    import numpy as np
    import matplotlib.pyplot as plt
    
    # 离散类别与服务数值数据
    categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
    servings = np.array([4, 3, 2, 5, 3, 1])
    
    # 1. 传统垂直条形图 (使用 bar 函数)
    plt.bar(categories, servings, color="skyblue")
    plt.title("Daily Food Consumption")
    plt.xlabel("Food Category")
    plt.ylabel("Servings (Quantity)")
    plt.show()
    
    # 2. 水平条形图 (使用 barh 函数)
    # 注意：在 barh 中，原本的分类坐标将移至 Y 轴
    plt.barh(categories, servings, color="#ff8a5c")
    plt.title("Daily Food Consumption (Horizontal)")
    plt.xlabel("Servings (Quantity)")
    plt.ylabel("Food Category")
    plt.show()
    ```
    

## 7. 饼图 (Pie Chart) 深度定制 `[00:27:57 - 00:34:12]`

### 💡 核心概念

- **主要用途**：用于展示各部分在整体（100%）中所占的百分比和分布比例。
    
- **爆破效果 (Explode)**：通过让某一块或几块切片在径向方向往外凸出，能够极好地聚焦观众视线。
    
- **格式说明符 `autopct`**：通过控制特定的 C 语言风格格式化占位符，控制切片上百分比小数点的保留位数（如 `%0.1f%%` 表示保留一位小数且尾部附带 `%` 符号）。
    

### 📊 饼图定制元素

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

### 💻 完整命令与代码解析

- **多维度个性化饼图实战**：
    
    ```
    import numpy as np
    import matplotlib.pyplot as plt
    
    # 学院学生分布数据
    classes = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
    student_counts = [300, 250, 275, 225]
    
    # 定制每个类别的专色
    slice_colors = ["#f05454", "#e8e8e8", "#30475e", "#17b978"]
    
    # 定制凸出效果元组（长度须与分类数一致，0 代表贴紧，值越大凸出越远）
    # 此处让最后的 "Seniors" 凸出 0.2 个单位
    explode_rules = [0, 0, 0, 0.2]
    
    plt.pie(
        student_counts,
        labels=classes,
        autopct="%0.1f%%",         # 显示百分比，保留一位小数，使用 %% 转义打印 '%' 符号
        colors=slice_colors,
        explode=explode_rules,     # 应用爆破
        shadow=True,               # 开启立体阴影
        startangle=90              # 旋转图形，使起始绘制角度为垂直向上 90度
    )
    
    plt.title("Student Distribution by Class", fontsize=20, fontweight="bold")
    plt.show()
    ```
    

## 8. 散点图 (Scatter Plot) 与相关性分析 `[00:34:12 - 00:40:58]`

### 💡 核心概念

- **作用**：探究和展示两个连续变量之间的关联规律（如：正相关、负相关、不相关）。
    
- **透明度 (Alpha)**：通过控制 `alpha` 的取值区间 `[0.0, 1.0]`，可以极好地解决因数据点过于密集导致的“数据点重叠覆盖”问题。
    
- **图例 (Legend)**：当一个坐标系内包含两个不同的群体点集（如 A 班和 B 班）时，使用标签标记并通过 `plt.legend()` 将其显示出来，实现多维对比。
    

### 💻 完整命令与代码解析

- **双班级对比散点图实战**：
    
    ```
    import numpy as np
    import matplotlib.pyplot as plt
    
    # A班数据 (自变量：学习时长，因变量：考试成绩)
    x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])
    y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87])
    
    # B班数据 (学习效率略有差异的班级)
    x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8])
    y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97])
    
    # 1. 绘制 A班 散点点集 (浅蓝色，尺寸为200，半透明)
    plt.scatter(x1, y1, color="skyblue", s=200, alpha=0.7, label="Class A")
    
    # 2. 绘制 B班 散点点集 (红色)
    plt.scatter(x2, y2, color="#ff4a4a", s=200, alpha=0.7, label="Class B")
    
    # 3. 标签与图例设定
    plt.title("Study Hours vs. Exam Grades")
    plt.xlabel("Hours Studied")
    plt.ylabel("Exam Grades (%)")
    
    # 唤醒图例，自动抓取各 scatter 的 'label' 值并呈现在图表内部最佳空白处
    plt.legend()
    
    plt.show()
    ```
    

## 9. 直方图 (Histogram) 与分布可视化 `[00:40:58 - 00:47:13]`

### 💡 核心概念

- **直方图 vs 条形图**：
    
    - **条形图**：展示定性分类数据（如品牌、城市）。
        
    - **直方图**：展示定量连续分布数据（如年龄分布、考试得分区间），它通过自动或者指定的 **区间桶 (Bins)** 将数值分组并统计其频数。
        
- **高斯/正常分布生成 (`np.random.default_rng().normal`)**：
    
    - `loc`：均值（正态分布中心）。
        
    - `scale`：标准差（越小分布越陡峭，越大越分散）。
        
- **边界约束 (`np.clip`)**：用于对异常数据进行约束。在模拟考试分时，通过 `np.clip` 可以将计算产生的低于 `0` 岁或大于 `100` 分的极端随机值规整到合理范围内。
    

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

```
import numpy as np
import matplotlib.pyplot as plt

# 1. 初始化先进的随机生成器
rng = np.random.default_rng(seed=42)

# 2. 生成一个中心为80、标准差为10、样本数为100的考试成绩分布数组
raw_scores = rng.normal(loc=80, scale=10, size=100)

# 3. 为防止物理成绩溢出百分制，强制把得分约束在 [0, 100] 区间
scores = np.clip(raw_scores, 0, 100)

# 4. 绘制直方图，将其切分为 10 个数据桶
plt.hist(
    scores,
    bins=10,
    color="lightgreen",
    edgecolor="black"        # 轮廓边线设为黑色，防止桶之间粘连变成色块
)

plt.title("Exam Score Distribution")
plt.xlabel("Score Interval")
plt.ylabel("Number of Students")
plt.show()
```

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
    
    ```
    import numpy as np
    import matplotlib.pyplot as plt
    
    # 数据集准备
    x = np.array([1, 2, 3, 4, 5])
    
    # 返回画布和 2D 结构的 Axes 子图数组 (2行2列)
    fig, axes = plt.subplots(nrows=2, ncols=2)
    
    # 1. 绘制左上子图 [row 0, col 0] - 一次正比例
    axes[0, 0].plot(x, x * 2, color="red")
    axes[0, 0].set_title("Linear (x * 2)")
    
    # 2. 绘制右上子图 [row 0, col 1] - 平方曲线
    axes[0, 1].plot(x, x ** 2, color="blue")
    axes[0, 1].set_title("Quadratic ($x^2$)")
    
    # 3. 绘制左下子图 [row 1, col 0] - 立方曲线
    axes[1, 0].plot(x, x ** 3, color="green")
    axes[1, 0].set_title("Cubic ($x^3$)")
    
    # 4. 绘制右下子图 [row 1, col 1] - 四次方曲线
    axes[1, 1].plot(x, x ** 4, color="purple")
    axes[1, 1].set_title("Quartic ($x^4$)")
    
    # 核心：自动调整间距，防止坐标轴文字重叠
    plt.tight_layout()
    
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