# AIRBOT Play：从 Windows / 裸机到 Ubuntu 与 SDK 配置完成

> 面向第一次接触 Ubuntu 和 AIRBOT Play 的用户。完成本文后，你应当能够在 Ubuntu 中识别机械臂的 CAN 接口、启动 `airbot-arm` 控制服务、安装并验证 Python SDK。
>
> 本文按本工程截至 **2026-07-18** 的资料编写，主流程对应当前最新版 **V5.2.2**。V5.1.6 及更早版本请看文末“旧版本用户”说明，切勿混用两代软件包和命令。

## 1. 先确定安装方案

控制真实机械臂需要稳定访问 USB-2 对应的 SocketCAN 设备。第一次配置时，建议使用安装在实体电脑上的 Ubuntu，不建议把 WSL 或普通虚拟机作为主控制环境；它们还需要额外配置 USB 直通，排错更复杂。

可选择以下一种方案：

| 方案 | 适用场景 | 建议 |
| --- | --- | --- |
| Ubuntu 独占整块磁盘 | 专用机器人电脑，Windows 不再需要 | 最省事、最稳定，但会清空目标磁盘 |
| Windows + Ubuntu 双系统 | 同一台电脑仍需使用 Windows | 推荐大多数现有 Windows 用户使用 |
| Ubuntu 安装到第二块 SSD | 电脑可加装硬盘 | 最推荐：Windows 与 Ubuntu 彼此隔离，风险较低 |

### 推荐的软件基线

- **系统**：发布包分别提供 Ubuntu 20.04、22.04、24.04 对应的 SDK 目录；其中**推荐使用 Ubuntu Desktop 22.04 LTS 64 位（Jammy）**。Ubuntu 22.04 自带 Python 3.10，与 V5.2 SDK 的 Python 3.10+ 要求直接匹配，也是本工程教程采用的主要基线。已经在使用 Ubuntu 20.04 或 24.04 的用户不必仅为此重装系统，但安装时必须选择与当前 Ubuntu 版本对应的文件夹。
- **处理器架构**：常见 Intel / AMD 电脑选择 `amd64` / `x86_64` 软件包；ARM 主机必须获取 `aarch64` 对应包。
- **CPU**：至少 4 核。
- **内存**：基础 SDK 控制建议至少 8 GB。
- **磁盘**：Ubuntu 官方给出的桌面安装最低空间是 25 GB，工程资料另要求至少 5 GB 可用于软件和数据。实际建议给 Ubuntu **至少 80 GB，AIRBOT 开发环境推荐 150 GB 或更多**；需要仿真、模型或采集数据时应预留 200 GB 以上。
- **U 盘**：12 GB 或更大，制作启动盘会清空其中全部内容。
- **接口**：基础单臂控制需要一个可用 USB 口；ALOHA / Mobile ALOHA 等多外设场景建议至少 3 个。

Ubuntu 版本与 SDK 目录必须按下表匹配；如果主程序发布包也按系统版本分目录，则 `.deb` 采用同样的匹配规则：

| 当前系统 | 代号 | 应选择的 SDK 目录 | 说明 |
| --- | --- | --- | --- |
| Ubuntu 20.04 LTS | `focal` | 标有 `20.04` / `ubuntu20.04` / `focal` 的目录 | 可用，但系统默认 Python 3.8；安装 Python SDK 前仍须满足 Python 3.10+ |
| **Ubuntu 22.04 LTS** | `jammy` | 标有 `22.04` / `ubuntu22.04` / `jammy` 的目录 | **推荐版本，也是本文默认路径** |
| Ubuntu 24.04 LTS | `noble` | 标有 `24.04` / `ubuntu24.04` / `noble` 的目录 | 使用该版本专用目录，不要安装 22.04/Jammy 目录中的文件 |

> 目录的具体拼写以实际发布包为准，判断依据是目录中的 Ubuntu 版本号或代号。**20.04、22.04、24.04 三个 SDK 目录中的文件不能交叉使用。**即使文件名或 SDK 版本号相同，也必须从当前系统对应的目录安装。Ubuntu 22.04 的[常规维护更新到 2027 年 4 月](https://documentation.ubuntu.com/release-notes/22.04/)。

## 2. Windows 用户：备份并释放空间

### 2.1 先分清“可用空间”和“未分配空间”

- Windows 资源管理器中 C 盘、D 盘等卷显示的“可用空间”，仍然属于该卷现有的 NTFS 文件系统。它不是可直接分配给 Ubuntu 的“未分配空间”。
- Windows“磁盘管理”中的“压缩卷”会缩小所选卷，并在**同一块物理磁盘上、该卷末尾之后**生成一段黑色标记的“未分配”空间。普通文件会由 Windows 自动移动，不需要先格式化原卷。
- 应根据物理磁盘编号、盘符、容量、文件系统和数据备份情况选择要压缩的卷，不能简单地选择“剩余空间最大的磁盘”。选错卷可能导致 Ubuntu 空间出现在错误的物理磁盘上。
- 给 Ubuntu 留出的未分配空间不要在 Windows 中新建简单卷、分配盘符或格式化成 NTFS；应保持“未分配”状态，交给 Ubuntu 安装器使用。
- 空间规划不是统一的硬性标准：基础系统和 SDK 建议至少 80 GB；用于 AIRBOT 日常开发时推荐 150 GB 或更多；还要安装仿真器、模型或保存采集数据时建议 200 GB 以上。

### 2.2 安全清理顺序

先把文档、照片、代码、浏览器资料和软件许可证备份到移动硬盘或云端。双系统安装会修改分区表，即使正常流程不会删除 Windows，仍然必须提前备份。

随后按以下顺序释放空间：

1. 打开“设置 → 系统 → 存储 → 清理建议”，逐项检查临时文件、大型或未使用文件、云同步文件和未使用应用，再执行清理。不要在没看清内容时勾选“下载”文件夹。
2. 清空回收站，并整理“下载”、桌面、视频、安装包和旧压缩包。
3. 在“设置 → 应用 → 已安装的应用”中按大小排序，卸载不再使用的软件和游戏。
4. 将大型视频、数据集、虚拟机镜像和游戏平台库移动到其他磁盘。OneDrive 文件确认已经同步后，可按需设为“释放空间/仅联机”。
5. 如果仍然不够，可在“以管理员身份运行”的终端中关闭休眠：

   ```powershell
   powercfg.exe /hibernate off
   ```

   这会删除休眠文件并同时停用休眠相关能力。它也有利于避免双系统下 Windows 快速启动造成 NTFS 分区处于未完全关闭状态。以后如需恢复，可执行：

   ```powershell
   powercfg.exe /hibernate on
   ```

Microsoft 的[磁盘空间清理说明](https://support.microsoft.com/en-us/windows/empty-the-recycle-bin-in-windows-10-d4c8f8ef-a12e-8250-b0cf-2311960a31f9)和[`powercfg` 说明](https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/disable-and-re-enable-hibernation)提供了上述操作的官方依据。

### 2.3 先处理 BitLocker / 设备加密

1. 在 Windows 搜索“管理 BitLocker”或“设备加密”。
2. 若系统盘已加密，先把 48 位恢复密钥备份到另一个设备或 Microsoft 账户，并实际确认能够找到它。Microsoft 明确说明无法替用户重建丢失的恢复密钥，参见[恢复密钥备份说明](https://support.microsoft.com/en-us/Windows/Security/encryption/back-up-your-bitlocker-recovery-key)。
3. 双系统安装需要 Ubuntu 安装器读取 Windows 分区结构。若目标磁盘启用了 BitLocker，应在 Windows 中选择“关闭 BitLocker”，等待完整解密结束并重启后再压缩和安装。仅“暂停保护”不等同于完整解密。
4. 安装完成并确认两个系统都可启动后，再根据 Windows 版本和组织策略决定是否重新开启加密。

Ubuntu 官方对双系统 BitLocker 的解释和关闭步骤见：[BitLocker during Ubuntu installation](https://ubuntu.com/desktop/docs/en/latest/reference/bitlocker-during-ubuntu-installation/)。

### 2.4 从 Windows 详细压缩卷

#### 2.4.1 压缩前确认

开始前逐项确认：

- 重要文件已经备份，笔记本已连接电源；
- BitLocker 恢复密钥已经备份，目标磁盘已按上一节完成解密；
- 已关闭游戏、虚拟机、下载工具、数据库等会持续写入磁盘的程序；
- 准备压缩的是 NTFS 基本卷。Microsoft 的磁盘管理只能压缩 NTFS 或无文件系统的基本卷；不要尝试压缩 EFI、恢复、OEM、MSR 或文件系统不明的分区；
- 压缩后还要给 Windows 留出正常运行和更新空间。不要把“可用压缩空间大小”全部分给 Ubuntu；建议 Windows 系统卷压缩后至少保留 50 GB 可用空间，软件和游戏较多时应保留更多。

> “压缩卷”缩小的是一个卷，不是整块硬盘。例如一块 SSD 可能显示为“磁盘 0”，其内部包含 C 盘、EFI 和恢复分区。你应右键 C 盘或确认过的数据卷，不能右键“磁盘 0”，更不能删除旁边的小型系统分区。

#### 2.4.2 打开磁盘管理并识别目标卷

可以使用以下任一方法打开 Windows 10/11 的“磁盘管理”：

1. 按 `Win + X`，选择“磁盘管理”；
2. 按 `Win + R`，输入 `diskmgmt.msc` 后按回车；
3. 右键“此电脑”→“管理”→“存储”→“磁盘管理”。

在下方面板中核对：

1. **物理磁盘编号**：例如“磁盘 0”或“磁盘 1”；
2. **目标卷盘符**：例如 `C:` 或 `D:`；
3. **容量和已用空间**：应与资源管理器中看到的信息吻合；
4. **文件系统**：应显示 `NTFS`；
5. **磁盘状态**：应显示“联机”，目标卷应显示“状态良好”。

如果电脑有多块 SSD，先确认 Ubuntu 准备安装到哪一块。压缩某个卷后，未分配空间只会出现在该卷所在的同一块物理磁盘上，不能因为另一个盘剩余空间更多就随意选择另一个盘。

#### 2.4.3 计算要输入的容量

右键目标 NTFS 卷，选择“压缩卷”。Windows 会先查询可压缩空间，随后显示四项数据：

| 对话框字段 | 含义 |
| --- | --- |
| 压缩前的总计大小（MB） | 目标 Windows 卷目前的总容量 |
| 可用压缩空间大小（MB） | Windows 当前允许从卷末尾释放的最大容量 |
| 输入压缩空间量（MB） | **要分给 Ubuntu 的容量**，需要用户填写 |
| 压缩后的总计大小（MB） | 操作完成后 Windows 目标卷的容量 |

“输入压缩空间量”不是 Windows 分区最终要保留的大小。例如，要给 Ubuntu 150 GB，就输入约 `153600 MB`，而不是输入 Windows 分区压缩后的容量。

按 `目标 GB × 1024` 计算输入值：

| Ubuntu 目标空间 | 输入压缩空间量 |
| --- | ---: |
| 80 GB（基础安装建议下限） | `81920 MB` |
| 120 GB | `122880 MB` |
| 150 GB（AIRBOT 开发推荐） | `153600 MB` |
| 200 GB（仿真/数据场景） | `204800 MB` |

输入值必须小于或等于对话框显示的“可用压缩空间大小”。还要检查“压缩后的总计大小”，确保 Windows 卷不会被压得过小。

#### 2.4.4 执行并验证结果

1. 再次确认目标盘符、输入值和压缩后的容量；
2. 点击“压缩”，等待磁盘管理完成操作。期间不要关机、强制重启或拔掉外接目标磁盘；
3. 完成后，在同一物理磁盘的图形视图中应看到一段黑色顶栏、标记为“未分配”的空间；
4. 核对未分配空间容量是否与输入值大致相符。界面单位换算和取整可能造成少量差异；
5. **到此停止**：不要右键未分配空间创建“新建简单卷”，不要分配盘符，也不要格式化；
6. 关闭磁盘管理并正常重启 Windows，确认 Windows 仍能启动、目标卷和个人文件正常，再继续制作启动盘或安装 Ubuntu。

Microsoft 说明，压缩卷会从现有卷的末尾创建相邻、连续的未分配空间，普通文件会自动移动，不需要重新格式化原卷。操作本身按设计不会删除普通文件，但分区操作始终存在意外断电、硬件故障或误选目标的风险，因此备份仍是必需步骤。参见 Microsoft 的[磁盘管理概览](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/disk-management-in-windows)和[压缩基本卷说明](https://learn.microsoft.com/en-us/windows-server/storage/disk-management/shrink-a-basic-volume)。

#### 2.4.5 可压缩空间明显不足时

资源管理器显示的可用空间可能很多，但“可用压缩空间大小”仍可能很小。原因通常是分页文件、卷影副本等不可移动文件位于卷的后部；Windows 只能压缩到第一个不可移动文件之前。按以下顺序处理：

1. 取消压缩对话框，确认重要文件已备份；
2. 完成第 2.2 节的磁盘清理，关闭不必要程序并正常重启 Windows；
3. 如果已经决定关闭休眠，确认已用管理员终端执行 `powercfg.exe /hibernate off`，然后再重启一次；
4. 重新打开磁盘管理查询可压缩空间；
5. 仍不足时，可在“事件查看器 → Windows 日志 → 应用程序”中检查事件 ID `259`，判断哪个不可移动文件阻止压缩；
6. 对分页文件、系统保护或卷影副本不熟悉时，不要为追求更大空间而自行关闭或删除它们。优先选择较小但仍满足需求的容量、压缩另一块合适的 NTFS 卷、安装到第二块 SSD，或请有经验的管理员处理。

不要用“删除分区”“格式化”“转换为动态磁盘”来解决压缩空间不足，也不建议新手使用第三方分区工具强行移动 Windows 系统分区。Microsoft 官方同样指出，不可移动文件和磁盘坏簇都会限制压缩范围。

#### 2.4.6 常见异常

| 现象 | 原因与处理 |
| --- | --- |
| “压缩卷”为灰色 | 可能选中了 EFI/恢复分区，或目标卷不是受支持的 NTFS 基本卷；停止操作并重新确认目标 |
| 可用压缩空间为 0 或远小于空闲空间 | 通常存在不可移动文件；按上一节处理，不要直接删除系统文件 |
| 提示文件系统错误 | 先备份数据，在管理员终端执行 `chkdsk C: /scan` 检查；把 `C:` 换成实际目标盘符 |
| 压缩后没有看到未分配空间 | 检查同一物理磁盘的右侧区域并刷新磁盘管理；不要到另一块磁盘上查找 |
| 数值输入后 Windows 剩余空间过小 | 取消操作并重新计算；“输入压缩空间量”是释放给 Ubuntu 的量，不是 Windows 最终容量 |
| 想在安装 Ubuntu 前撤销压缩 | 若未分配空间仍紧邻原卷右侧，可右键原卷选择“扩展卷”并合并回去；操作前仍需备份并确认目标 |

## 3. 制作 Ubuntu 22.04 启动盘（新安装推荐）

已经正常使用 Ubuntu 20.04 或 24.04、且不准备重装系统的用户，可以跳过第 3、4 节，直接从第 5 节开始；后续安装 AIRBOT 软件时选择当前系统对应的版本目录即可。新安装用户推荐按本文安装 Ubuntu 22.04。

1. 从 Ubuntu 官方[旧版镜像页面](https://releases.ubuntu.com/22.04/)下载最新的 Ubuntu 22.04 Desktop `amd64.iso`。不要从不明网盘下载修改版镜像。
2. 可同时下载同页的 `SHA256SUMS`，在 Windows PowerShell 中校验：

   ```powershell
   Get-FileHash .\ubuntu-22.04.5-desktop-amd64.iso -Algorithm SHA256
   ```

   输出应与 `SHA256SUMS` 中对应 ISO 的值完全一致。若镜像文件名已更新，以实际下载名为准。
3. 备份 U 盘文件。按 Ubuntu 官方[桌面安装教程](https://ubuntu.com/tutorials/install-ubuntu-desktop)，使用 balenaEtcher 等镜像写入工具选择 ISO 和正确的 U 盘并写入。注意：这是“写入镜像”，不是把 ISO 文件复制到 U 盘。
4. 写入完成后，Windows 可能提示 U 盘某个分区需要格式化，选择“取消”；这是 Linux 启动盘的正常现象。

## 4. 从 U 盘启动并安装 Ubuntu

### 4.1 启动前检查

- 笔记本接通电源。
- 暂时拔掉除键盘、鼠标、Ubuntu 启动盘以外的不必要 USB 设备，机械臂也先不要连接。
- 再次确认重要数据和 BitLocker 恢复密钥已有备份。
- 记下电脑厂商的启动菜单按键。常见为 `F12`，也可能是 `Esc`、`F2`、`F10` 或 `F11`。

重启电脑并连续按启动菜单键，选择带有 `UEFI` 字样的 U 盘。若不能启动，先检查 U 盘是否写入成功；通常不需要关闭 Secure Boot。

### 4.2 先试用再安装

进入 Ubuntu 菜单后先选择 “Try Ubuntu / 试用 Ubuntu”，检查以下项目：

- 键盘、触控板、显示器正常；
- Wi-Fi 或有线网络可用；
- 声音不是必需项，但可顺便测试；
- “磁盘”应用能看到预期的 SSD 和此前留出的未分配空间。

确认无误后，双击桌面的 “Install Ubuntu 22.04 LTS”。

### 4.3 安装器中的关键选择

1. 选择语言和键盘布局，连接网络。
2. 推荐选择“正常安装”，并勾选安装第三方图形和 Wi-Fi 硬件软件；离线环境也可先安装、进入系统后再补驱动。
3. 到“安装类型”时：
   - **双系统**：优先选择 “Install Ubuntu alongside Windows Boot Manager / 与 Windows 共存”，确认分配给 Ubuntu 的容量对应此前留下的未分配空间；
   - **Ubuntu 独占专用盘**：只有在已确认目标磁盘可被彻底清空时，才选择 “Erase disk and install Ubuntu / 清除磁盘并安装”；
   - **Something else / 其他选项**：属于手动分区。新手如果看不到“与 Windows 共存”，不要凭感觉删除分区，应先退出安装器排查 BitLocker、RST 或启动模式。
4. 选择时区、用户名和密码。请牢记该密码，后续所有 `sudo` 命令都需要它；输入密码时终端不会显示字符，这是正常现象。
5. 安装完成后按提示重启、拔出 U 盘并按回车。

如果安装器提示 **Intel RST**，不要直接在 BIOS 中从 RAID/RST 改成 AHCI，否则现有 Windows 可能无法启动。先退出安装，按 Ubuntu 官方文档完成 [RST/AHCI 迁移](https://ubuntu.com/desktop/docs/en/latest/)或联系电脑厂商支持。

## 5. Ubuntu 首次启动后的基础配置

进入 Ubuntu，按 `Ctrl + Alt + T` 打开终端，依次执行：

```bash
sudo apt update
sudo apt full-upgrade -y
sudo apt install -y can-utils python3-pip python3-venv
sudo reboot
```

重启后检查系统信息：

```bash
lsb_release -ds
lsb_release -rs
lsb_release -cs
uname -m
python3 --version
df -h /
```

首先根据 `lsb_release -rs` 和 `lsb_release -cs` 的输出确认系统版本与代号：

| `lsb_release -rs` | `lsb_release -cs` | 后续必须选择的目录 |
| --- | --- | --- |
| `20.04` | `focal` | 20.04 / focal 目录 |
| `22.04` | `jammy` | 22.04 / jammy 目录（推荐） |
| `24.04` | `noble` | 24.04 / noble 目录 |

其余检查结果应满足：

- Intel / AMD 电脑显示 `x86_64`；
- Python 为 `3.10.x` 或更高；
- 根分区仍有足够可用空间。

> Ubuntu 20.04 默认的 Python 3 通常是 3.8，不满足当前 V5.2 SDK 文档要求的 Python 3.10+。20.04 用户除了选择 20.04/focal SDK 目录，还必须先执行 `python3 --version` 核对版本，并按 AIRBOT 发布包说明或技术支持提供的方法配置 Python 3.10+；不能因为存在 20.04 目录就忽略 Python 版本要求。Ubuntu 22.04 默认 Python 3.10，因此仍是最省事的推荐选择。

> 工程早期 V5.1.6 软件教程包含 Docker，但当前 V5.2.2 的基础 SDK 安装流程只要求 `airbot-arm` 主程序和 `arm-sdk` Python 包。仅在后续算法、容器或仿真教程明确要求时再安装 Docker。

## 6. 下载并确认 AIRBOT V5.2.2 软件包

当前 V5.2 需要两个包：

| 包 | 作用 |
| --- | --- |
| `airbot-arm` 的 `.deb` | 机械臂控制服务 |
| `arm-sdk` 的 `.whl` | Python 客户端、CLI 和示例 |

从本工程[更新日志 V5.2](changelog.en.md#v5.2)中的官方链接下载：

- `airbot_arm_release.tar.gz`：主程序；
- `sdk_client_release.tar.gz`：SDK。

若链接或版本已经变化，以技术支持提供的**同一发布批次**为准。不要把 V5.1.6 的 `airbot-configure` / `airbot_py` 与 V5.2 的 `airbot-arm` / `arm_sdk` 混装。

假设文件已下载到 `~/Downloads`，可执行：

```bash
mkdir -p ~/Downloads/airbot-v5.2/main
mkdir -p ~/Downloads/airbot-v5.2/sdk
tar -xzf ~/Downloads/airbot_arm_release.tar.gz -C ~/Downloads/airbot-v5.2/main
tar -xzf ~/Downloads/sdk_client_release.tar.gz -C ~/Downloads/airbot-v5.2/sdk
find ~/Downloads/airbot-v5.2 -maxdepth 4 -type d -print | sort
```

先查询当前系统，再从上一步列出的目录中选择完全对应的版本文件夹：

```bash
lsb_release -rs
lsb_release -cs
```

选择规则如下：

- 输出 `20.04` / `focal`：只进入发布包的 20.04/focal 文件夹；
- 输出 `22.04` / `jammy`：只进入发布包的 22.04/jammy 文件夹，**本文推荐此项**；
- 输出 `24.04` / `noble`：只进入发布包的 24.04/noble 文件夹。

`sdk_client_release` 中不同 Ubuntu 版本对应不同的 SDK 文件夹。必须从所选文件夹中寻找 `.whl`；如果 `airbot_arm_release` 也按 Ubuntu 版本分目录，则 `.deb` 同样必须从对应目录选择。下面的命令仅用于查看候选文件，不能看到多个结果后随意挑选：

```bash
find ~/Downloads/airbot-v5.2 -type f \( -name '*.deb' -o -name '*.whl' \) -print
```

安装前执行一次“三重匹配”检查：

1. **SDK 目录匹配**：20.04 对 20.04/focal、22.04 对 22.04/jammy、24.04 对 24.04/noble；主程序如有相同分类，也按此匹配；
2. **CPU 架构匹配**：`x86_64` 对 `amd64`，`aarch64` 对 ARM64 包；
3. **软件版本匹配**：`airbot-arm` 与 `arm-sdk` 应来自同一发布批次，例如均为 V5.2.2。

再核对所选 `.deb` 的包信息：

```bash
dpkg-deb -f /实际路径/airbot-arm_实际文件名.deb Package Version Architecture Depends
```

此处的 `/实际路径/...` 是占位符，不能原样复制。可先输入命令前半部分，再把实际文件从“文件”应用拖入终端，或使用 Tab 补全路径。如果主程序压缩包中也存在 20.04、22.04、24.04 文件夹，路径必须经过当前系统对应的文件夹；`Architecture` 也应与主机匹配，例如 `amd64` 对应 `x86_64`。

## 7. 安装 `airbot-arm` 主程序

使用 `apt` 安装本地 deb，以便同时处理 `can-utils` 等依赖：

```bash
sudo apt install /实际路径/airbot-arm_实际文件名.deb
```

如果 `airbot_arm_release` 中的 `.deb` 也按 Ubuntu 版本分文件夹，Ubuntu 22.04 用户应使用 22.04/jammy 文件夹，Ubuntu 20.04 或 24.04 用户则使用各自的 20.04/focal 或 24.04/noble 文件夹；如果主程序只有一个通用 `.deb`，按发布包原有结构安装即可。不要把推荐使用 22.04 误解为所有系统都应安装 22.04 目录中的文件。

验证安装：

```bash
dpkg-query -W -f='${Status} 版本=${Version} 架构=${Architecture}\n' airbot-arm
command -v airbot-arm
```

正常情况下第一条应包含 `install ok installed`，第二条会输出 `airbot-arm` 的可执行文件路径。工程 V5.2.2 示例中的版本号为 `5.2.2`。

## 8. 创建 Python 环境并安装 SDK

不要直接用 `sudo pip install` 修改 Ubuntu 系统 Python。先检查将用于创建虚拟环境的解释器：

```bash
python3 --version
```

Ubuntu 22.04 和 24.04 用户在输出满足 Python 3.10+ 时，可创建虚拟环境：

```bash
python3 -m venv ~/airbot-venv
```

Ubuntu 20.04 用户不能使用默认的 Python 3.8 创建当前 SDK 环境。按 AIRBOT 发布包说明配置 Python 3.10+ 后，使用实际的解释器命令创建环境，例如：

```bash
python3.10 -m venv ~/airbot-venv
```

随后三个版本都执行：

```bash
source ~/airbot-venv/bin/activate
python -m pip install --upgrade pip
python -m pip install /实际路径/对应Ubuntu目录/arm_sdk_实际文件名.whl
```

这里的 SDK wheel 同样必须来自当前 Ubuntu 对应的文件夹：20.04 使用 20.04/focal 文件夹，22.04 使用 22.04/jammy 文件夹，24.04 使用 24.04/noble 文件夹。安装前可再次执行 `lsb_release -rs`，不要仅凭文件名相似就跨目录安装。

激活成功后，终端提示符前通常会出现 `(airbot-venv)`。验证 SDK：

```bash
python --version
python -m pip show arm-sdk
arm-sdk version
arm-sdk examples list
```

预期 `arm-sdk version` 显示与主程序相同的版本，例如 `5.2.2`。以后每次打开新终端使用 SDK 前，都要执行：

```bash
source ~/airbot-venv/bin/activate
```

退出虚拟环境可执行 `deactivate`。

## 9. 连接机械臂并检查 CAN 接口

### 9.1 硬件与安全检查

1. 用底板和夹具把机械臂牢固固定在桌面，清空最大工作半径 647 mm 周围的人和物品。
2. 如安装 G2/G2L 夹爪或 E2 示教器，断电操作，并只连接到教程指定的 J6 接口；不要拉扯线缆。
3. 将机械臂底座的 **USB-2 Type-C** 连接到 Ubuntu 主机。USB-1 主要用于末端相机数据，不是本流程的控制口。
4. 接通 24 V 电源，等待自检。不要在机械臂可能运动时把手放在关节或夹爪附近。

灯带含义：

| 灯带 | 含义 / 处理 |
| --- | --- |
| 黄灯常亮 | 正在自检，等待完成 |
| 黄灯闪烁 | 零位丢失，需要执行下述零位校准 |
| 红灯常亮 | 自检失败，停止操作并联系技术支持 |
| 白灯常亮 | 自检完成，尚未检测到 USB |
| 白色呼吸 | USB 已连接，正在等待控制服务启动 |
| 绿色流动 | 控制服务初始化中 |
| 绿色常亮 | 控制服务已启动，可接受外部指令 |

### 9.2 仅在黄灯闪烁时校零

1. 长按底座按钮约 3 秒，听到“咔哒”声后关节进入可手动调整状态。
2. 扶稳机械臂，缓慢对齐各连杆的零位标记；工程教程说明 J4、J5、J6 可保持任意位置。
3. 再按一次底座按钮，听到提示声即完成。
4. USB 已连接时，成功后应为白色呼吸灯。

具体姿态图片见工程的[首次上电教程](quick-start/running.en.md#_3)。

### 9.3 加载 SocketCAN 模块并识别接口

```bash
sudo modprobe slcan
lsmod | grep '^slcan'
ip link | grep -E 'can[0-9]+'
```

最后一条通常能看到 `can0`；多台设备可能依次为 `can1`、`can2`。记录机械臂对应的接口名。若没有输出：

```bash
lsusb
sudo dmesg --follow
```

保持第二条命令运行，重新插拔 USB-2，观察是否出现新的 USB/CAN 设备日志；按 `Ctrl + C` 停止查看。仍无法识别时，换一个确认支持数据传输的 USB 线和 USB 口后重试。

## 10. 启动机械臂控制服务

根据实际硬件选择 `arm_type`：

| 参数 | 硬件 |
| --- | --- |
| `airbot_play` | AIRBOT Play 六轴机械臂，无指定末端 |
| `airbot_play_g2` | AIRBOT Play + G2 夹爪 |
| `airbot_play_g2l` | AIRBOT Play + G2L 夹爪 |
| `airbot_play_e2` | AIRBOT Play + E2 示教器，仅重力补偿模式 |
| `airbot_play_g2_d405` | AIRBOT Play + G2 + RealSense D405 |
| `airbot_play_g2l_d405` | AIRBOT Play + G2L + RealSense D405 |
| `airbot_replay` | AIRBOT Replay 示教器 |
| `airbot_replay_mini` | AIRBOT Replay Mini 示教器 |

例如，G2 夹爪机械臂连接为 `can0` 时：

```bash
sudo airbot-arm -i can0 -t airbot_play_g2
```

主程序必须使用 `sudo`。保持这个终端开启，等待日志稳定且灯带变为绿色常亮。默认 SDK 连接地址为本机 `localhost:50051`。

多台设备必须使用不同 CAN 接口和不同端口，例如第二台设备：

```bash
sudo airbot-arm -i can1 -t airbot_play_g2l --address 0.0.0.0:50052
```

对应 SDK 客户端也必须使用端口 `50052`。`0.0.0.0` 会监听所有网络接口；如果没有远程控制需求，使用默认地址即可，并避免在不可信网络暴露端口。

> 默认按 `Ctrl + C` 退出服务时，机械臂会执行回零。只有明确知道后果时才加 `--no-return`。USB 意外断开可能导致 gRPC 服务异常退出，应关闭该服务终端，确认端口释放后再重新连接。

## 11. 验证 SDK 已经配置完成

打开第二个终端：

```bash
source ~/airbot-venv/bin/activate
arm-sdk version
arm-sdk examples list
```

再创建一个只读取状态、不发送运动指令的测试文件：

```bash
nano ~/airbot_sdk_check.py
```

粘贴以下内容：

```python
from arm_sdk import AirbotClient


def main():
    with AirbotClient(host="localhost", port=50051) as arm:
        service_state = arm.get_service_state()
        firmware_info = arm.get_firmware_info()
        print("service_state:", service_state)
        print("firmware_info:", firmware_info)
        if service_state is None:
            raise SystemExit("未读取到服务状态，请检查 airbot-arm 服务和端口。")


if __name__ == "__main__":
    main()
```

按 `Ctrl + O`、回车保存，再按 `Ctrl + X` 退出，然后运行：

```bash
python ~/airbot_sdk_check.py
```

能打印非 `None` 的服务状态，且控制服务终端没有报错，即可认为以下链路已经打通：

```text
机械臂 USB-2 → SocketCAN(can0) → airbot-arm(:50051) → arm_sdk / AirbotClient
```

此时才建议开始看例程。先列出例程并查看某个例程的参数：

```bash
arm-sdk examples list
arm-sdk examples run 例程名称 -h
```

例程可能让机械臂运动。运行前必须固定机械臂、清空工作空间、确认关节未接近限位，并准备随时停止程序。不要在不理解参数时直接运行运动例程。

## 12. 正确停止与日常启动

停止时：

1. 先在 SDK 程序终端按 `Ctrl + C` 停止客户端；
2. 再到 `airbot-arm` 服务终端按 `Ctrl + C`，观察机械臂回零；
3. 等动作完全停止后，如需断电，按硬件教程要求从底座 Base Board 处拔下电源连接器，不要只关闭仍连接着机械臂的插线板。

以后日常启动只需：

```bash
# 终端 1：确认 CAN 名称并启动服务
ip link | grep -E 'can[0-9]+'
sudo airbot-arm -i can0 -t airbot_play_g2

# 终端 2：激活 SDK 环境
source ~/airbot-venv/bin/activate
arm-sdk examples list
```

## 13. 常见问题

| 现象 | 检查与处理 |
| --- | --- |
| `arm-sdk: command not found` | 先执行 `source ~/airbot-venv/bin/activate`，再检查 `python -m pip show arm-sdk` |
| wheel 无法安装 | 检查 `python --version` 是否至少 3.10、`uname -m` 是否与发布包匹配，并确认没有误用 V5.1.6 的 wheel |
| 找不到 `can0` | 确认接的是 USB-2、线缆支持数据、白色呼吸灯正常；执行 `sudo modprobe slcan` 后重新插拔 |
| `airbot-arm` 权限错误 | 主程序按工程要求使用 `sudo` 启动 |
| SDK 连接失败 | 确认服务终端仍在运行、客户端端口与 `--address` 一致；默认是 `50051` |
| 端口已占用 | 执行 `sudo ss -ltnp | grep 50051` 找到旧服务，先在旧服务终端正常停止，不要同时启动两个相同端口的服务 |
| 无法取得控制权 | V5.2 使用独占 Lease；关闭其他正在控制的客户端，等待租约释放后重试 |
| 灯带红色或日志报告电机错误 | 不继续发送动作命令，记录完整日志、机械臂序列号和固件信息并联系售后 |
| Ubuntu 安装器看不到 SSD | 常见原因是 Intel RST/RAID；退出安装，不要直接格式化磁盘或盲目切 AHCI |
| 双系统安装后 Windows 要恢复密钥 | 使用安装前备份的 BitLocker 恢复密钥；不要反复修改 BIOS/TPM 设置 |

## 14. 旧版本用户必须注意

- 当前主线 V5.2：主程序是 `airbot-arm`，Python 包/模块是 `arm-sdk` / `arm_sdk`，主类是 `AirbotClient`。
- V5.1.6：驱动包是 `airbot-configure`，Python 包是 `airbot_py`，示例和类名也不同。
- V2.9、V4.x 或更早软件通常还涉及固件升级。仅安装新 `.deb` / `.whl` 并不能完成跨代升级。
- 工程资料要求兼容的 OD 电机固件为 `04114` 或更高；V5.1.6 用户还需特别确认 DM 电机固件为 `5015`。

若现有机械臂曾使用旧版软件、固件版本不明确或启动日志与教程不同，请把序列号和完整启动日志发给技术支持，获取成套的固件、主程序和 SDK。不要自行拼接不同版本，更不要在没有官方升级流程时刷写固件。

当前 V5.2 教程只明确提供 Python `arm-sdk` 的安装流程。若项目需要 C++ SDK、ROS/ROS 2、Docker、DISCOVERSE 或多臂方案，应向技术支持取得与 V5.2 同批次、与 Ubuntu 版本和 CPU 架构相符的包，再进入对应专题配置。

## 15. 完成检查表

- [ ] Windows 数据与 BitLocker 恢复密钥已备份，或使用专用空磁盘；
- [ ] Ubuntu 20.04、22.04 或 24.04 LTS 能正常启动、联网和更新；新安装优先使用 22.04；
- [ ] 已根据 `lsb_release -rs` / `lsb_release -cs` 选择完全对应的 20.04、22.04 或 24.04 SDK 目录；主程序如有版本目录也已正确匹配；
- [ ] `uname -m` 与 AIRBOT 软件包架构一致；
- [ ] `airbot-arm` 和 `arm-sdk` 版本一致；
- [ ] `arm-sdk version` 可正常输出；
- [ ] 机械臂已固定，USB-2 和电源连接正确；
- [ ] `ip link` 能看到 `can0` 或相应 CAN 接口；
- [ ] `sudo airbot-arm ...` 正常运行，灯带绿色常亮；
- [ ] `airbot_sdk_check.py` 能读取服务状态；
- [ ] 运行任何运动例程前已清空工作空间并了解停止方法。

## 参考资料

工程内资料：

- [V5.2 软件安装](sdk/quickstart/installation.en.md)
- [CAN 接口检查](sdk/quickstart/can-interface.en.md)
- [启动主程序](sdk/quickstart/run-service.en.md)
- [SDK 例程](sdk/quickstart/examples/list.en.md)
- [电机版本要求](sdk/quickstart/motor-version.en.md)
- [灯带状态](sdk/concepts/arm-status-led.en.md)
- [机械臂装配与接线](quick-start/inventory.en.md)
- [版本更新日志](changelog.en.md)

系统官方资料：

- [Ubuntu Desktop 安装教程](https://ubuntu.com/tutorials/install-ubuntu-desktop)
- [Ubuntu 22.04 发布与下载](https://releases.ubuntu.com/22.04/)
- [Microsoft：释放 Windows 磁盘空间](https://support.microsoft.com/en-us/windows/empty-the-recycle-bin-in-windows-10-d4c8f8ef-a12e-8250-b0cf-2311960a31f9)
- [Microsoft：压缩基本卷](https://learn.microsoft.com/en-us/windows-server/storage/disk-management/shrink-a-basic-volume)
- [Ubuntu：BitLocker 与双系统安装](https://ubuntu.com/desktop/docs/en/latest/reference/bitlocker-during-ubuntu-installation/)
