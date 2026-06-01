# Customization Guide — Adapting AI Dev Flow to Your Needs

> AI Dev Flow is an extensible framework. This document teaches you how to customize it for your own scenarios.

---

## 1. How to Add New Domain Templates

### Steps

1. Open `references/domain-templates.md`
2. Add a new domain table following the existing format
3. Each domain includes: dimensions, questions, options, recommended defaults
4. Test: walk through the ordering flow once with the new domain

### Domain Template Design Principles

- **No more than 6 dimensions** (too many makes it feel like filling out a test)
- **No more than 4 options per dimension** (more than 4 causes decision fatigue)
- **Must have a "you decide" option** (lets users who don't want to choose skip)
- **Must have recommended defaults** (for preference learning and quick ordering)
- **Design dimensions from the user's perspective**, not from a technical perspective

> Counter-example: ❌ "Choose an ORM framework" → ✅ "Data storage: Simple file / Lightweight database / Full database"

### Example: Adding an "IoT" Domain

Below is a complete IoT domain template that can be added directly to `domain-templates.md`:

```
### 🏠 Internet of Things (IoT)

| Dimension | Question | Options | Recommended Default |
|------|------|------|---------|
| Device Type | What device do you want to control? | A. Sensors (temperature/humidity/light/motion) / B. Actuators (switches/motors/relays) / C. Displays (LCD/LED/OLED) / D. You decide | Sensors |
| Connectivity | How do devices connect? | A. WiFi (convenient indoors) / B. Bluetooth (short range, low power) / C. LoRa (long range, low power) / D. You decide | WiFi |
| Control Method | How do you control devices? | A. Mobile app / B. Web page / C. Button/remote control / D. You decide | Mobile app |
| Data Handling | How do you use collected data? | A. Real-time display / B. Historical records + charts / C. Smart alerts / D. You decide | Real-time display |
| Platform Choice | What development platform? | A. Arduino (easy to start) / B. ESP32 (full-featured) / C. Raspberry Pi (powerful) / D. You decide | ESP32 |
| Deployment Scale | How many devices? | A. Single device prototype / B. Small network (5-10 devices) / C. Large-scale deployment / D. You decide | Single device prototype |
```

**Design Notes**:
- Only 6 dimensions — not overwhelming for users
- 4 options per dimension (including "you decide")
- Plain language: says "How do devices connect?" instead of "Communication protocol"
- Recommended defaults cover the most common beginner scenarios

---

## 2. How to Add New Set Meals

### Steps

1. Open `references/set-meals.md`
2. Add a new set meal following the existing format
3. Each set meal includes: name, emoji, type/style/technology/scale/suitable for/time estimate/one-line description
4. Place it in the appropriate group (beginner/intermediate/advanced)

### Set Meal Design Principles

- **Set meals are "shortcuts for dimension combinations"** — essentially preset answers for domain templates
- **Cover the most common scenarios** — 80% of user needs should be covered by set meals
- **Naming should be intuitive** — users should understand at a glance ("Personal Showcase Page" is better than "SPA Profile")
- **One-line description should highlight the core value** — clearly state "what you get from this"

### Example: Adding IoT Set Meals

```
### 🏠 IoT Beginner Set Meals

**🅰 Sensor Monitoring Set Meal**
- emoji: 🌡️
- Type: Sensor → Temperature & humidity
- Style: Real-time display
- Technology: ESP32 + WiFi
- Scale: Single device
- Suitable for: People who want to quickly learn about IoT
- Time estimate: ~30 minutes
- One-liner: "Build a smart sensor that displays temperature & humidity in 30 minutes"

**🅱 Smart Home Control Set Meal**
- emoji: 💡
- Type: Actuator → Relay switch
- Style: Mobile app control
- Technology: ESP32 + WiFi
- Scale: Small network (5 devices)
- Suitable for: People who want to DIY smart home
- Time estimate: ~2 hours
- One-liner: "Control your lights and outlets from your phone"
```

---

## 3. How to Customize Research Templates

### Steps

1. Refer to `references/research-prompts.md` and `references/domain-research-prompts.md`
2. Create 3 role-based prompts for the new domain:
   - **Pioneer Agent**: Deep dive into core concepts
   - **Support Agent 1**: Application perspective
   - **Support Agent 2**: Pitfalls perspective

### Research Prompt Design Principles

- **The Pioneer Agent's prompt should guide inquiry-driven deep dives** — each answer should lead to the next question
- **Support Agent prompts should specify a clear angle** — avoid vague generalizations
- **All prompts should require "specific data and case studies"** — avoid empty theory
- **End with derived questions** — ensure the research can continue to go deeper

### Example: IoT Research Prompts

```
#### Pioneer Agent — IoT Core Concepts

You are a deep researcher in the field of Internet of Things. Please answer the following questions in extreme detail:

**Research Goal**: {User's selected IoT scenario}

Please dig deeper from the following angles:
1. What is the core tech stack for this scenario? Compare technology choices at each layer
2. Communication protocol selection: MQTT vs HTTP vs WebSocket vs CoAP — applicable scenarios for each
3. Hardware selection: performance/power consumption/cost comparison of different MCUs (with specific parameters)
4. Cloud platform comparison: AWS IoT / Azure IoT / Alibaba Cloud IoT / self-built — pros and cons analysis

Requirements:
- Provide specific model numbers, parameters, and price ranges
- Provide real project selection case studies
- List the 3 most common technical pitfalls

At the end of your response, propose 3 deeper questions marked with 【Next Question】.

---

#### Support Agent 1 — IoT Practical Applications

You are a product manager for IoT projects. Please answer from the "user value" perspective:

1. Who are the users of this IoT solution? What are their core needs?
2. Market case studies of similar solutions (2 successes and 2 failures)
3. What are the 3 most common user complaints?
4. What features should the MVP (Minimum Viable Product) include?

Requirements: Provide specific user feedback and data.

---

#### Support Agent 2 — IoT Pitfalls and Risks

You are an IoT security expert and project post-mortem analyst. Please answer from the "lessons learned" perspective:

1. The 5 most common failure reasons for IoT projects (with case studies)
2. Security risks: common attack surfaces for device intrusion and data breaches
3. Hardware supply chain risks: strategies for chip shortages and discontinuations
4. Long-term maintenance costs: real data on device maintenance, firmware updates, and cloud costs

Requirements: Each pitfall must include "how to avoid it" recommendations.
```

---

## 4. How to Adjust the Tier System

### Adding Custom Tiers

If your scenario needs a tier between L1-L8:

1. **Choose the nearest base tier** as your starting point
2. **Modify the number of agents or review rules**
3. **Document the custom tier definition**

#### Example: L2.5 — "Quick Review" Tier

```
Tier L2.5 Quick Review
- Approach: 1 agent implements + 1 agent quick-reviews (only checks key issues, not line-by-line review)
- Suitable for: Medium tasks, time-constrained but needing basic assurance
- Token multiplier: ~3x
- Falls between L2 (Partner) and L3 (Team)
```

#### Example: L4.5 — "Double Review" Tier

```
Tier L4.5 Double Review
- Approach: Architecture → Implementation → Testing + 2 independent auditors review separately
- Suitable for: Important deliverables needing multi-angle review
- Token multiplier: ~10x
- Falls between L4 (Audit) and L5 (Dual Path)
```

### Customizing Optimization Goals

The default optimization goals for three-way forking are "Performance / Maintainability / Simplicity". You can customize based on project type:

| Project Type | Path A | Path B | Path C |
|---------|--------|--------|--------|
| **Web Projects** | Performance | SEO Optimization | Accessibility |
| **Data Projects** | Accuracy | Speed | Interpretability |
| **Security Projects** | Security | Usability | Compliance |
| **Education Projects** | Teaching Effectiveness | Engagement | Extensibility |
| **Mobile Projects** | User Experience | Performance | Compatibility |
| **AI/ML Projects** | Model Accuracy | Inference Speed | Interpretability |

**Usage**: In Step 3 forking, simply replace the default optimization goal descriptions.

---

## 5. How to Adapt to New Platforms

### General Adaptation Steps

1. **Identify the platform's core capabilities**: Can it run in parallel? Can it interact? Can it access files? Can it run terminal commands?
2. **Map to the four-step flow**: How each Step is implemented on this platform
3. **Degradation strategy**: For capabilities the platform lacks, provide fallback approaches
4. **Write platform-specific installation instructions**

### Adaptation Checklist

- [ ] Can it ask one question at a time? (Step 1 Ordering)
- [ ] Can it research from multiple angles? (Step 2 Research)
- [ ] Can it execute in parallel? (Step 3 Forking, optional)
- [ ] Can it run code for verification? (Step 4 Delivery)
- [ ] Can it save files? (Output for all Steps)
- [ ] Can it access the network? (Enhancement for Step 2 Research)

### Platform Capability Matrix

| Platform | One Question at a Time | Multi-Angle Research | Parallel Execution | Code Verification | File Saving | Network Access |
|------|---------|-----------|---------|---------|---------|---------|
| Hermes Agent | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude Code | ✅ | ✅ | ⚠️ Serial simulation | ✅ | ✅ | ❌ |
| Cursor/Windsurf | ✅ | ✅ | ⚠️ Serial simulation | ✅ | ✅ | ❌ |
| ChatGPT/Claude | ✅ | ✅ | ❌ | ⚠️ Limited | ❌ | ✅ |
| Generic Agent | ✅ | ⚠️ Requires tricks | ❌ | ⚠️ Depends on platform | ⚠️ Depends on platform | ⚠️ Depends on platform |

### Degradation Strategy Template

Fallback strategies when the platform lacks a certain capability:

| Missing Capability | Degradation Strategy | Quality Impact |
|---------|---------|---------|
| Parallel Execution | Serial simulation: execute sequentially, compare at the end | Slower, but quality unaffected |
| Code Verification | Manual verification: provide a testing checklist to the user | May miss runtime errors |
| File Saving | Output to chat: paste complete code in messages | User must save manually |
| Network Access | Pre-built knowledge: research based on existing knowledge | May lack the latest information |

---

## 6. Advanced Customization

### Custom Metaphors

Not limited to the milk tea shop — choose different metaphors based on user scenarios:

| Metaphor | Cultural Background | Suitable Scenarios | Example Dialogue |
|------|---------|---------|---------|
| 🧋 Milk Tea Shop | East Asian | Default choice, relaxed atmosphere | "Large or small? Add boba?" |
| ☕ Coffee Shop | Western | Business scenarios | "What roast level? Add foam?" |
| 🍽 Restaurant Ordering | Universal | Formal scenarios | "What for appetizer? How well-done for the main course?" |
| 🛒 Product Shopping | E-commerce | Product scenarios | "What color? What configuration?" |
| 💊 Pharmacy Consultation | Medical/Diagnostic | Technical diagnosis scenarios | "What are the main symptoms? How long has it lasted?" |
| 🏠 Interior Design | Architecture/Design | Design projects | "What style? How many rooms? What's the budget?" |

**Principles for choosing metaphors**:
- Match the user's language habits and cultural background
- Use metaphors for the first 3 rounds to lower the barrier
- Switch to professional but friendly language from the 4th round onwards
- If the user is clearly experienced, skip the metaphor entirely

### Custom Confirmation Slip Format

The confirmation slip can be adjusted based on project needs. Core elements:

```
📋 Confirmation Slip Elements:

1. Title — Project name or description
2. Confirmed Options — Displayed as a clear list
3. Visual Borders — Use ┌─│└ to enhance readability
4. Unselected Features — Mark as "Not selected" so users know what's optional but not chosen
5. Expected Output — File types and quantities
6. Estimated Time — Based on tier estimation
7. Interaction Prompt — "Confirm to start? Or tell me what to change"
```

**Confirmation slip variants for different scenarios**:

| Scenario | Adjustments |
|------|--------|
| Simple projects | Condense to 3 lines for quick confirmation |
| Complex projects | Staged confirmation (confirm the big picture first, then details) |
| Team projects | Add "Responsible Person" and "Priority" fields |
| Learning projects | Add "Learning Objectives" and "Prerequisites" fields |

### Integrating with Other Skills

This skill can work alongside other specialized skills to form a complete development pipeline:

| When to Call | Skill to Call | Purpose |
|---------|-----------|------|
| Step 2 Research | `web-scraping` | Collect latest technical materials and competitor information |
| Step 2 Research | `arxiv` | Search for related academic papers |
| Step 3 Execute | `test-driven-development` | Implement with TDD to ensure quality |
| Step 3 Execute | `code-quality-mastery` | Real-time code quality checks |
| Step 4 Deliver | `systematic-debugging` | Systematic debugging before delivery |
| Step 4 Deliver | `code-quality-mastery` | Final code quality review |
| After delivery | `writing-plans` | Create execution plans for subsequent iterations |
| After delivery | `obsidian` | Record project notes and lessons learned |

**Integration method**: In the corresponding Step, the agent automatically identifies needed specialized capabilities and calls the corresponding skill.

---

## 7. Internationalization (Creating Other Language Versions)

If you want to create a translated version of this skill for users in other languages:

### Steps
1. Create a new skill (e.g., `order-your-milk` for English)
2. Translate SKILL.md and all files in `references/` to the target language
3. Preserve all technical terms, code blocks, emoji, and table structures
4. Adapt cultural references (e.g., "中文文档" → "English documentation")
5. Start the new version at 1.0.0
6. Run the smoke test to verify completeness

### Translation Fidelity Check (Mandatory)
After translation, run 3-4 parallel sub-agents for section-by-section comparison audit:
- Each file must have the same number of sections, table rows, and examples
- All unique selling points must be preserved
- Smoke test keywords must match the ACTUALLY translated text (don't use expected translations — grep the actual content)

### Verified Translations
- 🇨🇳 Chinese: `ai-dev-flow` (original version)
- 🇬🇧 English: `order-your-milk` (full translation, 47/47 smoke test passed)

---

## 8. Contribution Guide

If you want to share your customizations with the community:

1. **Fork** the repository
2. Add your template to the corresponding file:
   - New domain template → `references/domain-templates.md`
   - New set meal → `references/set-meals.md`
   - New research prompt → `references/domain-research-prompts.md`
   - New platform adaptation → `references/platform-adapters.md`
3. **Submit a PR**, explaining:
   - Applicable scenarios
   - Design rationale
   - Testing results (at least one complete flow walkthrough)
4. Wait for review and merge

### Contribution Quality Standards

| Item | Requirements |
|------|------|
| Domain Template | 4-6 dimensions, 3-4 options each, with default values |
| Set Meal | Has name/emoji/one-liner, placed in the correct group |
| Research Prompt | All 3 roles present, with specific data requirements |
| Platform Adaptation | Passes all 4 items on the adaptation checklist |

### Contributor Code of Conduct

- Respect different cultures and technical preferences
- Templates should be designed for real users, not to show off
- Keep it concise: if 3 options suffice, don't use 4
- Test before submitting: you should have walked through the flow at least once yourself

---

## Quick Reference

| Customization Type | File to Modify | Complexity |
|---------|---------|--------|
| Add new domain | `domain-templates.md` | ⭐ Simple |
| Add new set meal | `set-meals.md` | ⭐ Simple |
| Custom research prompt | `domain-research-prompts.md` | ⭐⭐ Medium |
| Adjust tiers | SKILL.md corresponding section | ⭐⭐ Medium |
| Custom optimization goals | SKILL.md Step 3 section | ⭐ Simple |
| Adapt new platform | `platform-adapters.md` | ⭐⭐⭐ Complex |
| Custom metaphor | SKILL.md Step 1 section | ⭐ Simple |
| Integrate other skills | No file modification needed, agent calls automatically | ⭐ Simple |
