### 配置文件路径
文件名：  
ollama.service

路径：  
/etc/systemd/system/

### 开启与关闭服务
sudo systemctl daemon-reload
sudo systemctl enable ollama

卸载:  
sudo systemctl disable ollama

### 启动与关闭
sudo systemctl start ollama

sudo systemctl stop ollama


### 查看日志
要查看作为启动服务运行的Ollama的日志，请运行：

journalctl -u ollama



sudo systemctl stop ollama

sudo tar -xzf - -C /usr/local


### 配置
vim /etc/systemd/system/ollama.service 
Environment="OLLAMA_HOST=0.0.0.0:11434"
Environment="OLLAMA_KEEP_ALIVE=30m"