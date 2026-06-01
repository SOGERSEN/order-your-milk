---
name: order-your-milk
description: "Order Your Milk — Structured AI development workflow. A four-step methodology from fuzzy idea to high-quality delivery: Requirements Elicitation (Order) → Deep Research (Investigate) → Parallel Execution (Diverge) → Verified Delivery. Works on any AI Agent platform."
version: "1.0.0"
author: SOGERSEN
license: MIT
tags: [workflow, requirements-elicitation, deep-research, multi-agent, parallel-execution, beginner-friendly, cross-platform]
triggers:
  - "I want to build"
  - "help me make"
  - "build a"
  - "create a"
  - "make a"
  - "develop a"
  - "I'd like to create"
  - "help me build"
  - "from scratch"
---

# Order Your Milk — From Fuzzy Idea to High-Quality Delivery

> **One-liner**: Give your AI Agent the structured thinking ability to go from a fuzzy idea to a high-quality delivery.

## Why Do You Need This Skill?

**Every AI coding tool on the market is missing one critical ability: helping you go from a vague idea to concrete requirements.**

| Tool | Approach | What's Missing |
|------|----------|----------------|
| ChatGPT/Claude | You say anything, I build anything | No structured guidance — output often misses the mark |
| Bolt.new/Lovable | You describe, I generate | No requirements clarification — beginners don't know what to describe |
| Cursor/Windsurf | You write code, I assist | Assumes you already know what you want |
| **With this skill installed** | **Step-by-step guidance to clarify requirements, then multi-solution selection** | **Nothing missing** |

**This is not a code framework — it's a thinking methodology.** It works when installed on any AI Agent.

---

## Quick Demo

```
User: "I want to build a website"
  ↓
Agent (Order): "What type? Showcase / Functional / Tool?"
User: "Showcase"
Agent (Order): "What style? Minimal / Tech-cool / Business?"
User: "Minimal"
Agent (Order): "📋 Confirmed: single-page showcase site, minimal style, pure frontend, double-click to open. Start?"
User: "Start"
  ↓
Agent (Execute): → Generates a polished webpage
  ↓
Agent (Deliver): "Done! Double-click to open. Happy with it?"
```

**3 questions, from "I want to build a website" to "Done!" — that's Order Your Milk.**

---

## Core Philosophy: The Three Metaphors

| Metaphor | Purpose | Core Action |
|----------|---------|-------------|
| 🧋 **Order** | Clarify requirements | One question at a time, gradually converge |
| 🔬 **Investigate** | Deep research | Multi-angle parallel drilling |
| ⚡ **Diverge** | Parallel execution | Multiple solutions at once, pick the best |
| ✅ **Deliver** | Verify output | Test + Confirm + Feedback |

**Use as needed**: The four steps have no fixed order. Requirements already clear? Skip the Order. Tech stack familiar? Skip the Investigation. Simple task? Use L1 and just build it.

---

## What Makes This Skill Special?

### 1. Drink Shop Ordering-Style Requirements Elicitation — A Feature No One Else Has

**All mainstream AI coding tools assume the user already knows what they want.** Bolt.new, Lovable, v0.dev, Cursor, Windsurf — they all use a "you describe, I generate" model.

But the biggest pain point for beginners is: **"I don't know what I want."**

This skill's ordering system uses structured option guidance — 3–5 questions to turn a vague idea into a concrete requirement. There is no direct competitor in the market.

### 2. Multi-Angle Parallel Research — Deeper Than Deep Research

Perplexity/OpenAI's Deep Research is **serial** — one direction at a time. This skill's research uses **three parallel tracks**:
- Pioneer Agent: Go straight to the core
- Support Agent 1: Expand from the application perspective
- Support Agent 2: Expand from the pitfall perspective

Combined with cavity detection and automatic bypass, it achieves higher coverage.

### 3. Three-Track Divergence — Unique Diversity Injection

No framework on the market natively supports "multiple paths for the same task." This skill injects diversity through **differentiated optimization objectives**:
- Path A: Pursue performance
- Path B: Pursue maintainability
- Path C: Pursue simplicity

This is not simple repetition — it systematically explores different solution spaces.

### 4. Cross-Agent Compatible — Pure Methodology, Platform-Agnostic

This is not a code framework — it's a **thinking methodology**. It works when installed on any AI Agent:
- Hermes Agent → Full capability (with parallelism)
- Claude Code → Full capability (serial simulation)
- Cursor/Windsurf → Full capability (serial simulation)
- Any Agent with system prompt support → Basic capability

### 5. Eight-Level Execution System — Precise Cost/Quality Control

From L1 Solo (1x tokens) to L8 Diamond (20x tokens), users can precisely choose their investment based on task importance. No other system offers this level of granularity.

---

## Trigger Conditions

### When to Activate This Skill

When the user's request meets any of these conditions:

- The user describes a **finished product/artifact** need (website, app, script, paper, system)
- The description is **brief and vague** ("build a landing page" "help me with a tool" "I want to learn XX")
- The task involves **multi-dimensional choices** (tech stack, style, features, scale)
- The user is a **technical beginner**, unsure what they want

### When Not to Activate

- User says "just do it" "don't ask" "same as last time"
- Simple queries ("what time is it" "search this for me")
- User has already provided a detailed requirements document/spec
- Continuation of an already in-progress task

### Preference Memory System

The Agent should remember user preferences to reduce repetitive questioning:

**Memory Granularity**:
| Level | What to Remember | Example |
|-------|-----------------|---------|
| Explicit Preferences | Preferences the user clearly stated | "I like dark themes" |
| Implicit Preferences | Inferred from repeated choices | User chose "minimal" 3 times in a row → prefers minimal |
| Project Preferences | Agreements for a specific project | "This project uses React" |
| Global Preferences | Cross-project general preferences | "Code should have detailed comments" |

**Preference Confidence & Behavior**:
| Confidence | Condition | Behavior |
|------------|-----------|----------|
| High (≥3 consistent times) | "Dark theme" chosen 3+ times | Skip that dimension's question, apply directly |
| Medium (1–2 times) | Chose "minimal" last time | "Use the minimal style from last time?" |
| Low (no record) | First interaction | Full questioning |

**Preference Storage Locations**:
- Hermes Agent → memory tool, target='user'
- Claude Code → "## User Preferences" section in CLAUDE.md
- Cursor → Preferences section in .cursorrules
- Generic → `.ai-dev-flow-prefs.json` in project root

**Preference File Format** (`.ai-dev-flow-prefs.json`):
```json
{
  "version": "1.0",
  "preferences": {
    "style": {"value": "minimal-clean", "confidence": "high", "count": 5},
    "tech": {"value": "pure-frontend", "confidence": "high", "count": 4},
    "scale": {"value": "single-page", "confidence": "medium", "count": 2}
  },
  "project_specific": {
    "dashboard-app": {"tech": "React+TypeScript", "style": "dark-tech"}
  }
}
```

### Teaching Mode (Advanced)

Explain "why we're doing this" during execution to help users learn:

| Mode | Behavior | Best For |
|------|----------|----------|
| **Silent Mode** (default) | Only output results and brief notes | Experts, time-pressured users |
| **Teaching Mode** | Explain decision rationale at every step | Beginners, learning scenarios |
| **Expert Mode** | Discuss trade-offs and alternatives | Advanced users, technical discussions |

**How to activate**:
- User says "teach me" "explain why" → Switch to Teaching Mode
- User says "don't explain" "just do it" → Silent Mode
- User asks "why not approach X?" → Temporarily switch to Expert Mode

**Teaching Mode Example**:
```
[Silent] "Using ECharts as the charting library."
[Teaching] "Choosing ECharts over D3.js because: (1) Your needs are standard chart types,
       and ECharts works out of the box with 60% less code; (2) ECharts has excellent
       English documentation, making troubleshooting easy; (3) D3.js is suited for custom
       visualizations but has a steep learning curve — for your use case, it would be over-engineering."
```

---

## ⚡ Dual Mode System — Fast Mode vs Deep Mode

Order Your Milk has two execution rhythms, automatically selected based on the user's time and quality needs:

| Mode | Name | Goal | Time | Quality Level |
|------|------|------|------|---------------|
| ⚡ **Fast Mode** | Fast Mode | Get usable results ASAP | 5–15 min | Functional + Looks acceptable |
| 🔬 **Deep Mode** | Deep Mode | Pursue the highest quality delivery | 30–120 min | Secure + Maintainable + Production-ready |

### When to Use Which Mode?

**Automatic Selection Rules**:

| What the User Says | Selection | Reason |
|--------------------|-----------|--------|
| "Quick build" "just throw something together" "let me see the effect" "demo" | ⚡ Fast | User wants speed |
| "Build me an XX to see" "make a prototype first" | ⚡ Fast | Prototype-oriented |
| "Doesn't matter" "not important" "good enough is fine" | ⚡ Fast | Low importance |
| "Important" "can't afford mistakes" "must be secure" "production" | 🔬 Deep | High quality required |
| "Do it carefully" "take your time" "pursue perfection" | 🔬 Deep | User wants quality |
| Involves payments/auth/security/user data | 🔬 Deep | Security-sensitive |
| No clear signal | ⚡ Fast (default) | Deliver fast first, upgrade if not satisfied |

**Manual Mode Switching**:
- "Use fast mode" → ⚡ Fast
- "Use deep mode" / "do it carefully" → 🔬 Deep
- "Quick look first, then refine" → ⚡ Fast prototype → 🔬 Deep polish

### ⚡ Fast Mode Flow

Fast Mode compresses the four-step process, skipping non-essential stages, aiming for **usable results in the shortest time**:

```
⚡ Fast Mode Flow Diagram

  Order(30s) ─→ Research(skip) ─→ Execute(L1-L2) ─→ Deliver(quick check)
      │              │              │              │
      │              │              │              └─ Syntax check + functional verification
      │              │              └─ Single Agent directly, or build + review
      │              └─ Skip research, use proven solutions
      └─ 1-2 core questions, or use set meals / smart defaults
```

**Fast Mode Step Details**:

| Step | Fast Mode Approach | What's Skipped |
|------|--------------------|----------------|
| **Order** | 1–2 core questions, rest use defaults | Follow-ups, preference learning, confirmation sheet beautification |
| **Research** | Skip entirely, use proven solutions | Three-track parallel drilling |
| **Execute** | L1 Solo or L2 Partner, single Agent completes | Multi-track divergence, cross-review |
| **Deliver** | Syntax check + core functional verification | Boundary testing, 5-round validation |

**Fast Mode Quality Assurance**:
While Fast Mode omits parts of the process, it **never cuts quality corners**:
- ✅ Code runs (syntax correct)
- ✅ Core functions work (basic functional verification)
- ✅ Includes usage instructions
- ❌ No multi-solution comparison
- ❌ No deep security review
- ❌ No boundary stress testing

**Fast Mode Example**:
```
User: "Quick build a calculator"
Agent: "Sure, dark theme + basic four operations, OK?"
User: "Yep"
Agent: (L1 directly generates an HTML calculator)
Agent: "Done! Double-click to open. Want to add scientific calculator features?"
Time: 3 minutes
```

### 🔬 Deep Mode Flow

Deep Mode follows the complete four-step process and applies **Advanced Coding Principles** during the coding phase:

```
🔬 Deep Mode Flow Diagram

  Order(2-4 rounds) ─→ Research(3 tracks) ─→ Diverge(L3-L8) ─→ Deliver(comprehensive)
      │              │              │              │
      │              │              │              └─ 5-round testing + boundary + security
      │              │              └─ Multi-track parallel + cross-review + fusion
      │              └─ Three-track parallel drilling (core/application/pitfalls)
      └─ Full ordering + confirmation sheet + preference learning

  🔑 Key difference: Execute phase enforces Advanced Coding Principles (see below)
```

**Deep Mode vs Fast Mode — Execute Phase Comparison**:

| Aspect | ⚡ Fast Mode | 🔬 Deep Mode |
|--------|-------------|-------------|
| Level | L1–L2 | L3–L8 |
| Number of Paths | 1 | 2–3 parallel |
| Coding Principles | Standard quality | **Advanced Coding Principles** (see below) |
| Review | Optional (L2) | Mandatory (L3+) |
| Cross-validation | None | L7+ mutual review |
| Test Depth | Syntax + Function | Syntax + Function + Boundary + Security + Performance |
| Code Review Focus | "Runs OK" | Security + Maintainability + Long-term reliability |

### 🔬 Deep Mode: Advanced Coding Principles

During the coding phase of Deep Mode, all Agents **must follow these four principles**. These principles come from industry best practices and significantly improve code quality:

#### Principle 1: Think Before Coding

**Don't assume. Don't hide confusion. Surface trade-offs.**

Before writing any code:
- ✅ **State assumptions explicitly** — If unsure, ask first
- ✅ **List all interpretations when ambiguous** — Don't silently pick one
- ✅ **Speak up when a simpler approach exists** — Push back with reasons
- ✅ **Stop when something is unclear** — Explain what's confusing, then ask

```
❌ Wrong: Start coding right away, assuming the user wants MySQL
✅ Right: "There are several data storage options: SQLite (lightweight),
    MySQL (production-grade), file storage (simplest). For your use case,
    I recommend SQLite because..."
```

#### Principle 2: Simplicity First

**Minimum code to solve the problem. No speculative design.**

- ❌ Don't build features that weren't requested
- ❌ Don't abstract code used only once
- ❌ Don't add "flexibility" or "configurability" that wasn't asked for
- ❌ Don't write error handling for impossible scenarios
- ✅ If 200 lines can be reduced to 50, rewrite

**Self-check question**: *"Would a senior engineer consider this code over-complicated?"* If yes, simplify.

```
❌ Wrong: Write a factory pattern + strategy pattern + observer pattern for a simple calculator
✅ Right: One function handles the four operations, clear and clean
```

#### Principle 3: Surgical Changes

**Only touch what must be touched. Only clean up your own mess.**

When editing existing code:
- ❌ Don't "improve" nearby code, comments, or formatting along the way
- ❌ Don't refactor things that aren't broken
- ✅ Match existing style, even if you have different preferences
- ✅ Found unrelated dead code? Mention it, but don't delete it

**Change verification standard**: *Every modified line should be directly traceable to the user's request.*

```
❌ Wrong: User asked to add a search feature, and you refactored the entire routing system
✅ Right: Only add the search-related route and handler, leave everything else untouched
```

#### Principle 4: Goal-Driven Execution

**Define success criteria. Loop until verification passes.**

Turn tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix a bug" → "Write a reproduction test, then fix it"
- "Refactor X" → "Ensure tests pass before and after refactoring"

**List a plan for multi-step tasks**:
```
1. Design database schema → Verify: schema can create tables
2. Implement API endpoints → Verify: curl test CRUD all works
3. Add auth middleware → Verify: no token returns 401
4. Write integration tests → Verify: all pass
```

**Strong success criteria let Agents work independently. Weak criteria ("make it work") require constant clarification.**

### Applying Coding Principles to Divergence

In Deep Mode, each Path in the three-track divergence must include these four principles in its prompt:

```
Path A prompt (Performance optimization + Coding Principles):

You are a senior engineer who pursues extreme performance.

**Task**: {task_description}

**Mandatory Coding Principles**:
1. Think Before Coding — Clarify assumptions, surface trade-offs before coding
2. Simplicity First — Minimum code to solve the problem, no speculative design
3. Surgical Changes — Only touch what's needed, match existing style
4. Goal-Driven — Define success criteria, loop verification until passed

**Your core optimization target is [Performance Efficiency]**:
...
```

### Mode Upgrade & Downgrade

Users can switch modes at any time:

| Scenario | Handling |
|----------|----------|
| Fast Mode done, user says "not good enough" | Upgrade to Deep Mode, optimize on current results |
| Deep Mode too slow, user says "faster" | Downgrade to Fast Mode, skip remaining deep process |
| Fast Mode done, user says "add XX feature" | Assess: simple feature → Fast Mode append; complex feature → suggest Deep Mode |
| A track fails in Deep Mode | Follow downgrade strategy (see Section 3.5.2) |

---

## Step 1: Order — Requirements Elicitation (Clarify)

> Core Goal: Transform the user's vague idea into concrete technical specifications.

### 1.1 Metaphor Selection

Based on the user's cultural background and context, choose the most natural metaphor:

| Metaphor | Best For | Example |
|----------|----------|---------|
| 🧋 Drink Shop | East Asian users, relaxed atmosphere | "Large or small? Add boba?" |
| ☕ Coffee Shop | Western users, business settings | "Large or small? Add foam?" |
| 🍽 Restaurant | General, formal settings | "What appetizer? How do you want the steak done?" |
| 🛒 Shopping | E-commerce/product settings | "What color? What configuration?" |

**Default to the drink shop metaphor** unless the user's cultural background or context is better suited to another metaphor.

### 1.2 Ordering Flow

```
User: "I want to build a website"
         │
         ▼
   ┌──────────────────────────┐
   │  Q1: What type?           │  ← Most important dimension first
   │  A. Showcase              │
   │  B. Functional            │
   │  C. Tool                  │
   │  D. Not sure, help me pick│
   └────────┬─────────────────┘
            ▼
   ┌──────────────────────────┐
   │  Q2: What style?          │  ← Adjust options based on Q1 answer
   │  A. Minimal & Clean       │
   │  B. Tech & Cool           │
   │  C. Professional Business │
   │  D. You choose for me     │
   └────────┬─────────────────┘
            ▼
   ┌──────────────────────────┐
   │  Q3: Technical approach?  │
   │  A. Pure frontend (open)  │
   │  B. With backend (stronger│
   │  C. Not sure, you decide  │
   └────────┬─────────────────┘
            ▼
   ┌──────────────────────────┐
   │  Q4: Scale?               │
   │  A. Single page           │
   │  B. Multi-page (3-5 pages)│
   │  C. Full application      │
   └────────┬─────────────────┘
            ▼
      Requirements Sheet → Next Step
```

### 1.3 The Iron Rule of Ordering

**⚠️ Ask only one question at a time.** Don't dump all questions at once and make the user "take an exam."

Correct approach:
```
Agent: "Let's start with a type — showcase, functional, or tool?"
User: "Functional"
Agent: "Great, functional it is. Style-wise, do you prefer minimal & clean, tech & cool, or professional business?"
User: "Tech & cool"
Agent: "Got it. Technically, pure frontend (double-click to open) or with backend (more powerful but needs deployment)?"
```

Wrong approach:
```
Agent: "Please answer the following: 1. Type? 2. Style? 3. Tech? 4. Scale? 5. Security?"
User: "......" (has left)
```

### 1.4 Set Meals System

For common needs, offer preset "set meals" for one-click selection:

```
🍽 I have a few ready-made set meals that might suit you:

🅰 Personal Portfolio — Single page, minimal style, pure frontend, done in 10 min
🅱 Small Tool — Functional, dark theme, single page, with interaction
🅲 Admin Dashboard — Multi-page, professional style, with data tables and charts
🅳 Custom Build — I'll walk you through step by step

Which one?
```

**Core value of set meals**: Reduce decision fatigue for beginners. Don't know what to pick? Just pick a set meal.

### 1.5 Follow-Up Strategy

Based on the user's selections, decide whether follow-up questions are needed:

| User Selected | What to Ask | How Many Rounds |
|--------------|-------------|-----------------|
| "Tech & cool" | Specific color preference? Blue-purple / Green / Red? | 1 round |
| "With backend" | Database choice? SQLite / MySQL / Don't care? | 1 round |
| "Full application" | What core features are included? | 1–2 rounds |
| "You choose" | **Skip follow-up**, recommend directly | 0 rounds |

**Follow-ups should not exceed 2 rounds.** Too many questions annoy users.

### 1.6 Requirements Confirmation Sheet

After ordering is complete, output a confirmation sheet for the user to review:

```
📋 Your Order Confirmation:

┌─────────────────────────────┐
│ 🧋 Need: Data Visualization │
│    Dashboard                 │
│                             │
│ Type: Functional            │
│ Style: Tech & Cool (dark)   │
│ Tech: Pure frontend         │
│      (HTML+CSS+JS)          │
│ Scale: Single page          │
│                             │
│ Core Features:              │
│  ✅ Real-time data charts   │
│  ✅ Filtering & search      │
│  ✅ Responsive layout       │
│  ☐ User login (not selected)│
│                             │
│ Expected output: 1 HTML file│
│ Double-click to open in     │
│ browser                     │
└─────────────────────────────┘

Confirm and start? Or tell me what to change~
```

### 1.7 Preference Learning (Advanced)

If this is a repeated interaction, remember the user's choices:

- User always picks "minimal" → Default to recommending minimal next time
- User always picks "pure frontend" → Skip the tech stack question next time
- User wasn't happy with "tech-cool style" last time → Don't recommend it next time

**Confidence Rules**:
- Consistent choice 3+ times → Execute automatically ("Done based on your usual preferences")
- Consistent choice 1–2 times → "Use the same approach as last time?"
- No record → Full ordering flow

### 1.8 Shortcut: Skipping the Order

When a user clearly indicates they don't want the ordering flow, **you must respect that** — don't insist on guiding:

| What the User Says | Correct Response | Wrong Response |
|-------------------|------------------|----------------|
| "Just do it" | Generate confirmation sheet (based on known info), skip questions | "But I still want to ask you a few things..." |
| "Don't ask" | Same as above | "Let me first understand..." |
| "Same as last time" | Look up previous preferences, reuse directly | "What was it last time?" |
| "You decide" | Generate confirmation sheet using default recommendations | "I still need you to tell me..." |
| Provides detailed requirements spec | Convert directly to confirmation sheet, confirm then execute | Ask again based on the detailed spec |

**Shortcut Flow**:
```
User: "Just do it, React+TypeScript TodoMVC"
         │
         ▼
   ┌──────────────────────────────┐
   │ Agent: Quick confirmation     │
   │                              │
   │ 📋 Based on your description:│
   │ • Tech: React + TypeScript   │
   │ • Feature: TodoMVC           │
   │ • Mode: L2 Partner           │
   │                              │
   │ Start?                       │
   └──────────────────────────────┘
         │
         ▼ Go directly to Step 3
```

**Decision criteria**: Is the information provided enough to generate an executable confirmation sheet?
- Yes → Generate confirmation sheet, execute after confirmation
- No → Politely explain what key information is still needed (ask 1–2 questions at most)

---

## Step 2: Research — Deep Investigation (Research)

> Core Goal: Before starting, figure out "what's the best way to do this."

### 2.1 When to Start Research

- The user wants to build something in an **unfamiliar domain** ("help me with blockchain" "help me train a model")
- There are **multiple technical approaches** to compare
- The user explicitly says "help me research this" "look into it first"
- Task complexity is high, need to build a knowledge foundation first

### 2.2 Cone Drilling Model

```
                    🎯 Target Topic
                       │
           ┌───────────┼───────────┐
           ▼           ▼           ▼
      Pioneer Agent  Support Agent  Support Agent
      (Go Deep)     (Expand Left)  (Expand Right)
           │           │           │
           ▼           ▼           ▼
      One more       Maintain 2-3  Maintain 2-3
      level down     level depth   level depth
           │        gap           gap
           ▼           │           │
         ...          ...         ...
```

**Pioneer Agent**: Inquiry-driven deep dive — each answer leads to the next question, drilling as deep as possible.
**Support Agent**: Branch out from the pioneer's pivot points, covering peripheral knowledge.

### 2.3 Research Execution Method

**Choose execution method based on host Agent capabilities**:

| Host Capability | Execution Method | Effect |
|----------------|------------------|--------|
| Supports parallel sub-Agents | 3 Agents drill simultaneously | Best: wide coverage, fast |
| Supports serial sub-Agents | Execute 3 rounds sequentially, different angles each time | Good: wide coverage, slower |
| Single Agent | Same Agent queries 3 times, different angles each time | Basic: needs more rounds |

**Regardless of method, the key is three tracks from different angles**:
- Track A (Pioneer): Deep into core concepts, asking "why"
- Track B (Support 1): Practical applications, asking "how to use"
- Track C (Support 2): Problems and pitfalls, asking "what could go wrong"

### 2.4 Research Prompt Template

```
You are a deep researcher in {field}. Please answer the following question in extreme detail, providing as much content as possible:
- Specific data and facts
- Comparison tables
- Real-world examples
- Common pitfalls

If up-to-date information is needed, search and then answer.

Question: {question}

At the end of your answer, propose 3 new, deeper questions related to the current topic, marked with [Next Question].
```

### 2.5 Depth Control

Deeper isn't always better. Stop when it's enough.

| Depth | Rounds | Use Case | Stop Criteria |
|-------|--------|----------|---------------|
| Shallow | 3–5 | Quick overview, learning to use | Core concepts covered |
| Medium | 5–15 | Solution design, tech selection | Understand principles + best practices + common pitfalls |
| Deep | 15+ | Frontier research, algorithm innovation | Reached knowledge boundary or diminishing practical returns |

**"The Electric Screwdriver Principle"**: We're here to use it — knowing how to turn it on and how to use it is enough. We're not here to study its motor efficiency.

### 2.6 Cavity Detection & Bypass

When a direction can't be answered further (response contains "uncertain" "cannot determine", too vague), don't stop:

1. **Flank around** — Rephrase from a related but different angle
2. **Decompose** — Break the big question into smaller ones
3. **Analogical transfer** — "Is there a mature, similar approach in this domain?"
4. **Mark and skip** — Acknowledge this is a knowledge gap, continue other directions

### 2.7 Research Output

```
📊 Research Report: {Topic}

## Key Findings
- Finding 1: ...
- Finding 2: ...
- Finding 3: ...

## Technical Solution Comparison
| Solution | Pros | Cons | Recommendation |
|----------|------|------|----------------|
| A        | ...  | ...  | ⭐⭐⭐           |
| B        | ...  | ...  | ⭐⭐⭐⭐          |

## Common Pitfalls
1. ...
2. ...

## Recommended Solution
Based on research, recommend Solution X because...
```

---

## Step 3: Diverge — Parallel Execution (Execute)

> Core Goal: Take the same task down multiple paths, pick the best result.

### 3.1 When to Start Divergence

- The task is **important** — mistakes are not acceptable
- There are **multiple reasonable implementation approaches**
- The user pursues **highest quality**
- Sufficient token budget is available

### 3.2 Eight-Level Execution System

Based on task importance and budget, choose the appropriate execution level:

| Level | Name | What It Does | Best For |
|-------|------|--------------|----------|
| **L1** | Solo | Single Agent, direct execution | Simple tasks, quick prototypes |
| **L2** | Partner | Build + someone reviews | Standard tasks, basic quality assurance |
| **L3** | Team | Architecture → Implementation → Testing (3 phases) | Medium complexity, complete flow |
| **L4** | Audit | Team + independent auditor | Important deliverables, security-sensitive |
| **L5** | Dual | 2 teams at once, pick the best | High risk, uncertain best approach |
| **L6** | Triple | 3 teams at once, pick the best | Pursue highest quality ⭐ Recommended |
| **L7** | Cross | Triple + mutual review & scoring | Safety-critical, cannot afford errors |
| **L8** | Diamond | Triple + cross + fuse best elements | Only perfection accepted 💎 Extreme |

### 3.3 Level Selection Decision

**Quick decision** (3-second level selection):

| If Your Task Is... | Choose This Level | Reason |
|--------------------|-------------------|--------|
| "Just throw it together, good enough" | **L1 Solo** | One Agent handles it directly |
| "It needs to look decent" | **L2 Partner** | Someone checks it once |
| "Serious project, do it right" | **L3 Team** | Design → Implement → Test, complete flow |
| "This is important, no mistakes" | **L4 Audit** | External perspective review |
| "Not sure which approach is best" | **L5 Dual** | Two paths to explore |
| "I want the best result" | **L6 Triple** ⭐ | Three-way competition, pick the winner |
| "Absolutely cannot fail" | **L7 Cross** | Three-way + mutual review |
| "Only perfection accepted" | **L8 Diamond** 💎 | Three-way + review + fusion |

**Default recommendation: L6 Triple Divergence** — the optimal balance of quality and cost.

### 3.3.1 Smart Level Recommendation

Automatically recommend the most suitable level based on task characteristics, reducing user decision burden:

```
Input: Task description + User preferences
         │
         ▼
   ┌──────────────────────────┐
   │ Assess task complexity     │
   │ • Number of features       │
   │ • Technical uncertainty    │
   │ • Cross-domain extent      │
   └────────┬─────────────────┘
            ▼
   ┌──────────────────────────┐
   │ Assess risk level          │
   │ • Security sensitivity     │
   │ • Cost of failure          │
   │ • User visibility          │
   └────────┬─────────────────┘
            ▼
   ┌──────────────────────────┐
   │ Match level + explain why  │
   └──────────────────────────┘
```

**Automatic Recommendation Rules**:

| Task Characteristics | Recommended Level | Reason |
|---------------------|-------------------|--------|
| Single file, clear requirements, no security needs | L1 Solo | Simple tasks don't need multiple people |
| Standard CRUD, clear tech stack | L2 Partner | Needs one review |
| Multiple modules, multiple tech stacks | L3 Team | Needs design → implementation → testing |
| Involves payments/auth/security | L4 Audit | Security needs an external perspective |
| Uncertain of best technical approach | L5 Dual | Needs comparative exploration |
| Highest quality, important project | L6 Triple ⭐ | Multi-solution competition for the best |
| Safety-critical, cannot fail | L7 Cross | Mutual review prevents blind spots |
| Only perfection accepted, extreme scenarios | L8 Diamond 💎 | Full fusion |

**User Override**: Users can say "use L3" or "keep it simple" at any time to override the recommendation.

### 3.3.2 Custom Optimization Objectives

The three-track divergence's default optimization targets are "performance / maintainability / simplicity," but different projects need different optimization dimensions. **Optimization objectives must be configured based on project type**:

| Project Type | Path A | Path B | Path C |
|-------------|--------|--------|--------|
| **Web Frontend** | Performance efficiency | Accessibility (a11y) | Visual fidelity |
| **Backend API** | Response latency | Security | Code maintainability |
| **Data Science** | Prediction accuracy | Interpretability | Training speed |
| **AI/LLM App** | Response quality | Cost control | Latency optimization |
| **CLI Tool** | Execution speed | User experience | Code simplicity |
| **Security System** | Security | Compliance | Performance |
| **Education Project** | Teaching effectiveness | Fun factor | Extensibility |
| **Default** | Performance efficiency | Maintainability | Minimal simplicity |

**Customization**: Users can say "the three paths should optimize XX, YY, and ZZ respectively" to fully customize objectives.

**Objective Differentiation Emphasis**: In the divergence prompt, each path's optimization objective must be explicitly emphasized:
```
Path A prompt: "Your core optimization target is [Performance Efficiency].
  In design decisions, prefer code complexity in pursuit of maximum speed.
  Specific requirements: ... (refined per target)"

Path B prompt: "Your core optimization target is [Maintainability].
  In design decisions, prefer sacrificing a bit of performance for clear, readable code.
  Specific requirements: ... (refined per target)"
```

---

### 3.4 Three-Track Divergence Explained (L6, Recommended Level)

```
              Task Description + Requirements Spec
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
    ┌─────────┐  ┌─────────┐  ┌─────────┐
    │ Path A   │  │ Path B   │  │ Path C   │
    │          │  │          │  │          │
    │ Optimize:│  │ Optimize:│  │ Optimize:│
    │ Perf     │  │ Maintain │  │ Simple   │
    │          │  │          │  │          │
    │ 1.Design │  │ 1.Design │  │ 1.Design │
    │ 2.Build  │  │ 2.Build  │  │ 2.Build  │
    │ 3.Test   │  │ 3.Test   │  │ 3.Test   │
    │          │  │          │  │          │
    │ Soln A   │  │ Soln B   │  │ Soln C   │
    └────┬─────┘  └────┬─────┘  └────┬─────┘
         │             │             │
         └─────────────┼─────────────┘
                       ▼
              ┌─────────────────┐
              │ Compare 3 Solns │
              │ Pick best / fuse│
              └─────────────────┘
```

**Diversity Injection** (key design): The three tracks are not simple repetitions — they are assigned different optimization objectives to ensure exploration of different solution spaces:

- **Path A**: "Pursue extreme performance — prefer code complexity for maximum speed"
- **Path B**: "Pursue elegant maintainability — prefer sacrificing some performance for clarity"
- **Path C**: "Pursue minimal simplicity — solve the problem with the least code"

### 3.5 Path-Internal Execution (Team Mode per Path)

Each path executes three phases internally (serial):

```
Architect → Design solution (module structure, interfaces, tech choices)
    ↓
Implementer → Write code (implement according to architectural design)
    ↓
Tester → Verify quality (write tests, check boundaries, confirm functionality)
```

**Choose execution method based on host Agent capabilities**:

| Host Capability | Execution Method |
|----------------|------------------|
| Supports parallel sub-Agents | 3 tracks launch simultaneously, each track serial internally |
| Supports serial sub-Agents | 3 tracks execute sequentially, each track serial internally |
| Single Agent | Same Agent executes 3 times (different prompts), compare results |

### 3.5.1 Ready-to-Use Divergence Prompt Templates

Below are complete, directly copy-pasteable divergence prompts. **These are not conceptual descriptions — they are instructions ready to paste to an Agent**:

#### Path A Prompt Template (Example: "Performance Optimization" Target)

```
You are a senior engineer who pursues extreme performance.

**Task**: {task_description}

**Requirements Specification**:
{requirements_spec}

**Your core optimization target is [Performance Efficiency]**:
- In design decisions, prefer code complexity in pursuit of maximum speed
- Prioritize algorithms with optimal time complexity
- Make reasonable use of caching, indexing, and pre-computation
- Avoid unnecessary I/O and memory allocation
- Use low-level optimization when necessary (bit operations, direct DOM manipulation, etc.)

**Execution Steps**:
1. Architecture Design: Analyze requirements, design the most performant module structure and interfaces
2. Core Implementation: Write code, with comments explaining the rationale behind each performance optimization
3. Self-Test Verification: Write test cases, verify functional correctness and performance metrics

**Output Format**:
- Architecture design document (with module diagrams, interface definitions)
- Complete, runnable code
- Test cases and test results
- Performance self-assessment (complexity analysis, bottleneck estimation)
```

#### Path B Prompt Template (Example: "Maintainability" Target)

```
You are a senior engineer who pursues elegant code.

**Task**: {task_description}

**Requirements Specification**:
{requirements_spec}

**Your core optimization target is [Maintainability]**:
- In design decisions, prefer sacrificing a bit of performance for clear, readable code
- Use meaningful naming — code as documentation
- Follow SOLID principles and design patterns
- Modular, low coupling, high cohesion
- Each function does one thing
- Key logic must have comments

**Execution Steps**:
1. Architecture Design: Analyze requirements, design the clearest module structure and interfaces
2. Core Implementation: Write code, prioritize readability, then performance
3. Self-Test Verification: Write test cases, verify functional correctness

**Output Format**:
- Architecture design document (with module diagrams, interface definitions, design decision rationale)
- Complete, runnable code (with detailed comments)
- Test cases and test results
- Maintainability self-assessment (module responsibility descriptions, extension point annotations)
```

#### Path C Prompt Template (Example: "Minimal Simplicity" Target)

```
You are a senior engineer who pursues simplicity.

**Task**: {task_description}

**Requirements Specification**:
{requirements_spec}

**Your core optimization target is [Minimal Simplicity]**:
- Solve the problem with the least code
- No over-engineering, no speculative extension
- Prefer standard libraries and built-in language features
- Eliminate redundancy — every line of code has a reason to exist
- Flat file structure, no excessive layering

**Execution Steps**:
1. Architecture Design: Analyze requirements, design the most minimal structure (single file if possible)
2. Core Implementation: Write code, pursue simplicity without sacrificing readability
3. Self-Test Verification: Write test cases, verify functional correctness

**Output Format**:
- Brief design notes (1-2 paragraphs)
- Complete, runnable code
- Test cases and test results
- Simplicity self-assessment (line count, file count, complexity)
```

#### Prompt Variable Reference

| Variable | Source | Example |
|----------|--------|---------|
| `{task_description}` | Step 1 confirmation sheet's requirements description | "Build a real-time data dashboard" |
| `{requirements_spec}` | Step 1 confirmation sheet's full spec | "Dark theme, ECharts, pure frontend..." |
| `{optimization_target}` | Step 3.3.2 configured target | "Performance Efficiency" / "Security" / "Interpretability" |

**When using**: Replace `{task_description}` and `{requirements_spec}` with actual content, and replace the optimization target with the corresponding project type configuration.

### 3.5.2 Divergence Failure Handling (Downgrade Strategy)

When a path fails, **don't let the entire divergence process stop because of it**:

| Failure Scenario | Downgrade Strategy | Notes |
|-----------------|-------------------|-------|
| **A path times out** | Cancel that path, compare with remaining 2 | 2 paths still better than 1 |
| **A path produces very poor quality** | Mark as unusable, pick best from remaining 2 | Record failure reason for reference |
| **A path throws an error** | Record error, remaining 2 continue | Common when a tech approach doesn't fit |
| **2 paths fail** | Downgrade to L2 (single path + review) | At least review ensures quality |
| **All 3 paths fail** | Downgrade to L1, try a different tech approach | May be a requirements misunderstanding — go back to Step 1 |
| **Comparison scores are identical** | Choose the one with the fewest lines of code | Simplicity as default tiebreaker |

**Downgrade Flow Diagram**:
```
3-track divergence starts
    │
    ├── All 3 succeed → Normal comparison scoring
    │
    ├── 2 succeed → Compare 2, note why the 3rd failed
    │
    ├── 1 succeeds → Downgrade to L2 (that path + review)
    │
    └── 0 succeed → Check reason:
                   ├── Misunderstood requirements? → Go back to Step 1
                   ├── Wrong tech approach? → Try a different approach
                   └── Task too complex? → Downgrade to L1 + manual intervention
```

**Failure Analysis Report**: After each divergence failure, output a brief analysis:
```
⚠️ Divergence Report:
- Path A: ✅ Success (maintainable solution, 85 points)
- Path B: ❌ Failed (out of memory, reason: data volume exceeded expectations)
- Path C: ✅ Success (minimal solution, 78 points)
- Downgrade strategy: Compare Path A and Path C
- Final selection: Path A (maintainability better for long-term operation)
```

### 3.6 Solution Comparison & Selection

After all three tracks complete, compare and score:

| Scoring Dimension | Weight | Criteria |
|-------------------|--------|----------|
| Correctness | 30% | Feature complete, tests pass, boundary handling |
| Code Quality | 25% | Readability, maintainability, naming conventions |
| Performance | 15% | Runtime efficiency, resource consumption |
| Security | 15% | Input validation, error handling, no vulnerabilities |
| Simplicity | 15% | Moderate code volume, no redundancy |

**Selection Method**:
- If one solution leads in all dimensions → Select directly
- If each solution excels in different areas → Take the best parts from each and fuse
- If hard to judge → Start cross-validation (L7)

### 3.7 Cross-Validation (L7–L8)

L7 adds tournament-style cross-validation:

```
Solution A's team reviews Solution B → Score + issue list
Solution B's team reviews Solution C → Score + issue list
Solution C's team reviews Solution A → Score + issue list
```

Review requirements:
- Must find at least 3 specific issues (can't just say "looks good")
- Must reference specific code lines
- Score each of the 5 dimensions on a scale of 1–10

L8 adds a fusion Agent on top of L7:
- Extract the best elements from all 3 solutions
- Fuse into one unified super-solution
- Ensure consistent style and compatible interfaces

---

## Step 4: Deliver — Verification & Output (Deliver)

> Core Goal: Ensure the output **works, works well, and the user is satisfied**.

### 4.1 Pre-Delivery Check (Mandatory)

**Before telling the user "it's done," complete the following checks**:

| Check Item | How to Check | What If It Fails |
|-----------|--------------|-------------------|
| Syntax correct | Run the code, check for errors | Fix errors |
| Core functions | Actually operate it, confirm features work | Fix functionality |
| Edge cases | Empty input, extra-long values, special characters | Add validation |
| Can actually run | Run it once following the instructions | Complete the instructions |

**⚠️ Don't skip the actual run!** "Should work" and "actually works" are two different things.

### 4.2 Delivery Format

Delivery must include:

```
✅ Done!

📁 File: xxx.html (at /path/to/xxx.html)

🚀 How to use:
  Double-click the file to open in browser
  Or: python xxx.py / node xxx.js

📋 Features:
  - Feature 1: ...
  - Feature 2: ...
  - Feature 3: ...

💬 Happy with it? Anything to adjust?
```

### 4.3 Feedback Collection

After delivery, ask about user satisfaction. Feedback is used to optimize future ordering and execution:

| User Feedback | What to Do Next Time |
|--------------|---------------------|
| 😊 Very satisfied | Remember preferences, automate next time |
| 🙂 Not bad | Remember preferences, minor tweaks |
| 😐 So-so | Ask specifically what's not great, improve |
| 😞 Not satisfied | Understand the problem in detail, re-execute |

### 4.4 Delivery Guidelines for Common Project Types

| Project Type | Delivery Method | Usage Instructions |
|-------------|-----------------|-------------------|
| Pure Frontend HTML | Generate .html file | "Double-click to open" |
| Python Script | Generate .py file | "Run python xxx.py" |
| Node.js Project | Generate project directory | "Run npm install && npm start" |
| CLI Tool | Generate script + instructions | "Run python xxx.py --help for usage" |
| Data Analysis | Generate script + charts | "Running it generates charts in the current directory" |

### 4.5 Post-Delivery Follow-Up Support

Users may say "change this" or "add a feature." Handling:

| What the User Says | How to Handle |
|--------------------|---------------|
| "Change this here" (small fix) | Make the change directly, don't re-run the flow |
| "Add an XX feature" (new feature) | Assess whether a new ordering round is needed |
| "Start over completely" (complete redo) | Run the full flow again |
| "Great job" | Remember preferences, done |

---

## Cross-Platform Adaptation Guide

This skill is pure methodology, with no dependency on any specific platform's API. Below are adaptation suggestions for each platform:

### Hermes Agent

```
Step 1 (Order): Use clarify() tool's choices parameter
Step 2 (Research): Use delegate_task() for parallel distribution
Step 3 (Diverge): Use delegate_task() + terminal(background) for parallel execution
Step 4 (Deliver): Use terminal() to run tests
```

### Claude Code

```
Step 1 (Order): Ask step-by-step in conversation, use numbered lists for options
Step 2 (Research): Same Agent queries 3 times (different angles)
Step 3 (Diverge): Use --print mode to execute 3 times (different prompts), compare output
Step 4 (Deliver): Use bash to run tests
```

### Cursor / Windsurf

```
Step 1 (Order): Ask step-by-step in AI chat
Step 2 (Research): Multi-round deep questioning in chat
Step 3 (Diverge): Use Agent mode to execute 3 times (different prompts), compare results
Step 4 (Deliver): Use terminal to run tests
```

### OpenCode

```
Step 1 (Order): Ask step-by-step in conversation
Step 2 (Research): Use opencode run to execute 3 times
Step 3 (Diverge): Use opencode run to execute 3 times (different prompts)
Step 4 (Deliver): Use terminal to run tests
```

### Universal Adaptation Principles

Regardless of platform, the core methodology remains unchanged:
1. **Order** = Multi-round conversation, one question at a time, give options
2. **Research** = Multi-angle deep questioning, at least 3 directions
3. **Diverge** = Same task, multiple solutions, compare and pick the best
4. **Deliver** = Test and verify, confirm usability

---

## Beginner-Friendly Design

### Why Do Beginners Need This Skill?

The three death valleys for beginners:

| Death Valley | Pain Point | How This Skill Solves It |
|-------------|-----------|--------------------------|
| Don't know what they want | "I want to build a website" but don't know the specifics | Step 1 Ordering — guided step by step |
| Don't know how to do it | Don't know what tech or approach to use | Step 2 Research — build a knowledge foundation first |
| Don't know if it's correct | Code runs but not sure it's right | Steps 3–4 Divergence + Verification — pick the best from multiple solutions |

**Note**: This skill does not solve "environment setup" or "deployment" problems — those are the host Agent's responsibility. This skill focuses on the **thinking layer** guidance.

### Beginner Usage Recommendations

```
Beginner's first time:
  → Walk through the full flow: Step 1 (Order) → Step 2 (Research) → Step 3 (L3 Team) → Step 4 (Deliver)
  → Experience the complete process

Beginner's second time:
  → Simplified Step 1 (remembered preferences) → Skip Step 2 (already familiar) → Step 3 (L2 Partner) → Step 4

Experienced user:
  → Go directly to Step 3 (L6 Triple Divergence) → Step 4
  → Or only call specific steps as needed
```

---

## Real-World Examples

### Example 1: Beginner Wants a Personal Homepage

```
User: "I want to build a personal homepage"

Agent (Step 1 Order):
  Q: "Showcase (pure info display) or Functional (with interactive features)?"
  A: "Showcase"
  Q: "Style? Minimal & clean, tech & cool, or creative art?"
  A: "Minimal & clean"
  Q: "Pure frontend (double-click to open) or needs a backend?"
  A: "Pure frontend"
  Q: "Single page or multi-page?"
  A: "Single page"

Agent: "📋 Confirmed: single-page personal homepage, minimal style, pure HTML+CSS+JS, double-click to open. Start?"
User: "Start"

Agent (Step 3, L1 Solo):
  → Directly generates a polished personal homepage HTML file

Agent (Step 4 Deliver):
  → "Done! File is at xxx.html, double-click to open. Happy with it?"
```

### Example 2: Building an Important Data Visualization Tool

```
User: "I need to build a real-time data dashboard to show to clients"

Agent (Step 1 Order):
  Q: "Data source? API endpoint, CSV file, or mock data?"
  A: "API endpoint"
  Q: "Chart types? Line, bar, pie, or all of them?"
  A: "All of them"
  Q: "Style? Dark tech, bright business?"
  A: "Dark tech"

Agent (Step 2 Research):
  → 3-track parallel drill: D3.js vs Chart.js vs ECharts comparison
  → Output research report: Recommend ECharts (comprehensive features, excellent docs)

Agent (Step 3, L6 Triple Divergence):
  Path A (Performance): Use Canvas direct rendering, requestAnimationFrame optimization
  Path B (Maintainable): Use ECharts with component-based encapsulation
  Path C (Simple): Minimum code, use ECharts basic configuration
  → Comparison: Path B is best (complete features + easy to maintain)

Agent (Step 4 Deliver):
  → Deliver Path B solution with usage instructions
```

---

## Relationship with Other Skills

This skill is the **process orchestration layer**, which can call other specialized skills as execution engines:

| Called Skill | At Which Step | Purpose |
|-------------|---------------|---------|
| `systematic-debugging` | Step 4 | Pre-delivery debugging |
| `code-quality-mastery` | Step 4 | Code quality checks |
| `test-driven-development` | Step 3 | Test-driven implementation |
| `writing-plans` | Between Steps 2–3 | Create detailed execution plans |
| `web-scraping` | Step 2 | Data collection during research |

---

## Quality Standards

### Code Quality Iron Rules

Regardless of which level is used, the produced code must satisfy:

1. **Secure** — Input validation, error handling, no injection vulnerabilities
2. **Maintainable** — Naming conventions, modular, documented
3. **Extensible** — No hardcoding, leave interfaces, easy to modify
4. **Defensive** — Better to over-write error handling than under-write
5. **Long-term perspective** — Focus on long-term operation, not just immediate functionality

### Verification Checklist

After each task, check:

- [ ] Requirements correctly understood (Step 1 confirmation sheet)
- [ ] Research sufficiently thorough (Step 2 report, if applicable)
- [ ] Code runs normally
- [ ] Edge cases handled
- [ ] Usage instructions included
- [ ] User satisfied

---

## Pitfalls

### 🔴 Fatal Errors (Must Avoid)

| Error | Consequence | Correct Approach |
|-------|-------------|-----------------|
| Ask 5 questions at once | User leaves | Ask only one question at a time |
| Skip ordering, build directly | Output isn't what user wanted | Better to spend 1 extra minute ordering |
| Confirmation sheet without user confirmation | Misunderstood requirements | Must wait for user to say "start" |
| Deliver without actual running | Delivered code doesn't work | Must run it once before delivery |
| User says "just do it" but you still insist on guiding | Terrible user experience | Respect the user, skip the ordering |

### 🟡 Common Errors (Watch Out)

| Error | Consequence | Correct Approach |
|-------|-------------|-----------------|
| Research exceeds 15 rounds | Diminishing returns, wasted tokens | 5–15 rounds is enough — stop |
| Three-track objectives too vague | All three produce the same thing | Force different optimization targets |
| Review only says "looks good" | Problems won't be found | Must find 3 specific issues |
| Scare beginners with jargon | Beginners afraid to ask | "Pure frontend" → "Double-click to open" |
| More than 4 options | Users get decision paralysis | Max 4 options, use staged questions if more |
| One path fails → restart everything | Wastes successful solutions | Downgrade to use remaining solutions |

### 🟢 Advanced Notes

| Note | Details |
|------|---------|
| Metaphor usage | Use metaphors for the first 3 rounds to lower the barrier, switch to professional language from round 4 onward; experienced users skip metaphors entirely |
| Preference memory | 3 consistent choices → auto-apply; first time → full questioning |
| Teaching mode | Default silent; user says "explain" → switch to teaching mode |
| Optimization objectives | Different project types use different three-track target configurations |
| Cross-platform downgrade | Non-parallel platforms → simulate 3 tracks serially, slightly reduced effect but methodology unchanged |
| **Mode Selection** | No clear signal → default ⚡ Fast Mode; user says "take it slow" → 🔬 Deep Mode |
| **Coding Principles** | 🔬 Deep Mode enforces four principles; ⚡ Fast Mode uses standard quality |

### 🔧 Technical Pitfalls (for skill development/maintenance)

| Pitfall | Description | Solution |
|---------|-------------|----------|
| `skill_manage write_file` path restriction | Can only write to `references/`, `templates/`, `scripts/`, `assets/` subdirectories — cannot write `README.md` directly to skill root | Write to `references/README.md` first, then `mv` via `terminal` |
| Smoke test keyword mismatch when translating | Chinese keyword "智能推荐" becomes "Smart Level Recommendation" in English — no literal match | Always run smoke test after translation, fix each failing keyword check individually |
| Parallel translation JSON parse failure | `delegate_task` tasks array fails JSON parsing if unescaped quotes are embedded in task descriptions | Keep task descriptions clean; let subagents read source files via `skill_view` themselves |
| Subagent skill creation path inconsistency | Some subagents create skills at `~/.hermes/skills/name/`, others at `~/.hermes/skills/category/name/` | Specify full path in task descriptions; use `find` afterward to confirm actual location |

---

## Quick Reference — One-Page Cheat Sheet

> Print this section and tape it next to your monitor.

### 🧋 Order Quick Reference

```
One question at a time → Max 4 rounds → Confirmation sheet → User confirms → Next step
"Just do it" → Skip ordering, generate confirmation sheet
"You choose" → Use default recommendations
```

**Default recommendations**: Functional / Minimal & Clean / Pure Frontend / Single Page / Responsive

### 🔬 Research Quick Reference

```
Three-track parallel: Pioneer (core deep) + Support 1 (applications) + Support 2 (pitfalls)
Stop when it's enough → Electric Screwdriver Principle
```

**Depth selection**: Shallow (3–5 rounds) / Medium (5–15 rounds) / Deep (15+ rounds)

### ⚡ Divergence Quick Reference

| Level | Agents | Tokens | Best For |
|-------|--------|--------|----------|
| L1 Solo | 1 | 1x | Simple / quick prototype |
| L2 Partner | 2 | 2x | Standard / with review |
| L3 Team | 3 | 4x | Medium / complete flow |
| L4 Audit | 4 | 6x | Important / security-sensitive |
| L5 Dual | 6 | 8x | High risk / uncertain |
| **L6 Triple** ⭐ | **9** | **12x** | **Highest quality** |
| L7 Cross | 9+3 | 16x | Safety-critical |
| L8 Diamond 💎 | 9+4 | 20x | Only perfection accepted |

**Default: L6**. Smart recommendation: single file→L1, standard→L2, complex→L3, security→L4+.

### ✅ Deliver Quick Reference

```
Syntax check → Functional verification → Boundary testing → Actual run → Usage instructions → Ask for feedback
⚠️ Don't skip the actual run!
```

### 🔑 Key Rules

| Rule | Details |
|------|---------|
| One question at a time | Don't make users "take an exam" |
| Confirm before executing | Confirmation sheet must wait for user to say "start" |
| Actually run it | "Should work" ≠ "works" |
| Electric Screwdriver Principle | Stop when it's enough, don't over-research |
| Failure downgrade | One path fails → use remaining solutions, don't abort |

### ⚡/🔬 Dual Mode Quick Reference

| Signal | Mode | Order | Research | Execute | Deliver |
|--------|------|-------|----------|---------|---------|
| "quick" "demo" "prototype" | ⚡ Fast | 1–2 Qs | Skip | L1–L2 | Quick check |
| "important" "secure" "careful" | 🔬 Deep | Full | 3 tracks | L3–L8 | Comprehensive |
| No clear signal | ⚡ Fast default | 1–2 Qs | Skip | L1–L2 | Quick check |

**Deep Mode Coding Principles**: Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution

### 📁 File Structure

```
order-your-milk/
├── SKILL.md                    ← Core methodology (this file)
├── README.md                   ← Project introduction
└── references/
    ├── set-meals.md            ← 16 preset meals
    ├── domain-templates.md     ← 12 domain templates
    ├── research-prompts.md     ← Universal research templates
    ├── domain-research-prompts.md ← 5 domain-specific research templates
    ├── platform-adapters.md    ← Platform adapters + config templates
    ├── conversation-examples.md← 8 complete conversation examples
    ├── customization-guide.md  ← Customization guide
    └── competitive-analysis.md ← Competitive analysis
```

## What This Skill Does NOT Do

Clear boundaries to avoid misunderstandings:

| Doesn't Do | Why | Who Does It |
|-----------|-----|-------------|
| Environment setup (install Node.js, configure database) | This is the host Agent's capability | Host Agent |
| Deployment (push to server, configure domain) | This is the host Agent's capability | Host Agent |
| Debugging (read errors, fix bugs) | This is the host Agent's capability | Host Agent |
| Write detailed technical documentation | This is a specialized skill's job | `code-quality-mastery` |
| Code review | This is a specialized skill's job | `systematic-debugging` |

**This skill focuses on the "thinking layer"**: requirements elicitation, technical research, solution comparison, quality assurance.
All technical execution is delegated to the host Agent.

---

## License

MIT License — free to use, modify, and distribute.

If you find this skill useful, feel free to Star, Fork, or open an Issue.
