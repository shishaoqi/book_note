# 在 Google Cloud Shell Editor 中浏览面向开发者的 Gemini Code Assist Standard 和 Enterprise

## [1. 简介](https://codelabs.developers.google.com/codelabs/cloud-developer-duetai?hl=zh-cn#0)

在本实验中，您将使用 Gemini Code Assist，它是 Google Cloud 中的一个 AI 赋能的协作工具。您将学习如何使用 Gemini Chat 和内嵌代码助理来生成代码、理解代码以及执行其他 AI 辅助编码任务。

## **实践内容…**

- 您将使用 Cloud Shell IDE 下载某个 Web 应用的现有代码模板。
- 您将使用 Cloud Shell IDE 中的 Gemini Chat 来询问有关 Google Cloud 的常见问题。
- 您将使用 Cloud Shell IDE 中的 Gemini Code Assist 内嵌代码助理来生成、总结和补全代码。

## **学习内容…**

- 如何使用 Gemini Code Assist 执行多项开发者任务，例如代码生成、代码补全和代码总结。
- 如何使用 Cloud Assist 了解 Google Cloud。

## **所需条件…**

- Chrome 网络浏览器
- Gmail 账号
- 启用了结算功能的 Cloud 项目
- 为您的 Cloud 项目启用了 Gemini Code Assist

本实验的适用对象为各种水平的开发者，包括新手。虽然示例应用使用的是 Python 语言，但您无需熟悉 Python 编程就能理解代码内容。我们的重点是==让开发者熟悉 Gemini Code Assist 的各项功能。==


## [2. 设置](https://codelabs.developers.google.com/codelabs/cloud-developer-duetai?hl=zh-cn#1)

本部分涵盖了开始此实验所需执行的所有操作。

## **在 Google Cloud 项目中启用 Cloud Assist**

我们现在将在 Google Cloud 项目中启用 Cloud Assist。请按下面给出的步骤操作：

1. 访问 [https://console.cloud.google.com](https://console.cloud.google.com/?hl=zh-cn)，并确保您已选择计划用于本实验的 Google Cloud 项目。点击右上角显示的“打开 Gemini”图标。

![28f084ec1e159938.png](https://codelabs.developers.google.com/static/codelabs/cloud-developer-duetai/img/28f084ec1e159938.png?hl=zh-cn)

2. Cloud Assist 聊天窗口会在控制台右侧打开。点击“启用”按钮，如下所示。如果您没有看到**启用**按钮，而是看到了聊天界面，可能是因为您已经为项目启用了 Cloud Assist，可以直接执行下一步。

![3d9ae68104b49a5b.png](https://codelabs.developers.google.com/static/codelabs/cloud-developer-duetai/img/3d9ae68104b49a5b.png?hl=zh-cn)

3. 启用 Cloud Assist 后，您可以向其发出一两条提示来测试一下。下方显示了几个查询示例，不过您可以尝试诸如 **`What is Cloud Run?`** 之类的查询

![27835a44c7b7f7c.png](https://codelabs.developers.google.com/static/codelabs/cloud-developer-duetai/img/27835a44c7b7f7c.png?hl=zh-cn)

Cloud Assist 会回答您的问题。您可以点击右上角的 ![f68286b2b2ea5c0a.png](https://codelabs.developers.google.com/static/codelabs/cloud-developer-duetai/img/f68286b2b2ea5c0a.png?hl=zh-cn) 图标关闭 Cloud Assist 聊天窗口。

## **在 Cloud Shell IDE 中启用 Gemini Code Assist**

在此 Codelab 的其余部分，我们将使用 Cloud Shell IDE，这是一个基于 [Code OSS](https://github.com/microsoft/vscode) 的全代管式开发环境。我们需要在 Cloud Shell IDE 中启用和配置 Code Assist，相关步骤如下所示：

1. 访问 [ide.cloud.google.com](http://ide.cloud.google.com/?hl=zh-cn)。IDE 可能需要一段时间才能显示，因此请耐心等待。
2. 如图所示，点击底部状态栏中的 **Cloud Code - 登录**按钮。按照说明对插件进行授权。如果您在状态栏中看到 **Cloud Code - no project**，请选择该选项，然后从项目列表中选择您打算使用的 Google Cloud 项目。

![609d1645201cc7a3.png](https://codelabs.developers.google.com/static/codelabs/cloud-developer-duetai/img/609d1645201cc7a3.png?hl=zh-cn)

3. 如图所示，点击右下角的 **Gemini** 按钮，然后再选择一次正确的 Google Cloud 项目。如果系统要求您启用 **Gemini for Google Cloud API**，请先执行此操作，然后再继续操作。
4. 选择 Google Cloud 项目后，请确保您能够在状态栏的 Cloud Code 状态消息中看到该项目，并且在状态栏右侧看到已启用 Code Assist，如下所示：

![365a09ae0c4b1ac6.png](https://codelabs.developers.google.com/static/codelabs/cloud-developer-duetai/img/365a09ae0c4b1ac6.png?hl=zh-cn)

Gemini Code Assist 已可供使用！

Gemini Code Assist 还适用于 [Visual Studio Code](https://code.visualstudio.com/) 或 [JetBrains IntelliJ](https://www.jetbrains.com/idea) 等本地 IDE。它也适用于 Google Cloud Workstations。此 Codelab 重点介绍 Cloud Shell IDE，以便让所有人使用相同的环境，但您也可以随意尝试自己喜欢的设置，并点击[此链接](https://cloud.google.com/gemini/docs/codeassist/use-in-ide?hl=zh-cn)了解详情。

**可选**：如果您在右下角的状态栏中没有看到 Gemini，则需要在 Cloud Code 中启用 Gemini。在执行此操作之前，请确保已在 IDE 中启用 Gemini，方法是前往 **Cloud Code 扩展程序 → 设置**，然后输入文本 **Gemini**，如下所示。确保选中此复选框。您应重新加载 IDE。这将在 Cloud Code 中启用 Gemini，并且 IDE 中会显示状态栏中的 Gemini 图标。

![3741f07b73a939c8.png](https://codelabs.developers.google.com/static/codelabs/cloud-developer-duetai/img/3741f07b73a939c8.png?hl=zh-cn)