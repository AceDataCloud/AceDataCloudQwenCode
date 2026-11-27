# 在 Qwen Code 中使用 ACE Music

[English](../README.md)

此插件连接 [ACE Music MCP](https://platform.acedata.cloud/documents/mcp-acemusic)。可按描述或自定义歌词创作歌曲、上传参考音频、翻唱一条自己的音轨、融合两条不同的兼容音轨，并查询原任务。

## 安装

```sh
qwen extensions install AceDataCloud/ACEMusicQwenCode
```

通过密钥管理器将 `ACEDATACLOUD_ACEMUSIC_TOKEN` 注入 Qwen 进程的环境变量，并重启 Qwen。扩展从进程环境读取该变量，作为 HTTPS 请求头。使用 `/mcp` 检查连接。 在[应用管理](https://platform.acedata.cloud/console/applications)创建允许访问 ACE Music 的通用或服务 API Key。将原始 Key 提供给客户端的凭据配置，避免粘贴到对话或代码中。

先问“ACE Music 支持哪些模型和操作？”即可免费查看。输入主题或提供标题、歌词和风格可以创作歌曲，成功后交付两首候选。生成歌词与导入参考音频分别计费。保留返回的任务 ID，断线后查询同一任务；部分失败时可取回已完成的音轨。[服务价格](https://platform.acedata.cloud/services/acemusic) · [工具说明](https://platform.acedata.cloud/documents/mcp-acemusic)
