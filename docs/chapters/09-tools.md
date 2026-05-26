<script setup>
import Quiz from '../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'Which of the following is a typical function of a dedicated RE tool?',
    options: [
      'Compiling source code',
      'Managing requirements attributes, traceability, and baselines',
      'Running automated tests',
      'Designing system architecture',
    ],
    answer: 1,
    explanation: 'Dedicated RE tools focus on managing requirements: storing them with attributes, establishing traceability links, maintaining baselines, supporting change management, and generating reports.',
  },
  {
    text: 'What is a key risk of introducing an RE tool?',
    options: [
      'It automatically makes requirements perfect',
      'The tool can become the focus rather than the RE process — a bad process with a tool is still a bad process',
      'RE tools are too simple to be useful',
      'Tools eliminate the need for stakeholder communication',
    ],
    answer: 1,
    explanation: 'A tool supports the process but cannot fix a broken process. Organizations sometimes focus on tool selection while neglecting process improvement. "A fool with a tool is still a fool."',
  },
  {
    text: 'Which type of tool is LEAST suited for managing requirements in a large project?',
    options: [
      'Dedicated RE management tool (e.g., DOORS, Jama)',
      'Spreadsheet (e.g., Excel)',
      'Wiki-based tool with traceability plugins',
      'ALM tool with requirements module (e.g., Azure DevOps)',
    ],
    answer: 1,
    explanation: 'Spreadsheets lack traceability, versioning, multi-user collaboration, and baselining features needed for large projects. They work for small projects but don\'t scale. Dedicated RE tools and ALM tools are designed for this purpose.',
  },
  {
    text: 'What should be considered when evaluating an RE tool for your organization?',
    options: [
      'Only the purchase price',
      'The tool\'s feature set, integration capabilities, team adoption effort, and fit with existing processes',
      'Only whether it supports UML diagrams',
      'Only the vendor\'s market share',
    ],
    answer: 1,
    explanation: 'Tool evaluation should consider features, integration with existing toolchain, cost (purchase + training + maintenance), team readiness, process fit, and vendor support. No single factor is sufficient.',
  },
]
</script>

# Chapter 9: Tool Support

<div class="exam-tip">
  <strong>Exam weight:</strong> ~3% of questions. This is the lightest chapter — know the general categories and evaluation criteria.
</div>

## Why Tool Support?

RE activities generate substantial information that must be stored, organized, traced, and maintained. Tools support this by:

- **Storing** requirements with structured attributes
- **Managing** traceability links between requirements and other artifacts
- **Versioning** requirements and maintaining baselines
- **Searching and filtering** large sets of requirements
- **Reporting** on status, coverage, and progress
- **Collaboration** — enabling multiple team members to work on requirements concurrently

## Types of RE Tools

### 1. Dedicated RE Management Tools

Purpose-built tools for managing requirements throughout their lifecycle.

**Examples:** IBM DOORS, Jama Connect, Helix RM (formerly Caliber)

**Features:**
- Requirement storage with rich attributes
- Traceability matrices
- Baseline management
- Impact analysis
- Workflow and approval processes
- Reporting and dashboards

**Best for:** Large, complex, or regulated projects where traceability and formal change management are critical.

### 2. ALM / Issue Tracking Tools

Application Lifecycle Management tools that include requirements management as one capability among many.

**Examples:** Azure DevOps, Jira (with plugins), Polarion

**Features:**
- Requirements linked to tasks, tests, and defects
- Agile board integration
- CI/CD pipeline integration
- Lightweight traceability

**Best for:** Agile teams that want requirements integrated with their development workflow.

### 3. Modeling Tools

Tools for creating and managing requirement models (UML, BPMN, SysML).

**Examples:** Enterprise Architect, Camunda Modeler, draw.io

**Features:**
- Graphical diagram editors
- Model consistency checking
- Code generation (some tools)
- Model simulation

**Best for:** Projects with significant modeling needs (embedded systems, complex business processes).

### 4. General-Purpose Tools

Tools not specifically designed for RE but commonly used for it.

**Examples:** Microsoft Word, Excel, Confluence, Google Docs

**Features:**
- Familiar to all users
- No special training needed
- Flexible formatting

**Limitations:**
- No built-in traceability
- No baselining or versioning (beyond document versions)
- No structured attributes
- Poor scalability for large requirement sets
- Concurrent editing issues (Word/Excel)

**Best for:** Small projects, early-stage projects, or organizations just starting with RE.

### Tool Category Comparison

| Capability | Dedicated RE Tool | ALM Tool | Modeling Tool | General-Purpose |
|-----------|-------------------|----------|---------------|-----------------|
| Requirement storage | Excellent | Good | Limited | Basic |
| Traceability | Excellent | Good | Limited | Manual |
| Baselining | Excellent | Moderate | None | Manual |
| Modeling | Limited | Limited | Excellent | None |
| Collaboration | Good | Excellent | Moderate | Variable |
| Learning curve | Steep | Moderate | Moderate | Flat |
| Cost | High | Moderate | Variable | Low/Free |

## Tool Evaluation and Introduction

### Evaluation Criteria

When selecting an RE tool, consider:

| Criterion | Questions to Ask |
|-----------|-----------------|
| **Features** | Does it support the RE activities we need? |
| **Integration** | Does it connect with our existing tools (Jira, Git, CI/CD)? |
| **Scalability** | Can it handle our project size and team count? |
| **Usability** | Will the team actually use it, or is it too complex? |
| **Cost** | Purchase/license + training + maintenance — is the total cost justified? |
| **Process fit** | Does it match our existing processes, or will we need to change them? |
| **Vendor** | Is the vendor stable? Good support? Active development? |
| **Migration** | Can we import existing requirements? Can we export if we switch? |

### Introduction Strategy

<div class="key-concept">

Introducing an RE tool is a **change management challenge**, not just a technical one. Steps:

1. **Define goals** — what specifically should the tool improve?
2. **Evaluate options** — assess against criteria above
3. **Pilot** — try the tool on a small project first
4. **Train** — ensure the team knows how to use it effectively
5. **Roll out gradually** — don't force a full organization switch overnight
6. **Measure** — track whether the tool is delivering the expected benefits

</div>

::: warning Key Principle
"A fool with a tool is still a fool." A tool cannot fix a broken process. Ensure your RE process is sound *before* investing in expensive tooling. Conversely, a good tool amplifies a good process.
:::

### Common Pitfalls

- **Over-investing in tools before establishing a process** — the tool becomes "shelfware"
- **Choosing the most feature-rich tool** when a simpler one would suffice
- **Underestimating training and adoption costs** — the tool is only useful if people use it correctly
- **Forcing all projects into one tool** — different project types may need different approaches

## Practice Quiz

<Quiz :questions="questions" />

---

**Previous:** [← Chapter 8: Requirements Management](/chapters/08-management)
| **Return to:** [Home →](/)
