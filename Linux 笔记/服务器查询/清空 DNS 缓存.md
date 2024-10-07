Postman 本身不提供直接清空 DNS 缓存的功能，因为 DNS 缓存通常存储在操作系统层面。但是，你可以通过操作系统提供的方法来清除 DNS 缓存。不同的操作系统有不同的命令来完成这个任务。

### 对于 Windows 用户：

1. **通过命令提示符**：
   打开命令提示符（以管理员身份），然后输入以下命令：
   ```cmd
   ipconfig /flushdns
   ```

2. **通过 PowerShell**（Windows 8 和更高版本）：
   打开 PowerShell（以管理员身份），然后输入以下命令：
   ```powershell
    Clear-DnsClientCache
    ```

### 对于 macOS 用户：

1. **通过终端**：
   打开终端应用程序，然后输入以下命令：
   ```bash
   sudo killall -HUP mDNSResponder
   ```

### 对于 Linux 用户：

1. **通过终端**：
   打开终端，然后根据你使用的 DNS 服务，输入不同的命令。对于大多数基于 Linux 的系统，可以使用：
   ```bash
   sudo systemctl restart nscd
   ```
   或者，对于使用 `systemd-resolved` 的系统：
   ```bash
   sudo systemd-resolve --flush-caches
   ```

### 注意事项：

- 在执行这些命令之前，确保你了解它们的作用，并且拥有相应的权限。
- 清空 DNS 缓存将移除所有已解析的 DNS 记录，这意味着在缓存被再次填充之前，你的系统可能需要更长时间来解析域名。
- 在某些情况下，重启计算机也可以清除 DNS 缓存。
- 如果你在公司网络或使用 VPN，可能需要与你的网络管理员联系，以了解正确的清除 DNS 缓存的方法。

清除 DNS 缓存后，Postman 将使用更新的 DNS 信息来发起请求。
