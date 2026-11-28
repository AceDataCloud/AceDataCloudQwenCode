# Veo

Use `veo_list_models` for the local model reference. For text or image generation, use the matching service tool only when the user requests it. Generation spends Ace Data Cloud credits. Return and retain the original task ID and use `veo_get_task` for follow-up. If credentials are missing, direct the user to [Applications](https://platform.acedata.cloud/console/applications?utm_source=qwen-code&utm_medium=referral&utm_campaign=evergreen) and [pricing](https://platform.acedata.cloud/models?utm_source=qwen-code&utm_medium=referral&utm_campaign=evergreen).

先用 `veo_list_models` 查看模型。用户要求生成时，再按文字或参考图选择对应工具，保存任务 ID；查询进度使用 `veo_get_task`。请用户在环境变量 `ACEDATACLOUD_VEO_TOKEN` 中配置密钥。
