# FLUX

Call `flux_list_models` to read the package’s built-in model reference. For text-to-image use `flux_generate_image`; for an existing reference, use `flux_edit_image`. Use `flux_generate_video` when the user requests video. Generation and editing consume credits. Keep the task ID and use `flux_get_task` to check the original request. For setup, use [Applications](https://platform.acedata.cloud/console/applications?utm_source=qwen-code&utm_medium=referral&utm_campaign=evergreen) and [pricing](https://platform.acedata.cloud/models?utm_source=qwen-code&utm_medium=referral&utm_campaign=evergreen). Only submit billable work on the user's request.

先调用 `flux_list_models` 读取包内模型说明。文生图使用 `flux_generate_image`，参考图编辑使用 `flux_edit_image`，视频生成使用 `flux_generate_video`。生成和编辑会消耗积分，保存任务 ID 后以 `flux_get_task` 查询。 请用户将密钥配置在系统环境变量 `ACEDATACLOUD_FLUX_TOKEN` 中。
