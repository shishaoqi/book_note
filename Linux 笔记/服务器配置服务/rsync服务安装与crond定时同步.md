* https://developer.aliyun.com/article/931870

* https://www.8kiz.cn/archives/13044.html


### /etc/rsyncd.conf
```
pid file = /var/run/rsyncd.pid
lock file = /var/run/rsyncd.lock
log file = /var/log/rsyncd.log
secrets file = /etc/rsyncd.password

[shared]
path = /data_disk/docker_ubuntu_desktop/Documents/linux_chat
comment = Shared Data
read only = no
list = yes
uid = root
gid = root
auth users = root
```

### /etc/rsyncd.password
```
rsync:wuning*123
```

### 连接服务，同步远程文件
rsync -avz --progress rsync@192.168.8.250::shared ./


### 脚本代码
```
#!/bin/bash
rsync -avz --progress root@192.168.8.250::shared /docker_ubuntu_desktop/Documents --password-file=/docker_ubuntu_desktop/rsync.password
```


### crond 定时任务
```
crond -e

# 写入
*/3 * * * * /docker_ubuntu_desktop/sync-file.sh
```

#### 启动与关闭定时任务
service cron start
service cron stop
