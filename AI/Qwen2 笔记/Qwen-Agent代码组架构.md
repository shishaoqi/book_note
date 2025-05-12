# 框架

### 组件
框架提供了大模型（LLM，继承自class BaseChatModel，并提供了Function Calling功能）和工具（Tool，继承自class BaseTool）等原子组件，也提供了智能体（Agent）等高级抽象组件（继承自class Agent）。

* LLM，继承自 class BaseChatModel
* Tool，继承自 class BaseTool
* 智能体（Agent），继承自 class Agent

### 代码对应文件
LLM类提供了[函数调用](https://github.com/QwenLM/Qwen-Agent/blob/main/examples/function_calling.py)的支持。此外，一些 `Agent` 类如 `FnCallAgent` 和 `ReActChat` 也是基于函数调用功能构建的。

*  FnCallAgent 在 /qwen_agent/fncall_agent.py
*  ReActChat 在 /qwen_agent/react_chat.py


### 代码细节与结构

/qwen_agent/agents 下有：aritcle_agent/fncall_agent/user_agent 都继承自 Agent 类（/qwen_agent/agent.py）