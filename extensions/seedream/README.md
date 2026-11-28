# Seedream

![Seedream](assets/icon.png)

Create or edit Seedream images through Ace Data Cloud and check the original task ID. Inspect supported models and sizes locally.

## Install

Install `uv` so `uvx` is on your PATH, then run:

```sh
qwen extensions install AceDataCloud/SeedreamQwenCode
```

Restart Qwen Code after adding your [Seedream application key](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen) to the process environment as `ACEDATACLOUD_SEEDREAM_TOKEN`. Use your operating system’s secret manager or shell configuration. Do not paste credentials into chat or commit them to a project. The extension sets `ACEDATACLOUD_API_TOKEN` only for the pinned MCP subprocess.

## First use

Use `seedream_list_models` to inspect the local package information. Image generation and editing consume credits. Keep the task ID returned by a submission. Use the task lookup on that same ID to retrieve its result; a pending job does not require another generation. [Service pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen)

Available native tools: `seedream_list_models`, `seedream_list_sizes`, `seedream_generate_image`, `seedream_edit_image`, `seedream_get_task`, `seedream_get_tasks_batch`.

[MCP package on PyPI](https://pypi.org/project/mcp-seedream-pro/2026.11.27.0/) · [MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.AceDataCloud%2Fmcp-seedream-pro/versions/latest)
