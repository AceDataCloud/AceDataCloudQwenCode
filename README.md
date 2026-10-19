# Ace Data Cloud native extensions for Qwen Code

**Runtime blocker / 运行阻塞（2026-10-18）:** Qwen 0.25.2 stores the native sensitive setting but does not expand it into MCP HTTP Headers or stdio environment references. Upstream confirmed: https://github.com/QwenLM/qwen-code/issues/14532 . These candidates are not yet ready for real authenticated media calls; install/discovery alone is not success. 原生敏感设置加载修复未发布前，不声称可鉴权调用。


Search by the service you need, and install only that extension. This is a supplementary source catalog, not an all-in-one plugin and not an official Qwen default marketplace. Each extension has its own source, sensitive credential prompt and review PR.

**Catalog source prerelease `0.1.0-rc.2`:** GPT Image now pins its independent RC2 dedicated five-tool stdio release; the other four services retain RC1 and their unchanged immutable commits. It is a user-added source, not an official Qwen default market or authenticated-media general-availability release. The runtime gate below remains in force.

[简体中文](README_zh_Hans.md) · [Official Qwen source/discovery documentation](https://qwenlm.github.io/qwen-code-docs/en/users/extension/introduction/#managing-marketplace-sources)

## Credential storage and verified platform boundary

**Wait for an official Qwen release containing [fix #14544](https://github.com/QwenLM/qwen-code/pull/14544) before using this extension with a real Token.** Qwen0.25.2 is the installation baseline, not a fixed authenticated-runtime version. No fixed release version has been verified yet.

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
| Suno by Ace Data Cloud | [SunoQwenCode](https://github.com/AceDataCloud/SunoQwenCode/tree/2a46582fd0bdec3ca3ab81b9037e399fa5a19c08) | https://github.com/AceDataCloud/SunoQwenCode/pull/1 |
| Seedance by Ace Data Cloud | [SeedanceQwenCode](https://github.com/AceDataCloud/SeedanceQwenCode/tree/edd900cde0d31b506f0ad300a0caf9350bb9358e) | https://github.com/AceDataCloud/SeedanceQwenCode/pull/1 |
| HappyHorse by Ace Data Cloud | [HappyHorseQwenCode](https://github.com/AceDataCloud/HappyHorseQwenCode/tree/36dfa83ba2dcf51ac2407f6773121ed37191ab5b) | https://github.com/AceDataCloud/HappyHorseQwenCode/pull/1 |
| GPT Image by Ace Data Cloud | [GPTImageQwenCode](https://github.com/AceDataCloud/GPTImageQwenCode/tree/dc18d2ddd2bb95da28ba49f2efe34e0ef836bee3) | https://github.com/AceDataCloud/GPTImageQwenCode/pull/2 |
| Nano Banana by Ace Data Cloud | [NanoBananaQwenCode](https://github.com/AceDataCloud/NanoBananaQwenCode/tree/eb29126040cb149b1d751242750fa19e446bb8f6) | https://github.com/AceDataCloud/NanoBananaQwenCode/pull/1 |

A normal direct install is `qwen extensions install AceDataCloud/<Service>QwenCode`; append `--ref v0.1.0-rc.2` for GPT Image or `--ref v0.1.0-rc.1` for the other four services. See each service README. On an unfixed official CLI, enter only a synthetic placeholder and do not invoke business tools.

GPT Image RC2 requires **uv/uvx and Python 3.10+** and launches the existing published `mcp-openai-pro==2026.10.19.5 --profile gpt-image`. Its five `gpt_image_*` tools exclude the general OpenAI and retired Sora surface; it does not fall back to the general hosted URL. See the pinned service README for setup. This does not remove the official fixed-Qwen prerequisite.

## Register / API Token / first result

[Register or sign in → Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=qwencode_catalog_readme_api_key). Open **General application**, or initialize it, then copy or create a dedicated Token with the chosen service's permissions. Review [current prices and balance](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=qwencode_catalog_readme_pricing). After a fixed official CLI is verified, paste the raw Token into the native extension's hidden **Ace Data Cloud API Token** prompt; never into chat, exported manifests or command arguments.

![Actual Ace Key controls](_assets/tutorial/get-api-key-en.png)

![Create a dedicated key](_assets/tutorial/create-api-key-en.png)

Real shared Ace application UI screenshots, SunoDify source pinned 2026-10-07; reused 2026-10-18 with no visible real credentials. The service READMEs include exact steps, platform screenshots/reference boundaries and same-task status commands.

Media generation is metered separately from installing this free source. Only submit a generation after choosing the permitted model/inputs and authorizing cost. Save the returned task ID, query the same ID, and verify a terminal success plus usable returned media. Do not regenerate to poll, auto-switch models or claim a result from “Connected”. No paid end-to-end Qwen result has been validated here.

## Native LLM provider line

These are tool extensions, not a selectable built-in LLM provider. Ace native-provider admission is tracked in the independent Qwen report. Qwen's [contribution policy](https://github.com/QwenLM/qwen-code/blob/main/CONTRIBUTING.md#adding-a-provider-preset) treats a built-in preset as endorsement and requires a prior approved feature issue plus affiliation, operations/security transparency, organic demand and maintenance. Do not infer approval from this catalog.

## Removal and support

Uninstall only the service you no longer need through `/extensions manage`; remove this source with `qwen extensions sources remove ace-data-cloud-qwen-code`. Revoke its dedicated API Token separately in Ace Applications. No install automatically approves all business tools. Contact dev@acedata.cloud with task/trace ID, not a credential.
