# Ace Data Cloud native extensions for Qwen Code

**Runtime blocker / 运行阻塞（2026-10-18）:** Qwen 0.25.2 stores the native sensitive setting but does not expand it into MCP HTTP Headers. Upstream confirmed: https://github.com/QwenLM/qwen-code/issues/14532 . These candidates are not yet ready for real authenticated media calls; install/discovery alone is not success. 原生敏感设置加载修复未发布前，不声称可鉴权调用。


Search by the service you need, and install only that extension. This is a supplementary source catalog, not an all-in-one plugin and not an official Qwen default marketplace. Each extension has its own source, sensitive credential prompt and review PR.

**Candidate catalog:** implementation is on `codex/native-qwen-extension`; default main is not a released catalog until review/merge. Package entries pin each candidate's immutable source commit. No generated media, paid results, official listing or user counts are claimed.

[简体中文](README_zh_Hans.md) · [Official Qwen source/discovery documentation](https://qwenlm.github.io/qwen-code-docs/en/users/extension/introduction/#managing-marketplace-sources)

## Add the source and discover a service

```bash
qwen extensions sources add https://raw.githubusercontent.com/AceDataCloud/AceDataCloudQwenCode/codex/native-qwen-extension/.claude-plugin/marketplace.json
qwen extensions sources list
```

Open Qwen and run `/extensions manage` → **Discover**. Search `suno`, `seedance`, `happyhorse`, `gpt image`, or `nano banana`, review the author **Ace Data Cloud** and selected service, then install that entry. Entries carry relevant service terms in names/descriptions rather than claiming search rankings or invented install counts. Some search UI builds match names/descriptions; keywords are supplementary metadata.

Use the direct JSON URL above. Each entry points to an HTTPS immutable native extension archive; this preserves the `qwen-extension.json` sensitive-settings flow. Installing the entire catalog as a Claude plugin would use a different converter and is not this path.

## Independent service packages

| Service | Independent source | Candidate implementation PR |
|---|---|---|
| Suno by Ace Data Cloud | [SunoQwenCode](https://github.com/AceDataCloud/SunoQwenCode/tree/e3fe407694b0b4ec28c6a63c0499de38d3701004) | https://github.com/AceDataCloud/SunoQwenCode/pull/1 |
| Seedance by Ace Data Cloud | [SeedanceQwenCode](https://github.com/AceDataCloud/SeedanceQwenCode/tree/35aea8ee419559dad3a431d9878840e916237e24) | https://github.com/AceDataCloud/SeedanceQwenCode/pull/1 |
| HappyHorse by Ace Data Cloud | [HappyHorseQwenCode](https://github.com/AceDataCloud/HappyHorseQwenCode/tree/98e7a524a81c76e0e1b7bedf9a43f6cc9f33ce53) | https://github.com/AceDataCloud/HappyHorseQwenCode/pull/1 |
| GPT Image by Ace Data Cloud | [GPTImageQwenCode](https://github.com/AceDataCloud/GPTImageQwenCode/tree/f65b7bd2cb40a5ce646a43547d0d509f844ce78e) | https://github.com/AceDataCloud/GPTImageQwenCode/pull/1 |
| Nano Banana by Ace Data Cloud | [NanoBananaQwenCode](https://github.com/AceDataCloud/NanoBananaQwenCode/tree/50df30f954d202f378741bf3ccaf171a2c4e0148) | https://github.com/AceDataCloud/NanoBananaQwenCode/pull/1 |

A direct package install is also possible with `qwen extensions install AceDataCloud/<Service>QwenCode --ref codex/native-qwen-extension` while the PR is open. See the selected package's English/Chinese README for the exact command. Do not replace this with the default-branch command before release.

## Register / API Token / first result

[Register or sign in → Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=qwencode_catalog_readme_api_key). Open **General application**, or initialize it, then copy or create a dedicated Token with the chosen service's permissions. Review [current prices and balance](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=qwencode_catalog_readme_pricing). Paste the raw Token into the native extension's hidden **Ace Data Cloud API Token** prompt; never into chat, exported manifests or command arguments.

![Actual Ace Key controls](_assets/tutorial/get-api-key-en.png)

![Create a dedicated key](_assets/tutorial/create-api-key-en.png)

Real shared Ace application UI screenshots, SunoDify source pinned 2026-10-07; reused 2026-10-18 with no visible real credentials. The service READMEs include exact steps, platform screenshots/reference boundaries and same-task status commands.

Media generation is metered separately from installing this free source. Only submit a generation after choosing the permitted model/inputs and authorizing cost. Save the returned task ID, query the same ID, and verify a terminal success plus usable returned media. Do not regenerate to poll, auto-switch models or claim a result from “Connected”. No paid end-to-end Qwen result has been validated here.

## Native LLM provider line

These are tool extensions, not a selectable built-in LLM provider. Ace native-provider admission is tracked in the independent Qwen report. Qwen's [contribution policy](https://github.com/QwenLM/qwen-code/blob/main/CONTRIBUTING.md#adding-a-provider-preset) treats a built-in preset as endorsement and requires a prior approved feature issue plus affiliation, operations/security transparency, organic demand and maintenance. Do not infer approval from this catalog.

## Removal and support

Uninstall only the service you no longer need through `/extensions manage`; remove this source with `qwen extensions sources remove ace-data-cloud-qwen-code`. Revoke its dedicated API Token separately in Ace Applications. No install automatically approves all business tools. Contact dev@acedata.cloud with task/trace ID, not a credential.
