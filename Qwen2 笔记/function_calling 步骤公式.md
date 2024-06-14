# 实现一个 Function_Calling

### 共4步
1. send the conversation and available functions to the model


2. check if the model wanted to call a function


3. call the function


4. send the info for each function call and function response to the model


### 代码实现
LLM类提供了[函数调用](https://github.com/QwenLM/Qwen-Agent/blob/main/examples/function_calling.py)的支持。此外，一些Agent类如FnCallAgent和ReActChat也是基于函数调用功能构建的。

*  FnCallAgent 在 /qwen_agent/fncall_agent.py
*  ReActChat 在 /qwen_agent/react_chat.py