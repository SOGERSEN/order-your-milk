---
name: order-your-milk
description: "Order Your Milk — Structured AI development methodology. From vague ideas to high-quality delivery: Clarify → Research → Execute → Deliver."
version: "1.1.0"
author: SOGERSEN
license: MIT
tags: [workflow, requirements-elicitation, deep-research, multi-agent, parallel-execution, cross-platform]
triggers:
  - "I want to build"
  - "help me make"
  - "build a"
  - "create a"
  - "make a"
  - "I want to make"
  - "help me build"
  - "from scratch"
---

# Order Your Milk — From Vague Ideas to High-Quality Delivery

> **One-liner**: Give your AI Agent structured thinking ability. Not a code framework — a thinking methodology.

Every AI coding tool assumes you already know what you want. **This one guides you.** Structured option-based questions turn vague ideas into clear specs in 3 questions.

```
You: "I want to build a website"
AI:  "What type? Showcase / Functional / Tool?"
You: "Showcase"
AI:  "Style? Minimal / Techy / Business?"
You: "Minimal"
AI:  "🎨 Here's what you can personalize:
      ✅ Color theme    ☐ AI decides
      ☐ Animations      ✅ AI decides
      ☐ Layout          ✅ AI decides
      Which to customize? (or 'none')"
You: "Color theme"
AI:  "Colors? A. Warm tones  B. Cool tones  C. Monochrome  D. AI decides"
You: "Cool tones"
AI:  "🎚️ Effort level? L1 Quick / L2 Standard / L3 Thorough (recommended: L1)"
You: "L1"
AI:  "📋 Your order: Showcase, minimal, cool tones, L1. Start?"
You: "Go"
AI:  → ✨ Done!
```

---

## ⚡ How It Works

```
┌─────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  🧋     │     │  🔬      │     │  ⚡      │     │  ✅      │
│ CLARIFY │────▶│ RESEARCH │────▶│ EXECUTE  │────▶│ DELIVER  │
│ One Q   │     │ Triple   │     │ Multi-   │     │ Test &   │
│ at a    │     │ parallel │     │ path     │     │ verify   │
│ time    │     │ drilling │     │ diverge  │     │          │
└─────────┘     └──────────┘     └──────────┘     └──────────┘
```

**Use as needed** — skip any step. Clear requirements? Skip Clarify. Simple task? Use L1 directly.

---

## What Makes This Skill Special?

### 1. 🧋 Drink Shop Ordering — Structured Requirements Elicitation

Structured option-based guidance turns *"I want a website"* into a clear spec in 3 questions. One question at a time, max 4 rounds, then a confirmation sheet. No guesswork.

### 2. 🔬 Triple Parallel Research

Three agents drill simultaneously from different angles: **Pioneer** (core concepts), **Auxiliary 1** (real-world applications), **Auxiliary 2** (common pitfalls). With cavity detection and auto-bypass when one direction runs dry.

### 3. ⚡ Triple-Path Divergence — Diversity Injection

Same task, three paths, each optimizing for a **different target** (e.g. performance / maintainability / simplicity). Not repetition — systematic exploration of different solution spaces. Compare, pick the best, or fuse.

### 4. 🌍 Cross-Agent Universal

Pure methodology, no API dependencies. Works on any AI Agent with a system prompt — Hermes, Claude Code, Cursor, Windsurf, Copilot, OpenCode, or any other.

### 5. 🎚️ Eight-Level Execution System

From L1 Solo (1× token) to L8 Diamond (20× token), precisely control cost/quality based on task importance.

---

## Trigger Conditions

### When to Activate

- User describes a **deliverable** (website, app, script, system)
- Description is **vague** ("build a login page", "make a tool")
- Task involves **multiple dimensions** (tech stack, style, scope)
- User is **uncertain** what they want

### When NOT to Activate

- User says "just do it", "don't ask", "same as last time"
- Simple queries ("what time is it", "search for X")
- User already provided detailed specs
- Continuation of an ongoing task

---

## ⚡🔬 Dual Mode System

Two execution rhythms, auto-selected based on user signals:

| | ⚡ Fast Mode | 🔬 Deep Mode |
|:--|:--|:--|
| **Goal** | Working result ASAP | Highest quality delivery |
| **Clarify** | 1–2 core questions | Full 2–4 round ordering |
| **Research** | Quick scan (understand enough to execute) | Triple parallel drill |
| **Execute** | L1–L2 (single path) | L3–L8 (multi-path + coding principles) |
| **Verify** | Syntax + basic function | 5-round full validation |
| **Default** | ✅ When no clear signal | When user says "take your time" |

**Auto-select**: "quick", "demo", "prototype", "just make something" → ⚡ Fast. "important", "secure", "careful", "production" → 🔬 Deep. User can override anytime.

### 🔬 Deep Mode: Advanced Coding Principles

Deep Mode enforces **4 coding principles from Andrej Karpathy's [CLAUDE.md](https://github.com/anthropics/claude-code/blob/main/CLAUDE.md)** — proven to reduce LLM coding mistakes:

#### 1. Think Before Coding
**Don't assume. Don't hide confusion. Surface tradeoffs.**
- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.

#### 2. Simplicity First
**Minimum code that solves the problem. Nothing speculative.**
- No features beyond what was asked.
- No abstractions for single-use code.
- If you write 200 lines and it could be 50, rewrite it.
- Self-check: *"Would a senior engineer say this is overcomplicated?"*

#### 3. Surgical Changes
**Touch only what you must. Clean up only your own mess.**
- Don't "improve" adjacent code that isn't broken.
- Match existing style, even if you'd do it differently.
- Test: *Every changed line should trace to the user's request.*

#### 4. Goal-Driven Execution
**Define success criteria. Loop until verified.**
- Transform tasks into verifiable goals: "Add validation" → "Write tests for invalid inputs, then make them pass."
- For multi-step tasks, state a brief plan with verification checkpoints.
- Strong success criteria = independent work. Weak criteria = constant clarification.

These principles are injected into every divergence prompt — each Path (A/B/C) must follow them.

---

## Step 1: Clarify — Requirements Elicitation

> Turn vague ideas into clear specs. **Every order deserves customization — even simple ones.**

### Ordering Flow

```
User: "I want to build X"
         │
         ▼
   ┌──────────────────────────┐
   │  Phase A: Core Questions  │  ← 1-2 questions to understand the task
   │  "What type? What style?" │
   └────────────┬─────────────┘
                ▼
   ┌──────────────────────────┐
   │  Phase B: Customize Menu  │  ← "Here's what you can personalize:"
   │  ☑ Ball colors  ☐ Chart   │     Checked = user customizes
   │  ☐ Background   ☐ Layout  │     Unchecked = AI decides
   └────────────┬─────────────┘
                ▼
   ┌──────────────────────────┐
   │  Phase C: Detail Choices  │  ← Only for checked items (max 4 options each)
   │  "Rainbow / Single color?"│     Always include "Skip — AI decides"
   └────────────┬─────────────┘
                ▼
   ┌──────────────────────────┐
   │  Phase D: Effort Level    │  ← L1-L8, with smart recommendation
   │  "How much effort? L1-L8" │
   └────────────┬─────────────┘
                ▼
   ┌──────────────────────────┐
   │  Phase E: Confirmation    │  ← Summary of all choices + AI defaults
   │  "Confirm your order?"    │
   └──────────────────────────┘
```

**The metaphor**: We're running a drink shop. Every customer gets asked about their preferences — sweetness, ice, toppings. Not because they MUST choose, but because the CHOICE is part of the experience. And if they say "you decide" — great, we use our best recipe.

### Phase A: Core Questions (1-2 questions)

Ask the most important dimensions first. **One question at a time, using interactive UI.**

| Question | Options | When to Ask |
|:---------|:--------|:------------|
| Q1: What type? | Showcase / Functional / Tool / Custom | Always |
| Q2: What style? | Minimal / Techy / Business / Creative | Adapt to Q1 |
| Q3: What tech? | Pure frontend / With backend / You decide | If relevant |

### Phase B: Customization Menu

After core questions, **always** present a customization menu as **interactive checkboxes**:

```
🎨 Here's what you can personalize for your {project type}:

  ☑ Visual Style          ☐ AI decides
  ☑ Layout & Structure    ☐ AI decides
  ☐ Interaction Details   ☐ AI decides
  ☐ Data & Content        ☐ AI decides

  ✅ = I want to customize  |  ☐ = AI uses best judgment
```

**How to identify customizable aspects**:
- Think about what a user would NOTICE in the final output
- Group related options into ASPECTS (not individual settings)
- Typically 3-6 aspects per project
- Each aspect should be meaningful enough to matter

**Rules**:
- Always present the menu, even if user gave detailed specs
- Default: 1-2 aspects checked (the most impactful ones), rest AI decides
- User can check/uncheck any aspect
- User can say "none" → all AI decides
- User can say "all" → customize everything

### Phase C: Detail Choices (for checked aspects only)

For each checked aspect, present as **interactive clickable options**:

```
🎨 Ball Colors:
  [Rainbow]  [Single color]  [Gradient]  [AI decides]
```

**Rules**:
- Only ask for CHECKED aspects — skip unchecked ones entirely
- Max 4 options per aspect + "AI decides"
- One question at a time (never list all aspects as a test form)
- Options should be concrete and visual (colors, not "option A/B/C")

### Phase D: Effort Level Selection

**Always** let the user choose the effort level as **interactive selection**:

```
🎚️ How much effort should I put in?

  [L1 Quick]  [L2 Standard]  [L3 Thorough]  [L6 Maximum]

  Recommended for this task: L2
```

**Smart recommendation** based on task complexity:
- Single file, visual demo → recommend L1-L2
- Multi-file, functional app → recommend L2-L3
- Security/auth/payment → recommend L4-L6

**After level selection**:
- If user chose L3+: re-offer customization for unchecked items
  ```
  You chose L3 (Thorough). Want to customize any additional aspects
  before I start? [Yes, show me] [No, proceed]
  ```
- If user declines → proceed with AI defaults for unchecked items

### Phase E: Requirements Confirmation Sheet

Before executing, output a confirmation sheet showing **all choices + AI defaults**, with **[Confirm] [Modify]** buttons:

```
📋 Your Order:
┌──────────────────────────────────────┐
│ 🧋 Type: Physics Simulation          │
│                                      │
│ YOUR CHOICES:                        │
│  ✅ Ball colors: Rainbow gradient     │
│  ✅ Background: Dark space theme      │
│  ✅ Chart: Bell curve overlay         │
│                                      │
│ AI DECIDES (Chef's recipe):          │
│  🤖 Counter design: LED-style digits  │
│  🤖 Layout: Simulation on top,        │
│           chart below                │
│                                      │
│ ⚡ Effort: L2 Standard               │
│                                      │
│ Output: Single HTML file             │
└──────────────────────────────────────┘

[✅ Confirm & Start]  [✏️ Modify]
```

**Wait for user to confirm** or request changes.

### ⚠️ Interactive UI Rules (CRITICAL)

**Never ask users to type A/B/C/D.** Always use platform-native interactive elements:

| Platform | How to Present Options |
|:---------|:----------------------|
| **Feishu (Lark)** | Interactive card buttons — use Feishu card JSON with clickable buttons |
| **Hermes Agent** | `clarify()` tool with `choices` parameter — renders as clickable options |
| **OpenCode** | Native interactive selection — arrow keys + Enter |
| **Cursor / Windsurf** | Inline suggestions or numbered quick-pick |
| **CLI / Terminal** | Use readline/inquirer-style interactive prompts with arrow key navigation |

**The experience should feel like a drink shop touchscreen kiosk — tap your choice, not type it.**

If the platform genuinely has NO interactive capability, then and only then fall back to numbered options — but this should be the last resort.

### Handling Detailed Specs

When user provides a complete detailed spec (not just "build X"):

1. **Don't re-ask questions** — the spec already answers them
2. **Show understanding checklist** — summarize what you understood:

```
📋 I understand your requirements:

  1. Physics simulation: balls falling through nail grid
  2. Galton Board (bean machine) physics
  3. HTML5 Canvas, single file
  4. Balls accumulate to form bell curve
  5. Realistic physics with gravity and collision

  Is this correct? Anything to add or change?
```

3. **Then show customization menu** — even with detailed specs, there are always aspects to personalize
4. **Then show effort level** — let user choose L1-L8
5. **Then confirm** — final confirmation sheet

### Iron Rules

1. **One question at a time** — never dump all questions as a form
2. **Always show customization menu** — even for "simple" requests
3. **Always offer effort level** — user controls quality investment
4. **"AI decides" is always an option** — never force choices
5. **Wait for confirmation** — never start without user's "go"
6. **Use interactive UI** — clickable buttons, not text input (see Interactive UI Rules)

### Set Meals

For common scenarios, offer pre-built "meals" that skip customization:

```
🅰 Personal Showcase — minimal, single page (quick order)
🅱 Tool Widget — dark theme, interactive (quick order)
🅲 Dashboard — data visualization (quick order)
🅳 Full Custom — step by step with all choices
```

Full meal list: `references/set-meals.md` (16 meals across 3 tiers)

### Skip Shortcut

When user says "just do it" / "don't ask" → generate confirmation sheet with ALL AI defaults, still show it for approval. User can say "go" immediately or tweak specific items.

---

## Step 2: Research — Deep Investigation

> Build knowledge foundation before executing. Skip if domain is familiar.

### Cone Drilling Model

```
                🎯 Topic
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
  Pioneer Agent  Auxiliary 1  Auxiliary 2
  (drill deep)  (applications) (pitfalls)
       │           │           │
     Deeper      2-3 layer    2-3 layer
       │         depth gap    depth gap
       ▼           ▼           ▼
```

**Three angles, simultaneous**: core concepts + real-world use + common traps.

### Depth Control

| Depth | Rounds | When |
|-------|--------|------|
| Shallow | 3–5 | Quick understanding, learning to use |
| Medium | 5–15 | Solution design, tech selection |
| Deep | 15+ | Frontier research, algorithm innovation |

**"Electric Screwdriver Principle"**: We're here to USE it, not study its motor efficiency. Stop when you know enough.

### Cavity Detection

When one direction stalls (vague answers, "uncertain"):
1. **Side-step** — rephrase from a different angle
2. **Break down** — split big question into smaller ones
3. **Analogize** — "any mature solutions in related fields?"
4. **Mark & skip** — acknowledge the gap, continue elsewhere

### Research Output

```
📊 Research Report: {Topic}

Key Findings:
- Finding 1: ...
- Finding 2: ...

Solution Comparison:
| Solution | Pros | Cons | Rating |
|----------|------|------|--------|
| A        | ...  | ...  | ⭐⭐⭐   |
| B        | ...  | ...  | ⭐⭐⭐⭐  |

Common Pitfalls: ...
Recommendation: ...
```

Full research prompt templates: `references/research-prompts.md`
Domain-specific templates: `references/domain-research-prompts.md`

---

## Step 3: Diverge — Parallel Execution

> Same task, multiple paths. Pick the best result.

### Eight-Level System

| Level | Name | Agents | Cost | Use When |
|:-----:|:-----|:------:|:----:|:---------|
| **L1** | 🏃 Solo | 1 | 1× | Simple tasks, quick prototype |
| **L2** | 🤝 Partner | 2 | 2× | Standard tasks, basic review |
| **L3** | 👥 Team | 3 | 4× | Medium complexity, full pipeline |
| **L4** | 🔍 Audit | 4 | 6× | Important deliverables, security |
| **L5** | 🔀 Dual | 6 | 8× | High risk, uncertain approach |
| **L6** | ⭐ Triple | 9 | 12× | **Highest quality (recommended)** |
| **L7** | 🏆 Cross | 12 | 16× | Safety-critical |
| **L8** | 💎 Diamond | 13 | 20× | Only perfection accepted |

**Default: L6** — three paths exploring different optimization targets simultaneously.

### Smart Level Recommendation

| Task Characteristics | Recommended |
|:-----|:-----|
| Single file, clear specs, no security | L1 |
| Standard CRUD, known tech stack | L2 |
| Multi-module, multiple tech stacks | L3 |
| Payment/auth/security involved | L4 |
| Uncertain best approach | L5 |
| Important project, highest quality | L6 |

User can override: "use L3" or "keep it simple".

### Custom Optimization Targets

Default targets are **performance / maintainability / simplicity**, but adapt by project type:

| Project Type | Path A | Path B | Path C |
|:-------------|:-------|:-------|:-------|
| Web Frontend | Performance | Accessibility | Visual fidelity |
| Backend API | Latency | Security | Maintainability |
| Data Science | Accuracy | Interpretability | Speed |
| AI/LLM App | Response quality | Cost control | Latency |
| Security | Security | Compliance | Performance |

User can fully customize: "three paths should optimize X, Y, Z".

### Three-Track Divergence (L6)

```
              Task + Requirements Spec
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
    ┌─────────┐  ┌─────────┐  ┌─────────┐
    │ Path A   │  │ Path B   │  │ Path C   │
    │ Optimize: │  │ Optimize: │  │ Optimize: │
    │Performance│  │Maintain- │  │ Simplicity│
    │          │  │ ability  │  │          │
    │ Design→  │  │ Design→  │  │ Design→  │
    │ Build→   │  │ Build→   │  │ Build→   │
    │ Test     │  │ Test     │  │ Test     │
    └────┬─────┘  └────┬─────┘  └────┬─────┘
         └─────────────┼─────────────┘
                       ▼
              Compare & Pick Best
```

### Scoring Dimensions

| Dimension | Weight | Criteria |
|:----------|:------:|:---------|
| Correctness | 30% | Features complete, tests pass, edge cases handled |
| Code Quality | 25% | Readable, maintainable, well-named |
| Performance | 15% | Efficient runtime, reasonable resources |
| Security | 15% | Input validation, error handling, no vulnerabilities |
| Simplicity | 15% | Right-sized, no bloat |

### Failure Handling

| Scenario | Strategy |
|:---------|:---------|
| One path times out | Cancel it, compare remaining 2 |
| One path produces poor quality | Mark unusable, use remaining 2 |
| Two paths fail | Downgrade to L2 (single path + review) |
| All three fail | Check: wrong requirements? wrong tech route? |

---

## Step 4: Deliver — Verification & Output

> Ensure the output **works, is useful, and satisfies the user**.

### Pre-Delivery Checklist (Mandatory)

| Check | How | If Fails |
|:------|:----|:---------|
| Syntax correct | Run the code | Fix errors |
| Core functions | Actually use it | Fix functions |
| Edge cases | Empty, long, special chars | Add validation |
| Actually runnable | Run it once as described | Complete instructions |

**⚠️ Never skip actual execution.** "Should work" ≠ "Works."

### Delivery Format

```
✅ Done!

📁 File: xxx.html (at /path/to/xxx.html)

🚀 Usage:
  Double-click to open in browser
  Or: python xxx.py / node xxx.js

📋 Features:
  - Feature 1: ...
  - Feature 2: ...

💬 Satisfied? Anything to adjust?
```

### Post-Delivery

| User Says | Response |
|:----------|:---------|
| "Change this" (small fix) | Direct fix, don't re-run workflow |
| "Add X feature" (new feature) | Assess: quick fix or new cycle? |
| "Redo everything" | Full restart |
| "Great!" | Remember preferences, done |

---

## Pitfalls

### 🔴 Fatal (Must Avoid)

| Mistake | Consequence | Correct |
|:--------|:-----------|:--------|
| Ask 5 questions at once | User leaves | One question at a time |
| Skip ordering, build directly | Not what user wanted | Spend 1 min clarifying |
| Skip confirmation sheet | Misunderstood requirements | Wait for "go" |
| Deliver without running | Broken code | Actually run before delivering |
| Insist on ordering when user says "just do it" | Bad UX | Respect user, skip ordering |

### 🟡 Common (Watch Out)

| Mistake | Consequence | Correct |
|:--------|:-----------|:--------|
| Research exceeds 15 rounds | Diminishing returns | 5–15 rounds, stop when sufficient |
| Vague divergence targets | All 3 paths produce same thing | Force different optimization targets |
| Review says "looks good" | Misses issues | Must find 3 specific problems |
| Jargon with beginners | User intimidated | "Pure frontend" → "Double-click to open" |
| More than 4 options | Decision paralysis | Max 4 options, split if more |
| Skip customization menu | User misses personalization | ALWAYS show customize menu |
| Force user to choose everything | User frustrated | "AI decides" is always an option |
| Skip effort level selection | User has no control | ALWAYS offer L1-L8 |
| Ask user to type A/B/C/D | Bad UX, feels like a test | Use interactive clickable buttons |

### 🟢 Advanced

| Note | Detail |
|:-----|:-------|
| Metaphor choice | Use drink shop metaphor for first 3 rounds, then switch to professional language |
| Mode selection | No clear signal → default ⚡ Fast; user says "careful" → 🔬 Deep |
| Coding principles | 🔬 Deep Mode forces all 4 Karpathy principles; ⚡ Fast Mode uses standard quality |
| Platform adaptation | All major platforms support parallel sub-agents. See `references/platform-adapters.md` |

---

## Quick Reference

| Step | Action | Key Rule |
|:-----|:-------|:---------|
| 🧋 Clarify | Core Qs → Customize Menu → Detail Choices → Level → Confirm | Always offer customization |
| 🔬 Research | Triple parallel drill (core/app/pitfalls) | Electric Screwdriver — stop when sufficient |
| ⚡ Execute | L1–L8 multi-path, pick best | Force different optimization targets |
| ✅ Deliver | Syntax → Function → Edge → Actually run | Never skip actual execution |

**Dual Mode**: ⚡ Fast = quick scan + L1-L2. 🔬 Deep = full research + L3-L8 + Karpathy's 4 principles.

**Coding Principles**: Think Before Coding · Simplicity First · Surgical Changes · Goal-Driven Execution

**6 Iron Rules**: One Q at a time · Always show customize menu · Always offer L1-L8 · "AI decides" always OK · Wait for "go" · Use interactive UI

---

## What This Skill Does NOT Do

| Does NOT do | Who does it |
|:------------|:------------|
| Environment setup (install Node, configure DB) | Host Agent |
| Deployment (push to server, configure domain) | Host Agent |
| Debugging (read errors, fix bugs) | Host Agent |
| Detailed technical documentation | Specialized skill (`code-quality-mastery`) |
| Code review | Specialized skill (`systematic-debugging`) |

**This skill focuses on the thinking layer**: requirements elicitation, technical research, solution comparison, quality assurance. Technical execution is delegated to the host Agent.

---

## File Structure

```
order-your-milk/
├── SKILL.md                          ← This file (core methodology)
├── README_EN.md                      ← English README
├── README_CN.md                      ← Chinese README
└── references/
    ├── set-meals.md                  ← 16 preset meals
    ├── domain-templates.md           ← 12 domain templates
    ├── research-prompts.md           ← General research prompts
    ├── domain-research-prompts.md    ← Domain-specific prompts
    ├── platform-adapters.md          ← Platform config templates
    └── conversation-examples.md      ← Complete conversation examples
```

---

## License

MIT License — free to use, modify, and distribute.
