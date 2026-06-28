> [!warning] NumPy vs OpenCV：宽高顺序的"暗坑"
> 
> 这是 OpenCV 初学者最容易犯的错，**贯穿所有后续操作**（画图、缩放、裁剪等），务必牢记。
> 
> | 来源 | 顺序 | 代码写法 |
> |:---:|:---:|------|
> | **NumPy**（`shape`） | **(高, 宽)** | `frame.shape[0]` = 高度，`frame.shape[1]` = 宽度 |
> | **OpenCV**（`resize`、`circle` 等） | **(宽, 高)** | `dimensions = (width, height)` |
> 
> **为什么顺序不同？**
> *   **NumPy 的视角（矩阵视角）**：把图片看作矩阵，规格是"行 × 列"，行数 = 高度，列数 = 宽度 → 所以是 **(高, 宽)**。
> *   **OpenCV 的视角（几何视角）**：使用数学课上的**笛卡尔坐标系 $(X, Y)$**，$X$ = 宽度，$Y$ = 高度 → 所以是 **(宽, 高)**。
> 
> **口诀：读 shape 是"高宽"，传参数是"宽高"。** 懂了这一个坑，你就超越了 90% 的 OpenCV 初学者。

## 一、Open CV 的安装

可以在虚拟环境下安装也可以全局安装 <br>

```
打开终端输入以下命令:

📌 先建立虚拟环境
python -m venv .venv  

📌 再激活该虚拟环境
.venv\Scripts\activate

📌 最后安装 opencv 包
pip install opencv-python

如果想全局安装直接执行: pip install opencv-python 即可

```


## 二、读取图片和视频

1. 图片的读取:<br>
	  `.imread()` 用来读取图片，把图片文件加载到内存里变成一个数组,读取完, img 就是个数组 ,里边的值就是每个像素的颜色。
	<br>

```python
import cv2 as cv

path1 = "E:/All_Projects/pycharm_project/Data _analysis_study/Opencv/attachments/Ellie.png"

img = cv.imread(path1)

if img is None:
	raise FileNotFoundError(f"图片读取失败：{path1}")

📌 弹窗显示图片,参数1显示图片名字,参数二是要显示的图片
cv.imshow("Ellie", img) 

cv.waitKey(0)
print(img.shape) # 输出图片的尺寸信息

```

> 注意 : 
> 
> 1. `.imread()` 返回的不是原图文件，是副本，改 img 不会影响原文件。
> <br>
> 2. VS Code 的 Pylance 静态分析可能会提示"shape”不是 "None" 的已知属性。它的意思是说 cv2.imread 有可能 返回 **None**（比如文件不存在时），以此提醒你 .shape 可能出问题。所以添加一个 **if判断**抛出错误。
> 	<br>
> 3. `.waitKey(自己填入数值):`  等待按键事件，就是显示图片后暂停程序，不让窗口马上关闭 括号内数值为等待的时间, 单位毫秒。
> <br>

<br>
> [!info] 图像在计算机中存储的核心本质
> 
> **像素颜色和图像尺寸，其实就是同一个多维数组（矩阵）的值和形状。** 理解了"三维数组"，就理解了计算机视觉的基石。更直观的类比见下方 ↓

### 🧩 图解：像素、图片尺寸与多维数组的关系

我们把这个抽象的数学概念，拆解成一个**看得见、摸得着的物理模型**。

请暂时忘掉"三维数组"这种计算机专业词汇，我们用 **"药盒"** 来做类比。

---

#### 第一步：先看最基础的单位——"像素"（一格药盒）

屏幕上的每一个彩色发光点，叫一个**像素（Pixel）**。
为了配出任何颜色，每个像素点里都有三个微小的发光灯管：**红灯、绿灯、蓝灯**（OpenCV 里的顺序是蓝、绿、红 BGR）。

在 Python 里，我们要描述某一个像素点的颜色，需要 3 个数字。比如：
`[255, 0, 0]` （代表蓝灯开到最亮，绿灯和红灯熄灭。在 OpenCV 里这就是纯蓝色）。

*   **物理模型**：这就像一个**只能装 3 颗药丸的小药盒**。
*   这个小药盒的内部结构是：`[第一格放蓝药, 第二格放绿药, 第三格放红药]`。

---

#### 第二步：把小药盒拼成一个"药盒矩阵"（宽和高）

现在，我们要拼出一张宽为 4 个像素、高为 3 个像素的微型彩色图片。

我们拿 **12 个**刚才那样的小药盒，整整齐齐地摆在桌子上，摆成 **3 行、4 列**：

```
第一行： [药盒] [药盒] [药盒] [药盒]
第二行： [药盒] [药盒] [药盒] [药盒]
第三行： [药盒] [药盒] [药盒] [药盒]
```

这就是你的图片。

---

#### 第三步：现在，我们要数数了（理解 `img.shape`）

当你在 Python 里输入 `img.shape` 时，计算机其实是在帮你数这个"药盒方阵"的尺寸。它会按照 **"由外到内"** 的顺序数出三个数字：

1.  **第一个数字（高 Height）**：数一数，桌子上有几行药盒？ 👉 答：**3 行**。
2.  **第二个数字（宽 Width）**：数一数，每行有几列药盒？ 👉 答：**4 列**。
3.  **第三个数字（通道数 Channels）**：打开任意一个药盒，里面有几格放药的位置？ 👉 答：固定是 **3 格**（放蓝、绿、红药丸）。

所以，计算机数出来的结果就是：`shape = (3, 4, 3)`

---

#### 第四步：怎么用坐标找药丸？（理解图片定位）

如果你想吃 **"第二行、第三列药盒里的红药丸"**，你在 Python 里该怎么写？

在 Python（Numpy 数组）里，**计数是从 0 开始的**：
*   "第二行"对应的索引是 `1`
*   "第三列"对应的索引是 `2`
*   "红药丸"（第3格）对应的索引是 `2`（0是蓝，1是绿，2是红）

所以，你直接在代码里写：

```python
药丸 = img[1, 2, 2]
```

计算机就会精准地定位到第二行、第三列那个药盒，打开第三个格子，把里面的数字（比如 `255`）取出来给你。

---

#### 总结：为什么说它们是"同一个东西的两个角度"？

| 角度 | 描述 | 对应概念 |
|:---:|------|------|
| **A. 尺寸/形状** | 从远处看，这是一个 $3 \times 4 \times 3$ 的三维药盒立方体 | `img.shape` |
| **B. 像素/颜色** | 凑近看，里面每一个格子里存的数字（0\~255），决定了那个位置发什么光 | 图像的像素值 |

图片在计算机里**根本不是什么艺术品**，它就是一个**整整齐齐码放数字的、有长宽深的立方体盒子**。理解了这一点，你就真正入门了计算机视觉（CV）。
> 



2. 视频的读取:<br>
		`.VideoCapture():` 打开视频,即 python 拿到一个视频对象
		<br>
		`xxx.read():` 读取视频的一帧, 因为视频就是连续动的图片,read()每次只能读取一张画面, 所以使用while循环来读取每一帧画面。
		<br>
```python
import cv2 as cv
path2 = "E:/All_Projects/pycharm_project/Data _analysis_study/Opencv/attachments/5.1-2025-深圳大学(2).mp4"

cap = cv.VideoCapture(path2)

📌 因为是视频是一帧一帧读取的, 所以需要使用while循环
while True:
	isTrue, frame = cap.read() # 首先读取视频
	if not isTrue:
		print("📹 视频播放结束，或者摄像头已断开连接。安全退出中...")
		break
	cv.imshow("video", frame)
	
	if cv.waitKey(20) & 0xFF == ord('0')
		break
		
cap.release()
cv.destroyAllWindows()
```

> 注意 : 
> 1.  `.read()`会返回两个值,且这两个值会以**元组**的形式打包在一起返回, 所以要使用 **两个变量** 来接收返回值。
> 	 <br>
> 2. 第一个返回值 isTrue（行业内通常写成 ret，即 return value 的缩写)：
> 	- 它是一个**布尔值 (Boolean)**，只有 True（真）或 False（假）两种状态。
> 	- **作用**：告诉你“这一帧画面有没有读取成功”。如果视频正在正常播放，它就是 True；如果视频放完了，或者摄像头突然被拔掉了，它就会变成 False。
> 	<br>
> 3. **第二个返回值 frame**：
> 	- 它才是真正的**图像矩阵（numpy 数组）**。
> 	

<br>

> [!question] OpenCV为什么要设置 `isTrue` ,为什么不能直接返回 `frame` ?
> - 这就是**控制工程中的“鲁棒性（Robustness/健壮性）”设计**
> 	<br>
> - 如果视频播放完了，或者摄像头线断了，cap.read() 拿不到图像。如果它只返回 frame，你的程序在执行到 imshow 时就会因为读到空数据而**直接闪退（Crash）**。这在工业机器人控制中是极其致命的。
> 	<br>
> - 有了 isTrue，就可以在程序里做一个“**安全保护/边界拦截**”。即 if条件语句判断。
> 	<br>
> -  `ord()` 是 Python 的一个内置函数，它的全称是 **ordinal（序号/顺序）**。**作用:** 输入一个字符,返回ASCII 码值。
> 	<br>
> - `& 0xFF` 是 **按位与** 操作, 作用是保留低8位, 屏蔽高位。
> 	<br>
> 	- 在 64 位操作系统上，`cv.waitKey()` 返回的可能是一个 32 位的整数（而不仅仅是 8 位的 ASCII 码）。
> 	<br>
> 	- `0xFF` 的二进制是 `11111111`（即低 8 位全为 1，高位全为 0）。
> 	<br>
> 	- 通过按位与运算 `& 0xFF`，可以将返回的 32 位整数的高 24 位全部清零，只保留最右边的 8 位。
> 	<br>
> 	- 这样可以确保在不同操作系统（如 Windows, Linux, macOS）或不同架构（32位/64位）下，获取到的按键值都是标准的 ASCII 码，避免因系统差异导致比对失败。
> 	<br>


## 三、调整和缩放视频帧与图像尺寸/

### 为什么需要缩放？

在控制工程和机器人视觉中，摄像头的原始画面可能非常大（比如 $1920 \times 1080$）。如果直接让算法去处理这么大的图片，电脑会非常卡（**实时性变差**）。

所以我们需要一个工具：**把每一帧画面等比例缩小（比如缩小到 75%），从而提高程序的运行速度。**

> [!tip] 1.缩放本地视频文件或静态图片
> 不要去死记硬背整段代码。把写代码的过程想象成 **"把人类的语言，翻译成计算机的步骤"**。下面这个流程图，就是从中文逻辑翻译到代码的完整过程：

```mermaid
graph TD
    A["① 拿到原图的宽和高
    shape[0] = 高, shape[1] = 宽"] --> B["② 乘以缩放比例，转换成整数
    int(宽 * scale), int(高 * scale)"]
    B --> C["③ 打包成 (宽, 高) 的元组
    dimensions = (width, height)"]
    C --> D["④ 调用 cv.resize 缩小并返回
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)"]
```


```python
import cv2 as cv

📌 因为是个重复动作,以后可能会复用,所以写成函数而不是直接塞进while循环

def rescaleFrame(frame, scale=0.75)

	width = int(frame.shape[1] * scale) # 拿到原图的宽然后缩小
	height = int(frame.shape[0] * scale) # 拿到原图的高然后缩小
	dimensions = (width,height) # OpenCV 缩放函数需要的尺寸参数是一个元组（Tuple），所以把算好的宽和高用圆括号 () 打包在一起。
return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

path2 = "E:/All_Projects/pycharm_project/Data _analysis_study/Opencv/attachments/5.1-2025-深圳大学(2).mp4"

cap = cv.VedioCapture(path2)

while True:
	isTrue, frame = cap.read() 
	frame_resized = rescaleFrame(frame)
	if not isTrue:
		print("📹 视频播放结束，或者摄像头已断开连接。安全退出中...")
		break
	
	cv.imshow("ori_video", frame)
	cv.imshow("resized_video", frame_resized)
	
	if cv.waitKey(20) & 0xFF == ord('0')
		break

cap.realse()
cv.destoryAllWindows()
```

> [!tip]
> - 我们不需要自己写复杂的图像缩放数学公式，OpenCV 提供了一个现成的 API 叫 `cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)`。
> 	<br>
>  - 只需要去查它的**函数签名（接口说明）**，知道它需要三个参数：
> 	  - 参数1：frame（原图）
> 	  - 参数2：dimensions（新尺寸）
> 	  - 参数3：interpolation（插值算法）。代码里用的 `cv.INTER_AREA` 是 OpenCV 官方推荐的 **最适合缩小图像** 的数学算法。
> 	  - 类似的还有 :
>		  - `cv.INTER_NEAREST`（最近邻插值）：直接复制最近的像素，不计算。**最快但最粗糙**，适合放大像素画。
>		  - `cv.INTER_LINEAR`（双线性插值）：用周围 4 个像素加权平均。**默认值**，速度和质量平衡。
>		  - `cv.INTER_CUBIC`（双三次插值）：用周围 16 个像素加权平均。比 LINEAR 更平滑，适合**放大**图像。
>		  - `cv.INTER_LANCZOS4`（Lanczos 插值）：用周围 8×8 像素计算。**质量最高但最慢**。
>
>	**选择口诀：**
>	  - **缩小**图像 → 用 `INTER_AREA`（避免波纹伪影）
>	  - **放大**图像 → 用 `INTER_CUBIC` 或 `INTER_LANCZOS4`（更清晰）
>	  - **速度优先** → 用 `INTER_NEAREST`（最快）
>	  - **不确定** → 不写这个参数，默认 `INTER_LINEAR`（够用）

---

> [!tip] 2. 专门针对实时视频流（如摄像头实时画面）修改分辨率 的方法
> - **直接修改摄像头等硬件的采集参数**。即在画面还没采集出来前，通知摄像头按指定的宽高捕获画面。
> - **仅适用于实时视频（Live Video）**：

即 `capture.set(propId, value)` ,该方法用于直接设置视频流的各种硬件/流属性：

```python

📌 1. 开启摄像头（0 代表默认摄像头） 
capture = cv.VideoCapture(0)

📌 直接在硬件级别设置摄像头帧的宽高
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
    
📌 将摄像头的捕获分辨率强制更改为 $1280 \times 720$ (720P 高清) 
changeRes(1280, 720)
    
📌 这里的 `capture` 是通过 `cv.VideoCapture` 创建的视频捕获对象。
```

- **参数 `3`**：代表宽度属性，在 OpenCV 中对应的常量是 `cv.CAP_PROP_FRAME_WIDTH`。这行代码的意思是将视频流的帧宽度设置为传入的 `width`。
    
- **参数 `4`**：代表高度属性，在 OpenCV 中对应的常量是 `cv.CAP_PROP_FRAME_HEIGHT`。这行代码的意思是将视频流的帧高度设置为传入的 `height`。
    
- **参数 `10`**  可能代表亮度属性 `cv.CAP_PROP_BRIGHTNESS`，传入数值可以调节画面的采集亮度。

## 四、在图像上绘制形状和书写文字 

### 1. 创建画布

OpenCV 里没有"新建画布"按钮，但可以用 NumPy 创建一张纯黑的空白图像：

```python
import cv2 as cv
import numpy as np

blank_image = np.zeros((500, 500, 3), dtype='uint8')  # 500x500 的黑色图像
```

*   `np.zeros()` 创建一个全零数组（全零 = 全黑）
*   `(500, 500, 3)` → 高500、宽500、3个颜色通道（BGR）
*   `dtype='uint8'` → 每个像素值范围 0\~255（无符号8位整数）

### 2. 给图像上色

```python
# 全图铺满颜色（注意 BGR 顺序，不是 RGB）
blank_image[:] = 34, 139, 34
cv.imshow('Green', blank_image)

# 部分区域上色：200到300行，300到400列的区域涂成红色
blank_image[200:300, 300:400] = 0, 0, 255
cv.imshow('Green with Red Square', blank_image)
```

> [!tip] 数组切片上色的原理
> 还记得"药盒"类比吗？`blank_image[200:300, 300:400]` 就是选中第 200\~300 行、第 300\~400 列的所有药盒，然后把它们统一换成新颜色。

### 3. 绘制矩形

```python
cv.rectangle(blank_image, (0, 0), (blank_image.shape[1]//2, blank_image.shape[0]//2), (46, 123, 85), thickness=5)
cv.imshow("Rectangle", blank_image)
```

| 参数 | 含义 |
|------|------|
| `(0, 0)` | 左上角坐标 (x, y) |
| `(shape[1]//2, shape[0]//2)` | 右下角坐标（注意：宽高顺序！用整除 `//` 保证是整数） |
| `(46, 123, 85)` | 颜色（BGR） |
| `thickness=5` | 线宽，设为 `-1` 则填满整个矩形 |

### 4. 绘制圆形

```python
cv.circle(blank_image, (blank_image.shape[1]//2, blank_image.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow("Circle", blank_image)
```

| 参数 | 含义 |
|------|------|
| `(shape[1]//2, shape[0]//2)` | 圆心坐标（图片正中心） |
| `40` | 半径（像素） |
| `(0, 0, 255)` | 颜色（红色） |
| `thickness=-1` | `-1` 表示**填充实心圆**，正数则只画边框 |

### 5. 绘制线条

```python
cv.line(blank_image, (0, 0), (blank_image.shape[1]//2, blank_image.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow("Line", blank_image)
```

*   起点 `(0, 0)` → 终点 `(宽的一半, 高的一半)`，画一条从左上角到中心的白线。

### 6. 绘制文字

```python
cv.putText(blank_image, "Hello World", (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), thickness=2)
cv.imshow("Text", blank_image)
```

| 参数 | 含义 |
|------|------|
| `"Hello World"` | 要写的文字 |
| `(225, 225)` | 文字左下角的坐标 |
| `cv.FONT_HERSHEY_TRIPLEX` | 字体样式 |
| `1.0` | 字体大小（缩放倍数） |
| `(255, 255, 255)` | 颜色（白色） |
| `thickness=2` | 笔画粗细 |

### 完整代码

```python
import cv2 as cv
import numpy as np

blank_image = np.zeros((500, 500, 3), dtype='uint8')

# 1. 给图像上色
blank_image[:] = 34, 139, 34
cv.imshow('Green', blank_image)

blank_image[200:300, 300:400] = 0, 0, 255
cv.imshow('Green with Red Square', blank_image)

# 2. 绘制矩形
cv.rectangle(blank_image, (0, 0), (blank_image.shape[1]//2, blank_image.shape[0]//2), (46, 123, 85), thickness=5)
cv.imshow("Rectangle", blank_image)

# 3. 绘制圆形
cv.circle(blank_image, (blank_image.shape[1]//2, blank_image.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow("Circle", blank_image)

# 4. 绘制线条
cv.line(blank_image, (0, 0), (blank_image.shape[1]//2, blank_image.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow("Line", blank_image)

# 5. 绘制文字
cv.putText(blank_image, "Hello World", (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), thickness=2)
cv.imshow("Text", blank_image)

cv.waitKey(0)
```

