NVM（Node Version Manager）是一个用于管理Node.js版本的命令行工具。它允许开发者在同一台机器上安装和切换多个版本的Node.js，以便在不同的项目中使用不同的Node.js版本。

### 安装NVM

#### Linux 和 macOS 安装

在终端执行以下命令：
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
```

#### Windows安装

推荐使用`nvm-windows`：
1. **下载nvm-windows安装包**：从[nvm-windows官方仓库](https://github.com/coreybutler/nvm-windows/releases)下载安装包。
2. **运行安装程序**：按照提示完成安装。
3. **验证安装**：
    ```cmd
    nvm version
    ```

### 常用命令

#### 查看可用Node.js版本
```bash
nvm ls-remote
```
列出所有可用的Node.js版本。

#### 安装指定版本
```bash
nvm install <version>
```

例如：
```bash
nvm install 16.20.0
```

#### 切换Node.js版本
```bash
nvm use <version>
```

例如：
```bash
nvm use 16.20.0
```

#### 查看已安装的Node.js版本
```bash
nvm ls
```

#### 设置默认版本
```bash
nvm alias default <version>
```

例如：
```bash
nvm alias default 16.20.0
```

#### 卸载Node.js版本
```bash
nvm uninstall <version>
```

### 使用示例
- **查看当前 Node.js 版本**：
    ```bash
    node -v
    ```

- **安装最新的LTS（长期支持）版本**：
    ```bash
    nvm install --lts
    ```

- **切换到最新版本**：
    ```bash
    nvm install node
    nvm use node
    ```

- **切换到不同版本**：
    ```bash
    nvm install 14.21.3
    nvm use 14.21.3
    ```

### 总结

NVM是一个强大的工具，可以帮助开发者轻松管理多个Node.js版本，提高开发效率。通过本文的介绍，相信你已经对NVM有了更深入的了解，并能够熟练地使用它来解决实际问题。在未来的Node.js开发中，NVM将成为你的得力助手，让你在版本管理的道路上更加游刃有余。

参考资料：
[1] https://blog.csdn.net/weixin_38383877/article/details/143077797
[2] https://nvm.nodejs.cn/docs/
[3] https://gitcode.gitcode.host/docs-cn/nvm-docs-cn/
[4] https://juejin.cn/post/7478863586091827215
[5] https://m.blog.csdn.net/qq_42343318/article/details/147048710
[6] https://longsheng.org/post/20872.html
[7] https://m.blog.csdn.net/m0_62854966/article/details/144507586
[8] https://m.blog.csdn.net/weixin_45815335/article/details/128797056
[9] https://m.blog.csdn.net/Shids_/article/details/145570953
[10] https://www.cnblogs.com/snowhite/p/18556421
[11] https://cloud.baidu.com/article/3286084
[12] https://developer.aliyun.com/article/1636299
[13] https://zhuanlan.zhihu.com/p/19474958752
[14] https://cloud.tencent.com/developer/article/2465204