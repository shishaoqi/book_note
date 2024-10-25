ubuntu   cd /var/lib/docker/
-bash: cd: /var/lib/docker/: Permission denied



使用 su 或 sudo -i 命令
如果你需要在超级用户环境下工作一段时间，你可以使用 su 命令切换到 root 用户，或者使用 sudo -i 来获取一个 root 用户的 shell：

bash
su
或者

bash
sudo -i
然后，你就可以访问 /var/lib/docker/ 目录了。