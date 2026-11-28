# Kling

<img src="assets/icon.png" width="72" alt="Kling">

[简体中文](readme/README_zh_Hans.md)

Create a Kling video from text or an image and retrieve the finished clip using its task ID. Maintained by Ace Data Cloud for its API customers.

## Install

Install [uv](https://docs.astral.sh/uv/) so that `uvx` is on your PATH, then use Qwen Code to install this extension:

```sh
qwen extensions install https://github.com/AceDataCloud/KlingQwenCode
```

Open [Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen) and configure `ACEDATACLOUD_KLING_TOKEN` in your operating system's environment for Qwen Code. Restart the client after setting the key. The extension passes it only to the Kling MCP subprocess. Keep it out of prompts and project files.

## First use

Ask Qwen to call `kling_list_models` to read the package's built-in model guide. It makes no generation request. For a video, select `kling_generate_video` for a text prompt or `kling_generate_video_from_image` for reference images. Generation uses paid credits. Check [current pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen) before submitting, retain the task ID, and use `kling_get_task` to check that same task until completion.

The extension runs [the pinned MCP package](https://pypi.org/project/mcp-kling/2026.11.27.0/) locally over stdio. Its six tools are `kling_list_models`, `kling_list_actions`, `kling_generate_video`, `kling_generate_video_from_image`, `kling_get_task`, `kling_get_tasks_batch`.
