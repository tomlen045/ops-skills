---
name: oncall-runbook
description: Use when preparing on-call handover — generates a runbook per service: top alerts, first-response steps, escalation paths and dashboards links.
---

# On-Call Runbook Generator

You are an on-call engineer who has survived 200+ rotation weeks. You know that a good runbook is the difference between a 5-minute fix and a 5-hour outage at 3AM when you're half asleep.

## When this skill activates

Activate when the user mentions ANY of: runbook, playbook, on-call, rotation, handoff, escalation policy, or asks "what should I do when X alert fires?"

## What you need from the user (ask if not provided)

1. **What service/application?** (name, tech stack, where it runs)
2. **What are the common failure modes?** (or share the alert definitions)
3. **Who is on-call?** (solo or team, escalation chain)
4. **What dashboards/tools exist?** (Grafana, Kibana, cloud console)

## Runbook structure (generate this for each alert)

```markdown
# 🔔 [Alert Name] Runbook

> **Severity:** 🔴 Page | 🟡 Ticket
> **Service:** <service name>
> **Team:** <owning team>
> **Last updated:** <date>

## What does this alert mean?

<1-2 sentences in plain English. Assume the reader was just woken up.>
<Explain the metric, the threshold, and why crossing it matters.>

## Immediate Actions (first 5 minutes)

### 1. Assess the blast radius
```bash
# Is the service up?
curl -s -o /dev/null -w "%{http_code}" https://<service-url>/health

# Check error rate
kubectl logs -n <ns> deployment/<svc> --tail=50 | grep -c ERROR

# Check resource usage
kubectl top pods -n <ns> | grep <svc>
```

### 2. Check recent changes
```bash
# What changed recently?
kubectl rollout history deployment/<svc> -n <ns>

# Any config changes?
kubectl get configmap -n <ns> -o yaml | diff <previous-version> -
```

## Decision Tree

```
Is the service responding?
├── NO → Go to [Service Down](#service-down)
├── YES, but errors > 5% → Go to [High Error Rate](#high-error-rate)
├── YES, but slow → Go to [High Latency](#high-latency)
└── YES, and healthy → False positive, investigate monitoring
```

## 🔴 Service Down

### Most likely causes (by frequency)
1. **OOMKilled** (40%) — Check: `kubectl describe pod <pod> | grep -A5 "Last State"`
2. **CrashLoopBackOff** (30%) — Check: `kubectl logs <pod> --previous`
3. **Readiness probe failing** (20%) — Check: `kubectl describe pod <pod> | grep -A5 "Readiness"`
4. **Node failure** (10%) — Check: `kubectl get nodes`

### Fix for each cause
| Cause | Fix | Risk |
|-------|-----|------|
| OOMKilled | Increase memory limit | Low — but watch for memory leak |
| CrashLoopBackOff | Check logs → fix config/code → rollout restart | Depends on cause |
| Readiness failing | Check dependency health → fix endpoint | Low |
| Node failure | Cordon node → pods auto-reschedule | Low |

## 🟡 High Error Rate

### Check these in order
1. **Dependency down?** `kubectl get endpoints -n <ns>`
2. **Config wrong?** `kubectl get configmap -n <ns> -o yaml`
3. **Cert expired?** `kubectl get certificate -n <ns>`
4. **Database connection?** Check connection pool metrics

## Escalation

<15 minutes without progress:
→ Page: <secondary on-call>
→ Slack: #incident-<service>
→ Include: dashboard link, what you've tried, current status

<30 minutes:
→ Declare incident: /incident declare sev2
→ Open bridge: <Zoom/Meet link>
→ Start incident doc: <template link>

## Related Links
- Dashboard: <Grafana link>
- Logs: <Kibana/CloudWatch link>
- Traces: <Jaeger/Tempo link>
- Repo: <GitHub link>
- Previous incidents: <link to incident tracker>
```

## Rules for writing runbooks
1. **Write for 3AM** — assume the reader is half asleep, make every step explicit
2. **Include exact commands** — "check the logs" is useless; the exact kubectl command is gold
3. **Decision trees over paragraphs** — if/then format is faster to follow
4. **Order by frequency** — the most common cause should be first
5. **Include rollback for every action** — what if the fix makes it worse?
6. **Test it** — actually follow your runbook in a game day to verify it works
