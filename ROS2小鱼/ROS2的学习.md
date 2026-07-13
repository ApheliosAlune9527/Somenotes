1. 创建工作空间
![[Pasted image 20260710150130.png]]

2. 构建工作空间所有功能包
![[Pasted image 20260710150258.png]]
3. 构建单独功能包
![[Pasted image 20260710150314.png]]

4. 这个package.xml是控制包的依赖关系的
![[Pasted image 20260710150337.png]]
## 三、话题
---

1. ![[Pasted image 20260712203319.png]]
2. ![[Pasted image 20260712203337.png]]
3. 详细接口定义查看方法：![[Pasted image 20260712203407.png]]
4. 发布话题需要知道：话题名字 `/turtle1/cmd_vel` 和 话题接口 `geometry_msgs/msg/Twist
![[Pasted image 20260712203440.png]]

### 1. 通过话题来发布小说
> *任务：*
![[Pasted image 20260712223534.png]]

1.  功能包创建 ：`ros2 pkg create demo_py_topic --build-type ament_python --dependencies rclpy example_interfaces --license Apache-2.0 `