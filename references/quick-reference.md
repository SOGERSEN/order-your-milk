# Order Your Milk — English Quick Reference

> **One-liner**: Give your AI Agent structured thinking ability — from vague ideas to high-quality delivery.

## Core Workflow

```
🧋 Clarify → 🔬 Research → ⚡ Execute → ✅ Deliver
```

### Step 1: Clarify (Requirements Elicitation)

- Ask ONE question at a time (max 4 rounds)
- Provide 2-4 options per question
- Output a confirmation sheet before execution
- Skip if user says "just do it" or provides detailed specs

**Default recommendations**: Functional / Clean minimal / Frontend-only / Single page / Responsive

### Step 2: Research (Deep Investigation)

- Three parallel angles: Core (pioneer), Application (auxiliary), Pitfalls (auxiliary)
- Stop when sufficient — "Electric Screwdriver Principle" (use it, don't study it)
- Depth levels: Shallow (3-5 rounds) / Medium (5-15) / Deep (15+)

### Step 3: Execute (Parallel Divergence)

8 execution levels for precise quality/cost control:

| Level | Name | Agents | Token | Use When |
|-------|------|--------|-------|----------|
| L1 | Solo | 1 | 1x | Simple tasks, quick prototype |
| L2 | Partner | 2 | 2x | Standard tasks, basic review |
| L3 | Team | 3 | 4x | Medium complexity, full pipeline |
| L4 | Audit | 4 | 6x | Important deliverables, security |
| L5 | Dual | 6 | 8x | High risk, uncertain approach |
| **L6** | **Triple** ⭐ | **9** | **12x** | **Highest quality (recommended)** |
| L7 | Cross | 9+3 | 16x | Safety-critical |
| L8 | Diamond 💎 | 9+4 | 20x | Only perfection accepted |

**Default recommendation**: L6 Triple — optimal balance of quality and cost.

### Step 4: Deliver (Verify & Output)

- Syntax check → Functional verification → Edge case testing → Actual run → Usage instructions
- ⚠️ Never skip actual execution! "Should work" ≠ "Works"

## Key Rules

| Rule | Description |
|------|-------------|
| One question at a time | Don't make users "take a test" |
| Confirm before execute | Wait for user to say "go" |
| Actually run the code | "Should work" is not enough |
| Electric Screwdriver | Use it, don't over-study it |
| Graceful degradation | If one path fails, use remaining results |

## Installation

**Hermes Agent**:
```bash
hermes skill install order-your-milk
```

**Claude Code**:
```bash
cp order-your-milk/CLAUDE-template.md ./CLAUDE.md
```

**Cursor**:
```bash
# Copy the .cursorrules template from references/platform-adapters.md
```

**Any Agent with system prompt**: Inject SKILL.md content as system prompt.

## What This Skill Does NOT Do

| Does NOT do | Why | Who does it |
|-------------|-----|-------------|
| Environment setup | Host Agent's capability | Host Agent |
| Deployment | Host Agent's capability | Host Agent |
| Debugging | Host Agent's capability | Host Agent |
| Technical docs | Specialized skill work | `code-quality-mastery` |
| Code review | Specialized skill work | `systematic-debugging` |

---

*This skill focuses on the **thinking layer**: requirements elicitation, technical research, solution comparison, quality assurance. Technical execution is delegated to the host Agent.*

## License

MIT License — free to use, modify, and distribute.
