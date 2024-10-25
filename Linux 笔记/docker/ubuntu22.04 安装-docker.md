在 Ubuntu 22.04 上安装 Docker 需要执行以下步骤：

1. **更新软件包索引**：
   打开终端，首先更新你的软件包索引：
   ```bash
   sudo apt update
   ```

2. **安装所需的软件包**：
   安装一些必要的软件包，这些软件包允许 `apt` 使用 HTTPS 仓库，并添加 Docker 的官方 GPG 密钥：
   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. **添加 Docker 的官方 GPG 密钥**：
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

4. **添加 Docker 仓库到 APT 源**：
   ```bash
   echo \
   "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

5. **再次更新软件包索引**：
   ```bash
   sudo apt update
   ```

6. **安装 Docker Engine**：
   安装 Docker Engine 社区版（CE）：
   ```bash
   sudo apt install docker-ce docker-ce-cli containerd.io
   ```

7. **验证 Docker 是否安装成功**：
   安装完成后，你可以运行 `hello-world` 镜像来验证 Docker 是否正确安装：
   ```bash
   sudo docker run hello-world
   ```
   输出：
   ```
   $ sudo docker run hello-world
    Unable to find image 'hello-world:latest' locally
    latest: Pulling from library/hello-world
    c1ec31eb5944: Pull complete 
    Digest: sha256:53cc4d415d839c98be39331c948609b659ed725170ad2ca8eb36951288f81b75
    Status: Downloaded newer image for hello-world:latest

    Hello from Docker!
    This message shows that your installation appears to be working correctly.

    To generate this message, Docker took the following steps:
    1. The Docker client contacted the Docker daemon.
    2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
        (amd64)
    3. The Docker daemon created a new container from that image which runs the
        executable that produces the output you are currently reading.
    4. The Docker daemon streamed that output to the Docker client, which sent it
        to your terminal.

    To try something more ambitious, you can run an Ubuntu container with:
    $ docker run -it ubuntu bash

    Share images, automate workflows, and more with a free Docker ID:
    https://hub.docker.com/

    For more examples and ideas, visit:
    https://docs.docker.com/get-started/
    ```

8. **非 root 用户运行 Docker**（可选）：
   默认情况下，Docker 需要 `root` 权限来运行。为了允许非 root 用户运行 Docker，你需要将用户添加到 `docker` 组：
   ```bash
   sudo usermod -aG docker your-username
   ```
   替换 `your-username` 为你的用户名。之后，你可能需要注销并重新登录，以使这些更改生效。

9. **安装 Docker Compose**（可选）：
   Docker Compose 是一个用于定义和运行多容器 Docker 应用程序的工具。你可以从 [Docker Compose 的 GitHub 仓库](https://github.com/docker/compose) 下载并安装它。

完成以上步骤后，Docker 应该已经成功安装在你的 Ubuntu 22.04 系统上，并且你可以开始创建和运行容器了。



### 安装NVIDIA Container Toolkit

1. 安装NVIDIA Container Toolkit：
```
sudo apt install -y nvidia-container-toolkit
```
或从官方文档查看并安装：
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-the-nvidia-container-toolkit

2. 验证NVIDIA Container Toolkit是否安装成功：

安装完成后，重启 Docker 服务以应用更改：
```
sudo systemctl restart docker

sudo docker run --rm --gpus all nvidia/cuda:11.7.1-runtime-ubuntu20.04 nvidia-smi
```