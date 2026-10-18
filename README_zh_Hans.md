# Qwen Code：Ace 独立品牌扩展目录

**Runtime blocker / 运行阻塞（2026-10-18）:** Qwen 0.25.2 stores the native sensitive setting but does not expand it into MCP HTTP Headers. Upstream confirmed: https://github.com/QwenLM/qwen-code/issues/14532 . These candidates are not yet ready for real authenticated media calls; install/discovery alone is not success. 原生敏感设置加载修复未发布前，不声称可鉴权调用。


这里是补充搜索来源，不是合集插件，也不是 Qwen 默认官方市场。Suno、Seedance、HappyHorse、GPT Image、Nano Banana 各自独立安装；凭据、权限和服务互不混装。

候选目录在 `codex/native-qwen-extension` 分支待人审。以下命令添加目录来源后，可在 `/extensions manage` → Discover 搜品牌名，选择作者 Ace Data Cloud 并安装单项。包源码固定到不可变提交，尚未合并的默认 main 不算已发布。

```bash
qwen extensions sources add https://raw.githubusercontent.com/AceDataCloud/AceDataCloudQwenCode/codex/native-qwen-extension/.claude-plugin/marketplace.json
```

- **Suno**：[SunoQwenCode 中文教程](https://github.com/AceDataCloud/SunoQwenCode/blob/2d5b084937c2be7344e325df8c5a80e9a21a2cff/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/SunoQwenCode/pull/1。
- **Seedance**：[SeedanceQwenCode 中文教程](https://github.com/AceDataCloud/SeedanceQwenCode/blob/8967fdf2d8f2e6724dab67ead29600b95da11ae9/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/SeedanceQwenCode/pull/1。
- **HappyHorse**：[HappyHorseQwenCode 中文教程](https://github.com/AceDataCloud/HappyHorseQwenCode/blob/6c87e9ef45c9e44a40b4b7bc30914ee7d71ee9bf/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/HappyHorseQwenCode/pull/1。
- **GPT Image**：[GPTImageQwenCode 中文教程](https://github.com/AceDataCloud/GPTImageQwenCode/blob/d68886220eae08382b0d82101a06ccf6e3683de8/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/GPTImageQwenCode/pull/1。
- **Nano Banana**：[NanoBananaQwenCode 中文教程](https://github.com/AceDataCloud/NanoBananaQwenCode/blob/70dde33acea66805e16ee52dfbe562eb0251bb78/readme/README_zh_Hans.md)，实现 PR https://github.com/AceDataCloud/NanoBananaQwenCode/pull/1。

注册/登录 [Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=qwencode_catalog_readme_api_key)，初始化或打开 **General application**，复制 API Key，或 Manage Keys → Create 创建独立 Token。核对服务权限、有效期、Allowed APIs、当前余额与价格；在 Qwen 扩展的 **Ace Data Cloud API Token** 隐藏提示框粘贴，不写进聊天或命令参数。

![真实应用页取 Key](_assets/tutorial/get-api-key-en.png)

![创建独立 Token](_assets/tutorial/create-api-key-en.png)

图来自 2026-10-07 固定 SunoDify 共用应用页教程，2026-10-18 复用；凭据已遮盖。各单服务教程另有 Qwen 历史原图改编，明确不是扩展设置的实拍；新图排队，不造假。

安装免费，模型对话与媒体操作按自己的应用计费。首次生成前选定模型、参数和预算并授权；保存 task_id，原 ID 查询直到终态成功且媒体可用，不因 pending 重新生成，不自动换模型。当前没有本批扩展的 Qwen 付费结果或营收数据。

这些工具扩展不等于内置 LLM 服务商；原生 Ace Provider 仍按 Qwen 官方背书准入另行申请。官方默认目录收录、正常公开安装、业务执行、终态账单、注册/付费分别验收，不能互相替代。

## 凭据存储与已验证平台边界

**真实 Token 使用必须等待包含[修复 #14544](https://github.com/QwenLM/qwen-code/pull/14544) 的官方 Qwen 版本发布并复验。** 0.25.2 只是安装基线，不是鉴权已修复版本；目前没有已核验的修复发行版。

[独立 fork 验证](https://github.com/AceDataCloud/qwen-code/actions/runs/39109190158)对同一修复候选构建 core，通过真实密钥存储、扩展加载器和 MCP transport 向 localhost 初始化，没有强制切换存储后端：

| 环境 | 实际选择的后端 | 验证结果 |
|---|---|---|
| Windows Server2022 x64，Node22.23.3 | keytar 系统凭据存储（`keychain`） | 26 项通过，含保存设置→Header→localhost 初始化；仅覆盖该托管会话，不覆盖所有用户权限/锁定状态。 |
| Linux x64，Node22.23.3 | Qwen 正常选择的 `encrypted_file` 加密文件后备 | 25 项通过；runner 系统 Secret Service 不可用，不能声称 Linux Keychain 已验。 |
| macOS | 平台补验处理中 | 既有本地 macOS x64 完整 CLI 验证只覆盖隔离加密文件后端；本地缺少 native keytar binding，不能证明 macOS Keychain。 |

本轮 Windows/Linux 补验构建 core 并使用真实存储/加载器/transport，不等于这两个平台完整交互 CLI 或已发布版本验收；既有 macOS 源码构建 CLI 证据单列。

安装器在 `.qwen-extension-settings.json` 记录后端，不需复制或展示密钥 bundle。系统后端不可用时，Qwen 原有机制可以选择加密文件，它不是明文 Token 后备。安装后既定存储缺失/不可读应视为故障，不能静默换凭据；修复候选会保留管理入口、禁用 MCP 并提示卸载重装。重装可能保留既有 workspace override，需要时通过隐藏输入核查/轮换相应 scope。不要全局导出 Token、强制换后端、写入 manifest/参数，或解锁 Keychain/修改 OS 权限来绕过候选阻塞。
