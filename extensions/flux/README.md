# FLUX

<img src="assets/icon.png" width="72" alt="FLUX">

[简体中文](readme/README_zh_Hans.md)

Generate or edit FLUX images, create a FLUX video, and retrieve the original task result. Maintained by Ace Data Cloud for its API customers.

## Install

Install [uv](https://docs.astral.sh/uv/) so that `uvx` is on your PATH, then install this extension in Qwen Code:

```sh
qwen extensions install https://github.com/AceDataCloud/FluxQwenCode
```

Open [Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen) and configure `ACEDATACLOUD_FLUX_TOKEN` in your operating system's environment for Qwen Code. Restart the client after setting the key. The extension passes it only to the FLUX MCP subprocess. Keep it out of prompts and project files.

## First use

Call `flux_list_models` to read the package’s built-in model reference. For text-to-image use `flux_generate_image`; for an existing reference, use `flux_edit_image`. Use `flux_generate_video` when the user requests video. Generation and editing consume credits. Keep the task ID and use `flux_get_task` to check the original request. See [current pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen) before submitting work.

This extension runs [the pinned MCP package](https://pypi.org/project/mcp-flux-pro/2026.11.27.0/) locally over stdio. Its tools are `flux_list_models`, `flux_list_actions`, `flux_generate_image`, `flux_edit_image`, `flux_generate_video`, `flux_get_task`, `flux_get_tasks_batch`.
