# 🔢 NumPy 一小时快速通关核心精华整合手册

本手册基于知名编程导师 Bro Code 的热门教程 **《Learn NumPy in 1 hour!》**（视频链接：[Learn NumPy in 1 hour!](https://www.youtube.com/watch?v=VXU4LSAQDSc "null")）进行深度解构。我们将视频中的核心概念、多维数据流向、API 指令解析、实战场景以及精确的时间戳索引全部整合在内，帮助您实现对 NumPy 的零基础快速精通。

## 目录

1. [NumPy 简介与安装配置](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#1-numpy-%E7%AE%80%E4%BB%8B%E4%B8%8E%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE-000000---000503 "null")
    
2. [多维数组 (ND-Arrays) 与索引机制](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#2-%E5%A4%9A%E7%BB%B4%E6%95%B0%E7%BB%84-nd-arrays-%E4%B8%8E%E7%B4%A2%E5%BC%95%E6%9C%BA%E5%88%B6-000511---001251 "null")
    
3. [数组切片 (Array Slicing) 深度探究](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#3-%E6%95%B0%E7%BB%84%E5%88%87%E7%89%87-array-slicing-%E6%B7%B1%E5%BA%A6%E6%8E%A2%E7%A9%B6-001258---002401 "null")
    
4. [数学与算术运算 (Arithmetic)](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#4-%E6%95%B0%E5%AD%A6%E4%B8%8E%E7%AE%97%E6%9C%AF%E8%BF%90%E7%AE%97-arithmetic-002409---003315 "null")
    
5. [广播机制 (Broadcasting) 的运行机制](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#5-%E5%B9%BF%E6%92%AD%E6%9C%BA%E5%88%B6-broadcasting-%E7%9A%84%E8%BF%90%E8%A1%8C%E6%9C%BA%E5%88%B6-003325---003936 "null")
    
6. [聚合函数 (Aggregate Functions) 与轴向分析](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#6-%E8%81%9A%E5%90%88%E5%87%BD%E6%95%B0-aggregate-functions-%E4%B8%8E%E8%BD%B4%E5%90%91%E5%88%86%E6%9E%90-003947---004342 "null")
    
7. [数组过滤与布尔过滤 (Filtering)](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#7-%E6%95%B0%E7%BB%84%E8%BF%87%E6%BB%A4%E4%B8%8E%E5%B8%83%E5%B0%94%E8%BF%87%E6%BB%A4-filtering-004352---005159 "null")
    
8. [随机数生成、原位洗牌与随机抽取 (Random Generator)](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#8-%E9%9A%8F%E6%9C%BA%E6%95%B0%E7%94%9F%E6%88%90%E5%8E%9F%E4%BD%8D%E6%B4%97%E7%89%8C%E4%B8%8E%E9%9A%8F%E6%9C%BA%E6%8A%BD%E5%8F%96-random-generator-005207---005951 "null")
    

## 1. NumPy 简介与安装配置 `[00:00:00 - 00:05:03]`

### 💡 核心概念

- **什么是 NumPy**：全称为 Numerical Python，是 Python 科学计算、数据分析和机器学习生态系统（如 Pandas、Scikit-learn、TensorFlow 等）的核心基石。
    
- **为什么要用 NumPy 替代 Python 原生 List**：
    
    - **超高性能**：NumPy 底层由 **C 语言** 编写，内存连续存放，避免了 Python 原生列表动态类型带来的开销，运算速度提升数个数量级。
        
    - **向量化操作 (Vectorized Operations)**：支持对整个数组执行整体数学运算，无需编写繁琐低效的 `for` 循环。
        

### 📊 运行机制图解

对比 Python 原生列表与 NumPy 数组在做“乘以 2”运算时的不同表现：

```
【Python 原生 List * 2】: 复制并拼接
[1, 2, 3] * 2  ==>  [1, 2, 3, 1, 2, 3]

【NumPy 向量化 Array * 2】: 元素级乘法 (速度极快)
np.array([1, 2, 3]) * 2  ==>  [2, 4, 6]
```

### 💻 完整命令与代码解析

- **安装指令**：
    
    ```
    pip install numpy
    ```
    
- **基础导入与版本验证**：
    
    ```
    import numpy as np
    
    # 检查当前 NumPy 版本
    print(np.__version__)  # 视频演示版本为 2.3.1 左右
    ```
    
- **验证向量化加速能力实战**：
    
    ```
    # 创建 NumPy 数组
    my_array = np.array([1, 2, 3, 4])
    print(type(my_array))  # 输出: <class 'numpy.ndarray'> (n-dimensional array)
    
    # 向量化乘法
    doubled_array = my_array * 2
    print(doubled_array)  # 输出: [2, 4, 6, 8]
    ```
    

## 2. 多维数组 (ND-Arrays) 与索引机制 `[00:05:11 - 00:12:51]`

### 💡 核心概念

- **维度的层次**：
    
    - **0D 标量 (Scalar)**：单一数值或字符。
        
    - **1D 向量 (Vector)**：一维排开的单行或单列数据。
        
    - **2D 矩阵 (Matrix)**：具有行 (Rows) 和列 (Columns) 的二维网络结构。
        
    - **3D 张量 (Tensor)**：类似于“分层蛋糕 (Layered Cake)”，由深度层 (Depth Layers)、行和列组成的三维阵列。
        
- **形状一致性约束 (Homogeneity Constraint)**：在多维数组中，子层级的数组必须拥有完全一致的元素数量（一致的 Shape）。若长度不一，将抛出 `ValueError: setting an array element with a sequence...`。
    
- **索引类型对比**：
    
    - **链式索引 (Chain Indexing)**：如 `arr[0][0][0]`，效率较低（每次调用都会创建一个临时临时对象）。
        
    - **多维索引 (Multi-dimensional Indexing)**：如 `arr[0, 0, 0]`，NumPy 推荐写法，直接定位，速度极快。
        

### 📊 多维数组结构图解 (3D 蛋糕模型)

```
3D 蛋糕矩阵形式：
┌─────────────────────────┐
│ Layer 0 (第0层 - A-I)    │
│  [A, B, C]  <- Row 0    │
│  [D, E, F]              │
│  [G, H, I]              │
└─────────────────────────┘
            │
            ▼ 叠放
┌─────────────────────────┐
│ Layer 1 (第1层 - J-R)    │
│  [J, K, L]              │
│  [M, N, O]  <- Row 1, Col 1 (N)
│  [P, Q, R]              │
└─────────────────────────┘
```

### 💻 完整命令与代码解析

- **多维数组属性查询**：
    
    - `array.ndim`：获取数组维数（维度数量）。
        
    - `array.shape`：获取各维度的长度元组，对于 3D 数组返回 `(深度/层数, 行数, 列数)`。
        
- **3D 数组声明与多维索引实战**：
    
    ```
    import numpy as np
    
    # 定义一个 3x3x3 的 3D 字符数组
    # 注意：每一层的形状必须绝对一致 (3行3列)，不一致时可用占位符 "_" 或空格补充
    three_d_array = np.array([
        [['A', 'B', 'C'],
         ['D', 'E', 'F'],
         ['G', 'H', 'I']],
    
        [['J', 'K', 'L'],
         ['M', 'N', 'O'],
         ['P', 'Q', 'R']],
    
        [['S', 'T', 'U'],
         ['V', 'W', 'X'],
         ['Y', 'Z', '_']]
    ])
    
    # 1. 查看物理属性
    print("维度数量:", three_d_array.ndim)  # 输出: 3
    print("形状 (层, 行, 列):", three_d_array.shape)  # 输出: (3, 3, 3)
    
    # 2. 索引方式对比
    # 获取 'N' 元素 (Layer 1, Row 1, Col 1)
    print("链式索引:", three_d_array[1][1][1])  # 输出: N
    print("多维索引:", three_d_array[1, 1, 1])  # 推荐！输出: N
    
    # 3. 趣味实战：多维提取并拼接单词 "ASS"
    # 'A' -> [0, 0, 0]
    # 'S' -> [2, 0, 0]
    char_a = three_d_array[0, 0, 0]
    char_s = three_d_array[2, 0, 0]
    word = char_a + char_s + char_s
    print("拼接得到的单词:", word)  # 输出: ASS
    ```
    

## 3. 数组切片 (Array Slicing) 深度探究 `[00:12:58 - 00:24:01]`

### 💡 核心概念

- **切片基本语法**：`[start:end:step]`（其中 `end` 索引为**非包含性/开区间**，即不包含该点本身）。
    
- **2D 数组的行列联合切片**：`array[行切片, 列切片]`。
    

### 📊 4x4 矩阵的“四象限”切片图解

假设我们有一个 $4 \times 4$ 的矩阵（数值从 1 到 16）：

```
  Col 0  Col 1  Col 2  Col 3
 ┌─────┬─────┬─────┬─────┐
 │  1  │  2  │  3  │  4  │  <- Row 0
 ├─────┼─────┼─────┼─────┤
 │  5  │  6  │  7  │  8  │  <- Row 1
 ├─────┼─────┼─────┼─────┤
 │  9  │ 10  │ 11  │ 12  │  <- Row 2
 ├─────┼─────┼─────┼─────┤
 │ 13  │ 14  │ 15  │ 16  │  <- Row 3
 └─────┴─────┴─────┴─────┘
```

- **左上象限 (11-12点钟)**：`array[0:2, 0:2]` $\rightarrow$ `[[1, 2], [5, 6]]`
    
- **右上象限 (1-2点钟)**：`array[0:2, 2:]` $\rightarrow$ `[[3, 4], [7, 8]]`
    
- **左下象限 (7-8点钟)**：`array[2:, 0:2]` $\rightarrow$ `[[9, 10], [13, 14]]`
    
- **右下象限 (4-5点钟)**：`array[2:, 2:]` $\rightarrow$ `[[11, 12], [15, 16]]`
    

### 💻 完整命令与代码解析

```
import numpy as np

# 构建 4x4 基础矩阵
matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

# ==================== 行选择系列 ====================
print("第一行:", matrix[0])        # 输出: [1 2 3 4]
print("最后一行:", matrix[-1])      # 输出: [13 14 15 16]
print("前三行:", matrix[0:3])       # 包含行 0,1,2。输出: 前三行
print("跳步选择 (每2行选一行):", matrix[::2])  # 输出行 0 和行 2
print("行倒序:", matrix[::-1])     # 将矩阵行上下颠倒

# ==================== 列选择系列 ====================
# 行占位符为 ":" 代表选择所有行
print("第一列:", matrix[:, 0])      # 输出: [1 5 9 13]
print("最后一列:", matrix[:, -1])    # 输出: [4 8 12 16]
print("前三列:\n", matrix[:, 0:3])  # 提取前三列
print("列倒序:\n", matrix[:, ::-1]) # 单独将列左右翻转

# ==================== 象限联合切片实战 ====================
print("左上象限:\n", matrix[0:2, 0:2])
print("右上象限:\n", matrix[0:2, 2:])
print("左下象限:\n", matrix[2:, 0:2])
print("右下象限:\n", matrix[2:, 2:])
```

## 4. 数学与算术运算 (Arithmetic) `[00:24:09 - 00:33:15]`

### 💡 核心概念

- **标量运算 (Scalar Arithmetic)**：将单一常数（标量）作用于整个 ndarray，NumPy 会自动应用到数组中的每一个元素上。
    
- **向量化数学函数 (Vectorized Functions)**：取代 `for` 循环的内置高速数学公式（如平方根、取整）。
    
- **元素级运算 (Elementwise Arithmetic)**：两个形状相同的数组直接进行数学运算，即对应索引处的元素一对一运算。
    
- **条件过滤与赋值 (Conditional Assignment)**：利用比较运算符产生的布尔数组对原数组进行选择性重写。
    

### 📊 算术操作流向示意图

```
【元素级乘法 (Elementwise Multiplication)】:
  [1, 2, 3]   x   [4, 5, 6]   =   [1*4, 2*5, 3*6]   =   [4, 10, 18]

【比较运算符过滤赋值流程】:
  Scores: [91, 55, 100, 73]  -->  判断 scores < 60  -->  [False, True, False, False]
  将 True 对应的位置赋值为 0  -->  Scores 变为: [91, 0, 100, 73]
```

### 💻 完整命令与代码解析

- **数学运算函数解析表**：
    
    |   |   |   |
    |---|---|---|
    |**函数**|**作用**|**备注**|
    |`np.sqrt(arr)`|计算每个元素的平方根|向量化运算|
    |`np.round(arr)`|四舍五入取整|向量化运算|
    |`np.floor(arr)`|向下取整|始终往更小的值取整|
    |`np.ceil(arr)`|向上取整|始终往更大的值取整|
    |`np.pi`|数学常数 $\pi$|$\approx 3.14159265...$|
    
- **综合代码演示**：
    
    ```
    import numpy as np
    
    # 1. 标量运算演示
    arr = np.array([1, 2, 3])
    print("加 1:", arr + 1)      # [2, 3, 4]
    print("乘 3:", arr * 3)      # [3, 6, 9]
    print("5次方:", arr ** 5)    # [1, 32, 243]
    
    # 2. 向量化函数与圆面积计算实战
    # 公式: Area = pi * r^2
    radii = np.array([1.0, 2.0, 3.0])  # 半径
    areas = np.pi * (radii ** 2)
    print("计算出的各个圆面积:", np.round(areas, 2))  # 输出: [ 3.14 12.57 28.27]
    
    # 3. 元素级运算 (Elementwise)
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print("对应元素相加:", arr1 + arr2)  # [5, 7, 9]
    print("对应元素次方幂:", arr1 ** arr2)  # 1^4, 2^5, 3^6 -> [1, 32, 729]
    
    # 4. 比较运算符与条件过滤重写
    scores = np.array([91, 55, 100, 73, 82, 64])
    print("谁拿了满分:", scores == 100)      # 布尔数组: [False, False, True, False, False, False]
    print("及格状态 (>=60):", scores >= 60)  # [True, False, True, True, True, True]
    
    # 实战：不及格分数置零
    scores[scores < 60] = 0
    print("重置不及格后的成绩单:", scores)  # 55 变为了 0 -> [91, 0, 100, 73, 82, 64]
    ```
    

## 5. 广播机制 (Broadcasting) 的运行机制 `[00:33:25 - 00:39:36]`

### 💡 核心概念

- **什么是广播**：广播是指 NumPy 在对不同形状的数组执行算术运算时，具有虚拟拉伸、扩展较小数组的能力，从而使它们的物理形状匹配，避免多余的内存拷贝。
    
- **广播的核心匹配规则 (非常重要)**：
    
    从最右侧（最低维度）向左逐一比对两个数组的各维度大小，若满足以下任意一条件则兼容，可以广播：
    
    1. **对应维度的尺寸完全相等**。
        
    2. **其中一个数组在该维度的尺寸为 1**。
        

### 📊 广播兼容性对比与虚拟拉伸图解

#### 案例一（兼容）：`(1, 4)` 乘以 `(4, 1)`

```
Array 1: 1 x 4 ──> [[ 1,  2,  3,  4 ]] 虚拟横向拉伸为 4x4 ──> [[ 1, 2, 3, 4 ], [ 1, 2, 3, 4 ], ...]
Array 2: 4 x 1 ──> [[ 1 ], [ 2 ], [ 3 ], [ 4 ]] 虚拟纵向拉伸 ──> [[ 1, 1, 1, 1 ], [ 2, 2, 2, 2 ], ...]
相乘结果形状: 4 x 4 (乘法表)
```

#### 案例二（不兼容）：`(2, 4)` 与 `(4, 1)`

```
从右向左对齐:
维度 2 (最右侧): Array 1 为 4，Array 2 为 1 ────> 兼容 (其中一个是 1)
维度 1 (倒数第二): Array 1 为 2，Array 2 为 4 ────> 【不兼容】 (既不相等，也没有 1)
报错信息: ValueError: operands could not be broadcast together...
```

### 💻 完整命令与代码解析

- **实战：通过广播生成 10x10 九九乘法表**：
    
    ```
    import numpy as np
    
    # 横向向量：1行10列 (Shape: 1, 10)
    horizontal_vector = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    
    # 纵向向量：10行1列 (Shape: 10, 1)
    vertical_vector = np.array([
        [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]
    ])
    
    print("横向 Shape:", horizontal_vector.shape)
    print("纵向 Shape:", vertical_vector.shape)
    
    # 发生广播运算
    multiplication_table = horizontal_vector * vertical_vector
    print("九九乘法表矩阵 (10x10):\n", multiplication_table)
    ```
    

## 6. 聚合函数 (Aggregate Functions) 与轴向分析 `[00:39:47 - 00:43:42]`

### 💡 核心概念

- **什么是聚合**：汇总一整组数据并计算出一个单一的缩减值（如总和、平均值）。
    
- **轴向 (Axis) 的概念（初学者易错点）**：
    
    - 在 NumPy 中，对于 2D 矩阵：
        
        - **`axis=0`**：沿着**列 (Columns) 方向**向下进行计算，即把所有的行压缩。
            
        - **`axis=1`**：沿着**行 (Rows) 方向**向右进行计算，即把所有的列压缩。
            

### 📊 轴向运作流向图解

```
       axis=0 (沿列压缩计算)
         │  │  │  │
         ▼  ▼  ▼  ▼
      ┌──1──2──3──4──┐
      │  5  6  7  8  │ ──► axis=1 (沿行压缩计算)
      └──9─10─11─12──┘
```

### 💻 完整命令与代码解析

- **聚合 API 快速检索**：
    
    - `np.sum(arr)`：计算数组内元素的总和。
        
    - `np.mean(arr)`：计算平均值。
        
    - `np.std(arr)`：计算标准差（数据的离散程度）。
        
    - `np.var(arr)`：计算方差。
        
    - `np.min(arr)` / `np.max(arr)`：计算极值。
        
    - `np.argmin(arr)` / `np.argmax(arr)`：返回极值所在的**一维化索引位置**。
        
- **代码演示**：
    
    ```
    import numpy as np
    
    # 创建一个 2 行 5 列的矩阵
    matrix = np.array([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ])
    
    # 1. 基础全局聚合
    print("全局总和:", np.sum(matrix))       # 55
    print("平均值:", np.mean(matrix))        # 5.5
    print("最大值位置索引:", np.argmax(matrix)) # 9 (最后一个元素)
    
    # 2. 轴向聚合实战 (指定 axis 参数)
    # axis=0: 计算各列的和 (将两行叠在一起相加)
    col_sum = np.sum(matrix, axis=0)
    print("每一列的总和 (5个元素):", col_sum)  # 输出: [ 7  9 11 13 15]
    
    # axis=1: 计算各行的和 (将5列压缩在一起)
    row_sum = np.sum(matrix, axis=1)
    print("每一行的总和 (2个元素):", row_sum)  # 输出: [15 40]
    ```
    

## 7. 数组过滤与布尔过滤 (Filtering) `[00:43:52 - 00:51:59]`

### 💡 核心概念

- **布尔索引过滤 (Boolean Indexing)**：根据特定条件对 ndarray 进行筛选。不满足条件的元素会被剥离。
    
    - **注意缺陷**：常规的布尔索引过滤会把 2D/3D 数组**强行拍平 (Flatten)** 为 1D 数组。
        
- **逻辑运算符要求**：因为 NumPy 底层由 C 语言驱动，因此复合逻辑判断**不能**使用 Python 关键字 `and`/`or`，必须分别使用位运算符：
    
    - **`&` (且)** 代替 `and`。
        
    - **`|` (或)** 代替 `or`。
        
    - _注意：多个条件表达式必须用圆括号 `()` 括起来。_
        
- **保形过滤 (`np.where`)**：若需要过滤数据同时**维持原有的多维 Shape 结构**，必须使用 `np.where(condition, if_true_fill, if_false_fill)`，其利用指定的填充值替代不合规数据。
    

### 📊 过滤方式对比图解

```
原 2D 矩阵 (2x4 形状):
[[15, 22],
 [ 9, 33]]

【方式一：布尔索引过滤年龄 >= 18】 ──► 降维拍平为 1D 向量:
[22, 33]

【方式二：np.where(年龄>=18, 原年龄, 0)】 ──► 维持 2x4 原形状不变 (用0代替不合规者):
[[ 0, 22],
 [ 0, 33]]
```

### 💻 完整命令与代码解析

```
import numpy as np

# 声明学生年龄 of 2D 矩阵 (模拟两个班级，2行8列)
ages = np.array([
    [21, 17, 19, 20, 16, 30, 18, 65],
    [39, 22, 15, 99, 18, 19, 20, 21]
])

# 1. 基础布尔索引 (筛选青少年 ages < 18)
teenagers = ages[ages < 18]
print("青少年名单 (被拍平成了 1D):", teenagers)  # 输出: [17 16 15]

# 2. 复合逻辑运算实战 (筛选成人但不包含老年人 18 <= age < 65)
# 注意括号和 '&'
adults = ages[(ages >= 18) & (ages < 65)]
print("青壮年名单:", adults)

# 3. 奇偶筛选 (取模运算)
even_ages = ages[ages % 2 == 0]
print("偶数年龄:", even_ages)

# 4. 关键保形函数 np.where() 实战
# 场景：筛选大于等于 18 岁的学生，不足 18 岁的座位在分布图上标记为 0，不能改变座位表形状
structured_adults = np.where(ages >= 18, ages, 0)
print("座位表保形输出 (2x8 矩阵):\n", structured_adults)
# 此时不合规位置变成了 0，而矩阵依然保持 2行8列 格式不变
```

## 8. 随机数生成、原位洗牌与随机抽取 (Random Generator) `[00:52:07 - 00:59:51]`

### 💡 核心概念

- **新一代随机生成器 (RNG)**：现代 NumPy 舍弃了老旧的全局 `np.random.randint`，推荐使用 `np.random.default_rng()`，它运行速度更快，多线程安全性能更佳。
    
- **种子 (Seed) 设定**：指定种子后，生成的随机序列将能百分之百重现，这对模型的调试复现与科研至关重要。
    
- **原位洗牌 (In-place Shuffle)**：直接打乱既有数组内元素的顺序，会改变原数组。
    
- **随机选择 (Random Choice)**：从给定的一维数组或列表中进行随机抽取，支持输出多维格式，甚至支持中文/Emoji 表情。
    

### 💻 完整命令与代码解析

- **随机生成器 API 速查表**：
    
    |   |   |   |
    |---|---|---|
    |**方法**|**作用**|**备注**|
    |`np.random.default_rng(seed)`|初始化随机数发生器|推荐使用|
    |`rng.integers(low, high, size)`|生成指定范围的整型数组|前闭后开区间（不包含 `high`）|
    |`rng.uniform(low, high, size)`|产生均匀分布的浮点数|默认在 0 到 1 之间|
    |`rng.shuffle(arr)`|原位打乱数组次序|改变传入的数组|
    |`rng.choice(arr, size)`|随机抽取样本元素|适合做概率或抽样模拟|
    
- **随机模块代码综合演示**：
    
    ```
    import numpy as np
    
    # 1. 建立生成器，传入固定种子 (seed=1) 保证结果可复现
    rng = np.random.default_rng(seed=1)
    
    # 2. 模拟掷 6 面骰子 (范围 1 到 6，高限写 7)
    single_roll = rng.integers(low=1, high=7)
    print("单次掷骰子:", single_roll)
    
    # 3. 生成 3行2列 的随机大范围整数矩阵 (1-100)
    random_matrix = rng.integers(low=1, high=101, size=(3, 2))
    print("随机 3x2 矩阵:\n", random_matrix)
    
    # 4. 生成均匀分布的浮点数矩阵 (-1.0 至 1.0 之间)
    float_matrix = rng.uniform(low=-1.0, high=1.0, size=(2, 3))
    print("随机浮点数矩阵:\n", float_matrix)
    
    # 5. 原位打乱 (Shuffle) 演示
    poker_deck = np.array([1, 2, 3, 4, 5])
    rng.shuffle(poker_deck)
    print("洗牌后的牌堆:", poker_deck)  # 原数组顺序已被彻底打乱
    
    # 6. Emojis 随机水果抽取矩阵实战
    fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
    # 抽取一个 3x3 形状的水果阵列
    fruit_slots = rng.choice(fruits, size=(3, 3))
    print("水果老虎机 3x3 结果:\n", fruit_slots)
    ```
    

_祝您 NumPy 学习愉快！更多内容请查阅官方文档。_