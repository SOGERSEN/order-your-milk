# Domain-Specific Ordering Dimension Templates

> Different domains require different questions when "ordering." Here are the standard dimensions for each domain. Each dimension includes a **recommended default value** — use it when the user can't decide.

---

## 1. General Web Project

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Type | What type? | Showcase / Functional / Utility | Functional |
| Style | What visual style? | Clean & Minimal / Tech & Cool / Professional Business / Playful & Cute | Clean & Minimal |
| Tech | What tech stack? | Pure Frontend / With Backend / You decide | Pure Frontend |
| Scope | How large? | Single Page / Multi-page (3-5) / Full Application | Single Page |
| Responsive | Mobile-friendly? | Required / Desktop-first / Doesn't matter | Required |

**Typical Decision Paths**:
- Personal tool → Utility + Pure Frontend + Single Page + Clean & Minimal
- Company website → Showcase + With Backend + Multi-page + Professional Business
- Internal system → Functional + With Backend + Full Application + Clean & Minimal

---

## 2. Login/Registration Page

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Login method | Which login methods? | Username & Password / Social Login / Phone Verification / All of them | Username & Password |
| Security level | Security protection? | Basic / Standard / Advanced | Standard |
| Registration | Need registration? | Yes / No | Yes |
| Remember me | Remember password? | Yes / No | Yes |
| MFA | Need MFA? | No / Email OTP / TOTP | No |

**Typical Decision Paths**:
- Internal tool → Username & Password + Basic + No registration
- User-facing product → All of them + Standard + Yes registration + Yes remember me
- High-security scenario → Username & Password + Advanced + MFA (TOTP)

---

## 3. Data Dashboard

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Data source | Where does data come from? | API / CSV file / Mock data | API |
| Chart types | What charts? | Line / Bar / Pie / Map / All of them | Line + Bar |
| Interactivity | Need interaction? | Display only / Filterable / Drill-down | Filterable |
| Real-time | Real-time updates? | Real-time / Periodic refresh / Static | Periodic refresh |
| Layout | Layout style? | Fixed grid / Free drag / Responsive | Responsive |

**Typical Decision Paths**:
- Business monitoring → API + Line+Bar + Filterable + Real-time + Responsive
- Data reporting → CSV + Pie+Bar + Display only + Static + Fixed grid
- Analytics platform → API + All of them + Drill-down + Periodic refresh + Free drag

---

## 4. Python Script/Tool

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Purpose | What's it for? | Data processing / Automation / File operations / API calls | Data processing |
| Input | What's the input? | File / CLI arguments / Interactive | File |
| Output | What's the output? | File / Terminal output / Charts | File |
| Packaging | Package as executable? | Yes (.exe) / No | No |
| Dependency mgmt | How to manage deps? | requirements.txt / uv / poetry | uv |

**Typical Decision Paths**:
- Data cleaning → Data processing + File input + File output + requirements.txt
- DevOps script → Automation + CLI arguments + Terminal output + No packaging
- One-off analysis → Data processing + Interactive + Charts + No packaging

---

## 5. API/Backend Service

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Framework | Which framework? | FastAPI / Express / Flask / You decide | FastAPI |
| Database | Which database? | SQLite / PostgreSQL / MongoDB / None | SQLite |
| Auth | Need user auth? | JWT / Session / None | JWT |
| Docs | Need API docs? | Swagger / None | Swagger |
| Deployment | How to deploy? | Docker / Direct run / Serverless | Docker |

**Typical Decision Paths**:
- MVP prototype → FastAPI + SQLite + JWT + Swagger + Direct run
- Production service → FastAPI + PostgreSQL + JWT + Swagger + Docker
- Lightweight microservice → FastAPI + None + None + Swagger + Serverless

---

## 6. CLI Command-Line Tool

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Language | Which language? | Python / Node.js / Go | Python |
| Interaction | Need interactive UI? | CLI arguments / Interactive menu / Both | CLI arguments |
| Distribution | How to distribute? | Direct run / pip package / Executable | pip package |
| Config | Config method? | CLI arguments / Config file / Env vars / All of them | All of them |
| Help docs | Need help docs? | Auto-generated / Manual / None | Auto-generated |

**Typical Decision Paths**:
- Developer tool → Python + CLI arguments + pip package + All of them + Auto-generated
- DevOps script → Python + Interactive menu + Direct run + Config file + Auto-generated
- High-perf tool → Go + CLI arguments + Executable + Env vars + Auto-generated

---

## 7. Data Visualization

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Chart type | What charts? | Bar / Line / Scatter / Heatmap / Map | Bar + Line |
| Interactivity | Need interaction? | Static / Hover tooltip / Zoomable / Filterable | Hover tooltip |
| Tech | Which library? | D3.js / Chart.js / ECharts / You decide | ECharts |
| Data volume | How much data? | <100 records / 100-10K / >10K | 100-10K |
| Export | Need export? | PNG / SVG / PDF / None | PNG |

**Typical Decision Paths**:
- Data report → Bar+Pie + Static + ECharts + <100 records + PDF
- Interactive analysis → Scatter+Heatmap + Zoomable+Filterable + D3.js + >10K + SVG
- Real-time monitoring → Line + Hover tooltip + ECharts + 100-10K + None

---

## 8. Game/Interactive App

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Type | What type? | Puzzle / Action / Strategy / Simulation | Puzzle |
| Platform | Where to run? | Browser / Mobile / Desktop | Browser |
| Tech | What to use? | Canvas / HTML5 / Three.js (3D) | Canvas |
| Difficulty | Game difficulty? | Easy / Medium / Hard / Adaptive | Medium |
| Multiplayer | Multiplayer support? | Single player / Two player / Online multiplayer | Single player |

**Typical Decision Paths**:
- Mini-game demo → Puzzle + Browser + Canvas + Easy + Single player
- 3D experience → Simulation + Browser + Three.js + Medium + Single player
- Social game → Strategy + Browser + HTML5 + Medium + Online multiplayer

---

## 9. AI/LLM Application 🆕

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Model choice | Which model? | GPT-4o / Claude / Open-source (local) / Multi-model routing | GPT-4o |
| Interaction | How to interact? | Chat-based / Completion-based / Both | Chat-based |
| Context mgmt | How to manage context? | Single-turn / Multi-turn / Persistent memory | Multi-turn |
| Output format | What output format? | Plain text / Structured JSON / Streaming / Markdown | Streaming |
| Deployment | How to deploy? | API backend / Web UI / Embed in existing system / CLI | Web UI |
| Security | Need security? | Prompt injection protection / Output filtering / Content moderation / All of them | Prompt injection protection + Output filtering |
| Cost control | Token cost control? | Unlimited / Rate limiting / Cache optimization / Model fallback | Cache optimization |

**Typical Decision Paths**:
- Customer service bot → GPT-4o + Chat-based + Multi-turn + Streaming + Web UI + All of them
- Code assistant → Claude + Completion-based + Single-turn + Structured JSON + Embed in existing system + Prompt injection protection
- Private deployment → Open-source (local) + Chat-based + Persistent memory + Streaming + API backend + All of them
- Multi-model platform → Multi-model routing + Chat-based + Multi-turn + Streaming + Web UI + Cache optimization

---

## 10. Mobile H5 Application 🆕

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Framework | Which framework? | Native H5 / uni-app / React Native Web / Flutter Web | uni-app |
| Adaptation | How to adapt? | Responsive / Mobile-first / Fixed width (375) | Mobile-first |
| Performance | Performance strategy? | Lazy loading / Offline cache / Image compression / All of them | Lazy loading + Image compression |
| Push notifications | Need push? | Browser notification / SMS / None | None |
| Payment | Need payment? | WeChat Pay / Alipay / None | None |
| Native features | Need native features? | Camera / Location / Contacts / None | None |
| Packaging | How to publish? | H5 link / App shell package / Mini program | H5 link |

**Typical Decision Paths**:
- Event page → Native H5 + Mobile-first + Lazy loading + None + H5 link
- E-commerce H5 → uni-app + Mobile-first + All of them + Browser notification + WeChat Pay + Alipay + App shell package
- Internal tool H5 → uni-app + Responsive + Lazy loading + None + Mini program
- Cross-platform app → uni-app + Mobile-first + All of them + Camera + Location + App shell package

---

## 11. Automation/Workflow 🆕

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Trigger | How to trigger? | Scheduled (cron) / Event-driven / Manual / All of them | Scheduled (cron) |
| Data source | Where does data come from? | Local file / API / Database / Message queue | API |
| Data processing | How to process? | Convert format / Filter & clean / Aggregate & stats / Complex logic | Convert format |
| Notification | Who to notify? | Email / Instant message (Feishu/DingTalk) / Log / Webhook | Log + Instant message |
| Error handling | What if it fails? | Auto-retry / Alert notification / Ignore & continue / Dead-letter queue | Auto-retry + Alert notification |
| Execution env | Where to run? | Local script / Cron container / Serverless / Workflow platform | Cron container |
| Monitoring | Need monitoring? | Run logs / Execution stats / Health check / None | Run logs + Health check |

**Typical Decision Paths**:
- Data sync → Scheduled + API + Convert format + Log + Auto-retry + Cron container
- Monitoring alerts → Event-driven + API + Filter & clean + Instant message + Alert notification + Serverless
- Batch job → Scheduled + Local file + Aggregate & stats + Email + Auto-retry + Alert notification + Cron container
- Complex orchestration → All of them + Message queue + Complex logic + Webhook + Dead-letter queue + Workflow platform

---

## 12. Data Science/ML Project 🆕

| Dimension | Question | Options | Recommended Default |
|-----------|----------|---------|-------------------|
| Data format | What format? | CSV / JSON / Database / Image/Audio / Stream | CSV |
| Task type | What task? | Classification / Regression / Clustering / NLP / Recommendation / Time series | Classification |
| Framework | Which framework? | scikit-learn / PyTorch / TensorFlow / HuggingFace | scikit-learn |
| Data scale | How much data? | <10K records / 10K-1M / >1M | <10K records |
| Model output | What output? | Evaluation report / Model file / Prediction API / Visualization dashboard | Evaluation report + Model file |
| Experiment mgmt | Need experiment tracking? | MLflow / W&B / Simple logs / None | Simple logs |
| Deployment | How to deploy model? | API service / Edge deployment / Embed in app / No deployment | API service |

**Typical Decision Paths**:
- Data exploration → CSV + Clustering + scikit-learn + <10K + Evaluation report + Visualization dashboard + Simple logs
- Production classifier → CSV/Database + Classification + PyTorch + 10K-1M + Model file + Prediction API + MLflow + API service
- NLP project → JSON + NLP + HuggingFace + 10K-1M + Model file + W&B + API service
- Quick prototype → CSV + Regression + scikit-learn + <10K + Evaluation report + None + No deployment

---

## Auto-Answer Templates

When the user says "you decide", "don't know", "help me choose", use these defaults:

### Universal Defaults (apply to all projects)

| Dimension | Default Recommendation | Reason |
|-----------|----------------------|--------|
| Type | Functional | Broadest coverage |
| Style | Clean & Minimal | Safest bet |
| Tech | Pure Frontend | Zero barrier, double-click to use |
| Scope | Single Page | Fast delivery, expand as needed |
| Responsive | Required | Modern baseline requirement |

### Domain-Specific Defaults

| Domain | Key Dimension(s) | Default Recommendation | Reason |
|--------|-----------------|----------------------|--------|
| Login/Registration | Login method | Username & Password | Most fundamental, most reliable |
| Data Dashboard | Data source + Interactivity | API + Filterable | Most common real-world scenario |
| Python Script | Purpose + Dependency mgmt | Data processing + uv | uv is modern Python standard |
| API Backend | Framework + Database | FastAPI + SQLite | Fastest startup, built-in docs |
| CLI Tool | Language + Distribution | Python + pip package | Richest ecosystem |
| Data Visualization | Tech + Interactivity | ECharts + Hover tooltip | Chinese-friendly, feature-complete |
| Game/Interactive | Type + Tech | Puzzle + Canvas | Lowest development complexity |
| AI/LLM Application | Model + Interaction | GPT-4o + Chat-based + Streaming | Most mature API + best UX |
| Mobile H5 | Framework + Adaptation | uni-app + Mobile-first + H5 link | Best cross-platform capability, highest dev efficiency |
| Automation/Workflow | Trigger + Error handling | Scheduled (cron) + Auto-retry + Log | Most reliable runtime pattern |
| Data Science/ML | Framework + Output | scikit-learn + Evaluation report + Simple logs | Lowest learning curve, fast validation |

### Quick Decision Matrix

When the user only gives a one-sentence description, use keyword matching to quickly identify the domain:

| Keywords User Mentions | Recommended Domain | Quick Template |
|----------------------|-------------------|---------------|
| "webpage", "website", "page" | General Web | Functional + Clean & Minimal + Pure Frontend |
| "login", "register", "user system" | Login/Registration | Username & Password + Standard security |
| "kanban", "dashboard", "data display" | Data Dashboard | API + Line+Bar + Filterable |
| "script", "automation", "process data" | Python Script | Data processing + File input + uv |
| "API", "backend", "interface" | API Backend | FastAPI + SQLite + JWT |
| "command line", "tool", "CLI" | CLI Tool | Python + CLI arguments + pip package |
| "chart", "visualization", "graph" | Data Visualization | ECharts + Hover tooltip + PNG export |
| "game", "mini-game", "interactive" | Game/Interactive | Puzzle + Canvas + Single player |
| "AI", "LLM", "chat", "GPT", "model" | AI/LLM Application | GPT-4o + Chat-based + Streaming + Web UI |
| "mobile", "H5", "smartphone", "mini program" | Mobile H5 | uni-app + Mobile-first + H5 link |
| "scheduled", "workflow", "automation", "sync" | Automation/Workflow | Scheduled (cron) + Auto-retry + Log |
| "machine learning", "model", "training", "prediction", "analysis" | Data Science/ML | scikit-learn + Classification + Evaluation report |
