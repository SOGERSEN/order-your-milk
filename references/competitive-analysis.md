# Competitive Analysis & Unique Value Assessment

> Research date: 2026-05-31
> Method: Hyper-Concurrent Questioning System (3-Agent parallel deep-drill)
> Updated: 2026-06-01 — Added user case studies and v2.0 comparison

## 1. Mainstream AI Coding Tool Comparison

### Requirements Elicitation Capability

| Tool | Elicitation Method | Depth | Assessment |
|------|-------------------|-------|------------|
| Bolt.new | Direct input box + "Plan" button | Shallow | "You describe, I build" — no guided questioning |
| v0.dev | Prompt for description, generate UI components | Shallow | Pure description→generation, no guided dialogue |
| Lovable | "Describe the app you want to create" | Shallow | Three-step flow, no proactive questioning |
| Replit Agent | Conversational interaction | Medium | Asks clarifying questions, but not systematic |
| Cursor | Agent mode dialogue | Medium | Follows up on details, but oriented toward experienced developers |
| Windsurf | Cascade feature | Medium | Multi-turn dialogue clarification, but not structured guidance |

**Conclusion: All mainstream tools use a "user describes → AI generates" model. None have "milk tea ordering"-style structured requirements elicitation.**

### Deep Research Capability

| Tool | Research Method | Parallelism | Depth |
|------|----------------|-------------|-------|
| Perplexity Deep Research | Multi-turn search + synthesis | Primarily serial | Deep |
| Google Deep Research | Gemini multi-step research | Partially parallel | Deep |
| OpenAI Deep Research | o3 model-driven | Internal reasoning chain | Very deep |

**Conclusion: Deep Research tools are serial — no "multi-angle parallel drilling + cavity detection".**

### Multi-Agent Orchestration Frameworks

| Framework | Stars | N-Version | Cross-Validation | Tiered Levels |
|-----------|-------|-----------|-----------------|---------------|
| CrewAI | 52.5k | ❌ | ❌ | ❌ |
| AutoGen | 58.6k | ⚠️ Manual | ❌ | ❌ |
| LangGraph | 33.4k | ⚠️ Manual | ❌ | ❌ |
| MetaGPT | 68.4k | ❌ | ❌ | ❌ |
| OpenAI Agents SDK | 26.8k | ⚠️ Manual | ❌ | ❌ |

**Conclusion: No mainstream framework natively supports N-Version parallel divergence, cross-validation, or tiered levels.**

## 2. Multi-Agent vs Single-Agent: Actual Performance

### Key Data

- **mini-SWE-agent** (100 lines of Python) achieves 74%+ pass rate on SWE-bench Verified
- UC Berkeley paper (2025): "Multi-agent systems often show marginal performance gains on mainstream benchmarks"
- Different instances of the same model tend to make the same errors (correlation problem)

### Conclusion

For coding tasks, multi-agent systems typically don't justify the 2-20x token cost. Model capability is the bottleneck, not orchestration complexity.

**Therefore, we position the system as a "methodology skill" rather than a "code framework" — we don't compete with CrewAI/LangGraph.**

## 3. Unique Value Confirmation

| Feature | Exists in Market? | Order Your Milk Advantage |
|---------|-------------------|--------------------------|
| Guided requirements elicitation | ❌ No direct competitor | Step 1: Clarify |
| Multi-angle parallel research | ⚠️ Deep Research has similar | Step 2: Triple parallel + cavity detection |
| Triple-path divergence execution | ❌ No framework natively supports | Step 3: Optimization target differentiation |
| End-to-end four-step flow | ❌ No product integrates this | Complete methodology |
| Cross-Agent universal | ❌ Most are platform-bound | Pure methodology, works on any platform |

## 4. Academic Support

- arXiv:2506.11610 — "Choice-based answering improves requirements clarity"
- arXiv:2009.01509 — "Guided multi-turn Q&A is the most effective requirements elicitation method"
- N-Version Programming (Avizienis, 1975) — Theoretical foundation for multi-version redundancy
- Ensemble Learning (Breiman, 1996) — Ensemble learning methodology
- Condorcet Jury Theorem (18th century) — Mathematical foundation for collective wisdom

## 5. Key Insights

1. **Milk tea ordering is the true innovation** — Market gap confirmed, academically supported
2. **Three-system fusion is the biggest differentiator** — No product does "guide → research → execute" as a complete chain
3. **Positioned as methodology, not framework** — Don't compete with CrewAI/LangGraph; do what they can't
4. **Cross-Agent universality is a key advantage** — Pure methodology, any AI Agent can install and use it

---

## 6. Real User Case Studies

> The following cases come from actual project usage records of Order Your Milk, demonstrating coverage from simple to complex scenarios.

### Case 1: Personal Homepage — L1 Quick Meal

- **Scenario**: User needed a personal portfolio page
- **Meal selected**: L1 Quick Meal (single-round delivery, ~15 minutes)
- **Flow**: Order → Select "L1 Quick" → AI generates HTML/CSS/JS directly → Preview and adjust → Done
- **Key point**: Zero-experience user completed requirements through multiple-choice questions (visual style, core content, interaction needs); AI output a deployable static page in one go
- **Result**: From "I want a homepage" to a previewable page, entire process under 10 minutes of dialogue

### Case 2: Data Dashboard — L6 Deep Research Meal

- **Scenario**: Team needed a real-time data monitoring dashboard (API integration + charts + alerts)
- **Meal selected**: L6 Deep Research Meal (research-driven, multi-round iteration)
- **Flow**: Order → Triple parallel research (tech stack / data architecture / visualization approach) → Research report synthesis → Triple-path divergence development (features / performance / UX) → Cross-validation → Integration testing
- **Key point**: Research phase discovered a data source rate-limiting issue the user hadn't mentioned; cache strategy was designed proactively
- **Result**: Compared to direct development, research-driven approach avoided 2 major rework cycles

### Case 3: Payment Page — L7 Cross-Validation Meal

- **Scenario**: E-commerce payment checkout page, involving payment API integration, form validation, security compliance
- **Meal selected**: L7 Cross-Validation Meal (dual-path parallel + manual arbitration)
- **Flow**: Order → Two independent solution paths (Path A focused on Stripe integration / Path B focused on multi-payment channels) → Structured diff comparison → User selects best solution → Refinement and delivery
- **Key point**: The two paths produced complementary security validation — Path A missed CSRF protection, Path B missed amount tampering detection; merged result had higher security
- **Result**: Cross-validation discovered security blind spots that a single solution couldn't self-check

### Case 4: Progressive Upgrade — Project Growth from L1 to L6

- **Scenario**: User initially built a simple blog page with L1, then progressively upgraded to a full site with CMS, comment system, and SEO optimization
- **Meal evolution**: L1 (static page) → L3 (add dynamic routing) → L5 (integrate CMS API) → L6 (comprehensive research on SEO + performance optimization)
- **Flow**: Each upgrade reused previous preference memory (React preference, dark theme, minimalist style) — no need to re-describe
- **Key point**: Preference memory system made each upgrade's dialogue cost decrease — by L6, all historical preferences were automatically applied
- **Result**: From single page to full site, 4 conversations completed, each under 20 minutes

### Case 5: Research-Driven — Blockchain Explorer

- **Scenario**: Build an on-chain data browser (multi-chain support, contract parsing, transaction tracing)
- **Meal selected**: L6 Deep Research + custom guide injection
- **Flow**: Order → Inject project custom guide (enterprise blockchain development standards) → Triple parallel research (chain node architecture / frontend data visualization / contract ABI parsing approach) → Teaching mode explains research conclusions → User confirms direction → Triple-path divergence development
- **Key point**: Custom guide injection ensured output code complied with internal enterprise standards; Teaching mode helped non-blockchain-background users understand tech selection rationale
- **Result**: Research phase output a complete multi-chain RPC node selection report, which directly became part of the project's technical documentation

---

## 7. v2.0 Update Highlights Comparison

> Order Your Milk v2.0 underwent a comprehensive upgrade over v1.0, with core improvements focused on "lowering the usage barrier + improving output quality".

### v1.0 vs v2.0 Feature Comparison Table

| Dimension | v1.0 | v2.0 | Improvement Notes |
|-----------|------|------|-------------------|
| **Number of meals** | 3 basic meals (L1/L3/L6) | 7 complete meals (L1-L7), including cross-validation L7 | More precise matching of project complexity |
| **Domain templates** | None | 12 frontend domain templates (Web/Mobile/3D/Data Viz, etc.) | Auto-detect domain during ordering, inject specialized guides |
| **Research templates** | Generic triple-path research | Domain-customized research templates (tech selection/competitive analysis/architecture design) | Research output more structured and targeted |
| **Conversation examples** | None | Each meal includes complete conversation examples (ordering→research→execution full flow) | Users can reference examples for quick onboarding |
| **Platform configuration** | None | 6 major platform config guides (Cursor/Windsurf/Claude Code/Codex/Hermes/OpenCode) | One-click adaptation to different AI coding environments |
| **Smart recommendation** | Manual meal selection | Auto-recommend meal + domain template based on requirements description | Reduces decision burden — "just describe your needs" |
| **Preference memory** | None | Cross-session preference persistence (tech stack/style/naming conventions, etc.) | Auto-reuse historical preferences when upgrading projects |
| **Teaching mode** | None | Can enable teaching explanations during research/execution phases | Tech selection has rationale, learn while building |
| **Divergence prompts** | Generic divergence instructions | Meal × domain customized divergence prompts (feature/performance/UX differentiation) | Greater output diversity across paths, higher cross-validation value |
| **Failure degradation** | None | Auto-degrade when meal doesn't match (e.g., L7→L6→L3), with reason explanation | Fallback mechanism to avoid deadlocks |
| **Custom guides** | None | Project-level custom guide injection (enterprise standards/team conventions/special requirements) | Output code directly meets team standards |
| **Quick reference card** | None | One-page quick reference (meal selection/common scenarios/quick entry points) | Find the right starting point in 30 seconds |

### v2.0 Core Improvement Summary

1. **From "usable" to "delightful"** — Smart recommendation + quick reference + conversation examples dramatically lower the barrier for first-time users
2. **From "generic" to "specialized"** — 12 domain templates + customized research templates make output quality domain-aware
3. **From "one-shot" to "continuous"** — Preference memory + progressive upgrade support for continuously improving long-term project experience
4. **From "self-service" to "teaching"** — Teaching mode lets non-technical users understand the rationale behind every decision
5. **From "idealistic" to "robust"** — Failure degradation + custom guide injection cover edge cases in real-world projects
