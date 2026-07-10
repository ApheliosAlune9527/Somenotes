# Ubuntu 上 VS Code 的 C/C++ 项目使用说明

这份说明是给 Ubuntu 虚拟机里的 VS Code 用的。目标是解决一个问题：以后你想写 C 或 C++ 时，应该怎么新建项目、怎么新建 `.c` / `.cpp` 文件、怎么编译、怎么调试。

## 先记住一句话

在 VS Code 里直接新建 `test.c` 或 `test.cpp` 是可以的。

但是：

- 文件本身只负责保存代码。
- 能不能按 `Ctrl+Shift+B` 编译，取决于当前项目文件夹里有没有 `.vscode/tasks.json`。
- 能不能按 `F5` 调试，取决于当前项目文件夹里有没有 `.vscode/launch.json`。

所以最稳的做法不是随便找个地方新建文件，而是先用模板命令创建一个已经配置好的项目文件夹。

## 推荐工作流

写 C 项目：

```bash
new-c-project c-demo
cd ~/code/c-demo
code --profile 'C/C++' .
```

写 C++ 项目：

```bash
new-cpp-project cpp-demo
cd ~/code/cpp-demo
code --profile 'C/C++' .
```

这三条命令的意思是：

1. 用模板创建项目。
2. 进入项目目录。
3. 用 VS Code 的 `C/C++` Profile 打开这个项目目录。

打开以后，你可以在 VS Code 里新建 `test.c`、`hello.c`、`test.cpp`、`main.cpp` 等文件。

## 第一条命令是什么意思

以 C 项目为例：

```bash
new-c-project c-demo
```

意思是：用已经准备好的 C 项目模板，新建一个叫 `c-demo` 的项目。

它会创建：

```text
/home/aphelios/code/c-demo
```

这个文件夹里应该自带：

```text
main.c
.vscode/
  c_cpp_properties.json
  tasks.json
  launch.json
```

其中：

- `main.c` 是示例代码文件。
- `.vscode/c_cpp_properties.json` 告诉 VS Code 用哪个编译器做代码提示。
- `.vscode/tasks.json` 告诉 VS Code 按 `Ctrl+Shift+B` 时怎么编译。
- `.vscode/launch.json` 告诉 VS Code 按 `F5` 时怎么调试。

C++ 项目同理：

```bash
new-cpp-project cpp-demo
```

会创建：

```text
/home/aphelios/code/cpp-demo
```

里面自带 `main.cpp` 和 `.vscode` 配置。

## 第二条命令是什么意思

```bash
cd ~/code/c-demo
```

`cd` 的意思是进入某个目录。

`~` 代表你的用户主目录：

```text
/home/aphelios
```

所以：

```bash
cd ~/code/c-demo
```

等价于：

```bash
cd /home/aphelios/code/c-demo
```

这一步的作用是：让终端进入刚才创建好的项目文件夹。

## 第三条命令是什么意思

```bash
code --profile 'C/C++' .
```

这条命令的意思是：用 VS Code 打开当前文件夹，并且使用 `C/C++` 这个 Profile。

拆开看：

- `code`：启动 VS Code。
- `--profile 'C/C++'`：指定使用 VS Code 里的 `C/C++` Profile。
- `.`：当前文件夹。

最后这个点 `.` 很重要。它表示打开当前目录，而不是只打开一个单独文件。

## 为什么要打开“文件夹”，不是只打开文件

VS Code 的 C/C++ 编译调试配置通常放在项目文件夹里的 `.vscode` 目录。

比如：

```text
/home/aphelios/code/c-demo/
  main.c
  test.c
  .vscode/
    tasks.json
    launch.json
    c_cpp_properties.json
```

如果你打开的是整个 `c-demo` 文件夹，VS Code 能看到 `.vscode` 配置，所以 `Ctrl+Shift+B` 和 `F5` 能正常工作。

如果你只是单独打开一个 `test.c` 文件，VS Code 可能看不到项目配置，编译和调试就不稳定。

## 可以直接在 VS Code 里新建 test.c 吗

可以。

正确方式是：

1. 先用模板打开项目：

```bash
new-c-project c-demo
cd ~/code/c-demo
code --profile 'C/C++' .
```

2. 在 VS Code 左侧资源管理器里新建文件：

```text
test.c
```

3. 写代码：

```c
#include <stdio.h>

int main(void) {
    printf("hello C\n");
    return 0;
}
```

4. 按 `Ctrl+Shift+B` 编译。

5. 按 `F5` 调试。

## 可以直接在 VS Code 里新建 test.cpp 吗

可以。

正确方式是：

```bash
new-cpp-project cpp-demo
cd ~/code/cpp-demo
code --profile 'C/C++' .
```

然后在 VS Code 里新建：

```text
test.cpp
```

写代码：

```cpp
#include <iostream>

int main() {
    std::cout << "hello C++" << std::endl;
    return 0;
}
```

然后：

- `Ctrl+Shift+B` 编译。
- `F5` 调试。

## 如果不用 VS Code 按钮，也可以直接终端编译

C 文件：

```bash
gcc -std=c17 -g test.c -o test
./test
```

C++ 文件：

```bash
g++ -std=c++17 -g test.cpp -o test
./test
```

这里：

- `gcc` 用来编译 C。
- `g++` 用来编译 C++。
- `-std=c17` 表示使用 C17 标准。
- `-std=c++17` 表示使用 C++17 标准。
- `-g` 表示生成调试信息，方便 GDB / VS Code 调试。
- `-o test` 表示输出程序名叫 `test`。
- `./test` 表示运行当前目录下的 `test` 程序。

## tasks.json 能不能删

一般不要删。

`tasks.json` 可以理解成 VS Code 的“编译按钮说明书”。

它告诉 VS Code：

- 用 `gcc` 还是 `g++`。
- 用什么标准，比如 `c17` 或 `c++17`。
- 输出文件叫什么。
- 按 `Ctrl+Shift+B` 时执行哪条命令。

如果删掉 `.vscode/tasks.json`：

- 代码文件还在。
- 你仍然可以手动用终端编译。
- 但是 `Ctrl+Shift+B` 可能就不知道该怎么编译。
- `F5` 调试也可能因为找不到预编译任务而失败。

所以模板项目里的 `.vscode/tasks.json` 建议保留。

## launch.json 能不能删

一般也不要删。

`launch.json` 可以理解成 VS Code 的“调试按钮说明书”。

它告诉 VS Code：

- 调试哪个程序。
- 用哪个调试器，比如 `/usr/bin/gdb`。
- 调试前是否先执行编译任务。

如果删掉 `.vscode/launch.json`：

- 你仍然可以手动运行程序。
- 但 `F5` 调试可能不能直接用。

所以模板项目里的 `.vscode/launch.json` 也建议保留。

## c_cpp_properties.json 能不能删

不建议删。

它主要影响代码提示、头文件搜索、智能补全和错误标红。

它告诉 VS Code：

- C 项目用 `/usr/bin/gcc`。
- C++ 项目用 `/usr/bin/g++`。
- IntelliSense 模式用 `linux-gcc-x64`。
- 使用什么 C / C++ 标准。

如果删掉它，有些代码仍然能编译，但 VS Code 的提示和标红可能不准。

## C 项目和 C++ 项目不要混用模板

C 项目用：

```bash
new-c-project 项目名
```

C++ 项目用：

```bash
new-cpp-project 项目名
```

区别是：

- C 项目用 `gcc` 编译。
- C++ 项目用 `g++` 编译。
- C 项目一般是 `.c` 文件。
- C++ 项目一般是 `.cpp` 文件。

不要把 `.cpp` 文件放进 C 模板里用 `gcc` 编译，也不要把纯 C 项目强行按 C++ 项目处理。

## 最常用操作

新建 C 项目：

```bash
new-c-project hello-c
cd ~/code/hello-c
code --profile 'C/C++' .
```

新建 C++ 项目：

```bash
new-cpp-project hello-cpp
cd ~/code/hello-cpp
code --profile 'C/C++' .
```

编译：

```text
Ctrl+Shift+B
```

调试：

```text
F5
```

打开终端：

```text
Ctrl+`
```

## 如果按 Ctrl+Shift+B 没反应

先检查你是不是打开了“项目文件夹”，而不是只打开了一个单独文件。

正确打开方式：

```bash
cd ~/code/你的项目名
code --profile 'C/C++' .
```

再检查项目里有没有：

```text
.vscode/tasks.json
```

如果没有，说明这个项目不是从模板创建的，或者 `.vscode` 被删了。

## 如果 F5 调试失败

先检查项目里有没有：

```text
.vscode/launch.json
```

再检查能不能手动编译：

C：

```bash
gcc -std=c17 -g test.c -o test
./test
```

C++：

```bash
g++ -std=c++17 -g test.cpp -o test
./test
```

如果手动编译都失败，说明是代码或编译命令问题。

如果手动编译成功但 F5 失败，说明是 `.vscode/launch.json` 或 `tasks.json` 配置问题。

## 最终结论

你可以在 VS Code 里直接新建 `test.c` 或 `test.cpp`。

但推荐前提是：先用模板命令创建项目，再在这个项目里新建文件。

推荐方式：

```bash
new-c-project c-demo
cd ~/code/c-demo
code --profile 'C/C++' .
```

或者：

```bash
new-cpp-project cpp-demo
cd ~/code/cpp-demo
code --profile 'C/C++' .
```

这样新建出来的文件就处在一个已经配置好编译和调试的项目环境里。

