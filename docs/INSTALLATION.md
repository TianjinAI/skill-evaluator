# Installation, updates and removal

## Install the complete folder

Use your agent's supported skill installation mechanism with:

**https://github.com/TianjinAI/skill-evaluator**

The repository root contains `SKILL.md`. Keep `references/`, `templates/`, and `scripts/` together; copying only SKILL.md loses important guidance. `agents/openai.yaml` is optional host-specific metadata; the core skill uses Markdown and does not require an OpenAI service.

For a host explicitly configured to discover the shared directory:

```sh
git clone https://github.com/TianjinAI/skill-evaluator ~/.agents/skills/skill-evaluator
```

This is an example location, not a universal path. If a same-named folder exists, inspect it first and preserve customizations. Do not overwrite it blindly.

## Versioned ZIP

Download the ZIP and matching `.sha256` file from [Releases](https://github.com/TianjinAI/skill-evaluator/releases). Extract the single `skill-evaluator` folder through your host's supported workflow. On systems with an SHA-256 utility, compare the ZIP's hash with the supplied value before extraction. Checksums establish file integrity against that release, not a security audit.

## WorkBuddy prompt

> 请通过你支持的技能安装方式，从 https://github.com/TianjinAI/skill-evaluator 安装完整的 skill-evaluator 目录。先检查是否有同名版本，保留自定义修改。完成后报告实际安装位置和能否读取 SKILL.md 及其 references。不要运行被评估候选的安装脚本。接着用这个技能对一个公开仓库做第一轮通用审查，不要自动安装候选技能。

WorkBuddy-specific UI, paths, discovery and execution have not been tested in this repository. Successful download is distinct from skill discovery and from a successful evaluation.

## Dependencies and permissions

The instructions need no package manager or API key. The optional initializer and local tests need Python 3.10+. The reviewer needs whichever repository/file access the task requires. Testing a candidate may need extra dependencies or permissions; that is decided per review. The skill does not install a background service, update itself or add telemetry.

The host agent and tools have their own data handling. Nothing in this package makes a cloud host offline or changes its permissions.

## Update deliberately

Read [CHANGELOG](../CHANGELOG.md) and preserve local modifications. For an unmodified Git checkout, fetch and review the diff before updating to the intended tag or branch. For ZIP installations, retain the previous folder until the replacement is discovered and usable. Re-run a representative request when instructions affecting your workflow change.

## Remove

Use your host's uninstall mechanism or remove only the installed skill folder after locating it. Keep any user-generated review records elsewhere. This package creates no global state; the optional initializer writes only to the destination supplied by the caller.
