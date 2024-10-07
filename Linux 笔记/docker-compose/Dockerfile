FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

# 更新包索引
RUN apt-get update

# 安装必要的软件包
RUN apt-get install -y curl vim screen

# 安装 systemctl 工具（如果需要）
RUN apt-get install -y systemd-sysv systemctl

# 安装 Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# 安装 Redis 服务器
RUN apt-get install -y redis-server

# 启动 Ollama 服务
# 注意：在 Docker 容器中，通常不使用 systemctl 来管理服务。
# 以下命令仅为示例，实际运行时可能需要调整。
#RUN systemctl start ollama
#RUN systemctl enable ollama

# 启动 Redis 服务器
# 同上，以下命令仅为示例，实际运行时可能需要调整。
#RUN systemctl start redis-server
#RUN systemctl enable redis-server

# 设置容器启动时运行的命令
# 这里我们直接启动 Redis 服务器和 Ollama 服务
# CMD ["bash", "-c", "redis-server & ollama serve"]