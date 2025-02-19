# ubuntu 表态ip设置

sudo vim /etc/netplan/00-installer-config-wifi.yaml

```
# This is the network config written by 'subiquity'
network:
  version: 2
  wifis:
    wlp5s0:
      dhcp4: false
      addresses: [192.168.8.250/24]
      routes:
        - to: default
        #- to: 192.168.8.0/24
          via: 192.168.8.1
      nameservers:
        addresses: [114.114.114.114,223.5.5.5,119.29.29.29]
      access-points:
        Wining:
          password: 963963qw
```

sudo netplan apply