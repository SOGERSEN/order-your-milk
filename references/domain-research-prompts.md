# Domain-Specific Research Prompt Template Library

> **Domain-specific** prompt templates for Step 2 (Research phase). Relationship with `research-prompts.md`:
>
> - `research-prompts.md` = **General templates**, applicable to any domain (Pioneer/Auxiliary general framework, technology selection, problem diagnosis, etc.)
> - This file = **Domain-specific templates**, tailored for deep research in specific technical domains — only insiders know what to ask
>
> **Usage tip**: First determine which domain the project belongs to, then use the corresponding domain template from this file to replace the general template. If the project spans multiple domains (e.g., "frontend + AI"), you can combine templates from multiple domains.
>
> **Note**: This file contains only the **Pioneer (deep drill)** prompt per domain. For Application auxiliary and Pitfalls auxiliary prompts, use the general templates in `research-prompts.md` and adapt them to your domain.

---

## How to Choose a Template

| Project Characteristics | Domain | Template Section |
|------------------------|--------|-----------------|
| Websites, Web Apps, Mini Programs, H5 pages | Web Frontend Development | §1 |
| API services, backend systems, microservices, web scrapers | Python Backend Development | §2 |
| Data analysis, predictive models, recommendation systems | Data Science/ML | §3 |
| AI chat, RAG systems, AI applications, LLM integration | AI/LLM Applications | §4 |
| App development, cross-platform apps, mobile H5 | Mobile/H5 | §5 |
| Uncertain | Use general templates | `research-prompts.md` |

---

## Common Variable Reference

All templates use the following variable placeholders:

| Variable | Meaning | Example |
|----------|---------|---------|
| `{project name}` | The project the user wants to build | "Online collaborative document editor" |
| `{core features}` | Description of the project's core features | "Real-time multi-user editing, version history, comments" |
| `{tech selection}` | Confirmed or candidate tech stack | "React + TypeScript" |
| `{constraints}` | Special limitations | "Must support IE11", "Limited budget", "Solo developer" |
| `{question}` | Specific research question | "React vs Vue — which to choose?" |

---

## §1 Web Frontend Development

### 1.1 Pioneer Agent — Technical Deep Dive

**Role orientation**: Front-end architect perspective. Deep research into framework selection, performance optimization strategies, and the underlying principles and best practices of the build toolchain.

```
You are a senior front-end architect, well-versed in the underlying principles and engineering practices of mainstream frameworks (React/Vue/Svelte/Angular).
You need to conduct a deep technical research for "{project name}".

Project information:
- Project: {project name}
- Core features: {core features}
- Constraints: {constraints}

Please research the following question in extreme detail: {question}

Research requirements:

1. **Framework selection deep comparison** (if applicable):
   - Architectural philosophy differences between React vs Vue vs Svelte vs Solid
   - Virtual DOM vs compile-time optimization technical route comparison
   - Reactive principles of each framework (Proxy vs Signal vs VDOM diff)
   - Ecosystem maturity: component libraries, state management, routing, SSR solutions
   - 2024-2026 community trends and enterprise adoption

2. **Performance optimization strategies**:
   - First-load optimization (Code Splitting, Tree Shaking, Lazy Loading)
   - Runtime performance (virtual lists, Web Workers, requestIdleCallback)
   - Rendering strategies (CSR vs SSR vs SSG vs ISR vs Streaming SSR)
   - Core Web Vitals optimization techniques for each metric
   - Performance Budget formulation methods

3. **Build toolchain**:
   - Vite vs Turbopack vs Rspack vs esbuild principles and performance comparison
   - Monorepo solutions (Turborepo vs Nx vs pnpm workspace)
   - Build caching strategies in CI/CD
   - Module Federation micro-frontend solutions

Please provide:
- Specific performance data and benchmark comparisons
- Architecture diagrams and flowcharts (described in text)
- Actual code examples
- Recommended scenarios for each option

At the end of your answer, propose 3 deeper new questions, marked with 【Next Question】.
```

**Usage notes**:
- Suitable for the **technology selection phase** of a project, before writing code
- Recommended research depth: Medium (5-15 rounds); framework selection questions typically need 5-8 rounds
- If the project's tech stack is already determined, focus on deep optimization of the specific framework

---

## §2 Python Backend Development

### 2.1 Pioneer Agent — Technical Deep Dive

**Role orientation**: Backend architect perspective. Deep research into framework selection, database ORM, and the underlying principles and best practices of async programming.

```
You are a senior Python backend architect, well-versed in the underlying principles of mainstream frameworks (FastAPI/Django/Flask/Tornado),
with hands-on experience in large-scale distributed systems. You need to conduct deep technical research for "{project name}".

Project information:
- Project: {project name}
- Core features: {core features}
- Constraints: {constraints}

Please research the following question in extreme detail: {question}

Research requirements:

1. **Framework selection deep comparison**:
   - Architectural philosophy of FastAPI vs Django vs Flask vs Starlette
   - Async support: native async/await vs WSGI vs ASGI
   - Performance comparison: RPS (Requests Per Second) benchmark data
   - Ecosystem comparison: ORM, Admin, authentication, API docs, task queues
   - Learning curve and team fit
   - 2024-2026 community trends and enterprise adoption

2. **Database & ORM**:
   - SQLAlchemy 2.0 vs Django ORM vs Tortoise ORM vs Peewee
   - Async ORM choices and limitations
   - Database migration strategies (Alembic vs Django Migrations)
   - Connection pool configuration and optimization (PgBouncer, SQLAlchemy pool)
   - Read-write splitting and database sharding solutions
   - NoSQL integration (Redis, MongoDB, Elasticsearch) best practices

3. **Async programming**:
   - asyncio core principles (event loop, coroutines, Task, Future)
   - Selection strategy: async vs threading vs multiprocessing
   - Async IO libraries: aiohttp vs httpx vs aiofiles
   - Async task queues: Celery vs Dramatiq vs arq vs taskiq
   - Async context managers and semaphores
   - Common async programming pitfalls (blocking calls mixed into async, event loop nesting)

Please provide:
- Performance benchmark data and comparison tables
- Architecture diagrams (described in text)
- Actual code examples
- Production environment configuration recommendations

At the end of your answer, propose 3 deeper new questions, marked with 【Next Question】.
```

**Usage notes**:
- Suitable for the **technology selection and architecture design phase**
- If the project already has a clear tech stack, focus on deep optimization of the specific framework
- Recommended research depth: Medium (5-15 rounds)

---

## §3 Data Science / ML

### 3.1 Pioneer Agent — Technical Deep Dive

**Role orientation**: ML engineer / data scientist perspective. Deep research into model selection, feature engineering strategies, and evaluation metric choices.

```
You are a senior machine learning engineer who has won gold medals on Kaggle,
with full-stack modeling capabilities from traditional ML to deep learning. You need to conduct deep technical research for "{project name}".

Project information:
- Project: {project name}
- Core features: {core features}
- Data characteristics: {constraints} (data volume, feature count, label type, etc.)

Please research the following question in extreme detail: {question}

Research requirements:

1. **Model selection**:
   - Problem type determination: classification/regression/clustering/ranking/generation/anomaly detection
   - Traditional ML: XGBoost vs LightGBM vs CatBoost vs Random Forest
   - Deep learning: MLP vs CNN vs RNN/LSTM vs Transformer (by problem type)
   - Transfer learning strategies with pre-trained models
   - AutoML solutions (AutoGluon, H2O, FLAML) applicable scenarios
   - Model selection decision tree: which model for which data

2. **Feature engineering strategies**:
   - Numerical features: standardization, normalization, binning, log transform, polynomial features
   - Categorical features: One-Hot, Target Encoding, Embedding, frequency encoding
   - Text features: TF-IDF, Word2Vec, BERT Embedding
   - Time series features: sliding windows, lag features, Fourier transform, time decomposition
   - Interaction features and feature selection methods (Filter/Wrapper/Embedded)
   - Automated feature engineering tools (Featuretools, tsfresh)

3. **Evaluation metric selection**:
   - Classification: Accuracy vs Precision vs Recall vs F1 vs AUC-ROC vs AUC-PR
   - Regression: MSE vs RMSE vs MAE vs MAPE vs R²
   - Ranking: NDCG, MAP, MRR
   - Clustering: Silhouette, Calinski-Harabasz, Davies-Bouldin
   - Metric selection guide for different business scenarios
   - Cross-validation strategies (K-Fold, Stratified, Time Series Split)

Please provide:
- Model comparison tables (with performance data)
- Feature engineering pipeline flowchart
- Actual code examples (scikit-learn / PyTorch)
- Recommended scenarios and considerations for each option

At the end of your answer, propose 3 deeper new questions, marked with 【Next Question】.
```

**Usage notes**:
- Suitable for the **problem definition and solution design phase** of a project
- First clarify the problem type and data characteristics, then select the model
- Recommended research depth: Medium (5-15 rounds); model selection may require more rounds

---

## §4 AI/LLM Applications

### 4.1 Pioneer Agent — Technical Deep Dive

**Role orientation**: AI application architect perspective. Deep research into model selection, prompt engineering strategies, and RAG architecture.

```
You are an AI application architect who has deeply used mainstream models including GPT-4o, Claude, Gemini, Llama, Qwen, and others,
having led the technical architecture for multiple RAG, Agent, and AI SaaS products. You need to conduct deep technical research for "{project name}".

Project information:
- Project: {project name}
- Core features: {core features}
- Constraints: {constraints} (budget, latency requirements, data privacy, etc.)

Please research the following question in extreme detail: {question}

Research requirements:

1. **Model selection**:
   - Closed-source model comparison: GPT-4o vs Claude 3.5/4 vs Gemini Pro vs others
   - Open-source model comparison: Llama 3 vs Qwen2.5 vs Mistral vs DeepSeek vs Yi
   - Model capability matrix: reasoning, code, multilingual, long context, multimodal
   - Cost comparison: input/output token pricing, API limits
   - Latency comparison: time to first token, throughput
   - Self-hosted vs API call TCO (Total Cost of Ownership) analysis

2. **Prompt Engineering strategies**:
   - System prompt design principles and templates
   - Few-Shot vs Zero-Shot vs Chain-of-Thought selection
   - Structured output (JSON Mode, Function Calling, Instructor)
   - Prompt template management and version control
   - Automatic prompt optimization (DSPy, OPRO)
   - Multi-turn conversation context management strategies

3. **RAG architecture**:
   - Basic RAG: document chunking → Embedding → vector retrieval → LLM generation
   - Advanced RAG: query rewriting, hybrid retrieval, Reranking
   - Agentic RAG: Agent-driven adaptive retrieval
   - Chunking strategies: fixed-size vs semantic chunking vs recursive chunking
   - Retrieval evaluation metrics: Recall@K, MRR, NDCG
   - RAG vs Fine-Tuning vs Long Context selection decision

Please provide:
- Architecture diagrams and data flow diagrams
- Cost/performance comparison tables for each option
- Actual code examples
- Recommended technical solutions and rationale

At the end of your answer, propose 3 deeper new questions, marked with 【Next Question】.
```

**Usage notes**:
- Suitable for the **technology selection and architecture design phase** of AI applications
- The AI/LLM field changes extremely fast — always search for the latest information during research
- Recommended research depth: Medium (5-15 rounds); RAG architecture may require more rounds

---

## §5 Mobile / H5

### 5.1 Pioneer Agent — Technical Deep Dive

**Role orientation**: Mobile architect perspective. Deep research into framework selection, cross-platform strategies, and performance optimization.

```
You are a senior mobile architect, well-versed in native development (Swift/Kotlin) and cross-platform solutions (React Native/Flutter/uniapp),
having led the technical architecture for apps with tens of millions of users. You need to conduct deep technical research for "{project name}".

Project information:
- Project: {project name}
- Core features: {core features}
- Constraints: {constraints} (target platform, team tech stack, budget, etc.)

Please research the following question in extreme detail: {question}

Research requirements:

1. **Framework selection deep comparison**:
   - React Native vs Flutter vs uniapp vs native development
   - Rendering principles: JS Bridge vs Dart VM vs WebView vs native rendering
   - Performance comparison: startup speed, frame rate, memory usage, package size
   - Development efficiency: hot reload, debugging tools, IDE support
   - Ecosystem comparison: third-party library count, native module calls, community activity
   - Enterprise adoption cases and user scale
   - 2024-2026 trends (KMP, Compose Multiplatform, and other new solutions)

2. **Cross-platform strategies**:
   - Code sharing ratio (100% vs 80% vs 60%)
   - Handling platform-specific code
   - UI consistency vs platform native experience trade-offs
   - Cross-platform state management solutions
   - Cross-platform navigation solutions (React Navigation vs GoRouter vs uni-simple-router)

3. **Performance optimization**:
   - Startup optimization: cold start / warm start optimization techniques
   - Rendering optimization: list scrolling, animation performance, GPU acceleration
   - Memory optimization: image caching, large image handling, memory leak detection
   - Network optimization: request batching, caching strategies, weak network adaptation
   - Package size optimization: dynamic loading, resource compression, on-demand imports
   - Battery optimization: background task management, sensor usage optimization

Please provide:
- Performance benchmark data for each framework
- Architecture diagrams and technical roadmap
- Actual code examples
- Recommended technical solutions and migration paths

At the end of your answer, propose 3 deeper new questions, marked with 【Next Question】.
```

**Usage notes**:
- Suitable for the **technology selection phase before project kickoff**
- Mobile framework selection is very difficult to change once made — research thoroughly
- Recommended research depth: Deep (10-15 rounds) — this decision affects the entire project lifecycle
