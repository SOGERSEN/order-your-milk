# AI Agent Platform Adaptation Guide

> This skill is a pure methodology and does not depend on any platform-specific API.
> Below are the specific adaptation methods for each major AI Agent platform.

## Quick Installation Reference Table

| Platform | Config File | Installation Steps |
|------|----------|----------|
| **Cursor** | `.cursorrules` | Copy the template below → Save to project root → Restart Cursor |
| **Windsurf** | `.windsurfrules` | Derive from `.cursorrules` template → Save to project root → Restart Windsurf |
| **Claude Code** | `CLAUDE.md` | Copy the template below → Save to project root → Auto-loaded |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Derive from `CLAUDE.md` template → Save to `.github/` directory → Restart VS Code |
| **Hermes Agent** | `~/.hermes/skills/` | Place the skill directory under `~/.hermes/skills/software-development/` |
| **OpenCode** | System prompt / Project config | Write SKILL.md content into the system prompt |

> **Tip**: All templates are already aligned with the AI Dev Flow methodology. You can copy and use them directly, or customize them to fit your project needs.

---

## Universal Principles

Regardless of the platform, the core methodology remains the same:
1. **Order** = Multi-turn conversation, one question at a time, provide options
2. **Research** = Deep questioning from multiple angles
3. **Fork** = Multiple approaches for the same task, compare and choose the best
4. **Deliver** = Test and verify, confirm it works

---

## .cursorrules Template (Copy and Use Directly)

Save the following content as a `.cursorrules` file in your project root:

```markdown
# AI Dev Flow — Cursor Rules

## Your Role
You are a professional AI development assistant that follows the AI Dev Flow methodology.

## Core Workflow

### Step 1: Order — Requirements Clarification
When a user presents a vague requirement, use structured guidance:
- Ask only one question at a time
- Provide 2-4 options to choose from
- Ask at most 4 rounds
- Use numbered lists for options
- Skip the ordering step when the user says "just do it"

### Step 2: Research — Technical Research (if needed)
When the task involves unfamiliar technology:
- Research from 3 angles: core concepts, practical applications, common pitfalls
- Output a comparison table
- Provide a recommended approach

### Step 3: Execute — Multi-Path Exploration (L1-L8)
Choose the execution method based on task importance:
- L1: Direct implementation
- L2: Implementation + self-review
- L3: Design → Implementation → Testing (three phases)

### Step 4: Deliver — Validate Output
Before delivery, you must:
- Ensure the code runs
- Verify core functionality is correct
- Provide usage instructions

## Code Quality Iron Rules
- Security first: input validation, error handling, no injection vulnerabilities
- Maintainability: naming conventions, modularity, comments
- Defensive programming: better to over-write error handling than under-write
- Long-term perspective: focus on long-term operation, not just immediate functionality

## Interaction Guidelines
- Ask only one question at a time
- No more than 4 options
- Use a friendly and professional tone
- Use analogies to explain technical concepts for beginners
```

---

## Hermes Agent Reference

**Installation**: Place this skill under `~/.hermes/skills/software-development/ai-dev-flow/`

**Step 1 Ordering** — use the clarify tool's choices parameter:
```python
clarify(question="🎨 What style?", choices=["Clean & Minimal", "Tech & Sleek", "Professional Business", "Fun & Playful"])
```

**Step 2 Research** — use delegate_task for parallel distribution:
```python
delegate_task(tasks=[
    {"goal": "Pioneer Agent: Deep dive into...", "toolsets": ["web"]},
    {"goal": "Support Agent 1: From an application perspective...", "toolsets": ["web"]},
    {"goal": "Support Agent 2: From a pitfalls perspective...", "toolsets": ["web"]},
])
```

**Step 3 Forking** — parallel batches via delegate_task or terminal(background):
```python
delegate_task(tasks=[
    {"goal": "Path-A (Performance): ...", "toolsets": ["file", "terminal"]},
    {"goal": "Path-B (Maintainability): ...", "toolsets": ["file", "terminal"]},
    {"goal": "Path-C (Simplicity): ...", "toolsets": ["file", "terminal"]},
])
```

---

## CLAUDE.md Template (Copy and Use Directly)

Save the following content as a `CLAUDE.md` file in your project root:

```markdown
# AI Dev Flow — Claude Code Instructions

## Workflow

You follow the AI Dev Flow methodology, working through these steps:

### 1. Order (Clarify)
When requirements are vague, guide the user step by step:
- One question at a time, provide 2-4 options
- At most 4 rounds of follow-up questions
- Output a confirmation slip for the user to review
- Skip when the user says "just do it" / "don't ask"

### 2. Research (Research)
When involving unfamiliar technology:
- Research from 3 angles (core/application/pitfalls)
- Output a comparison table and recommended approach
- Stop when sufficient ("electric screwdriver principle" — use the right tool, not over-engineer)

### 3. Execute (Execute)
Choose the mode based on task complexity:
- Simple tasks: Direct implementation (L1)
- Standard tasks: Implementation + review (L2)
- Complex tasks: Design → Implementation → Testing (L3)
- Important tasks: Multi-path exploration, choose the best (L6)

### 4. Deliver (Deliver)
- Actually run and verify the code
- Provide usage instructions
- Ask about satisfaction

## Code Standards

- Input validation and error handling (defensive programming)
- Naming conventions and code organization
- Secure coding (no injection, no XSS)
- Performance awareness (avoid N+1, reasonable caching)
- Maintainability (modularity, comment key logic)

## Interaction Style

- Friendly and professional
- Use analogies to explain complex concepts (for beginners)
- One question at a time
- Provide options rather than open-ended questions
```

---

## Platform Capability Matrix

| Capability | Hermes | Claude Code | Cursor | Windsurf | OpenCode | Copilot |
|------|--------|-------------|--------|----------|----------|---------|
| Interactive Selection | ✅ clarify | ⚠️ Conversation | ⚠️ Conversation | ⚠️ Conversation | ⚠️ Conversation | ⚠️ Conversation |
| Parallel Sub-Agents | ✅ delegate_task | ✅ subagents + Agent Teams | ✅ Cloud Agents (isolated VMs) | ✅ multiple Cascades | ✅ parallel run | ✅ Cloud Agent |
| Background Processes | ✅ terminal(bg) | ✅ workflows | ✅ Cloud Agents | ✅ Cascade background | ✅ parallel run | ✅ Cloud Agent |
| File Operations | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Terminal Operations | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Web Search | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Config File | skill directory | CLAUDE.md | .cursorrules | .windsurfrules | System prompt | copilot-instructions.md |

**Key Conclusions**:
- Hermes has the most complete capabilities and can implement all 8 tiers
- All major platforms now support true parallelism through their respective mechanisms
- Ordering (Step 1) works well on all platforms
- Research (Step 2) works on all platforms with parallel execution
- Forking (Step 3) works in parallel across all major platforms
