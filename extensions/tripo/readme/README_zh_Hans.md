# Tripo 3D

<img src="../assets/icon.png" width="72" alt="Tripo 3D">

[English](../README.md)

使用文字或参考图生成 3D 模型，为已有模型贴图、转换格式，并查询任务。 本扩展由 Ace Data Cloud 维护，连接你的 Ace 服务账户。

## 安装和配置

安装 [uv](https://docs.astral.sh/uv/)，确保 Qwen Code 的 PATH 中有 `uvx`。

```sh
qwen extensions install https://github.com/AceDataCloud/TripoQwenCode
```

从[应用管理](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen)获取具有 Tripo 3D 权限的应用密钥，在运行 Qwen Code 的操作系统环境中设置 `ACEDATACLOUD_TRIPO_TOKEN`，然后重启客户端。密钥只传给本扩展启动的 MCP 子进程，请勿写入项目文件或发送给模型。

## 使用

新建模型时使用 `tripo_generate_model`，在文字、单张参考图或按前/左/后/右排列的多视图中选择一种输入。多视图需要正面图和至少一个其他视角。已有模型可用 `tripo_texture_model` 贴图或 `tripo_convert_model` 转换格式。生成和贴图会消耗积分，转换费用取决于选项。保存任务 ID，再用 `tripo_get_task` 查询。 提交前请检查[当前价格](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen)。

本地 stdio 服务使用固定版本 [`mcp-tripo==2026.11.28.0`](https://pypi.org/project/mcp-tripo/2026.11.28.0/)。
