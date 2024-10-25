
apt install -y screen

systemctl start redis
systemctl start ollama

apt-get install tzdata


### 创建模型
cd /llm-model
ollama create gemma2:27b-it-0913-1 -f Modelfile.2024.09.13-1


### 创建 conda 环境
bash  Ana.....
source ~/.bashrc
conda create --name chat-server python=3.10
conda activate chat-server


### python 依赖
cd ~/code/chat-server

pip install some-package -i https://mirrors.aliyun.com/pypi/simple
pip install -r re....


cp env.example .env
vim .env  # 修改配置

### 启动服务
screen -S chat-server
python gemma2_server.py


### 测试
curl --location 'http://localhost:9005/load_redis_data' \
--header 'Content-Type: application/json' \
--data '{
    "token": "encrypt_token"
}'



# ----- 重启命令 ------
```
systemctl start redis
systemctl start ollama


cd ~/code/chat-server
conda activate chat-server


screen -S chat-server
screen -r chat-server
python gemma2_server.py


# 恢复缓存
curl --location 'http://localhost:9005/load_redis_data' \
--header 'Content-Type: application/json' \
--data '{
    "token": "encrypt_token"
}'

```

















```

#!/bin/bash

# 启动 Redis 服务
systemctl start redis

# 启动 ollama 服务
systemctl start ollama

# 检查并激活 Conda 环境
if [ -n "$(command -v conda)" ]; then
    cd ~/code/chat-server
    if [ -f "$HOME/.bashrc" ]; then
        source "$HOME/.bashrc"
    elif [ -f "$HOME/.zshrc" ]; then
        source "$HOME/.zshrc"
    else
        echo "未找到 .bashrc 或 .zshrc 文件."
        exit 1
    fi

    /root/anaconda3/bin/conda activate chat-server || { echo "激活 Conda 环境失败"; exit 1; }
  
    # 启动 Python 服务器
    if [ -x "python gemma2_server.py" ]; then
        screen -S chat-server -d -m python gemma2_server.py
    else
        echo "Python 脚本不可执行或不存在"
        exit 1
    fi
else
    echo "Conda 未安装或不可用"
    exit 1
fi

# 发送 HTTP 请求
curl --location 'http://localhost:9004/load_redis_data' \
--header 'Content-Type: application/json' \
--data '{"token": "encrypt_token"}' || { echo "发送 HTTP 请求失败"; exit 1; }

```