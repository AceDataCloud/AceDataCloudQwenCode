# Qwen Code：Ace 独立品牌扩展目录

**Runtime blocker / 运行阻塞（2026-10-18）:** Qwen 0.25.2 stores the native sensitive setting but does not expand it into MCP HTTP Headers. Upstream confirmed: https://github.com/QwenLM/qwen-code/issues/14532 . These candidates are not yet ready for real authenticated media calls; install/discovery alone is not success. 原生敏感设置加载修复未发布前，不声称可鉴权调用。


这里是补充搜索来源，不是合集插件，也不是 Qwen 默认官方市场。Suno、Seedance、HappyHorse、GPT Image、Nano Banana 各自独立安装；凭据、权限和服务互不混装。

候选目录在 `codex/native-qwen-extension` 分支待人审。以下命令添加目录来源后，可在 `/extensions manage` → Discover 搜品牌名，选择作者 Ace Data Cloud 并安装单项。包源码固定到不可变提交，尚未合并的默认 main 不算已发布。

```bash
qwen extensions sources add https://raw.githubusercontent.com/AceDataCloud/AceDataCloudQwenCode/codex/native-qwen-extension/.claude-plugin/marketplace.json
```

- **Suno**：[SunoQwenCode 中文教程](https://github.com/AceDataCloud/SunoQwenCode/blob/e3fe407694b0b4ec28c6a63c0499de38d3701004/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/SunoQwenCode/pull/1。
- **Seedance**：[SeedanceQwenCode 中文教程](https://github.com/AceDataCloud/SeedanceQwenCode/blob/35aea8ee419559dad3a431d9878840e916237e24/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/SeedanceQwenCode/pull/1。
- **HappyHorse**：[HappyHorseQwenCode 中文教程](https://github.com/AceDataCloud/HappyHorseQwenCode/blob/98e7a524a81c76e0e1b7bedf9a43f6cc9f33ce53/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/HappyHorseQwenCode/pull/1。
- **GPT Image**：[GPTImageQwenCode 中文教程](https://github.com/AceDataCloud/GPTImageQwenCode/blob/f65b7bd2cb40a5ce646a43547d0d509f844ce78e/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/GPTImageQwenCode/pull/1。
- **Nano Banana**：[NanoBananaQwenCode 中文教程](https://github.com/AceDataCloud/NanoBananaQwenCode/blob/50df30f954d202f378741bf3ccaf171a2c4e0148/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/NanoBananaQwenCode/pull/1。

注册/登录 [Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=qwencode_catalog_readme_api_key)，初始化或打开 **General application**，复制 API Key，或 Manage Keys → Create 创建独立 Token。核对服务权限、有效期、Allowed APIs、当前余额与价格；在 Qwen 扩展的 **Ace Data Cloud API Token** 隐藏提示框粘贴，不写进聊天或命令参数。

![真实应用页取 Key](_assets/tutorial/get-api-key-en.png)

![创建独立 Token](_assets/tutorial/create-api-key-en.png)

图来自 2026-10-07 固定 SunoDify 共用应用页教程，2026-10-18 复用；凭据已遮盖。各单服务教程另有 Qwen 历史原图改编，明确不是扩展设置的实拍；新图排队，不造假。

安装免费，模型对话与媒体操作按自己的应用计费。首次生成前选定模型、参数和预算并授权；保存 task_id，原 ID 查询直到终态成功且媒体可用，不因 pending 重新生成，不自动换模型。当前没有本批扩展的 Qwen 付费结果或营收数据。

这些工具扩展不等于内置 LLM 服务商；原生 Ace Provider 仍按 Qwen 官方背书准入另行申请。官方默认目录收录、正常公开安装、业务执行、终态账单、注册/付费分别验收，不能互相替代。
