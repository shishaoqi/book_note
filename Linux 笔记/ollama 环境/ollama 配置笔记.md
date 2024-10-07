
### 增加GPU显存占用的模型层数
修改模型配置文件:  
用查看模型配置文件
```
ollama show llama3:8b --modelfile
```
创建新的模型配置文件,在其中加入PARAMETER num_gpu 5参数指定加载进GPU的层数
用新的配置文件创建模型:ollama create mymodel -f mymodel.modefile
运行新创建的模型,查看日志可以看到GPU层数变为了5层



