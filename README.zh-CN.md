# 🛡 ops-skills

> **让你的 AI 编程助手变成运维专家。** 10 个实战级技能包，一行命令安装。

[English](README.md) | 简体中文

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/tomlen045/ops-skills/main/install.sh)"
```

**一行命令，10 个技能，零配置。**

## 解决什么问题

AI 编程助手写 React 组件很厉害，但你让它审查 Kubernetes 安全配置、或者带你走一遍生产故障排查流程？它只会给你 ChatGPT 级别的泛泛之谈。

因为它缺少**运维领域的专业上下文**——那些高级 SRE 花了好几年才积累的检查清单、优先级排序框架、以及"不这样做你凌晨三点会被叫起来"的血泪经验。

**ops-skills 补上了这个缺口。** 每个技能都是一组精心打磨的指令，把你的 AI 助手从通才变成运维专家。

## 10 个技能

| 技能 | 做什么 | 什么时候用 |
|------|--------|-----------|
| 🚨 **SRE 应急指挥官** | 带你走标准故障排查流程，含 SEV 定级、升级策略 | 生产挂了，你很慌 |
| ☸ **K8s 安全审查** | 15+ 项安全检查（CIS 基准、NSA 加固指南） | 部署到生产之前 |
| 🔒 **Linux 安全加固** | CIS 基准加固，每条建议含回滚方案 | 新服务器上线 |
| 📊 **Prometheus 架构师** | 生成该报警就报警、不该报警就闭嘴的告警规则 | 搭建监控系统 |
| 🗺 **架构图生成器** | 读 Terraform/compose/K8s → 生成 Mermaid 架构图 | 文档过期了（永远是） |
| 📝 **复盘文档写手** | 结构化故障报告：时间线、根因、行动项 | 火灭了之后写复盘 |
| 🏗 **Terraform 守护者** | 审查 IaC 安全、成本和可靠性问题 | `terraform apply` 之前 |
| 🔍 **日志侦探** | 从百万行日志里找到根因模式 | 盯着日志发呆的时候 |
| 🐳 **Docker 审查员** | Dockerfile 安全、体积、生产就绪审查 | 构建镜像之前 |
| 📖 **值班手册生成器** | 为每个告警生成决策树型值班手册 | 上值班之前 |

## 安装

### 一行命令（推荐）

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/tomlen045/ops-skills/main/install.sh)"
```

交互式脚本会检测你用的是 Claude Code 还是 Cursor，自动安装对应格式。

### 手动

**Cursor 用户：** 下载合并版 `.cursorrules` 文件，放到项目根目录。

**Claude Code 用户：** 下载 `CLAUDE.md` 文件，放到项目根目录。

**其他 LLM 用户：** 从 [`skills/`](skills/) 目录下载单个技能文件，作为系统提示词使用。

## 为什么有效

通用 AI 助手给泛泛建议，因为缺少**领域专业上下文**。这个技能包的每个文件都包含：

- **优先级排序的检查清单**——不是"检查一切"，是"先查这个"
- **结构化输出格式**——统一的严重度/证据/修复格式
- **反模式清单**——防止你凌晨三点被叫起来的"别这么做"清单
- **精确命令**——不是"看看日志"，是带参数的 `kubectl` 命令
- **风险评估**——每条建议都附带可能出什么问题
- **回滚方案**——因为在生产环境，"撤销"和"执行"同样重要

## 贡献

有一个救过你生产环境的技能？提 PR。要求：

1. 解决真实运维问题（不是理论上的）
2. 有结构化格式和严重度分级
3. 包含精确命令（不是模糊指令）
4. 有"不要做什么"部分
5. 用英文撰写

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
