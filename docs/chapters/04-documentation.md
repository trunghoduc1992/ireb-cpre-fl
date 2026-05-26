<script setup>
import Quiz from '../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'What is the primary purpose of requirements documentation?',
    options: [
      'To provide legal protection for the development team',
      'To serve as a communication medium and basis for agreement between stakeholders',
      'To replace direct communication between stakeholders',
      'To define the system architecture',
    ],
    answer: 1,
    explanation: 'Requirements documentation serves as a shared basis for communication and agreement between all parties. It does not replace direct communication, but supports and records it.',
  },
  {
    text: 'What is the difference between a requirements specification and a system specification?',
    options: [
      'A requirements specification is written by developers; a system specification by BAs',
      'A requirements specification describes the problem (what); a system specification describes the solution (how)',
      'They are different names for the same document',
      'A system specification only contains non-functional requirements',
    ],
    answer: 1,
    explanation: 'The requirements specification describes WHAT the system must do (problem-oriented). The system specification describes HOW the system will do it (solution-oriented). This is a key IREB distinction.',
  },
  {
    text: 'Which of the following is an appropriate way to document requirements?',
    options: [
      'Only in natural language text',
      'Only using formal models',
      'Using a combination of natural language, models, and templates as appropriate',
      'Only in user stories',
    ],
    answer: 2,
    explanation: 'IREB recommends using a combination of documentation forms. Natural language is universally readable, models reduce ambiguity for certain aspects, and templates ensure consistency.',
  },
  {
    text: 'Which document structure standard is commonly referenced for requirements specifications?',
    options: [
      'ISO 9001',
      'IEEE 830 / ISO/IEC/IEEE 29148',
      'PMBOK',
      'TOGAF',
    ],
    answer: 1,
    explanation: 'IEEE 830 (now superseded by ISO/IEC/IEEE 29148) is the classic standard for Software Requirements Specifications (SRS). IREB references this structure as a foundation for documentation.',
  },
  {
    text: 'What are the three forms of requirements documentation according to IREB?',
    options: [
      'User stories, use cases, and acceptance criteria',
      'Natural language, models, and mixed forms',
      'Formal, semi-formal, and informal',
      'Text, diagrams, and spreadsheets',
    ],
    answer: 1,
    explanation: 'IREB identifies three forms: natural language (text), model-based (diagrams/notations), and mixed forms (combining both). Each has strengths and is suited to different aspects.',
  },
]
</script>

# Chapter 4: Documentation Basics

<div class="exam-tip">
  <strong>Exam weight:</strong> Documentation chapters (4–6) together account for ~40% of the exam. This chapter covers fundamentals.
</div>

## Purpose of Requirements Documentation

Requirements documentation serves several purposes:

1. **Communication** — shared understanding between stakeholders, developers, and testers
2. **Agreement** — documented basis for contractual or project commitments
3. **Basis for design** — input for system architecture and detailed design
4. **Basis for testing** — test cases are derived from documented requirements
5. **Change management** — documented requirements can be tracked, versioned, and managed
6. **Organizational memory** — knowledge persists beyond individual team members

<div class="key-concept">

Documentation is not an end in itself. Its value comes from being **read and used** — by developers, testers, project managers, and future maintainers.

</div>

::: tip From Your Experience
As a tester, you know the pain of working from vague requirements. As a BA, you've seen specs that nobody reads. Good documentation strikes a balance: detailed enough to be useful, concise enough to be maintainable.
:::

## Three Forms of Documentation

IREB identifies three forms for documenting requirements:

### 1. Natural Language
Requirements written in everyday language (English, German, etc.).

- **Pro**: Everyone can read it; no special training needed
- **Con**: Prone to ambiguity, incompleteness, and inconsistency

### 2. Model-Based
Requirements expressed using graphical or formal notations (UML diagrams, state machines, etc.).

- **Pro**: Precise, reduces ambiguity for structural and behavioral aspects
- **Con**: Requires training to read and write; not all requirements are easily modeled

### 3. Mixed Forms
A combination of natural language and models — often the most practical approach.

<div class="example-box">

**Practical example — mixed form:**
"When a customer submits an order (see Use Case UC-03), the system shall validate the items against available stock (see Activity Diagram AD-05). If all items are in stock, the order status transitions to 'Confirmed' (see State Machine SM-02)."

This sentence uses natural language as the backbone and references models for precision.
</div>

## Requirements Specification vs. System Specification

<div class="key-concept">

This is a critical distinction for the exam:

- **Requirements Specification** — describes WHAT the system must do from the **user/stakeholder perspective** (problem-oriented)
- **System Specification** — describes HOW the system will behave from the **developer perspective** (solution-oriented)

</div>

| Aspect | Requirements Specification | System Specification |
|--------|---------------------------|---------------------|
| **Perspective** | User / stakeholder | Developer / architect |
| **Focus** | Problem domain (what) | Solution domain (how) |
| **Audience** | Stakeholders, testers, managers | Developers, architects |
| **Detail level** | Abstract, external behavior | Concrete, internal behavior |
| **Example** | "Users shall be able to search products" | "Search uses Elasticsearch with fuzzy matching on product name and description fields" |

::: warning Exam Trap
Don't confuse these two. A common exam question gives a statement and asks whether it belongs in a requirements specification or a system specification. If it mentions *internal implementation details*, it's a system specification.
:::

## Document Structure

A well-structured requirements document typically follows a standard layout. The IEEE 830 / ISO/IEC/IEEE 29148 standard provides a reference structure:

### Typical Structure of a Requirements Specification

1. **Introduction**
   - Purpose and scope
   - Definitions, acronyms, glossary references
   - References to related documents
   
2. **Overall Description**
   - Product perspective (context)
   - Product functions (summary)
   - User characteristics
   - Constraints
   - Assumptions and dependencies
   
3. **Specific Requirements**
   - Functional requirements (organized by feature, use case, or user class)
   - Quality requirements (performance, security, usability, etc.)
   - Interface requirements (external systems, hardware, communication)
   - Constraints
   
4. **Appendices**
   - Models, prototypes, data dictionaries

### Organizing Requirements

Requirements can be organized by:
- **Feature/function** — grouped by system capability
- **User class** — grouped by who uses the function
- **Use case** — grouped by usage scenario
- **Business process** — grouped by the workflow they support

::: info Key Point
The organization should serve the document's audience. For testing purposes, organizing by feature is often most practical. For stakeholder reviews, organizing by user class may work better.
:::

## Quality Criteria for Requirements

Individual requirements and the entire specification should meet quality criteria:

### Quality of Individual Requirements

| Criterion | Meaning |
|-----------|---------|
| **Unambiguous** | Only one interpretation is possible |
| **Complete** | Contains all necessary information |
| **Correct** | Accurately reflects the stakeholder's intention |
| **Verifiable** | A test or inspection can determine if it's met |
| **Consistent** | Does not contradict other requirements |
| **Traceable** | Can be linked to its source and to downstream artifacts |
| **Necessary** | Every requirement has a valid reason for being there |
| **Feasible** | Can realistically be implemented within constraints |

### Quality of the Entire Specification

| Criterion | Meaning |
|-----------|---------|
| **Complete** | All relevant requirements are documented |
| **Consistent** | No contradictions between requirements |
| **Modifiable** | Structure allows changes without cascading edits |
| **Traceable** | All requirements have unique IDs and are cross-referenced |

<div class="example-box">

**Bad requirement** (ambiguous, not verifiable):
"The system should be fast and user-friendly."

**Good requirement** (specific, verifiable):
"The system shall display search results within 2 seconds for queries returning up to 500 results, as measured at the client browser under normal network conditions."
</div>

## Unique Identification

Every requirement needs a **unique identifier** (ID) so it can be referenced, traced, and managed.

Common ID schemes:
- `REQ-001`, `REQ-002` — simple sequential
- `FR-001`, `QR-001`, `CON-001` — categorized by type
- `UC-01.FR-01` — hierarchical, tied to use cases

::: info
The ID scheme doesn't matter as long as it's consistent, unique, and maintainable. Never reuse a retired ID for a different requirement.
:::

## Practice Quiz

<Quiz :questions="questions" />

---

**Previous:** [← Chapter 3: Requirements Elicitation](/chapters/03-elicitation)
| **Next:** [Chapter 5: Natural Language →](/chapters/05-natural-language)
