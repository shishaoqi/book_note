
Andrej Karpathy:  
+1 for "context engineering" over "prompt engineering".  
“上下文工程”优于“提示工程”+1。  
  
People associate prompts with short task descriptions you'd give an LLM in your day-to-day use. When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information for the next step. Science because doing this right involves task descriptions and explanations, few shot examples, RAG, related (possibly multimodal) data, tools, state and history, compacting... Too little or of the wrong form and the LLM doesn't have the right context for optimal performance. Too much or too irrelevant and the LLM costs might go up and performance might come down. Doing this well is highly non-trivial. And art because of the guiding intuition around LLM psychology of people spirits.  
人们会把提示与你在日常使用中为LLM提供的简短任务描述联系起来。在每一个工业级的 LLM 应用中，上下文工程都是一门精妙的艺术和科学，它需要用恰当的信息填充上下文窗口，以便下一步操作。之所以说是科学，是因为正确地做到这一点需要任务描述和解释、少量示例、RAG、相关（可能是多模态）数据、工具、状态和历史记录、压缩……如果信息太少或形式不对，LLM 就无法获得最佳性能所需的正确上下文。如果信息太多或太不相关，LLM 的成本可能会上升，而性能可能会下降。做好这件事绝非易事。之所以说是艺术，是因为 LLM 的心理学指导着人们的精神世界。  
  
On top of context engineering itself, an LLM app has to:  
- break up problems just right into control flows  
- pack the context windows just right  
- dispatch calls to LLMs of the right kind and capability  
- handle generation-verification UIUX flows  
- a lot more - guardrails, security, evals, parallelism, prefetching, ...  
除了上下文工程本身之外，LLM 应用程序还必须：  
- 将问题分解为控制流  
- 正确打包上下文窗口  
- 向合适类型和能力的 LLM 发出请求  
- 处理生成验证 UI/UX 流程  
- 更多 - 护栏、安全、评估、并行性、预取......  
  
So context engineering is just one small piece of an emerging thick layer of non-trivial software that coordinates individual LLM calls (and a lot more) into full LLM apps. The term "ChatGPT wrapper" is tired and really, really wrong.  
因此，上下文工程只是新兴的、重要的软件厚层中的一小部分，该软件厚层将单个 LLM 调用（以及更多）协调到完整的 LLM 应用程序中。“ChatGPT 包装器”这个术语已经过时了，而且非常非常错误。

https://x.com/karpathy/status/1937902205765607626