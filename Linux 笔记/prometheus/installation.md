# 安装

### node_exporter

路径: /usr/local/node_exporter-1.8.2.linux-amd64
启动命令：  
nohup ./node_exporter  --web.listen-address=":9100" &


### docker-compos 安装 prometheus + grafana
路径： /home/wuning/code/docker/prometheus
配置文件： docker-compose.yml   prometheus.yml

热更新配置：  
curl -X POST http://localhost:6090/-/reload