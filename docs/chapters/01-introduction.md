<script setup>
import Quiz from '../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'Which of the following correctly lists the three kinds of requirements according to IREB?',
    options: [
      'User stories, epics, and acceptance criteria',
      'Functional requirements, quality requirements, and constraints',
      'Business requirements, system requirements, and user requirements',
      'Mandatory requirements, optional requirements, and deferred requirements',
    ],
    answer: 1,
    explanation: 'IREB distinguishes three kinds of requirements: functional requirements (what a system does), quality requirements (how well it does it), and constraints (limits on the solution space).',
  },
  {
    text: 'Which of the following is a typical symptom of inadequate Requirements Engineering?',
    options: [
      'Too many stakeholders are identified',
      'Requirements are documented too early in the project',
      'The assumption that the requirements are self-evident',
      'The development team uses agile methods',
    ],
    answer: 2,
    explanation: 'The syllabus lists four typical causes of inadequate RE: rushing into building the system, communication problems, assuming requirements are self-evident, and inadequate RE education and skills.',
  },
  {
    text: 'What are the major tasks in Requirements Engineering?',
    options: [
      'Planning, designing, coding, and testing',
      'Elicitation, documentation, validation, and management of requirements',
      'Analysis, specification, implementation, and deployment',
      'Interviewing, prototyping, modeling, and reviewing',
    ],
    answer: 1,
    explanation: 'The major tasks in RE are elicitation, documentation, validation, and management of requirements. Requirements analysis and conflict resolution are considered part of elicitation.',
  },
  {
    text: 'Which statement best describes the role of a Requirements Engineer?',
    options: [
      'A job title held exclusively by senior business analysts',
      'A role played by people who elicit, document, validate, and/or manage requirements as part of their duties',
      'A developer who also writes user stories',
      'A project manager responsible for scheduling requirements workshops',
    ],
    answer: 1,
    explanation: 'Requirements Engineer is typically a role, not a job title. People such as business analysts, product owners, systems engineers, and even developers may act in this role.',
  },
]
</script>

# EU 1: Introduction and Overview of Requirements Engineering

::: info Official Reference
**IREB CPRE-FL Syllabus v3.3.0** — Educational Unit 1 (L2, 1 hour)
[Download syllabus](https://cpre.ireb.org/en/downloads-and-resources/downloads)
:::

<div class="exam-tip">
  <strong>Exam weight:</strong> ~5.7% of points (3 questions, 4 points). Focus on definitions and the major RE tasks.
</div>

## 1.1 Requirements Engineering: What (L1)

People and organizations have desires and needs for new things to be built or existing things to be evolved. We call such needs **requirements**.

The things to be built or evolved may be:

- Products provided to customers
- Services made available to customers
- Devices, procedures, or tools that help achieve a specific goal
- Compositions or components of the above

All these things can be considered as **systems**. **Stakeholders** are persons or organizations who influence the requirements for a system or who are impacted by that system.

<div class="key-concept">

The goal of **Requirements Engineering (RE)** is to specify and manage requirements for systems such that the systems implemented and deployed satisfy their stakeholders' desires and needs.

</div>

Requirements are documented in a **requirements specification** — a work product that records the requirements for a system.

### Three Kinds of Requirements

RE distinguishes three kinds of requirements:

| Kind | Description | Example |
|------|-------------|---------|
| **Functional requirements** | Concern a result or behavior that shall be provided by a function of the system, including requirements for data or interaction with the environment | "The system shall allow users to search products by name." |
| **Quality requirements** | Pertain to quality concerns not covered by functional requirements — such as performance, availability, security, or reliability | "The search page shall load within 2 seconds under normal load." |
| **Constraints** | Limit the solution space beyond what is necessary to meet functional and quality requirements | "The system shall use the company's existing Oracle database." |

::: warning Common Exam Trap
A quality requirement describes *how well* the system performs. A constraint *restricts* how the system is built. "Response time < 2 seconds" is a quality requirement. "Must use Java" is a constraint.
:::

## 1.2 Requirements Engineering: Why (L2)

Adequate RE adds value in the process of developing and evolving a system:

- **Reducing the risk** of developing the wrong system
- **Better understanding** of the problem
- **Basis for estimating** development effort and cost
- **Prerequisite for testing** the system

### Symptoms of Inadequate RE

Typical symptoms of inadequate RE are missing, unclear, or incorrect requirements. This is particularly due to:

1. **Rushing straight into building** the system
2. **Communication problems** between involved parties
3. **The assumption** that the requirements are self-evident
4. **Inadequate RE education** and skills

<div class="example-box">

A team jumps directly into coding a new e-commerce platform without eliciting requirements. After six months, user acceptance testing reveals that the payment module does not support the international currencies the business needs. The cost to rework this is far greater than the cost of proper upfront RE would have been.

</div>

## 1.3 Requirements Engineering: Where (L2)

RE can be applied to requirements for any kind of system. However, the dominant application case today is systems in which software plays a major role — typically consisting of software components, physical elements, and organizational elements.

Requirements can occur as:

- **System requirements** — what a system shall do
- **Stakeholder requirements** — what stakeholders want from their perspective
- **User requirements** — what users want from their perspective
- **Domain requirements** — required domain properties
- **Business requirements** — business goals, objectives, and needs of an organization

## 1.4 Requirements Engineering: How (L1)

The major tasks in RE are:

1. **Elicitation** — discovering and gathering requirements (covered in EU 4)
2. **Documentation** — recording requirements in work products (covered in EU 3)
3. **Validation** — checking that requirements correctly reflect stakeholder needs (covered in EU 4)
4. **Management** — storing, changing, and tracing requirements (covered in EU 6)

**Tool support** (EU 7) may help perform these tasks. Requirements analysis and conflict resolution are considered part of elicitation.

::: info Key Point
In order to perform RE activities properly, a suitable RE process must be tailored from a broad range of possibilities (EU 5). There is no one-size-fits-all RE process.
:::

## 1.5 The Role and Tasks of a Requirements Engineer (L1)

**Requirements Engineer** is typically not a job title, but a role played by people who:

- Elicit, document, validate, and/or manage requirements as part of their duties
- Have in-depth knowledge of RE
- Can bridge the gap between the problem and potential solutions

In practice, business analysts, application specialists, product owners, systems engineers, and even developers act in the role of a Requirements Engineer.

## 1.6 What to Learn about Requirements Engineering (L1)

This syllabus covers the foundational skill set that a Requirements Engineer must learn:

| Educational Unit | What You'll Learn |
|-----------------|-------------------|
| EU 2 | The fundamental principles of RE |
| EU 3 | How to document requirements in various forms |
| EU 4 | How to elaborate requirements with various practices |
| EU 5 | How to define and work with suitable RE processes |
| EU 6 | How to manage existing requirements |
| EU 7 | How to employ tool support |

## Practice Quiz

<Quiz :questions="questions" />
