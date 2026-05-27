<script setup>
import Quiz from '../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'According to the syllabus, what should Requirements Engineers decide BEFORE selecting a tool?',
    options: [
      'The budget allocated for tool licenses',
      'Which tasks and activities during the RE process should be supported and how',
      'Which programming language the development team will use',
      'How many stakeholders will use the tool',
    ],
    answer: 1,
    explanation: 'Before selecting a tool, Requirements Engineers should decide which tasks and activities during the RE process should be supported and how. The tool should fit the process, not the other way around.',
  },
  {
    text: 'The syllabus differentiates between three categories of tool support. Which is NOT one of them?',
    options: [
      'Management of requirements',
      'Management of the RE process',
      'Documentation of knowledge about the requirements',
      'Automated generation of source code from requirements',
    ],
    answer: 3,
    explanation: 'The three categories are: management of requirements (attributes, prioritization, versions, tracing, changes), management of the RE process (measuring, reporting, workflow), and documentation of knowledge about requirements (sharing, modeling, collaboration, testing/simulation).',
  },
]
</script>

# EU 7: Tool Support

::: info Official Reference
**IREB CPRE-FL Syllabus v3.3.0** — Educational Unit 7 (L2, 1 hour)
[Download syllabus](https://cpre.ireb.org/en/downloads-and-resources/downloads)
:::

<div class="exam-tip">
  <strong>Exam weight:</strong> ~4.3% of points (2 questions, 3 points). Know the three categories of tool support and the key considerations for introducing tools.
</div>

## 7.1 Tools in Requirements Engineering (L1)

The RE process can be supported by tools that cover dedicated tasks and activities. Since the RE process is quite individual (EU 5), existing RE tools often focus only on certain aspects and rarely support all activities.

Before selecting a tool, Requirements Engineers should decide **which tasks and activities** should be supported and **how**.

### Three Categories of Tool Support

**1. Management of requirements:**
- Defining and storing requirements attributes
- Prioritizing requirements
- Managing versions and configurations
- Tracking and tracing requirements
- Managing changes to requirements

**2. Management of the RE process:**
- Measuring and reporting on the RE process
- Measuring and reporting on product quality
- Managing the RE workflow

**3. Documentation of knowledge about the requirements:**
- Sharing requirements
- Creating shared understanding of the requirements
- Modeling of requirements
- Collaboration in RE
- Testing/simulation of requirements

Tools often provide a **mixture** of these features. To ensure all RE tasks are covered, different tools might need to be combined.

::: warning Key Point
General-purpose tools (office or issue tracking tools) are sometimes used for requirements, but they have limitations and should only be used when the RE process is in control and requirements are aligned and quite stable.
:::

## 7.2 Introducing Tools (L2)

Selecting an RE tool is no different from selecting a tool for any other purpose: the **goal, context, and requirements** must be described before selection can be successful.

An appropriate tool can only be sought **once proper RE procedures and techniques have been introduced**. Tool introduction requires clear RE responsibilities and procedures.

### Key Considerations for Tool Introduction

| Consideration | Why It Matters |
|--------------|----------------|
| **All life cycle costs** beyond license costs | Maintenance, training, migration, and integration costs can exceed license costs |
| **Necessary resources** | People, time, and infrastructure needed for adoption |
| **Pilot projects** to avoid risks | Test the tool in a limited scope before full rollout |
| **Evaluation** according to defined criteria | Systematic comparison against requirements ensures the right choice |

<div class="example-box">

A company considering an enterprise RE tool should first establish sound RE practices, then evaluate tools against criteria like: Does it support our traceability needs? Can it integrate with our existing ALM tools? What is the total cost of ownership over 5 years? A pilot project with one team can reveal adoption challenges before a company-wide rollout.

</div>

## Practice Quiz

<Quiz :questions="questions" />
