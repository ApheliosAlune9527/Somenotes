# Ubuntu 上 VS Code 使用 CMake 写 C++ 的固定流程

这份文档按你的 Ubuntu 当前环境来写：

```text
项目文件夹: ~/桌面/test
当前源码: ~/桌面/test/cpp_test1.cpp
VS Code Profile: C/C++
编译器: /usr/bin/gcc 和 /usr/bin/g++
CMake Kit: GCC 11.4.0 x86_64-linux-gnu
```

## 1. CMake 是干什么的

先记住一句话：

```text
g++ 是编译器。
CMake 是项目构建管理工具。
```

以前单文件可以直接：

```bash
g++ cpp_test1.cpp -o cpp_test1
./cpp_test1
```

但是用了 CMake 之后，流程变成：

```text
CMakeLists.txt 写项目规则
cmake 配置项目
cmake --build build 编译项目
运行 build 里生成的程序
```

CMake 背后真正调用的还是 `g++`。

## 2. 以后打开项目的正确方式

不要只打开单个 `.cpp` 文件。

错误习惯：

```bash
code --profile 'C/C++' cpp_test1.cpp
```

推荐方式：

```bash
code --profile 'C/C++' ~/桌面/test
```

或者：

```bash
cd ~/桌面/test
code --profile 'C/C++' .
```

最后那个点 `.` 的意思是打开当前文件夹。

只要用 CMake，就要把整个文件夹当成项目打开。

## 3. 一个最小 CMake 项目长什么样

你的项目文件夹应该像这样：

```text
test/
├── CMakeLists.txt
├── cpp_test1.cpp
└── build/
```

其中：

```text
CMakeLists.txt 负责告诉 CMake 怎么编译
cpp_test1.cpp 是你的 C++ 源码
build/ 是 CMake 生成的构建目录
```

`build/` 不需要你手动写代码，它是 CMake 生成的。

## 4. CMakeLists.txt 最小模板

在 `~/桌面/test/CMakeLists.txt` 里写：

```cmake
cmake_minimum_required(VERSION 3.16)

project(test LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(cpp_test1 cpp_test1.cpp)
```

每一行意思：

```text
cmake_minimum_required(VERSION 3.16)
要求 CMake 版本至少是 3.16。

project(test LANGUAGES CXX)
项目名叫 test，使用 C++。

set(CMAKE_CXX_STANDARD 17)
使用 C++17 标准。

set(CMAKE_CXX_STANDARD_REQUIRED ON)
强制要求使用这个 C++ 标准。

add_executable(cpp_test1 cpp_test1.cpp)
把 cpp_test1.cpp 编译成一个叫 cpp_test1 的可执行程序。
```

## 5. VS Code 里第一次使用 CMake

第一次打开项目后，VS Code 可能会让你选择工具包 Kit。

选择这个：

```text
GCC 11.4.0 x86_64-linux-gnu
```

它的意思是：

```text
C 编译器: /usr/bin/gcc
C++ 编译器: /usr/bin/g++
```

不要选：

```text
[未指定]
```

## 6. VS Code 里的常用命令

按：

```text
Ctrl + Shift + P
```

常用这几个命令：

```text
CMake: Configure
CMake: Build
CMake: Run Without Debugging
```

含义：

```text
CMake: Configure
读取 CMakeLists.txt，生成 build/ 构建配置。

CMake: Build
编译项目。

CMake: Run Without Debugging
运行编译出来的程序。
```

## 7. 终端命令版

如果不用 VS Code 按钮，也可以在 Ubuntu 终端里这样做：

```bash
cd ~/桌面/test
cmake -S . -B build -G Ninja
cmake --build build
./build/cpp_test1
```

解释：

```text
cmake -S . -B build -G Ninja
配置项目。

-S .
源码目录是当前目录。

-B build
构建目录是 build。

-G Ninja
使用 Ninja 作为构建工具。

cmake --build build
编译项目。

./build/cpp_test1
运行生成出来的程序。
```

## 8. Build 和 Run 的区别

这两个不要混：

```text
Build = 编译
Run = 运行
```

比如你看到：

```text
ninja: no work to do.
生成已完成，退出代码为 0
```

这不是错误。

意思是：

```text
你的源码没有变化，之前已经编译好了，所以不用重新编译。
```

这时你要运行程序，而不是继续 Build。

运行方式：

```bash
./build/cpp_test1
```

或者在 VS Code 里执行：

```text
CMake: Run Without Debugging
```

## 9. 平时改代码之后怎么做

假设你修改了 `cpp_test1.cpp`。

之后只需要：

```bash
cd ~/桌面/test
cmake --build build
./build/cpp_test1
```

或者在 VS Code 里：

```text
CMake: Build
CMake: Run Without Debugging
```

## 10. 新增 cpp 文件后怎么做

假设你新增了：

```text
math_utils.cpp
```

你的项目变成：

```text
test/
├── CMakeLists.txt
├── cpp_test1.cpp
└── math_utils.cpp
```

那你必须修改 `CMakeLists.txt`：

```cmake
add_executable(cpp_test1
    cpp_test1.cpp
    math_utils.cpp
)
```

然后重新配置和构建：

```bash
cmake -S . -B build -G Ninja
cmake --build build
./build/cpp_test1
```

或者 VS Code 里：

```text
CMake: Configure
CMake: Build
CMake: Run Without Debugging
```

## 11. 新建另一个程序怎么写

如果你有两个独立程序：

```text
cpp_test1.cpp
hello.cpp
```

可以这样写：

```cmake
cmake_minimum_required(VERSION 3.16)

project(test LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(cpp_test1 cpp_test1.cpp)
add_executable(hello hello.cpp)
```

这样会生成两个程序：

```text
build/cpp_test1
build/hello
```

运行：

```bash
./build/cpp_test1
./build/hello
```

## 12. C 文件和 C++ 文件怎么区分

如果你以后要同时写 C 和 C++：

```text
.c 文件用 C
.cpp 文件用 C++
```

CMakeLists.txt 可以写：

```cmake
cmake_minimum_required(VERSION 3.16)

project(test LANGUAGES C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(c_program main.c)
add_executable(cpp_program main.cpp)
```

## 13. 什么时候需要重新 Configure

只改 `.cpp` 内容：

```text
只需要 Build。
```

新增 `.cpp` 文件，并且修改了 `CMakeLists.txt`：

```text
需要 Configure，然后 Build。
```

修改 CMakeLists.txt：

```text
需要 Configure，然后 Build。
```

如果你不确定：

```text
先 CMake: Configure
再 CMake: Build
再 CMake: Run Without Debugging
```

## 14. 最推荐你记住的固定流程

以后新建 C++ 项目就按这个来：

```bash
mkdir -p ~/桌面/my_cpp_project
cd ~/桌面/my_cpp_project
touch main.cpp
touch CMakeLists.txt
code --profile 'C/C++' .
```

`CMakeLists.txt` 写：

```cmake
cmake_minimum_required(VERSION 3.16)

project(my_cpp_project LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(my_cpp_project main.cpp)
```

然后：

```bash
cmake -S . -B build -G Ninja
cmake --build build
./build/my_cpp_project
```

或者用 VS Code：

```text
CMake: Configure
CMake: Build
CMake: Run Without Debugging
```

## 15. 一句话总结

```text
用 CMake 时，不要想着单独运行某个 cpp 文件。
你是在运行一个 CMake 项目里定义好的 executable。
```

这个 executable 是在 `CMakeLists.txt` 里用 `add_executable(...)` 定义的。

