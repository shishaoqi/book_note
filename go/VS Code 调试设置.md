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