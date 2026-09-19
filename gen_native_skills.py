#!/usr/bin/env python3
"""Generate native SKILL.md format (YAML frontmatter) from flat skill markdown files.
ops-skills v1.1: Claude Code / agent-native skills install support."""
import pathlib, re

ROOT = pathlib.Path("/Users/len/CodeBuddy/dx/ops-skills")
SRC = ROOT / "skills"
OUT = ROOT / "native"

# description = trigger contract. Frontmatter description drives auto-activation.
META = {
    "sre-incident-commander": "Use when production is down, an outage, 5xx errors, latency spike, error-rate alert, PagerDuty page, or any production incident — runs SEV triage, escalation and structured troubleshooting. Guides incident response like a senior SRE.",
    "k8s-security-reviewer": "Use before deploying Kubernetes manifests, or when reviewing YAML/Helm charts for security — 15+ checks against CIS and NSA hardening guidance.",
    "linux-security-hardener": "Use when hardening a new or existing Linux server — CIS benchmark checklist with rollback plans, SSH, firewall, kernel and service hardening.",
    "prometheus-architect": "Use when setting up monitoring, writing PromQL, or designing Prometheus/VictoriaMetrics alert rules that page when they should and stay quiet when they shouldn't.",
    "infra-diagram-gen": "Use when documentation is stale — reads Terraform, docker-compose or Kubernetes manifests and generates a Mermaid architecture diagram of the real infrastructure.",
    "postmortem-writer": "Use after an incident is resolved — writes a structured postmortem with timeline, root cause analysis, blast radius and action items; blameless format.",
    "terraform-guardian": "Use when reviewing or writing Terraform/IaC — catches security misconfigurations, state hazards, drift risks and cost surprises before apply.",
    "log-detective": "Use when debugging from logs — pattern recognition across app/system logs, error clustering, timeline reconstruction and root-cause hints.",
    "docker-reviewer": "Use when reviewing Dockerfiles or docker-compose files — image pinning, layer hygiene, secrets, root user, healthchecks and compose best practices.",
    "oncall-runbook": "Use when preparing on-call handover — generates a runbook per service: top alerts, first-response steps, escalation paths and dashboards links.",
}

ORDER = ["sre-incident-commander", "k8s-security-reviewer", "linux-security-hardener",
         "prometheus-architect", "infra-diagram-gen", "postmortem-writer",
         "terraform-guardian", "log-detective", "docker-reviewer", "oncall-runbook"]

count = 0
for name in ORDER:
    src = SRC / f"{name}.md"
    body = src.read_text(encoding="utf-8").strip()
    # strip leading H1 (frontmatter name replaces it visually, keep as heading anyway for context)
    m = re.match(r"^# (.+?)\n+", body)
    title = m.group(1) if m else name
    desc = META[name]
    dest_dir = OUT / name
    dest_dir.mkdir(parents=True, exist_ok=True)
    fm = (f"---\nname: {name}\n"
          f"description: {desc}\n"
          f"---\n\n# {title}\n\n")
    (dest_dir / "SKILL.md").write_text(fm + (body[m.end():] if m else body) + "\n", encoding="utf-8")
    count += 1
    print(f"native/{name}/SKILL.md  ({len(fm+body)} bytes)")

# sanity: validate frontmatter parses
ok = True
for d in sorted(OUT.iterdir()):
    t = (d / "SKILL.md").read_text(encoding="utf-8")
    if not t.startswith("---\n") or "name: " not in t.split("---")[1]:
        ok = False
        print(f"BAD frontmatter: {d}")
print(f"\n{count} skills generated, frontmatter {'OK' if ok else 'BROKEN'}")
