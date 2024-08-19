常用的docker命令整理
```
docker build -t myubuntu:v1 . # build Dockerfile
docker pull nvidia/cuda:10.2-devel-ubuntu18.04 # 拉取远端镜像

docker run -itd --runtime=nvidia --gpus=all -e NVIDIA_DRIVER_CAPABILITIES=compute,utility,video,graphics -v /root/Documents/xxx:/data/ --name test --privileged=true -v /dev/shm:/dev/shm -p 49154:22 IMAGE_ID /bin/bash
# -it必备 d表示在背景里运行; -v 磁盘挂载 本地绝对路径:容器的绝对路径; --name 给你的container取个响亮的芳名;-v /dev/shm:/dev/shm 共享内存; image ID; /bin/bash 执行命令; -p 端口映射 -p 49154:22

docker --help
docker pull pytorch/pytorch:latest #拉取仓库
docker images   #查看镜像
docker ps	    #查看运行着的容器
docker ps -a    #查看所有容器
docker exec -it container-id /bin/bash # 进入容器 
ctrl+D # 退出容器
docker start container-id   # 启动容器
docker stop container-id    # 停止容器
docker rmi image-id 	    # 删除镜像
docker rm container-id 	    # 删除容器

systemctl stop docker.service # 停止docker服务
systemctl start docker.service # 开启docker服务

docker export container-id > name.tar #容器的导出,可以带着它到处跑,直接导出的是没有压缩过的,你可以自己压缩一下。
# 还有，文件导出后它其实就不是一个运行着的实例了，它就变成了镜像。
docker import name.tar # 容器导入
```
                        


docker run -it -d -v ./code:/root/code -p 9000:9000 --name ubuntu220404-watermark ubuntu:22.04 /bin/bash



### cuda:11.7.1-cudnn8-devel-ubuntu20.04
```
docker pull nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04

docker run -it -d --runtime=nvidia --gpus=all -v ./water_mark:/root/water_mark -p 9900:9900 -p 7000:7000 --name cuda_11.7.1-cudnn8-devel-ubuntu20.04 nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04 /bin/bash

docker exec -it 52acf151710e bin/bash
```

### cuda:12.5.0-devel-ubuntu22.04
```
docker pull nvidia/cuda:12.5.0-devel-ubuntu22.04

docker run -it -d --runtime=nvidia --gpus=all -v ./docker_ollama:/root/docker_ollama -p 11431:11434 -p 7100:7100 --name cuda_12.5.0-devel-ubuntu22.04 nvidia/cuda:12.5.0-devel-ubuntu22.04 /bin/bash

docker exec -it 2da9d07bbba6 bin/bash
```

### 清除 nvidia 驱动后，docker环境要执行以下命令

docker run -it -d --runtime=nvidia --gpus=all -v ./water_mark:/root/water_mark -p 9900:9900 -p 7000:7000 --name cuda_11.7.1-cudnn8-devel-ubuntu20.04 nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04 /bin/bash
docker: Error response from daemon: unknown or invalid runtime name: nvidia.

以上报错解决：
```
apt install -y nvidia-docker2 # 安装nvidia-docker

sudo apt-get install nvidia-container-runtime

systemctl restart docker # 重启docker
```