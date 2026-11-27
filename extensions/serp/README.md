# Google Search by Ace Data Cloud

![Google Search](assets/icon.png)

Search Google web, images, or news with Ace Data Cloud. Inspect supported search types locally before a billable lookup.

## Install

Install `uv` so `uvx` is on your PATH, then run:

```sh
qwen extensions install AceDataCloud/SerpQwenCode
```

Restart Qwen Code after adding your [Google Search application key](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen) to the process environment as `ACEDATACLOUD_SERP_TOKEN`. Use your operating system’s secret manager or shell configuration. Do not paste credentials into chat or commit them to a project. The extension sets `ACEDATACLOUD_API_TOKEN` only for the pinned MCP subprocess.

## First use

Use `serp_list_search_types` to inspect the local package information. Web, image, and news queries consume search credits. Use the supported search types and country/language tools to prepare a query, then send it once. [Service pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen)

Available native tools: `serp_list_search_types`, `serp_list_countries`, `serp_list_languages`, `serp_google_search`, `serp_google_images`, `serp_google_news`.

[MCP package on PyPI](https://pypi.org/project/mcp-serp/2026.11.27.1/) · [MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.AceDataCloud%2Fmcp-serp/versions/latest)
