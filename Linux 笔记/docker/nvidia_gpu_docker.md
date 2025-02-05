# gpu服务器安装笔记

### Installing the NVIDIA Container Toolkit
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

### tolas--2 -----（后来使用 docker-compose 重新安装过，下面的已弃用）
docker pull nvidia/cuda:12.2.2-devel-ubuntu22.04

sudo docker run -dit --runtime=nvidia --gpus=0 -p 9002:9002 -v ./gpu-0-code:/root/code -v ./models:/llm-model  --name=gpu-0 nvidia/cuda:12.2.2-devel-ubuntu22.04

sudo docker run -dit --runtime=nvidia --gpus=1 -p 9003:9003 -v ./gpu-1-code:/root/code -v ./models:/llm-model  --name=gpu-1 nvidia/cuda:12.2.2-devel-ubuntu22.04

### tolas--3
docker pull nvidia/cuda:12.4.1-devel-ubuntu22.04

sudo docker run -dit --runtime=nvidia --gpus="0" -p 1012:22 -p 11431:11434 -p 9000:9000 -v ./gpu-0-code:/root/code -v ./models:/llm-model  --name=gpu-0 nvidia/cuda:12.4.1-devel-ubuntu22.04

sudo docker run -dit --runtime=nvidia --gpus 1 -p 1022:22 -p 11432:11434 -p 9001:9001 -v ./gpu-1-code:/root/code -v ./models:/llm-model  --name=gpu-1 nvidia/cuda:12.4.1-devel-ubuntu22.04



apt-get install wget
wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
bash Ana.....
conda create --name chat-server python=3.10
conda activate chat-server


apt-get install -y systemctl
apt-get install -y curl
curl -fsSL https://ollama.com/install.sh | sh
systemctl start ollama

ollama create gemma2:27b-it-0902-1 -f Modelfile.2024.09.02-1


apt install redis-server
systemctl start redis
systemctl enable redis
systemctl status redis




python gemma2_server.py




docker run -dit --runtime=nvidia --gpus=0 -p 9014:9014 -v ./gpu-14-code:/root/code -v ./models:/llm-model  --name=gpu-1 nvidia/cuda:12.2.2-devel-ubuntu22.04

docker run -dit --runtime=nvidia --gpus="0" -p 9014:9014 -v ./gpu-14-code:/root/code -v ./models:/llm-model  --name=gpu-014 nvidia/cuda:12.4.1-devel-ubuntu22.04