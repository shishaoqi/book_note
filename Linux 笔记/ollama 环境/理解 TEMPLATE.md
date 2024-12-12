`TEMPLATE` 在Ollama中定义了模型如何理解和格式化输入（prompt）和输出（response）。它是一个模板字符串，用于构建对话管理系统中的消息结构。下面是一个基本的`TEMPLATE`结构，以及如何正确书写它的指导：

### 基本结构

```plaintext
TEMPLATE """{{- if .Messages }}
{{- if or .System .Tools }}<|im_start|>system
{{- if .System }}
{{ .System }}
{{- end }}
{{- if .Tools }}
<tools>
{{- range .Tools }}
{"type": "function", "function": {{ .Function }}}
{{- end }}
</tools>
{{- end }}<|im_end|>
{{ end }}
{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 -}}
{{- if eq .Role "user" }}<|im_start|>user
{{ .Content }}<|im_end|>
{{ else if eq .Role "assistant" }}<|im_start|>assistant
{{ if .Content }}{{ .Content }}
{{- else if .ToolCalls }}<tool_call>
{{ range .ToolCalls }}{"name": "{{ .Function.Name }}", "arguments": {{ .Function.Arguments }}}
{{ end }}</tool_call>
{{- end }}{{ if not $last }}<|im_end|>{{ end }}
{{- else if eq .Role "tool" }}<|im_start|>user
<tool_response>
{{ .Content }}
</tool_response><|im_end|>
{{ end }}
{{- if and (ne .Role "assistant") $last }}<|im_start|>assistant
{{ end }}
{{- end }}
{{- else }}
{{- if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
{{ end }}{{ .Response }}{{ if .Response }}<|im_end|>{{ end }}"""
```

### 如何正确书写`TEMPLATE`

1. **理解模板语法**：
   - `{{ ... }}`：Go模板语法，用于条件判断和变量替换。
   - `<|im_start|>` 和 `<|im_end|>`：自定义的XML标签，用于标记消息的开始和结束。

2. **条件判断**：
   - `{{- if .Messages }}`：如果存在消息，则执行大括号内的代码块。
   - `{{- if or .System .Tools }}`：如果存在系统消息或工具，则执行大括号内的代码块。

3. **消息遍历**：
   - `{{- range $i, $_ := .Messages }}`：遍历所有消息，`$i`是当前消息的索引，`$_`是当前消息对象。
   - `{{- if eq .Role "user" }}`：如果消息的角色是用户，则按照用户消息格式化。

4. **工具调用**：
   - `<tool_call>`：用于包裹工具函数调用的JSON对象。
   - `{"name": <function-name>, "arguments": <args-json-object>}`：工具函数调用的格式。

5. **消息结束标记**：
   - `{{ if not $last }}<|im_end|>{{ end }}`：如果不是最后一条消息，则添加结束标记。

6. **系统和用户消息**：
   - `{{- if .System }}<|im_start|>system{{ .System }}<|im_end|>{{ end }}`：处理系统消息。
   - `{{ if .Prompt }}<|im_start|>user{{ .Prompt }}<|im_end|>{{ end }}`：处理用户提示。

7. **响应消息**：
   - `{{ .Response }}{{ if .Response }}<|im_end|>{{ end }}`：处理助手的响应消息。

### 注意事项

- 确保所有的开始和结束标签正确匹配，例如`<|im_start|>`和`<|im_end|>`。
- 确保使用正确的Go模板语法来处理条件和循环。
- 确保所有的工具函数调用都正确地格式化为JSON对象，并使用`<tool_call>`标签包裹。
- 测试`TEMPLATE`以确保它按照预期工作，特别是在处理不同的消息角色和工具调用时。

通过遵循这些指导原则，你可以正确地书写和理解Ollama中的`TEMPLATE`，从而有效地控制对话流程和消息格式化。
