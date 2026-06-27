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

```python
import cv2 as cv

path1 = "E:/All_Projects/pycharm_project/Data _analysis_study/Opencv/attachments/Ellie.png"

img = cv.imread(path1)

if img is None:
	raise FileNotFoundError(f"图片读取失败：{path1}")

cv.imshow("Ellie", img)

cv.waitKey(0)
print(img.shape) # 输出图片的尺寸信息

```

> 注意 : 
> - **VS Code** 的 **Pylance**静态分析可能会提示"shape”不是 "None" 的已知属性。它的意思是说 **cv2.imread** 有可能 返回 **None**（比如文件不存在时），以此提醒你 .shape 可能出问题。所以添加一个 **if判断**抛出错误。
> 	<br>
> - **.imread** 就是读取图片，把图片文件加载到内存里变成一个数组,读取完,**img** 就是个 **Numpy** 数组 ,里边的值就是每个像素的颜色。
> 	- 返回的不是原图文件，是副本，改 img 不会影响原文件。
> <br>
> - **.waitKey(自己填入数值)** : 等待按键事件，就是显示图片后暂停程序，不让窗口马上关闭 括号内数值为等待的时间, 单位毫秒。
> <br>

2. 视频的读取:<br>
```python
import cv2 as cv
path2 = "E:/All_Projects/pycharm_project/Data _analysis_study/Opencv/attachments/5.1-2025-深圳大学(2).mp4"

cap = cv.VideoCapture(path2)

📌 因为是视频是一帧一帧读取的, 所以需要使用while循环
while True:
	isTrue, frame = cv.read()



```

