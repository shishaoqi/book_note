#### docker-compose.yml
```
version: '3.8'

networks:
  monitor:
    driver: bridge

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus  # prometheus_data` 是一个 Docker 卷，其实际存储位置由 Docker 管理，通常在 `/var/lib/docker/volumes/` 目录下。
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
    restart: unless-stopped
    networks:
      - monitor

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=xxxxxx
    restart: unless-stopped
    networks:
      - monitor

# 声明两个 Docker 卷
volumes:
  prometheus_data:
  grafana_data:
```

#### 1. **`prometheus_data:/prometheus`**

- **作用**：将宿主机上的一个名为 `prometheus_data` 的 Docker 卷挂载到 Prometheus 容器的 `/prometheus` 目录。
    
- **目的**：
    
    - **数据持久化**：Prometheus 使用 `/prometheus` 目录存储其时间序列数据库（TSDB）。通过将这个目录挂载到 Docker 卷，即使 Prometheus 容器被删除或重新创建，存储在 `/prometheus` 目录中的数据仍然可以被保留下来。
        
    - **数据共享**：如果需要在不同的 Prometheus 容器之间共享数据，或者在容器重启后恢复数据，Docker 卷提供了一种方便的方式。
        
- **位置**：
    
    - 宿主机上：`prometheus_data` 是一个 Docker 卷，其实际存储位置由 Docker 管理，通常在 `/var/lib/docker/volumes/` 目录下。
        
    - 容器内：挂载到 `/prometheus` 目录，Prometheus 使用这个目录存储其数据。


### 总结
**`prometheus_data:/prometheus`** 和 **`grafana_data:/var/lib/grafana`** 是卷挂载点，用于将 Docker 卷挂载到容器内的特定目录，实现数据的持久化和共享

**`volumes:` 部分** 是对这些卷的声明，确保在启动时创建这些卷，并在需要时提供给容器使用。