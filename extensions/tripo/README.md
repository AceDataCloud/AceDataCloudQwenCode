# Tripo 3D

<img src="assets/icon.png" width="72" alt="Tripo 3D">

[简体中文](readme/README_zh_Hans.md)

Generate a 3D model from a prompt or reference images, texture or convert a model, and look up an existing task. Maintained by Ace Data Cloud for its API customers.

## Install

Install [uv](https://docs.astral.sh/uv/) so that `uvx` is on your PATH, then install this extension in Qwen Code:

```sh
qwen extensions install https://github.com/AceDataCloud/TripoQwenCode
```

Open [Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen) and configure `ACEDATACLOUD_TRIPO_TOKEN` in your operating system's environment for Qwen Code. Restart the client after setting the key. The extension passes it only to the Tripo 3D MCP subprocess. Keep it out of prompts and project files.

## First use

For a new 3D model, choose one prompt, one reference image, or ordered front/left/back/right views in `tripo_generate_model`. For multiple views, provide the front and at least one other image. To work with an existing model, choose `tripo_texture_model` or `tripo_convert_model`. Generation and texturing use credits; conversion can incur charges depending on its options. Save the task ID and call `tripo_get_task` to retrieve that same task. See [current pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen) before submitting work.

This extension runs [the pinned MCP package](https://pypi.org/project/mcp-tripo/2026.11.28.0/) locally over stdio. Its tools are `tripo_generate_model`, `tripo_texture_model`, `tripo_convert_model`, `tripo_get_task`, `tripo_get_tasks`.
