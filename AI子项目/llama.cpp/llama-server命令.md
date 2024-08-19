```
./llama-server -m /llm_models/glm-4-9b-chat-GGUF/glm-4-9b-chat-IMat.Q3_K_S.gguf --color -p "[gMASK]<|system|>\n你是一个智能助手<|user|>\n你好<|assistant|>\n" -t 16 --keep -1 -c 1024 -b 1024 -n -1  -ngl 36  -i --port 8000

```



```
./llama-server -m /llm_models/glm-4-9b-chat-GGUF/glm-4-9b-chat-1m.Q3_K_S.gguf --color -p "[gMASK]<|system|>\n你是一个智能助手<|user|>\n你好<|assistant|>\n" -t 8 --keep -1  -n -1 -ngl 36  -i --port 8080 --host 0.0.0.0

```




如何使用 llama.cpp 启动一个大模型, 所启动的服务在后端运行, 并开放出端口供他人使用

model


如何让上面所启动的服务在后端运行,并且时时检测服务是否正常运行?

model

请详细说明下: 在Linux 环境下,使用系统守护进程的方法

model


./llama-server -m /llm_models/gemma-2-9b-GGUF/gemma-2-27b-it.Q4_K_S.gguf --color -p "<bos><start_of_turn>user
{你是一个智能的助手}<end_of_turn>
<start_of_turn>model
{好的，我会尽我所能解答您的问题}<end_of_turn>
<start_of_turn>user
{结合给予的资料，合理回答我的问题。如果给予的资料中没有与我的问题有关的信息，你就直接回答：抱歉，所给资料中没有相关信息，回答不了你的问题。}<end_of_turn>" -t 8 --keep -1 -ngl 36 -i --port 8080 --host 0.0.0.0