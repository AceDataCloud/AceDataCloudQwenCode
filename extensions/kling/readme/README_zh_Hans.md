# Kling

<img src="../assets/icon.png" width="72" alt="Kling">

[English](../README.md)

用 Kling 将文字或参考图生成视频，并通过原任务 ID 查询结果。 本扩展由 Ace Data Cloud 维护，连接你的 Ace 服务账户。

## 安装和配置

安装 [uv](https://docs.astral.sh/uv/)，确保 Qwen Code 的 PATH 中有 `uvx`。

```sh
qwen extensions install https://github.com/AceDataCloud/KlingQwenCode
```

从[应用管理](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen)获取具有 Kling 权限的应用密钥，在运行 Qwen Code 的操作系统环境中设置 `ACEDATACLOUD_KLING_TOKEN`，然后重启客户端。密钥只传给本扩展启动的 MCP 子进程，请勿写入项目文件或发送给模型。

## 使用

先调用 `kling_list_models` 查看包内的模型说明。文生视频使用 `kling_generate_video`，参考图生成使用 `kling_generate_video_from_image`。视频生成会消耗积分，请先核对[当前价格](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen)。保存生成返回的任务 ID，之后调用 `kling_get_task` 查询同一任务。

本地 stdio 服务使用固定版本 [`mcp-kling==2026.11.27.0`](https://pypi.org/project/mcp-kling/2026.11.27.0/)。
