Hermes 是一个多功能的智能 Agent 框架，支持多模型接入、任务自动化和跨平台消息传递。部署 Hermes 能让你在微信、钉钉、飞书等环境中快速建立自己的 AI 助手。本文将从适用人群、环境选择到具体部署步骤进行完整讲解。

### 适合部署 Hermes 的人群

1. AI爱好者与开发者
    
    想要搭建自己的智能体，调度多模型（如 GPT 系列、Claude、Gemini、DeepSeek 等）并在工作流程中自动执行任务。
    
2. 有一台自己的服务器
    
    云服务器或者家庭内网的NAS主机即可，因为 Hermes 这类智能体服务最好保持长期在线。它不像普通网页工具，用完即关；它更适合像一个后台服务一样运行着，随时等待你的消息、指令和任务。
    
3. 拥有对应ai平台的apiKey
    
    hermes本质上是一个agent，需要接入llm作为大脑中枢来操作各类工具，所以需要对应大语言模型平台的api授权来进行驱动。
    

### 部署环境选择与差异

Hermes 可以在不同环境下部署，每种环境在使用体验上略有差异：

1. 常用办公电脑设备（win/mac）
    
    优点是方便调试和开发，缺点则是长时间运行任务可能受限；需保证网络通畅，并且关机后bot会失联。
    
2. 服务器宿主机
    
    优点是稳定，适合长期任务；可直接使用系统级服务管理，缺点则是可能agent因为误操作直接影响宿主机本体环境，导致服务器异常运行。
    
3. docker容器内（包含各类主机的docker 如win/mac/服务器/nas）
    
    优点是易于隔离环境，便于扩展和迁移，容器内发生的操作不会影响宿主机环境；不同版本 Hermes 可同时运行，而缺点是容器内需要映射端口和挂载卷；日志和持久化需要额外挂载卷。部分宿主机工具无法调用（例如调用宿主机的chrome来进行操作）。
    

## Hermes 部署前准备

1. **系统与依赖**
    
    - Docker 或 Docker Compose（推荐 20.10+）
        
    - Python 环境（仅在非容器部署时）
        
    - 网络访问权限，尤其是访问模型 API 和消息平台（访问国外大模型需要宿主机配置代理）
        
2. **账户与 API**
    
    - 微信账号/钉钉机器人apikey   （bot类按需配置）
        
    - 模型 API Key（OpenAI, Claude, DeepSeek等）
        
3. **硬件建议**
    
    - CPU ≥ 1核，内存 ≥ 2 GB
        
    - 磁盘 ≥ 20 GB（存储日志和容器预留操作区域）
        

## Hermes 部署步骤

### 1. 容器化部署（推荐）

如果只是临时体验，可以用 docker run 启动；但如果你打算长期使用 Hermes，推荐直接使用 **Docker Compose** 管理。

Docker Compose 的好处是：

- 配置集中，后续维护方便；
    
- 容器重启、端口映射、数据挂载都写在一个文件里；
    
- 后续增加 Dashboard、数据库、反向代理也更容易；
    
- 适合部署在内网服务器、NAS、云服务器或长期运行的宿主机上。
    

1. **创建工作目录**
    

> mkdir -p /home/hermes
> 
> cd /home/hermes

2. **创建docker-compose.yml文件**
    
    在 /home/hermes 目录下创建 docker-compose.yml
    

文件内容如下
![[Pasted image 20260620151408.png|693]]
> 图 : docker-compose.yml示例

docker-compose.yml下载

 3.启动hermes服务

> docker compose up -d

此处的up 代表启动  -d代表后台启动

执行命令后docker会自动拉取hermes的镜像、配置网络、运行服务，非常的方便。

4.进入容器进行初始化

> docker exec -it hermes-agent bash
> #此处后边的命令均为容器内操作

> #切换用户为容器内的hermes 避免文件权限异常问题
> 
> su hermes
> 
> #执行初始化脚本
> 
> /opt/hermes/.venv/bin/hermes setup

![[Pasted image 20260620151610.png]]
> 图: 选择快速设置

![[Pasted image 20260620151629.png]]
> 图: 选择模型提供商 此处选择deepseek

如果有自己的模型提供商可以直接选择，如果是第三方也可以选择custom (direct API)来配置baseUrl 和 apiKey
![[Pasted image 20260620151653.png]]
> 图: 输入deepseek官网的apiKey 然后回车


![[Pasted image 20260620151657.png]]
>图: #### 默认官网baseUrl无需修改 直接回车

![[Pasted image 20260620151701.png]]
> 图: 默认的模型 此处选deepseek-v4-flash

![[Pasted image 20260620151753.png]]
> 图: 选择终端运行环境为local

此处的local即代表容器内:
![[Pasted image 20260620151759.png]]
> 图: 工作目录 直接回车确认

![[Pasted image 20260620151830.png]]

如果开启sudo 则agent执行一些安装操作则无需进行二次确认，如果你们觉得危险的话可以关闭，此处是容器内部署，我觉得问题不大。选择y的话输入设置sudo密码即可

![[Pasted image 20260620151840.png]]

![[Pasted image 20260620151843.png]]

把常用的消息平台翻译标识在后边了，大家可以按需去激活（可以同时开启多个消息渠道的）

![[Pasted image 20260620151854.png]]

![[Pasted image 20260620151900.png]]

![[Pasted image 20260620151904.png]]

![[Pasted image 20260620151907.png]]

![[Pasted image 20260620151911.png]]
> 图:选第二个 允许所有的消息

![[Pasted image 20260620151927.png]]

![[Pasted image 20260620151930.png]]
> 图:设置你的微信账号为home channel 直接输入y 按回车

home channel是主消息渠道  定时任务和主要的消息通知会走主消息同步过来

![[Pasted image 20260620151950.png]]

![[Pasted image 20260620151957.png]]