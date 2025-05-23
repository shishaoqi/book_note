以下是 CentOS 系统下安装 Docker 和 Docker Compose 的详细步骤：

### 安装 Docker
1. **卸载旧版本的 Docker**（如果之前安装过）：
```bash
   sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
```
   即使未安装过，也建议执行此步骤，以避免潜在冲突。

2. **安装必要的依赖工具**：
```bash
   sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```

3. **添加 Docker 的官方 Yum 仓库**（推荐使用阿里云镜像源）：
```bash
   sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

4. **安装 Docker**：
```bash
	sudo yum install -y docker-ce docker-ce-cli containerd.io
```

5. **启动 Docker 服务并设置开机自启**：
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```
6. **验证 Docker 是否安装成功**：
   ```bash
   docker --version
   ```
   如果输出类似 `Docker version 20.10.xx`，则说明安装成功。

### 安装 Docker Compose
1. **下载 Docker Compose**：
```bash
   sudo curl -L "https://github.com/docker/compose/releases/download/v2.36.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
	其中 `v2.36.1` 是版本号，可以根据需要替换为其他版本。
	最新版本请到	 https://github.com/docker/compose/releases  查看

2. **赋予执行权限**：
   ```bash
   sudo chmod +x /usr/local/bin/docker-compose
   ```
3. **验证 Docker Compose 是否安装成功**：
   ```bash
   docker-compose --version
   ```
   如果输出类似 `Docker Compose version v2.32.2`，则说明安装成功。

### 配置 Docker 镜像加速（可选）
在国内网络环境下，访问 Docker Hub 可能较慢，可以通过配置国内镜像源加速拉取镜像：
1. **创建或编辑配置文件**：
   ```bash
   sudo tee /etc/docker/daemon.json <<-'EOF'
   {
       "registry-mirrors": [
           "https://docker.m.daocloud.io",
           "https://dockerproxy.com",
           "https://docker.mirrors.ustc.edu.cn"
       ]
   }
   EOF
   ```
2. **重启 Docker 服务**：
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart docker
   ```
   配置完成后，拉取镜像的速度会显著提升。