# 知识概念

### Prompt Templates -- 提示模板​
[提示模板--来自](https://python.langchain.com/v0.2/docs/tutorials/llm_chain/#prompt-templates)

我们将消息列表直接传递到语言模型中。这个消息列表从哪里来？通常，它是由用户输入和应用程序逻辑的组合构建的。此应用程序逻辑通常获取原始用户输入并将其转换为准备传递到语言模型的消息列表。常见的转换包括：1.添加系统消息 2.或使用用户输入`格式化`(得到最终的)模板。

`PromptTemplates` 是 LangChain 中的一个概念，旨在协助这种转换。它们接收原始用户输入并返回准备传递到语言模型的数据（即：提示）。

API 参考：[ChatPromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)