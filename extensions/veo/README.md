# Veo

<img src="assets/icon.png" width="72" alt="Veo">

[简体中文](readme/README_zh_Hans.md)

Create a Veo video from text or reference frames, then check the original task for the result. Maintained by Ace Data Cloud for its API customers.

## Install

Install [uv](https://docs.astral.sh/uv/) so that `uvx` is on your PATH, then use Qwen Code to install this extension:

```sh
qwen extensions install https://github.com/AceDataCloud/VeoQwenCode
```

Open [Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen) and configure `ACEDATACLOUD_VEO_TOKEN` in your operating system's environment for Qwen Code. Restart the client after setting the key. The extension passes it only to the Veo MCP subprocess. Keep it out of prompts and project files.

## First use

Ask Qwen to call `veo_list_models` to read the package's built-in model guide. It makes no generation request. For a video, select `veo_text_to_video` for a text prompt or `veo_image_to_video` for reference images. Generation uses paid credits. Check [current pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen) before submitting, retain the task ID, and use `veo_get_task` to check that same task until completion.

The extension runs [the pinned MCP package](https://pypi.org/project/mcp-veo/2026.11.27.0/) locally over stdio. Its six tools are `veo_list_models`, `veo_get_prompt_guide`, `veo_text_to_video`, `veo_image_to_video`, `veo_get_task`, `veo_get_tasks_batch`.
