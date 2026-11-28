# Fish Audio

![Fish Audio](assets/icon.png)

Generate speech with Fish Audio through Ace Data Cloud and check an existing task. Read the local usage guide before synthesis.

## Install

Install `uv` so `uvx` is on your PATH, then run:

```sh
qwen extensions install AceDataCloud/FishAudioQwenCode
```

Restart Qwen Code after adding your [Fish Audio application key](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen) to the process environment as `ACEDATACLOUD_FISH_TOKEN`. Use your operating system’s secret manager or shell configuration. Do not paste credentials into chat or commit them to a project. The extension sets `ACEDATACLOUD_API_TOKEN` only for the pinned MCP subprocess.

## First use

Use `fish_get_usage_guide` to inspect the local package information. Speech synthesis consumes credits. Use a voice you have permission to use. Keep the returned task ID and use the same ID when checking progress. [Service pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen)

Available native tools: `fish_get_usage_guide`, `fish_generate_audio`, `fish_get_task`, `fish_get_tasks_batch`.

[MCP package on PyPI](https://pypi.org/project/mcp-fish/2026.11.27.0/) · [MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.AceDataCloud%2Fmcp-fish/versions/latest)
