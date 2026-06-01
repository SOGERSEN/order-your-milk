# Research Prompt Template Library

> Prompt templates used during Step 2 (Research phase). Choose the appropriate template based on the domain.

## General Research Templates

### Pioneer Agent (Deep Dive)

```
You are a deep researcher in {domain}. Please answer the following question in extreme detail, outputting as much content as possible:
- Specific data and facts
- Comparison tables (at least 3 options compared)
- Real-world case studies and code examples
- Common pitfalls and solutions
- Performance data and benchmarks (if available)

If you need the latest information, search before answering.

Question: {question}

At the end of your answer, propose 3 new questions related to the current topic that go even deeper. Mark them with 【Next Question】.
```

### Auxiliary Agent (Lateral Expansion)

```
You are a senior engineer specializing in {domain}. Please answer the following question in extreme detail from the perspective of {angle}:
- Concrete implementation plans and code examples
- Comparison with alternative approaches
- Real-world experience and lessons learned
- Recommended best practices

If you need the latest information, search before answering.

Question: {question}

At the end of your answer, propose 3 new questions related to the current topic that go even deeper. Mark them with 【Next Question】.
```

## Technology Selection Research Template

```
I need to choose a tech stack for a {project type} project. Please conduct an in-depth analysis from the following angles:

1. **Comparison of mainstream options** (at least 3):
   - Option name and core features
   - Strengths and weaknesses
   - Best-fit scenarios
   - Community activity and ecosystem

2. **Performance comparison**:
   - Benchmark data (if available)
   - Memory usage
   - Startup speed
   - Runtime efficiency

3. **Learning curve**:
   - Beginner-friendliness
   - Documentation quality
   - Availability of learning resources

4. **Recommendation**:
   - For {specific scenario}, which option do you recommend?
   - What are the reasons?

Please provide specific comparison tables and supporting data.
```

## Framework/Library Comparison Research Template

```
Please conduct an in-depth comparison of {framework A}, {framework B}, {framework C} across the following dimensions:

| Dimension | {Framework A} | {Framework B} | {Framework C} |
|-----------|---------------|---------------|---------------|
| GitHub Stars | | | |
| Last Updated | | | |
| Package Size | | | |
| Learning Curve | | | |
| Performance | | | |
| Ecosystem/Plugins | | | |
| TypeScript Support | | | |
| Mobile Support | | | |

Please search for the latest data and provide specific numbers and links.
```

## Problem Diagnosis Research Template

```
I'm experiencing the following issue: {problem description}

Please conduct an in-depth analysis from the following angles:

1. **Possible causes** (list all possibilities):
   - Cause 1: ... (Probability: High/Medium/Low)
   - Cause 2: ...

2. **Diagnostic methods**:
   - How to confirm which cause is the issue?
   - What should be checked?

3. **Solutions**:
   - Solution A: ... (Recommendation: ⭐⭐⭐)
   - Solution B: ... (Recommendation: ⭐⭐)

4. **Preventive measures**:
   - How to prevent this issue from recurring?

Please provide specific commands, code, and configuration examples.
```

## Best Practices Research Template

```
What are the best practices for {technology/framework}? Please answer in extreme detail:

1. **Project structure**:
   - Recommended directory structure
   - File naming conventions
   - Module organization principles

2. **Coding standards**:
   - Naming conventions
   - Code style
   - Documentation standards

3. **Performance optimization**:
   - Common performance bottlenecks
   - Optimization techniques
   - Caching strategies

4. **Security practices**:
   - Common security vulnerabilities
   - Protective measures
   - Security checklist

5. **Testing strategy**:
   - Test types (unit/integration/E2E)
   - Recommended testing tools
   - Test coverage targets

Please provide specific code examples and configuration files.
```

## Research Depth Selection Guide

| User Intent | Depth | Agents | Rounds |
|------------|-------|--------|--------|
| "Help me learn about XX" | Shallow | 1-2 | 3-5 rounds |
| "Help me choose an approach" | Medium | 3 | 5-10 rounds |
| "Deep dive into XX" | Deep | 3 | 10-20 rounds |
| "Help me create a research report on XX" | Deep | 3 | 15-30 rounds |
