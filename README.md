# Ace Data Cloud native extensions for Qwen Code

Install any individual published entry using the full marketplace GitHub URL and extension name. For example, `qwen extensions install https://github.com/AceDataCloud/AceDataCloudQwenCode:google-search-by-ace-data-cloud`. Each catalog snapshot copies only the runtime files of the independently pinned release. `source-lock.json` records its commit and file hashes.

Qwen Code 0.28.7 shows the installation ID in its extension list. For example, the product **Suno** uses `suno-by-ace-data-cloud` for install, update and remove commands.


The full URL selects the vendor marketplace. In Qwen Code 0.28.7 the short `marketplace-name:extension` spelling can be parsed as an npm package. Marketplace conversion preserves the tools and the QWEN.md file. For the original native sensitive-settings UI in older service extensions, use their direct Git installation; the marketplace converter does not import native `settings` declarations.

## Kling and Veo video tools

Install either extension on its own. Start with the local model guide and check pricing before submitting a video.

| Product and setup guide | Install ID | Local model guide |
| --- | --- | --- |
| <img src="extensions/kling/assets/icon.png" width="28" alt=""> [Kling](https://github.com/AceDataCloud/KlingQwenCode/blob/8971d23e186de72d198afb8cbbcd5a6098c47c65/README.md) | `kling` | `kling_list_models` |
| <img src="extensions/veo/assets/icon.png" width="28" alt=""> [Veo](https://github.com/AceDataCloud/VeoQwenCode/blob/07861206ace0314af3ef5e73ea77bee7356868e4/README.md) | `veo` | `veo_list_models` |

## Search, image editing, and speech

These three native extensions start a pinned MCP package locally with `uvx`. Give each service its own application key as described in its linked repository. The first-use commands inspect local package information. Searches, image creation/editing, and speech synthesis incur charges when explicitly invoked.

| Service and source | Extension | Local first-use tool | Included tools |
| --- | --- | --- | --- |
| <img src="extensions/serp/assets/icon.png" width="28" alt=""> [Google Search](https://github.com/AceDataCloud/SerpQwenCode/tree/ab01b0bbdd1920d00b3aab693d9e203eb1a68e75) | `google-search-by-ace-data-cloud` | `serp_list_search_types` | 6 |
| <img src="extensions/seedream/assets/icon.png" width="28" alt=""> [Seedream](https://github.com/AceDataCloud/SeedreamQwenCode/tree/8ce06723fa88dad66050a8c274fd398300bdfcd3) | `seedream-by-ace-data-cloud` | `seedream_list_models` | 6 |
| <img src="extensions/fish/assets/icon.png" width="28" alt=""> [Fish Audio](https://github.com/AceDataCloud/FishAudioQwenCode/tree/d5b5c31ea735538940d105ff2f1f6fc7555465be) | `fish-audio-by-ace-data-cloud` | `fish_get_usage_guide` | 4 |

<img src="extensions/acemusic/_assets/icon.png" width="28" alt=""> ACE Music uses a process-environment token injected through your secret manager. Qwen Code 0.28.3 was verified to install the extension and attach that token to MCP initialization against a loopback receiver. The historical native *stored setting* limitation below applies to the older five packages. [ACE Music extension at its catalog revision](https://github.com/AceDataCloud/ACEMusicQwenCode/tree/607eaf57585f6c960152ede947e769ac4c8cfe1f)

**Runtime blocker / 运行阻塞（2026-10-18）:** Qwen 0.25.2 stores the native sensitive setting but does not expand it into MCP HTTP Headers or stdio environment references. Upstream confirmed: https://github.com/QwenLM/qwen-code/issues/14532 . These candidates are not yet ready for real authenticated media calls; install/discovery alone is not success. 原生敏感设置加载修复未发布前，不声称可鉴权调用。


Search by the service you need, and install only that extension. This is a supplementary source catalog, not an all-in-one plugin and not an official Qwen default marketplace. Each extension has its own source, sensitive credential prompt and review PR.

The five media extensions that use native credential settings remain prereleases. Each pinned service README links to its release and describes the current Qwen runtime requirement.

[简体中文](README_zh_Hans.md) · [Official Qwen source/discovery documentation](https://qwenlm.github.io/qwen-code-docs/en/users/extension/introduction/#managing-marketplace-sources)

## Credential storage and verified platform boundary

**Wait for an official Qwen release containing [fix #14544](https://github.com/QwenLM/qwen-code/pull/14544) before using one of these five stored-setting extensions with a real token.** Qwen0.25.2 is the installation baseline, not a fixed authenticated-runtime version. No fixed release version has been verified yet.

A [validation-only fork run](https://github.com/AceDataCloud/qwen-code/actions/runs/39109190158) built the owning core package at the exact fix candidate and exercised saved settings through Qwen's real MCP transport to localhost, without forcing a backend:

| Environment | Selected backend | Evidence |
|---|---|---|
| Windows Server2022 x64, Node22.23.3 | System credential store (`keychain` through keytar) | 26 checks PASS, including stored Token → extension Header → localhost initialize. This covers the hosted runner session, not every user's permission or lock state. |
| Linux x64, Node22.23.3 | Qwen's normal `encrypted_file` fallback | 25 checks PASS. The runner's system Secret Service was unavailable; this does not validate Linux Keychain. |
| macOS arm64, Node22.23.3 | Real system Keychain; follow-up 26 checks PASS | The original matrix failed at a workspace path alias. [Focused fix verification](https://github.com/AceDataCloud/qwen-code/actions/runs/39120588598) passes user/workspace/untrusted Header handshakes after canonical path identity. Fix candidate is now head6b5db858; it remains unreleased. The old matrix failure stays recorded. |

These additional Windows/Linux checks build core and use its real storage/manager/transport; they do not replace a full Windows/Linux interactive CLI test or prove a released fix. Existing macOS source-built CLI checks remain separately recorded.

The installer records the selected backend in `.qwen-extension-settings.json`; no need to copy or expose the secret bundle. Qwen can normally choose encrypted-file storage when the OS backend is unavailable; that is encrypted storage, not a plaintext Token fallback. A missing/unreadable selected store after installation is a failure, not permission to switch credentials silently. The fix candidate keeps the extension manageable and disables its MCP servers on an unreadable store. Check store availability and retry/reload first; do not uninstall for a transient lock or unavailable backend. Only after missing/corrupt settings are confirmed should you back up recoverable settings and consider reinstalling. Reinstall can preserve existing workspace overrides; review and rotate scoped settings through hidden input if needed. Do not export the Token globally, force a different backend, put it in manifests/arguments, unlock a keychain or change OS permissions to work around this candidate's blocker.

## Add the source and discover a service

```bash
qwen extensions sources add https://raw.githubusercontent.com/AceDataCloud/AceDataCloudQwenCode/main/.claude-plugin/marketplace.json
qwen extensions sources list
```

Open Qwen and run `/extensions manage` → **Discover**. Search `suno`, `seedance`, `happyhorse`, `gpt image`, or `nano banana`, review the author **Ace Data Cloud** and selected service, then install that entry. Entries carry relevant service terms in names/descriptions rather than claiming search rankings or invented install counts. Some search UI builds match names/descriptions; keywords are supplementary metadata.

Use the direct JSON URL above. Each entry points to an HTTPS immutable native extension archive; this preserves the `qwen-extension.json` sensitive-settings flow. Installing the entire catalog as a Claude plugin would use a different converter and is not this path.

## Independent service packages

| Service | Independent source | Merged source PR |
|---|---|---|
| <img src="extensions/suno/_assets/icon.jpg" width="28" alt=""> Suno | [SunoQwenCode](https://github.com/AceDataCloud/SunoQwenCode/tree/56ed1e4fa0976cb541d12439db2889835da2372f) | https://github.com/AceDataCloud/SunoQwenCode/pull/2 |
| <img src="extensions/seedance/_assets/icon.png" width="28" alt=""> Seedance | [SeedanceQwenCode](https://github.com/AceDataCloud/SeedanceQwenCode/tree/22bca001e0f768c0fb6e05ad530c20297841278e) | https://github.com/AceDataCloud/SeedanceQwenCode/pull/2 |
| <img src="extensions/happyhorse/_assets/icon.jpg" width="28" alt=""> HappyHorse | [HappyHorseQwenCode](https://github.com/AceDataCloud/HappyHorseQwenCode/tree/abdc9181206b1f0f9fb9b31499ec8a2a5a87354a) | https://github.com/AceDataCloud/HappyHorseQwenCode/pull/2 |
| <img src="extensions/gpt-image/_assets/icon.png" width="28" alt=""> GPT Image | [GPTImageQwenCode](https://github.com/AceDataCloud/GPTImageQwenCode/tree/4f7ebfbdd46379da85fe71eaccbd71770337d7fe) | https://github.com/AceDataCloud/GPTImageQwenCode/pull/3 |
| <img src="extensions/nano-banana/_assets/icon.jpg" width="28" alt=""> Nano Banana | [NanoBananaQwenCode](https://github.com/AceDataCloud/NanoBananaQwenCode/tree/e9a9f1e64c2a5b8c11bf2dc5fa02188ae1ee14fe) | https://github.com/AceDataCloud/NanoBananaQwenCode/pull/2 |

A normal direct install is `qwen extensions install AceDataCloud/<Service>QwenCode`; append `--ref <release-tag>` to install the pinned service version. On an unfixed official CLI, enter only a synthetic placeholder and do not invoke business tools.

GPT Image requires **uv/uvx and Python 3.10+** and launches the existing published `mcp-openai-pro==2026.10.19.5 --profile gpt-image`. Its five `gpt_image_*` tools exclude the general OpenAI and retired Sora surface; it does not fall back to the general hosted URL. See the pinned service README for setup. This does not remove the official fixed-Qwen prerequisite.

## Register / API Token / first result

[Register or sign in → Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen). Open **General application**, or initialize it, then copy or create a dedicated Token with the chosen service's permissions. Review [current prices and balance](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen). After a fixed official CLI is verified, paste the raw Token into the native extension's hidden **Ace Data Cloud API Token** prompt; never into chat, exported manifests or command arguments.

![Actual Ace Key controls](_assets/tutorial/get-api-key-en.png)

![Create a dedicated key](_assets/tutorial/create-api-key-en.png)

Real shared Ace application UI screenshots, SunoDify source pinned 2026-10-07; reused 2026-10-18 with no visible real credentials. The service READMEs include exact steps, platform screenshots/reference boundaries and same-task status commands.

Media generation is metered separately from installing this free source. Only submit a generation after choosing the permitted model/inputs and authorizing cost. Save the returned task ID, query the same ID, and verify a terminal success plus usable returned media. Do not regenerate to poll, auto-switch models or claim a result from “Connected”. No paid end-to-end Qwen result has been validated here.

## Native LLM provider line

These are tool extensions, not a selectable built-in LLM provider. Ace native-provider admission is tracked in the independent Qwen report. Qwen's [contribution policy](https://github.com/QwenLM/qwen-code/blob/main/CONTRIBUTING.md#adding-a-provider-preset) treats a built-in preset as endorsement and requires a prior approved feature issue plus affiliation, operations/security transparency, organic demand and maintenance. Do not infer approval from this catalog.

## Removal and support

Uninstall only the service you no longer need through `/extensions manage`; remove this source with `qwen extensions sources remove ace-data-cloud-qwen-code`. Revoke its dedicated API Token separately in Ace Applications. No install automatically approves all business tools. Contact dev@acedata.cloud with task/trace ID, not a credential.
