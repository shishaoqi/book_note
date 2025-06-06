###  创建调试的 launch.json 文件
点击视图左侧的 Run and Debug，点击创建launch.json文件。
```
{
	// Use IntelliSense to learn about possible attributes.
	// Hover to view descriptions of existing attributes.
	// For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Launch Package",
			"type": "go",
			"request": "launch",
			"mode": "auto",
			"program": "${fileDirname}"
		}
	]
}
```

若项目中有多个.go文件，打开任意一个.go文件都能进行断点调试，launch.json文件代码更新如下：（更改program）
```
{
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Launch Package",
			"type": "go",
			"request": "launch",
			"mode": "auto",
			"program": "${fileDirname}/${fileBasenameNoExtension}.go"
		}
	]
}
```


```json
{
	// 来自
	//http://www.randyfield.cn/post/2021-08-04-vscode-debug-golang
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Launch Package",
			"type": "go",
			"request": "launch",
			// "mode": "auto",
			"mode": "debug",
			"program": "${workspaceFolder}",
			"showGlobalVariables": false
		}
	]
}
```
**mode请更改为 `debug` ，如果为 `auto` 时，F5启动调试时：**
- 如果当前文件是单元测试，便会执行当前包中所有的单元测试文件，即mode切换至test
- 如果当前文件*.go, 才会执行main.go，即mode切换至debug