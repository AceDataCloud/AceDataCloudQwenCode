# Ace Data Cloud native extensions for Qwen Code

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
| Suno by Ace Data Cloud | [SunoQwenCode](https://github.com/AceDataCloud/SunoQwenCode/tree/bae22af3b51b645917a414ca6831bb51ddb16d44) | https://github.com/AceDataCloud/SunoQwenCode/pull/1 |
| Seedance by Ace Data Cloud | [SeedanceQwenCode](https://github.com/AceDataCloud/SeedanceQwenCode/tree/3eab17d7f1c3b51702fe13384b7788aa8130e706) | https://github.com/AceDataCloud/SeedanceQwenCode/pull/1 |
| HappyHorse by Ace Data Cloud | [HappyHorseQwenCode](https://github.com/AceDataCloud/HappyHorseQwenCode/tree/2823c4b5c14980ce73daf27fe329b830c06a6cf3) | https://github.com/AceDataCloud/HappyHorseQwenCode/pull/1 |
| GPT Image by Ace Data Cloud | [GPTImageQwenCode](https://github.com/AceDataCloud/GPTImageQwenCode/tree/b980d2d015113a7c3ccf927432e96d90d3b9290b) | https://github.com/AceDataCloud/GPTImageQwenCode/pull/1 |
| Nano Banana by Ace Data Cloud | [NanoBananaQwenCode](https://github.com/AceDataCloud/NanoBananaQwenCode/tree/b0078614ac4e806b1cdfd2f75653960f2bae0e6d) | https://github.com/AceDataCloud/NanoBananaQwenCode/pull/1 |

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
