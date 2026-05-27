<script setup>
import Quiz from '../../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'Which of the following is NOT a conflict type listed in the syllabus?',
    options: [
      'Subject matter conflict',
      'Interest conflict',
      'Budget conflict',
      'Relationship conflict',
    ],
    answer: 2,
    explanation: 'The syllabus lists six conflict types: subject matter, data, interest, value, relationship, and structural conflict. "Budget conflict" is not specifically listed.',
  },
  {
    text: 'What are the four tasks for identifying and resolving conflicts according to the syllabus?',
    options: [
      'Detect, analyze, resolve, document',
      'Plan, execute, review, close',
      'Escalate, negotiate, compromise, accept',
      'Identify, prioritize, implement, verify',
    ],
    answer: 0,
    explanation: 'The four tasks are: conflict identification, conflict analysis, conflict resolution, and documentation of conflict resolution (decisions made).',
  },
  {
    text: 'Which of the following is an important aspect of requirements validation?',
    options: [
      'Validation should be performed only once, at the end of the project',
      'The same person should both identify and correct defects simultaneously',
      'Validation should be done from different views and should be repeated',
      'Only the project manager should validate requirements',
    ],
    answer: 2,
    explanation: 'Important aspects include: involving the right stakeholders, separating identification from correction of defects, validation from different views, and repeated validation.',
  },
  {
    text: 'The syllabus classifies validation techniques into which two main categories?',
    options: [
      'Manual and automated techniques',
      'Review techniques and exploratory techniques',
      'Formal and informal techniques',
      'Static and dynamic techniques',
    ],
    answer: 1,
    explanation: 'Validation techniques are classified into review techniques (walkthroughs, inspections) and exploratory techniques (prototyping, alpha/beta testing, A/B testing, MVP, sample development).',
  },
]
</script>

# EU 4: Resolving Conflicts and Validation of Requirements

::: info Official Reference
**IREB CPRE-FL Syllabus v3.3.0** — Educational Unit 4, Sections 4.3-4.4 (L2)
[Download syllabus](https://cpre.ireb.org/en/downloads-and-resources/downloads)
:::

See also: [Sources and Elicitation](04a-sources-and-elicitation)

## 4.3 Resolving Conflicts regarding Requirements (L2)

Elicitation techniques alone do not ensure that the resulting set of requirements is consistent, complete, or conformant. All stakeholders must understand and **agree** on all requirements relevant to them. When stakeholders do not agree, this is a **conflict** that should be resolved.

### Four Tasks for Conflict Resolution

1. **Conflict identification** — recognizing that a conflict exists
2. **Conflict analysis** — understanding the nature and causes of the conflict
3. **Conflict resolution** — applying appropriate techniques to resolve it
4. **Documentation** — recording the decisions made

### Types of Conflict

| Conflict Type | Description |
|--------------|-------------|
| **Subject matter** | Disagreement about the content or substance of a requirement |
| **Data** | Different data or facts are used as the basis for decisions |
| **Interest** | Stakeholders have competing interests or priorities |
| **Value** | Stakeholders have different fundamental values or beliefs |
| **Relationship** | Personal tensions or communication problems between stakeholders |
| **Structural** | Organizational or power structures cause the conflict |

### Conflict Resolution Techniques

**Common techniques:**

| Technique | Description |
|-----------|-------------|
| **Agreement** | All parties reach a shared decision they all accept |
| **Compromise** | Each party gives up something to reach a mutually acceptable solution |
| **Voting** | A democratic decision by majority |
| **Overruling** | A person with authority makes the decision |
| **Definition of variants** | Multiple solution variants are defined to accommodate different needs |

**Auxiliary techniques:**

- **Consider-all-facts** — systematically listing all relevant facts
- **Plus-minus-interesting** — evaluating positive, negative, and interesting aspects
- **Decision matrix** — scoring options against weighted criteria

## 4.4 Validation of Requirements (L2)

Validating requirements is an important step toward a successful system (Principle 6 — Validation). Ensuring quality up front reduces wasted effort downstream. Validation means checking work products and individual requirements for **quality** (see the quality criteria in Section 3.8).

### Four Important Aspects of Validation

1. **Involvement of the right stakeholders** — those who can judge whether requirements correctly reflect needs
2. **Separating identification and correction of defects** — find problems first, fix them separately
3. **Validation from different views** — different stakeholders catch different types of issues
4. **Repeated validation** — validate at multiple points during the project, not just once

### Validation Techniques

| Category | Techniques | Description |
|----------|-----------|-------------|
| **Review techniques** | Walkthroughs, Inspections | Systematic examination of work products |
| **Exploratory techniques** | Prototyping, Alpha/Beta testing, A/B testing, Minimum Viable Product (MVP), Sample development | Exploring requirements by building and testing |

These techniques differ in **formality** and **effort**. The choice depends on:

- The software development life cycle model
- The maturity of the development process
- The complexity and risk level of the system
- Legal or regulatory requirements
- The need for an audit trail

::: warning Exam Distinction
**Walkthroughs** are informal to semi-formal: the author leads reviewers through the document. **Inspections** are formal: defined roles (moderator, author, reviewers, scribe), mandatory preparation, and a structured defect-detection process.
:::

## Practice Quiz

<Quiz :questions="questions" />
