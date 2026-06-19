
> 📚 本笔记整理自 numpy_course 项目，系统涵盖 NumPy 从基础到实战的核心知识点。

---

## 目录

- [[#一、ndarray 特性|一、ndarray特性]]
- [[#二、ndarray 属性|二、ndarray属性]]
- [[#三、ndarray 创建|三、ndarray创建]]
- [[#四、ndarray 索引与切片|四、ndarray索引与切片]]
- [[#五、ndarray 运算|五、ndarray运算]]
- [[#六、numpy 常用函数|六、numpy常用函数]]
- [[#七、numpy 统计函数|七、numpy统计函数]]
- [[#八、numpy 比较函数|八、numpy比较函数]]
- [[#九、numpy 排序函数|九、numpy排序函数]]
- [[#十、综合练习一|十、综合练习一]]
- [[#十一、综合练习二|十一、综合练习二]]

---

## 一、ndarray 特性

1.  多维性 : ndarray 可以是多维的,常见的一维 二维 三维等。
	- 多维的时候需要保证每个子列表长度一致,否则会被当成一维数组处理。
	- 格式 : 写起来和列表 `list[]` 差不多。
<br>
2.  同质性 : ndarray中的元素必须是**同一种数据类型**,如果混合了不同的数据类型,Numpy会自动将他们转换为一种兼容的类型。
<br>
3.  大小固定 : 一旦创建了 ndarray , 它的大小是固定的,不能动态调整。如果需要改变大小 , 需要创新一个新的 ndarray。

```python
import numpy as np
"""多维性"""
arr = np.array([1, 2, 3, 4, 5])
print(f"{arr}\narr的类型为:{type(arr)}\n维度:{arr.ndim}")

arr = np.array([[1,5,6,8,11,20], [8,56,2,11,32,0]])
print(f"{arr}\narr的类型为:{type(arr)}\n维度:{arr.ndim}")

"""同质性"""
arr = np.array([1, 'hello', 3.14])
arr2 = np.array([1, 2, 3.14])
print(f"{arr}\narr的类型为:{type(arr)}\n维度:{arr.ndim}")
print(f"{arr2}\narr2的类型为:{type(arr2)}\n维度:{arr2.ndim}")
```

---

## 二、ndarray 属性

1. 数组的形状 :  .shape( ) 用法 : `arr.shape` 返回一个元组 , 表示数组的维数和每个维度的大小。
<br>
2. 数组的维度 :   ndim 用法 : `arr.ndim` 返回一个整数 , 表示数组的维度。

>  注意多维的时候 : 是两层括号 `[[]]` 外层代表行数, 内层代表列数。

3. 数组内元素格式 : size 用法: `arr.size` 返回一个整数 , 表示数组中元素的总个数 。
<br>
4. 数组内的**元素类型:**   dtype 用法:   `arr.dtype` 返回一个数据类型对象,  表示数组中的元素类型 。
<br>
5. 数组的转置 T  用法 : `arr.T` 返回一个新的数组, 表示原数组的转置 。

```python
import numpy as np
arr1 = np.array(1) # 零维数组
arr2 = np.array([1,2,3])
arr3 = np.array([[7,8,9],[4,5,6]])
print(arr1)
print(arr2)
print(arr3)

# print(f"数组arr1的形状:{arr1.shape}\n数组arr2的形状:{arr2.shape}\n数组arr3的形状:{arr3.shape}")
# print(f"数组arr1的维数:{arr1.ndim}\n数组arr2的维数:{arr2.ndim}\n数组arr3的维数:{arr3.ndim}")
# print(f"数组arr1的元素个数:{arr1.size}\n数组arr2的元素个数:{arr2.size}\n数组arr3的元素个数:{arr3.size}")
# print(f"数组arr1的元素类型:{arr1.dtype}\n数组arr2的元素类型:{arr2.dtype}\n数组arr3的元素类型:{arr3.dtype}")
print(f"数组arr1转置后为:{arr1.T}\n数组arr2转置后为:{arr2.T}\n数组arr3转置后为:\n{arr3.T}")
```

---

## 三、ndarray 创建

1. ndarray 的创建

>[!example] 
>	list = [1, 2, 3]
>	arr = np.array(list)  当然直接把列表写到括号里边也行
>	ps :  .copy() 可以创建一个副本数组,  修改副本不会影响原数组 

2. 特殊创建 : 通过函数创建(全0 全1 未初始化 固定值(秩1阵))

>[!example]
>	 全0 : np.zeros(shape, dtype=float, order='C')
>	 全1数组: np.ones(shape, dtype=float, order='C')
>	 未初始化数组: np.empty(shape, dtype=float, order='C')
>	 固定值数组: np.full(shape, fill_value, dtype=float, order='C')

> [!example]- 1. 基础创建：从数据创建
> ```python
> import numpy as np
>
> arr = np.array([1, 2, 3])
> print(arr)  # [1 2 3]
>
> # 深拷贝：修改副本不影响原数组
> arr1 = np.copy(arr)
> arr1[0] = 24
> print(arr)   # [1 2 3]  原数组不变
> print(arr1)  # [24  2  3]
> ```

> [!example]- 2. 特殊创建：通过函数创建
> ```python
> # 全0数组（默认float，可用dtype指定）
> arr2 = np.zeros((2, 5))
> arr3 = np.zeros((3, 5), dtype=int)
>
> # 全1数组
> arr4 = np.ones((2, 5))
>
> # 未初始化数组（值为内存中的随机垃圾值，速度快）
> arr5 = np.empty((2, 5))
>
> # 固定值数组（所有元素相同，秩1阵）
> arr6 = np.full((3, 3), 7)
>
> # 等差数列 arange(start, stop, step)  右不包含
> arr7 = np.arange(0, 10, 2)  # [0 2 4 6 8]
>
> # 等间隔数列 linspace(start, stop, num)  右包含，num是元素个数，自动算步长
> arr8 = np.linspace(0, 10, 5)  # [ 0.   2.5  5.   7.5 10. ]
>
> # 对数等间隔数列 logspace(start, stop, num)  start/stop是指数，默认底数10
> # 先线性切分指数范围，再以10为底求值
> # start=0, stop=4, num=3 → 10^0, 10^2, 10^4 → [1, 100, 10000]
> f = np.logspace(1, 6, 1000)   # Bode图横轴
> arr9 = np.logspace(0, 4, 3)   # [1.e+00 1.e+02 1.e+04]
> ```

> [!example]- 3. 特殊矩阵
> ```python
> # 单位矩阵 eye(N, M=None, k=0)  N行 M列 k=对角线偏移
> eye = np.eye(3, 4, dtype=int)
>
> # 对角矩阵 diag(v, k=0)  v=对角线元素 k=对角线偏移
> diag = np.diag([1, 2, 3], k=0)
> ```

> [!tip]- 4. 随机数组（推荐使用新 Generator API）
> NumPy 1.17+ 推荐使用 `default_rng()` 创建独立实例，替代旧的 `np.random.xxx()` 全局函数。
>
> **创建 Generator 实例**（可传种子）：
> ```python
> rng = np.random.default_rng(42)
> ```
>
> | 方法 | 说明 | 示例 |
> |---|---|---|
> | `rng.random(size)` | 0~1 随机浮点数 | `rng.random((3, 4))` |
> | `rng.integers(low, high, size)` | 随机整数（不含high） | `rng.integers(0, 10, (3, 4))` |
> | `rng.normal(loc, scale, size)` | 正态分布 | `rng.normal(0, 1, (3, 4))` |
> | `rng.standard_normal(size)` | 标准正态（= normal(0,1)） | `rng.standard_normal((3, 4))` |
> | `rng.uniform(low, high, size)` | 均匀分布 | `rng.uniform(0, 10, (3, 4))` |
>
> ```python
> rng = np.random.default_rng(42)
>
> # 0~1 随机浮点数
> arr = rng.random((3, 4))
>
> # 随机整数（0到9）
> arr1 = rng.integers(0, 10, (3, 4))
>
> # 正态分布（均值0，标准差1）
> # 也等价于 rng.standard_normal((3, 4))，只需要传 size
> arr2 = rng.normal(0, 1, (3, 4))
>
> # 均匀分布（0到10）
> arr3 = rng.uniform(0, 10, (3, 4))
>
> print(arr3)
> ```

---

## 四、ndarray 索引与切片
- 基础知识 :
	- 索引从**0**开始 : 第一个元素是 `[0]` , 不是 `[1]` 
	<br>
	- 负索引 : `[-1]` 表示最后一个元素 , `[-2]` 表示倒数第二个
	<br>
	- 切片符号 ':' (冒号) , 切边规则 `[start : end]` 左闭右开
		<br>
	- 二维索引 : `arr[row, column]`
<br>

>**1. 一维数组 : 基本索引与切片**
```python
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(arr)

# ========== 基本索引 ==========

print(f"arr[0]:{arr[0]}")
prtit(f"arr[-1]:{arr[-1]}")
print(f"arr[-2]:{arr[-2]}")

# ========== 切片 arr[start:stop:step] ==========
print(arr[:]) # [10 20 ... 100 ]全部元素
print(arr[2:6]) # [30 40 50 60] 索引2到5(不含5)
print(arr[::2]) # [strp:2 即全部元素每隔一个元素取一个]
print(arr[::-1]) # [100 90 80 ...] 反转数组输出
print(arr[1:8:2]) # [20 40 60 80] 索引1到8,不长2

# ========== slice 对象（等价写法） ==========
print(arr[slice(1, 5)]) # 等价于 arr[1:5]
print(arr[slice(None, None, -1)])
```

>**2.二维数组: 索引与切片**

- **索引类型对比**：
    
    - **链式索引 (Chain Indexing)**：如 `arr[0][0][0]`，效率较低（每次调用都会创建一个临时临时对象）。
        <br>
    - **多维索引 (Multi-dimensional Indexing)**：如 `arr[0, 0, 0]`，NumPy 推荐写法，直接定位，速度极快。
	<br>
	
	
```python
import numpy as np
	arr = np.array( [1, 2, 3, 4],
				[5, 6, 7, 8],
				[9, 10, 11, 12])
					
	# 单元素访问(注意不论是行还是列 索引都是从0开始的)
	print(arr[0, 0]) # 1
	print(arr[1, 2]) # 7 
	print(arr[-1, -1]) # 12 
	
	# 取得完整的行(列) 注意不要省略逗号
	print(arr[0, :]) # 取得第1行全部元素 [1, 2, 3, 4]
	print(arr[:, 0]) # 取得第一列全部元素 [1, 5, 9]
		
	# 子矩阵切片
	print(arr[0:2,1:3]) # [2, 3]  前两行, 第2~3列
						# [6, 7]
		
	# 取得单行
	# 整数索引:消除维度,降一维,可以类比去图书馆从不同分区拿书,最后在你手上时,书从不同分区(维度)最后被你一次性全拿到手里(一维)
	# 切片索引（1:2）→ 保留该维度，即使只取了一行 意思就是"取第2行那一片区域" → 仍然放在原来的二维格子里
	print(arr[1,:]) # 第二行全部: [5, 6, 7, 8]
	print(arr[1:2,:]) # 二维 [[5, 6, 7, 8]] 
```
<br>

>[!Attention] 3.切片是视图, 不是副本 ! 
>	和Python的列表的切片区别在于 : Numpy 切片返回的是视图(view) , 修改切片会直接影响原数组 !
>	
>	arr = np.array([1, 2, 3, 4, 5]) 
>	sub = arr[1 : 4] 
>	# sub 拿到的是 : [2, 3 , 4]
>	# 但它不是自己存了一份附件 [2, 3, 4]
>	# 而是指向 arr 里 2、3、4
>	# 就像给 arr[1 : 4] 这一段取了个别名
>	sub[0] = 99 #  修改sub的第一个元素
>	# 明面上改的是 sub [0] 实际上是 arr[1] , 因为它们指向的是同一块内存
>	print(arr) # [1, 99, 3, 4, 5]
>	
>	# 如果想要个独立副本,使用 .copy()
>	sub2 = arr[1 : 4].copy()
>	sub[0] = 0
>	print(arr) # 原数组不变

>**4. 布尔索引**

基本原理：
1. 先用条件生成布尔数组
<br>
2. 再用布尔数组去原数组里取数，True 的位置留下，False 的位置丢掉
<br>
3. 布尔数组就像一张"筛子"，最终输出的是原数组的数字，不是 True/False

```python
import numpy as py

arr = np.array([3, 7, 1, 9, 4, 8, 2])
# print(arr > 5)            # [False  True False  True False  True False]
# print(arr[arr > 5])       # [7, 9, 8]
# print(arr[arr % 2 == 0])  # [4, 8, 2]

# 多条件组合（⚠️ 每个条件加括号）
print(arr[(arr > 3) & (arr < 9)])  # [7, 4, 8]
print(arr[~(arr > 5)])              # [3 1 4 2] 取反

# 二维布尔索引会降为一维！
A = np.array([[12, 3, 15], [2, 11, 9]])
print(A[A > 10])  # [12 15 11]  一维！

# 想保留形状用 np.where()
np.where(A > 10, A, 0)  # [[12 0 15] [0 11 0]]

# 配合 np.sum 统计满足条件的个数（True算1，False算0，求和就是个数）
print(np.sum(arr > 5))            # 3
print(np.count_nonzero(arr > 5))  # 3  等价写法

# 常用条件运算符：>  >=  <  <=  ==  !=
# 多条件组合：& 与  | 或  ~ 非（每个条件要加括号）
#   arr[(arr > 3) & (arr < 9)]    → 大于3且小于9
#   arr[(arr < 3) | (arr > 9)]    → 小于3或大于9
```

>[!Attention] 常见踩坑点
>   1. **二维布尔索引会降维**: A[A > 10] 返回一维数组，想保留形状用np.where()
>   2. **切片是视图**：改切片会改原数组，想要副本用 .copy()
>   3. **多条件必须加括号**：arr[arr > 3 & arr < 9] ❌ → arr[(arr > 3) & (arr < 9)] ✅ 
>   4. **逗号不能忘**：arr[行, 列]，不是 arr[行] [列]

---

## 五、ndarray 运算

### 5.1 基本四则运算

```python
# 简单的四则运算
import numpy as np
# 一维数组之间的运算
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)

# 二维数组之间的运算
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
```

### 5.2 广播机制 (Broadcasting)

>**广播规则:** 如果某一个维度满足以下两个条件之一,就可以成功广播
>-  这两个维度的数字完全相等。
>  <br>
>  -  其中一个维度的数字是 1
><br>

**具体操作：右对齐，从右往左逐维检查**

1. **维度对齐（左侧补 1 升维）**
   若两数组维度数不同，NumPy 必定在左侧补 1。
   例如：`(4,3)` 与 `(3,)` → `(3,)` 变为 `(1,3)`，绝不会补在右边变成 `(3,1)` 注意(3,)是一维数组,规则原因所以写成元组。

2. **逐维检查**，满足任一条件即可广播：
   - 该维度数字完全相等
   - 其中一方该维度为 1

3. 只要有一维不符合 → 报错 `ValueError (Shape Mismatch)`

> [!note]- 内存本质：步长 (Strides) 设为 0
>
> **广播不复制数据，只创建视图，把需要拉伸的维度步长改成 0，让指针原地循环读同一块内存。零额外内存，零复制开销。**
>
> ---
>
> **一、先搞懂什么是步长 (Strides)**
>
> NumPy 数组底层是一条连续内存，strides 就是**每走一步要跳多少字节**。
>
> ```python
> # 一维数组 [1, 2, 3]，dtype=int64（每个数占8字节）
> a = np.array([1, 2, 3], dtype=np.int64)
> print(a.strides)  # (8,)
> ```
>
> 内存图示：
> ```
> 地址:    0x00    0x08    0x10
> 数据:     [1]     [2]     [3]
>          ←8字节→ ←8字节→
> ```
>
> 再看二维：
> ```python
> b = np.array([[1, 2, 3],
>               [4, 5, 6]], dtype=np.int64)
> print(b.strides)  # (24, 8)
> ```
>
> ```
> 地址:    0x00  0x08  0x10  0x18  0x20  0x28
> 数据:     [1]   [2]   [3]   [4]   [5]   [6]
>          ←----一行3个=24字节----→
>
> strides = (24, 8)
>            ↑     ↑
>          行方向  列方向
>          跳24B   跳8B
> ```
>
> **行方向跳 24 字节** = 从 `b[0,0]` 到 `b[1,0]`，跳过一整行（3个元素 × 8字节）
> **列方向跳 8 字节** = 从 `b[0,0]` 到 `b[0,1]`，跳过一个元素
>
> ---
>
> **二、广播前：正常步长**
>
> `(3,)` 的数组 strides = `(8,)`，每走一步跳 8 字节。
>
> ```
> 内存:  [1]    [2]    [3]
> 地址:  0x00   0x08   0x10
>        ←8B→   ←8B→
>
> strides = (8,)
> ```
>
> ---
>
> **三、广播后：步长改成 0**
>
> 要把 `(3,)` 广播成 `(3,3)`，NumPy **不复制数据**，只创建一个新视图，把**行方向的步长改成 0**：
>
> ```
> 广播视图 shape=(3,3), strides=(0, 8)
>                            ↑
>                          行步长=0
>
> 内存里只有 3 个数：  [1]    [2]    [3]
> 地址：               0x00   0x08   0x10
> ```
>
> 访问过程：
> ```
> 第 0 行：指针从 0x00 开始，列步长 +8
>          读 0x00→1, 0x08→2, 0x10→3   → [1, 2, 3]
>
> 第 1 行：行步长 +0，指针还在 0x00
>          读 0x00→1, 0x08→2, 0x10→3   → [1, 2, 3]
>
> 第 2 行：行步长 +0，指针还在 0x00
>          读 0x00→1, 0x08→2, 0x10→3   → [1, 2, 3]
> ```
>
> 三行读的是同一块物理内存，指针在行方向"原地踏步"。
>
> ---
>
> **四、用代码验证**
>
> ```python
> a = np.array([1, 2, 3], dtype=np.int64)
>
> # 创建广播视图
> view = np.broadcast_to(a, (3, 3))
> print(view)
> # [[1 2 3]
> #  [1 2 3]
> #  [1 2 3]]
>
> print(view.strides)      # (0, 8)  ← 行步长=0！
> print(view.base is a)    # True    ← 底层数据还是 a，没复制
> ```
>
> ```python
> # 视图是只读的（因为多个位置指向同一块内存，改一个等于改所有）
> view[0, 0] = 99  # ❌ ValueError: assignment destination is read-only
>
> # 确实需要修改，先复制
> copy = view.copy()
> copy[0, 0] = 99  # ✅
> ```
>
> ---
>
> **五、为什么这么设计？**
>
> 瓶颈在内存带宽，不在 CPU。
>
> | 方案 | 额外内存 | 复制开销 |
> |------|---------|---------|
> | 真复制 | 8GB | 巨大 |
> | 步长=0 | **0 字节** | **零** |
>
> > NumPy 的计算大部分时间花在"把数据从内存搬到 CPU"，而不是 CPU 运算本身。步长设为 0 = 指针不动 = 零带宽开销。

**避坑指南**

| 类型 | 形状 | 说明 |
|------|------|------|
| 0 维标量 `5` | `()` | 适配任何维度 |
| 1 维行向量 `[1,2,3]` | `(3,)` | 广播时无条件补维成 `(1,3)` |
| 2 维列向量 | `(3,1)` | 只能横向拉伸 |

> [!warning] 双向广播陷阱
> `(3,) + (3,1)` 会双向广播，产生 `(3,3)` 矩阵！
> 若想对应元素计算，请用 `.reshape(3,1)` 或 `np.newaxis` 强锁 2D 维度

**演练场（从右往左看）**

| A | B | 对齐后 B | 过程 | 结果 |
|---|---|---------|------|------|
| `(4,3)` | `(3,)` | `(1,3)` | 末尾 3==3，倒数 1变4 | ✅ `(4,3)` |
| `(3,3)` | `(3,1)` | — | 末尾 1变3，倒数 3==3 | ✅ `(3,3)` |
| `(4,3)` | `(4,)` | `(1,4)` | 末尾 3与4 不匹配 | ❌ 报错 |
| `(2,3,4)` | `(3,1)` | — | 最后维 4与1（有1）；倒数第二维 3==3；最前面 2与1（有1） | ✅ `(2,3,4)` |

**双向广播实例：`(3,) + (3,1)`**

```python
a = np.array([1, 2, 3])       # (3,) -> 补为 (1, 3)
b = np.array([[4], [5], [6]])  # (3, 1)
print(a + b)                   # 双向广播，结果 (3, 3)
```

a `(1,3)` 纵向拉伸为 `(3,3)`：　　b `(3,1)` 横向拉伸为 `(3,3)`：

```
1  2  3                             4  4  4
1  2  3                             5  5  5
1  2  3                             6  6  6
```

对应元素相加 → 结果 `(3,3)`：

```
5  6  7
6  7  8
7  8  9
```

> [!tip] 内存效率
> NumPy 没有真的复制数据，步长设为 0 实现虚拟拉伸，效率很高

### 5.3 标量运算
由于广播机制的存在所以numpy数组可以和标量计算,因为标量属于**0维数组** , 广播的时候可以随意"拉伸、扩展" , 进而适配任意维度的数组

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
# print(arr + 10)
# print(arr * 10)
```

### 5.4 矩阵运算
**Numpy里矩阵运算分两种:**
- _元素级运算_: 就是对矩阵的每个元素进行相同的运算 , 比如 加减乘除等 , 这些运算都是逐元素进行的 , 结果也是一个矩阵 , 形状和元素组相同 。
<br>
- _矩阵乘法_ : 就是按照线性代数中定义的矩阵乘法运算 , 某一行和某一列的元素成绩之和(点积) 。 使用 @ 或者np.dot()函数 。

```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a * b)
print(a @ b)
```

---

## 六、numpy 常用函数

### 6.1 数学运算

| 函数               | 说明           | 示例结果                       |
| ---------------- | ------------ | -------------------------- |
| `np.sqrt(x)`     | 算术平方根        | `sqrt(16)` → 4.0           |
| `np.exp(x)`      | 指数（e 的 x 次方） | `exp(1)` → 2.718...        |
| `np.log(x)`      | 自然对数 ln      | `log(1)` → 0.0             |
| `np.power(x, n)` | 次幂           | `power(2, 3)` → 8          |
| `np.abs(x)`      | 绝对值          | `abs([-1,-2,3])` → [1,2,3] |

```python
import numpy as np

# 平方根
print(np.sqrt(16))              # 4.0
print(np.sqrt([1, 4, 9, 16]))   # [1. 2. 3. 4.]

# 指数
print(np.exp(1))   # 2.718281828...（e 的 1 次方）
print(np.exp(-1))  # 0.3678...

# 对数
print(np.log(1))       # 0.0  （ln(1) = 0）
print(np.log(np.e))    # 1.0  （ln(e) = 1）

# 次幂
print(np.power(2, 3))           # 8
print(np.power([1, 2, 3], 2))   # [1, 4, 9]  每个元素的平方

# 绝对值
arr = np.array([-1, -2, 3, -4])
print(np.abs(arr))  # [1 2 3 4]
```

### 6.2 三角函数

| 函数 | 说明 | 常用值 |
|------|------|--------|
| `np.sin(x)` | 正弦 | `sin(π/2)` → 1.0 |
| `np.cos(x)` | 余弦 | `cos(0)` → 1.0 |
| `np.tan(x)` | 正切 | `tan(π/4)` → 1.0 |

```python
print(np.sin(np.pi / 2))  # 1.0
print(np.cos(0))           # 1.0
print(np.tan(np.pi / 4))   # 0.9999...（接近 1）
```

### 6.3 取整与舍入

| 函数 | 说明 | 注意事项 |
|------|------|---------|
| `np.round(x, n)` | 四舍五入，保留 n 位小数 | ⚠️ 银行家舍入法：`.5` 向最近的**偶数**靠拢，如 `4.5 → 4`，`5.5 → 6`；但 `4.51 → 5` |
| `np.ceil(x)` | 向上取整 | `3.1` `3.5` `3.9` 都 → 4 |

```python
# 四舍五入
print(np.round(3.14159, 2))  # 3.14  保留两位小数
print(np.round(4.5))          # 4.0   银行家舍入，向偶数靠拢
print(np.round(5.5))          # 6.0   同上

# 向上取整
print(np.ceil([3.1, 3.5, 3.9]))  # [4. 4. 4.]
```

### 6.4 缺失值检测 & 累加

| 函数 | 说明 |
|------|------|
| `np.isnan(x)` | 检测 NaN，返回布尔数组（`True` 表示是缺失值） |
| `np.cumsum(x)` | 累加和，返回等长数组，每个元素是该位置及之前所有元素的和 |

> [!info] 关于 np.nan
> `np.nan` 是一个特殊的浮点数，表示缺失值或不可用的值。
> 它在数值计算中经常出现，比如除以零、无效操作或数据缺失等场景。

```python
# 检测缺失值
print(np.isnan(np.array([1, 2, 3, 4])))        # [False False False False]
print(np.isnan(np.array([1, 2, np.nan, 4])))    # [False False  True False]

# 累加和
print(np.cumsum([1, 2, 3, 4]))  # [ 1  3  6 10]
#  过程：1, 1+2=3, 1+2+3=6, 1+2+3+4=10
```

---

## 七、numpy 统计函数

### 7.1 基本统计量

| 函数 | 说明 |
|------|------|
| `np.sum(x)` | 求和（可指定 axis 按行或列求和） |
| `np.mean(x)` | 平均值 |
| `np.median(x)` | 中位数 |

```python
import numpy as np

arr = np.random.randint(1, 20, 8)
print(arr)
print(np.sum(arr))      # 求和
print(np.mean(arr))     # 平均值
print(np.median(arr))   # 中位数
```

### 7.2 离散程度

| 函数          | 说明                      |
| ----------- | ----------------------- |
| `np.var(x)` | 方差 = 每个数据点与平均值之差的平方的平均值 |
| `np.std(x)` | 标准差 = $\sqrt{方差}$       |

> [!info] 方差与标准差
> - **标准差越大**，数据越分散；**标准差越小**，数据越集中
> - 方差和标准差的关系：`std = √var`

```python
print(np.var(arr))   # 方差
print(np.std(arr))   # 标准差
```

### 7.3 分位数

`np.percentile(x, q)` — 将数据按大小排序后，按比例划分。`q` 是百分比（0~100）

| q 值 | 名称 | 含义 |
|------|------|------|
| 25 | 第一四分位数（Q1） | 25% 的数据小于等于该值 |
| 50 | 中位数（Q2） | 50% 的数据小于等于该值 |
| 75 | 第三四分位数（Q3） | 75% 的数据小于等于该值 |

```python
import numpy as np
np.random.seed(0)
arr = np.random.randint(0, 100, 4)
print(arr)                     # [44 47 64 67]
print(np.percentile(arr, 25))  # 46.25
print(np.percentile(arr, 50))  # 55.5
```

---

## 八、numpy 比较函数

```python
import numpy as np

# 比较是否大于 .greater(a, b) 返回一个布尔值数组，表示a中的元素是否大于b中的对应元素。

# print(np.greater(1, 2))
# print(np.greater([1, 2, 3], [2, 2, 2]))

# # 比较是否小于 .less(a, b) 返回一个布尔值数组，表示a中的元素是否小于b中的对应元素。
# print(np.less([1, 2, 7, 9, 55], 4))

# # 比较是否等于 .equal(a, b) 返回一个布尔值数组，表示a中的元素是否等于b中的对应元素。
# print(np.equal([5, 6, 7], 8))
# print(np.equal([1, 2, 3], [1, 2, 4]))

# print("分割线".center(50, "-"))

# # 与或非
# print(np.logical_and([1, 0, 1], [1, 1, 0]))
# print(np.logical_or([1, 0, 1], [1, 1, 0]))
# print(np.logical_not([1, 0, 1]))

# # 自定义条件 .where(condition, x, y) 根据条件返回x或y中的元素。 符合条件返回x，不符合条件返回y
# # 有点像三元运算符。 value_if_true if condition else value_if_false
# arr = np.array([1, 5, 11, 21, 78, 6])
# print(np.where(arr > 10, arr, 0))  # 大于10的元素保留，不大于10的元素替换为0
# print(np.where(arr % 2 == 0, 1, -1))

# score = np.random.randint(50, 100, 20)
# print(score)
# # print(np.where(score >= 60, "及格", "不及格"))
# print(np.where(score >= 90, "优秀", np.where((score > 60) & (score < 90), "良好", "不及格"))) # 嵌套使用

# np.select(conditions, choices, default=0) 根据多个条件返回对应的值。 conditions是一个条件列表，choices是一个值列表，default是默认值。

np.random.seed(0)
score = np.random.randint(50, 100, 20)
print(score)
conditions = [score >= 90, (score >= 60) & (score < 90), score < 60]
choices = ["优秀", "及格", "不及格"]
print(np.select(conditions, choices, default="未知"))
```

---

## 九、numpy 排序函数

```python
"""
  # ==================== NumPy 新版随机数生成器 ====================
  # 旧版用法：np.random.seed(42) + np.random.randint(...)，基于全局状态，容易被其他代码干扰
  # 新版用法：rng = np.random.default_rng(42)，返回独立的生成器对象，各管各的
  #
  # 什么是"独立生成器对象"？
  #   旧版所有随机操作共享一个全局种子，任何地方调用 np.random.xxx() 都会影响整体状态
  #   新版每个 rng 对象有自己的内部状态，多个 rng 互不干扰，适合多处需要独立随机的场景
  #   例如：
  #     rng1 = np.random.default_rng(1)   # 生成器1，独立状态
  #     rng2 = np.random.default_rng(2)   # 生成器2，独立状态
  #     rng1.integers(1,100,5)            # 不影响 rng2
  #     rng2.integers(1,100,5)            # 不影响 rng1
  #
  # 参数说明：
  #   np.random.default_rng(种子)  - 创建生成器对象，种子可以是整数、字符串，不传则每次随机
  # 
  # 常用方法：
  #   rng.integers(start, end, n)  - 生成 start~end-1 的随机整数数组，长度为 n
  #   rng.random(n)                - 生成 0~1 之间的随机浮点数数组，长度为 n
  #   rng.normal(均值, 标准差, n)   - 生成正态分布的随机数数组，长度为 n
  #   rng.choice(数组, n)          - 从数组中随机抽样 n 个（有放回，可能重复）
  #   rng.choice(数组, n, replace=False) - 从数组中随机抽样 n 个（无放回，不重复）
  #   rng.shuffle(arr)             - 原地打乱数组（会修改原数组）
  #   rng.permutation(arr)         - 返回打乱后的副本（不修改原数组）
  # ================================================================


"""
import numpy as np
rng = np.random.default_rng(42)
arr = rng.choice(range(1, 101), size=20, replace=False)
"""
rng.choice(a, size=None, replace=True, p=None, axis=0, shuffle=True)
    a:必填。抽样来源，可以是数组、列表、range，或一个整数（表示 range(a)）
    size:输出的形状，比如 5 或 (3, 4)，默认 None（返回单个值）
    replace:True 有放回（可重复），False 无放回（不重复），默认 True
    p:每个元素被选中的概率，长度必须和 a 相等，默认 None（等概率）
    axis:沿哪个轴抽样，默认 0
    shuffle:抽样前是否打乱，默认 True
"""
# print("原始数组:", arr)
# print(arr.sort()) # 原地排序，返回 None ，会修改原数组
# print("排序后的数组:", arr)

# 如果不想修改原数组，可以使用 np.sort()，它会返回一个新的排序后的数组。
arr1 = np.sort(arr)
print("原始数组:", arr)
print("排序后的数组:", arr1)
print("排序后原始数组:", arr)
print("索引位置:", np.argsort(arr))  # 返回排序后元素在原数组中的索引位置，长度和 arr 相同

print("分割线".center(50, "-"))
# 去重函数 .unique(arr) 返回一个排序后的唯一元素数组，默认升序 (去重但去重后剩下的元素数量会小于原数组)
arr2 = rng.choice(range(1, 11), size=20, replace=True)
print("原始数组:", arr2)
print("去重后的数组:", np.unique(arr2))

# 数组的拼接 .concatenate((a, b)) 将多个数组沿指定轴连接起来，默认 axis=0（竖直连接），也可以指定 axis=1（水平方向连接）
print("分割线".center(50, "-"))
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("拼接后的数组:", np.concatenate((a, b)))

# 数组的分割 .split(arr, indices_or_sections) 将数组分割成多个子数组，indices_or_sections 可以是整数（表示平均分成多少份）或一个索引列表（表示在哪些位置分割）
print("分割线".center(50, "-"))
print(np.split(arr, 4))  # 平均分成4份，无法平均分会报错
print(np.split(arr, [5, 10]))  # 在索引位置5和10分割，返回3个子数组

# 调整数组的形状 .reshape(new_shape) 返回一个新的数组，具有指定的形状，但元素数量必须保持不变
print("分割线".center(50, "-"))
print(arr.reshape(4, 5))
```

---

## 十、综合练习一

```python
import numpy as np
"""
练习一:
有一组数据表示某地7天的最高气温，分别为28, 30, 29, 31, 32, 30, 29。请使用NumPy计算以下内容：
1. 平均气温
2. 最大气温
3. 最小气温
4. 大于30度的天数
"""

# arr = np.array([28, 30, 29, 31, 32, 30, 29])
# print(f"平均气温为:{np.mean(arr)}°")
# print(f"最大气温为:{np.max(arr)}°")
# print(f"最小气温为:{np.min(arr)}°")
# # 1.使用布尔索引
# print(arr[arr > 30])
# print(len(arr[arr > 30]))
# print(f"1.大于30的元素个数为:{len(arr[arr > 30])}")

# # 2.使用广播特性
# # 广播特性,30是零维数组,广播后变成和arr一样的形状,每个元素都和30进行比较,得到一个布尔数组,再对布尔数组求和,True被当做1,False
# print(f"2.大于30的元素个数为:{np.sum(arr > 30)}")

# # 3.或者使用.where()函数来获取满足条件的元素的索引
# a = np.where(arr > 30, arr, 0)  # 满足条件的元素保留原值,不满足条件的元素替换为0
# print(a)
# print(np.sum(a > 0))

# # 4.或者让where返回1 然后求累加就行
# b = np.where(arr > 30, 1, 0)  # 满足条件的元素替换为1,不满足条件的元素替换为0 然后通过索引取到最后一个元素的值就是满足条件的元素个数
# print(np.cumsum(b)[-1])

#  练习二:矩阵运算 注意区分 元素级乘法 和 矩阵乘法
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# print(A + B)
# print(A * B) # 这是元素级乘法,不是矩阵乘法
# print(A @ B) # 这是矩阵乘法,也可以使用np.dot(A, B)来实现矩阵乘法


# 练习三: 生成一个3行4列的随机整数矩阵,元素范围在0到10之间,然后
# 计算每行和每列的最大值和最小值。
# 将数组中所有的奇数替换为-1。
rng = np.random.default_rng(42)
arr = rng.integers(0, 11, size=(3, 4))
print(arr)

# # : 切片操作符 : 表示从哪儿到哪儿 或者 全部的意思 这个0 : 就是第 0行全部
# print(f"第0行最大值:{np.max(arr[0, :])}", f"最小值: {np.min(arr[0, :])}")
# print(f"第1行最大值:{np.max(arr[1, :])}", f"最小值: {np.min(arr[1, :])}")
# print(f"第2行最大值:{np.max(arr[2, :])}", f"最小值: {np.min(arr[2, :])}")

# 或者使用max的参数axis来指定求最大值的轴,axis=0表示 按列 求最大值,axis=1表示 按行 求最大值
print(f"每列的最大值:{np.max(arr, axis=0)}", f"每列的最小值: {np.min(arr, axis=0)}")
print(f"每行的最大值:{np.max(arr, axis=1)}", f"每行的最小值: {np.min(arr, axis=1)}")


# .where(条件,参数1,参数2) 就是如果满足条件则保留原值(参数1), 不满足条件的元素替换为参数2
matrix1 = np.where(arr % 2 != 0, -1, arr)
print(matrix1)
```

---

## 十一、综合练习二

```python
import numpy as np

"""
练习一:
1. 创建一个包含1到12的数组，并将其重塑为3行4列的二维数组。
2. 计算每行的和，并打印结果。
3. 计算每列的平均值，并打印结果。
4. 将二维数组重新转换为一维数组，并打印结果。
"""

# arr1 = np.arange(1, 13)
# arr2 = np.reshape(arr1, (3, 4))
# print(arr2)
# row_sum = np.sum(arr2, axis=1)
# print(f"每行的和为:{row_sum}")
# col_mean = np.mean(arr2, axis=0)
# print(f"每列的平均值为:{col_mean}")
# arr3 = np.reshape(arr2,12)
# print("3*4矩阵转成一维数组:", arr3)


"""练习二:
随机生成一个5x5的整数数组，范围在0到20之间。
使用布尔索引找出数组中大于10的元素，并将它们替换为0。

"""
# rng = np.random.default_rng(42)
# A = rng.integers(0, 20, (5, 5))
# print(A)
# print("分隔线".center(50, '-'))
# # 使用布尔索引找出A中大于10的元素
# print(A[A > 10])
# a = A[A > 10] = 0
# print(a)

"""
练习三:
某公司的6个月的销售数据如下：120, 135, 110, 125, 130, 140。
1. 将销售数据存储在一个NumPy数组中。
2. 计算销售数据的总和、平均值和方差，并打印结果。
3. 找出销售额最高的月份和最低的月份，并打印结果。
"""

# sale = np.array([120, 135, 110, 125, 130, 140])
# print(np.sum(sale))
# print(np.mean(sale))
# print(np.var(sale))
# print(np.argmax(sale))  # 如果不带arg 则返回的是最大值，如果带arg则返回的是最大值的索引
# print(np.argmin(sale))

"""练习四:
给两个数组A和B，分别为A = [1, 2, 3]和B = [4, 5, 6]。
1.水平拼接A和B，得到一个新的数组。
2.垂直拼接A和B，得到一个新的数组。
"""
# A = np.array([1, 2, 3])
# B = np.array([4, 5, 6])
# print(np.concatenate((A, B)))  # 默认 axis=0 按行方向移动拼接
# print(np.concatenate([[A],[B]])) # 先将 A 和 B 包装成二维数组 [[1, 2, 3], [4, 5, 6]]，再按行方向拼接，结果是 [[1, 2, 3], [4, 5, 6]]


"""练习五:
给定数组arr = [2, 1, 2, 3, 1, 4, 3]
1.找出其中的唯一元素
2.并统计每个唯一元素在原数组中出现的次数。
"""
arr = np.array([2, 1, 2, 3, 1, 4, 3])
# NumPy 的函数，return_counts=True 表示"顺便告诉我每个数出现了几次"。
# 它返回两个数组：一个是去重后的唯一元素数组，另一个是对应的计数数组。
u_arr, counts = np.unique(arr, return_counts=True)
print(u_arr)  # 去重后的唯一元素数组
print(counts)  # 每个唯一元素在原数组中出现的次数
# 或者使用for循环+布尔索引找
my_list = []
for i in range(len(u_arr)):
    my_list.append(len(arr[arr == u_arr[i]]))
print(my_list)
```

---

## 📝 学习总结

### 核心知识点

| 模块 | 重点内容 |
|------|----------|
| ndarray 特性 | 多维性、同质性、大小固定 |
| ndarray 属性 | shape、ndim、size、dtype、T |
| 创建方法 | array、zeros、ones、arange、linspace、random |
| 索引切片 | 基本索引、切片、布尔索引 |
| 运算 | 四则运算、广播机制、矩阵乘法 |
| 常用函数 | sqrt、exp、log、abs、power、round |
| 统计函数 | sum、mean、median、std、var、percentile |
| 比较函数 | greater、less、equal、where、select |
| 排序函数 | sort、argsort、unique、concatenate、split、reshape |

### 关键要点

1. **广播机制**：右对齐，从右往左逐维检查，内存不复制（步长设为0）
2. **布尔索引**：用 True/False 数组筛选元素，结果降为一维
3. **元素级 vs 矩阵乘法**：`*` 是元素级，`@` 或 `np.dot()` 是矩阵乘法
4. **原地 vs 返回副本**：`.sort()` 原地排序，`np.sort()` 返回副本

---

> 📁 项目路径：`E:\All_Projects\pycharm_project\Data _analysis_study\numpy_course\`
> 
> 📅 整理时间：2026-06-16
