# 🛡 ops-skills

> **Make your AI coding assistant ops-smart.** 10 battle-tested skills that turn Claude Code / Cursor into a DevOps expert.

English | [简体中文](README.zh-CN.md)

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/tomlen045/ops-skills/main/install.sh)"
```

**One command. 10 skills. Zero configuration.**

## The Problem

AI coding assistants are great at writing React components and fixing TypeScript errors. But ask them to review a Kubernetes manifest for security issues, or guide you through a production incident, and they give you generic ChatGPT-level advice.

That's because they don't have **ops-specific context** — the checklists, the prioritization frameworks, the "don't do this or you'll wake up at 3AM" knowledge that senior SREs accumulate over years.

**ops-skills fixes this.** Each skill is a carefully crafted set of instructions that transforms your AI assistant from a generalist into an ops specialist.

## The 10 Skills

| Skill | What it does | When you need it |
|-------|-------------|-----------------|
| 🚨 **SRE Incident Commander** | Guides incident response with proper SEV triage, escalation, and structured troubleshooting | Production is down and you're panicking |
| ☸ **K8s Security Reviewer** | Reviews manifests against 15+ security checks (CIS, NSA guidelines) | Before deploying to production |
| 🔒 **Linux Security Hardener** | Server hardening with CIS benchmarks, includes rollback plans | Setting up a new server |
| 📊 **Prometheus Architect** | Generates alert rules that page when they should and don't when they shouldn't | Setting up monitoring |
| 🗺 **Infra Diagram Generator** | Reads Terraform/compose/K8s → generates Mermaid architecture diagrams | Documentation is stale (always) |
| 📝 **Postmortem Writer** | Structures incident reports with timeline, root cause, action items | After the fire is out |
| 🏗 **Terraform Guardian** | Reviews IaC for security, cost, and reliability issues | Before `terraform apply` |
| 🔍 **Log Detective** | Pattern-matches log output to identify root causes | Reading logs and going "???" |
| 🐳 **Docker Reviewer** | Reviews Dockerfiles for security, size, and production readiness | Before building images |
| 📖 **On-call Runbook Generator** | Generates decision-tree runbooks for each alert | Before going on-call |

## Installation

### One-liner (recommended)

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/tomlen045/ops-skills/main/install.sh)"
```

This interactive script detects whether you use Claude Code, Cursor, or both, and installs accordingly.

### Manual

**For Cursor users:** Download the combined `.cursorrules` file and place it in your project root.

**For Claude Code users:** Download `CLAUDE.md` and place it in your project root.

**For any LLM:** Download individual skill files from `skills/` and use them as system prompts.

### Just browsing?

Each skill is a standalone `.md` file in [`skills/`](skills/) — read them, copy them, remix them. They work as standalone prompts with any LLM.

## Why this works

Generic AI assistants give generic advice because they lack **domain-specific context**. Each skill in this pack includes:

- **Prioritized checklists** — what to check first, not just "check everything"
- **Structured output formats** — consistent severity/fvidence/fix format
- **Anti-patterns** — the "never do this" list that prevents 3AM pages
- **Exact commands** — not "check the logs" but the exact `kubectl` command with flags
- **Risk assessment** — every suggestion includes what could go wrong
- **Rollback plans** — because "undo" is important when you're in production

## Contributing

Got a skill that saved your production? PR it. Requirements:

1. Solves a real ops problem (not theoretical)
2. Structured format with severity levels
3. Includes exact commands (not vague instructions)
4. Has a "What NOT to do" section
5. Written in English

## License

MIT

---

<p align="center">Built by operators, for operators.<br>🔍 搜「小薅薅」看更多运维工具</p>

---

## 🫰 关注「小薅薅」· 每天发现一个宝藏工具

> **小薅薅** — 年轻人的赛博工具箱。每天为你发现一个好玩、实用、开源的小工具，帮你节省 1 小时探索时间。
>
> 📱 **微信搜索「小薅薅」** 或扫描下方二维码关注
>
> 后台回复关键词获取：
> - 回复 **「工具」** → 获取全部工具合集（离线可用）
> - 回复 **「运维」** → 获取运维/安全资源包
> - 回复 **「加群」** → 加入工具交流群

<div align="center">

| 🎯 更多作品 | 描述 | Stars |
|:---|:---|:---|
| [ops-doctor](https://github.com/tomlen045/ops-doctor) | 一条命令给Linux服务器做全套体检+健康分 | [⭐ 实用工具](https://github.com/tomlen045/ops-doctor) |
| [shellmbti](https://github.com/tomlen045/shellmbti) | 你的终端历史暴露了你是谁——Shell MBTI人格测试 | [⭐ 病毒传播](https://github.com/tomlen045/shellmbti) |
| [naicha-mbti](https://github.com/tomlen045/naicha-mbti) | 8道题测出你的奶茶人格，生成分享卡片 | [🧋 爆款](https://github.com/tomlen045/naicha-mbti) |
| [fafa-generator](https://github.com/tomlen045/fafa-generator) | 发疯文学生成器——一键生成发疯文案+卡片 | [🔥 热门](https://github.com/tomlen045/fafa-generator) |
| [life-progress](https://github.com/tomlen045/life-progress) | 人生进度条——把你的时间摆在眼前 | [⏳ 走心](https://github.com/tomlen045/life-progress) |

</div>

<div align="center">

**觉得有用？给个 ⭐ 让更多人看到 → [GitHub](https://github.com/tomlen045) | [Gitee](https://gitee.com/tomlen)**

</div>
