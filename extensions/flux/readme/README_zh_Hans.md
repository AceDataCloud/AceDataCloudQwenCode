# FLUX

<img src="../assets/icon.png" width="72" alt="FLUX">

[English](../README.md)

使用 FLUX 生成或编辑图像、生成视频，并从原任务查询最终结果。 本扩展由 Ace Data Cloud 维护，连接你的 Ace 服务账户。

## 安装和配置

安装 [uv](https://docs.astral.sh/uv/)，确保 Qwen Code 的 PATH 中有 `uvx`。

```sh
qwen extensions install https://github.com/AceDataCloud/FluxQwenCode
```

从[应用管理](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen)获取具有 FLUX 权限的应用密钥，在运行 Qwen Code 的操作系统环境中设置 `ACEDATACLOUD_FLUX_TOKEN`，然后重启客户端。密钥只传给本扩展启动的 MCP 子进程，请勿写入项目文件或发送给模型。

## 使用

先调用 `flux_list_models` 读取包内模型说明。文生图使用 `flux_generate_image`，参考图编辑使用 `flux_edit_image`，视频生成使用 `flux_generate_video`。生成和编辑会消耗积分，保存任务 ID 后以 `flux_get_task` 查询。 提交前请检查[当前价格](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen)。

本地 stdio 服务使用固定版本 [`mcp-flux-pro==2026.11.27.0`](https://pypi.org/project/mcp-flux-pro/2026.11.27.0/)。
