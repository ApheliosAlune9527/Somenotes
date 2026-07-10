# Ubuntu虚拟机远程连接配置流程

## 一、虚拟机设置

### 1. 安装Tailscale

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

弹出链接 → 浏览器打开 → 登录账号

### 2. 安装SSH服务

```bash
sudo apt update
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```

### 3. 关闭睡眠（可选）

```bash
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

## 二、腾讯云服务器设置

### 1. 安装Tailscale

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

弹出链接 → 浏览器打开 → 用同一个账号登录

### 2. 生成SSH密钥（如果还没有）

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
```

## 三、SSH密钥认证配置

### 1. 在腾讯云服务器上查看公钥

```bash
cat ~/.ssh/id_ed25519.pub
```

输出类似：

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAxxxxx... tencent-cloud
```

### 2. 在虚拟机上添加公钥

```bash
# 创建.ssh目录（如果不存在）
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# 添加公钥（把第一步的输出替换进去）
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAxxxxx... tencent-cloud" >> ~/.ssh/authorized_keys

# 设置权限
chmod 600 ~/.ssh/authorized_keys

# 检查内容（确保没有不完整的公钥）
cat ~/.ssh/authorized_keys
```

### 3. 测试连接

```bash
ssh -o ConnectTimeout=10 aphelios@100.121.103.61 "echo '连接成功！'"
```

## 四、日常使用

### 启动虚拟机后

- 不需要敲任何命令
- Tailscale自动启动
- SSH服务自动启动
- 直接告诉我"连接虚拟机"就行

### 如果连接失败

- 检查虚拟机是否在运行
- 检查Tailscale是否在运行：`sudo systemctl status tailscaled`
- 检查SSH是否在运行：`sudo systemctl status ssh`

## 五、关键信息

| 项目 | 值 |
|------|-----|
| 虚拟机用户名 | `aphelios` |
| 虚拟机Tailscale IP | `100.121.103.61` |
| 腾讯云Tailscale IP | `100.74.206.86` |
| SSH端口 | `22` |

## 六、一句话总结

装Tailscale → 装SSH → 生成密钥 → 虚拟机添加公钥 → 完成。以后只要虚拟机开着，我就能连。
