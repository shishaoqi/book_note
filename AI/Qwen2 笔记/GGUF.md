# GGUF

原文来自：https://qwen.readthedocs.io/zh-cn/latest/run_locally/llama.cpp.html


### 生成你的GGUF文件
我们在 [quantization/llama.cpp](https://qwen.readthedocs.io/zh-cn/latest/quantization/gguf.html) 中介绍了创建和量化GGUF文件的方法。您可以参考该文档获取更多信息。


通过llama.cpp，您不仅可以为自己的模型构建GGUF文件，还可以进行低比特量化操作。在GGUF格式下，您可以直接对模型进行量化而无需校准过程，或者为了获得更好的量化效果应用AWQ scale，亦或是结合校准数据使用imatrix工具。

#### https://qwen.readthedocs.io/zh-cn/latest/quantization/gguf.html 量化操作详细看这里