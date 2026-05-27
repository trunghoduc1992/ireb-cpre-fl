<script setup>
import Quiz from '../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'Which of the following is NOT a category of work product life span?',
    options: [
      'Temporary',
      'Evolving',
      'Durable',
      'Archived',
    ],
    answer: 3,
    explanation: 'The three life span categories are temporary (support communication), evolving (refined over iterations), and durable (baselined or released). "Archived" is not a syllabus category.',
  },
  {
    text: 'According to the syllabus, which general documentation guideline should be followed when creating work products?',
    options: [
      'Always use the most detailed notation available',
      'Avoid redundancy by referencing content instead of repeating it',
      'Include all requirements in a single work product for completeness',
      'Use informal language to ensure all stakeholders understand the content',
    ],
    answer: 1,
    explanation: 'The guidelines include: select a fitting work product type, avoid redundancy by referencing, ensure consistency between work products, use terms consistently per the glossary, and structure appropriately.',
  },
  {
    text: 'What are the two most important quality criteria for single requirements?',
    options: [
      'Complete and traceable',
      'Adequate and understandable',
      'Verifiable and consistent',
      'Necessary and modifiable',
    ],
    answer: 1,
    explanation: 'The syllabus states: "Adequacy and understandability are the most important quality criteria for single requirements. Without them, a requirement is useless or even harmful."',
  },
  {
    text: 'A product backlog, a sprint backlog, and a story map are examples of which kind of documentation?',
    options: [
      'Requirements specification documents',
      'Alternative documentation structures',
      'Model-based work products',
      'Template-based work products',
    ],
    answer: 1,
    explanation: 'The syllabus lists product backlog, sprint backlog, and story map as "frequently used alternative documentation structures" in contrast to classic documents like system requirements specifications.',
  },
  {
    text: 'Which type of prototype is described as a low-fidelity prototype built with simple materials or sketching tools?',
    options: [
      'Evolutionary prototype',
      'Mock-up',
      'Wireframe',
      'Native prototype',
    ],
    answer: 2,
    explanation: 'Wireframes are low-fidelity prototypes for discussing design ideas. Mock-ups are medium-fidelity (real screens, no real functionality). Native prototypes are high-fidelity (implement critical parts). Evolutionary prototypes are pilot systems that evolve into the final product.',
  },
]
</script>

# EU 3: Work Products and Documentation Practices

::: info Official Reference
**IREB CPRE-FL Syllabus v3.3.0** — Educational Unit 3 (L3, 6 hours)
[Download syllabus](https://cpre.ireb.org/en/downloads-and-resources/downloads)
:::

<div class="exam-tip">
  <strong>Exam weight:</strong> ~42.9% of points (18 questions, 30 points). This is the heaviest EU — study it thoroughly.
</div>

This page covers the fundamentals of work products, documentation structures, prototypes, and quality criteria. For the detailed documentation techniques, see:

- [Natural Language & Templates](03b-natural-language.md)
- [Model-Based Work Products](03c-models.md)

## 3.1 Work Products in Requirements Engineering (L2)

A **work product** is a recorded intermediate or final result generated in a work process. Work products in RE range from short-lived graphic sketches through evolving collections of user stories to formally released requirements specification documents.

### 3.1.1 Characteristics of Work Products (L1)

Work products are characterized by their **purpose**, **representation**, **size**, and **life span**.

**Work products by purpose:**

| Purpose | Examples |
|---------|----------|
| Single requirement | Individual requirements, user stories |
| Coherent set of requirements | Use cases, graphic models, task descriptions, interface descriptions, epics |
| Comprehensive documents | System requirements specifications, product and sprint backlogs, story maps |
| Other | Glossaries, textual notes, graphic sketches, prototypes |

**Work products by representation:**

- Natural-language-based (Section 3.2)
- Template-based (Section 3.3)
- Model-based (Section 3.4)
- Other representations (drawings, prototypes)

**Work products by life span:**

| Category | Description | Metadata | Change Control |
|----------|-------------|----------|----------------|
| **Temporary** | Support communication and shared understanding | None required | No |
| **Evolving** | Refined over several iterations | Some metadata needed | May apply |
| **Durable** | Baselined or released | Full metadata required | Must be followed |

A temporary work product can become evolving (by keeping it and adding metadata), and an evolving work product can become durable (by being baselined or released).

### 3.1.2 Abstraction Levels (L2)

Requirements usually exist on many different levels of abstraction — from high-level business process requirements down to detailed software component requirements.

- **Do not mix** requirements at different levels of abstraction in small and medium-sized work products
- In large documents, keep different abstraction levels **separate** through appropriate structuring
- A high-level requirement may be **refined** into several detailed requirements at lower levels

### 3.1.3 Level of Detail (L2)

The level of detail depends on several factors:

- The problem and development context
- The degree of shared understanding of the problem
- The degree of freedom left to designers and programmers
- Availability of rapid stakeholder feedback during design and implementation
- Cost vs. value of a detailed specification
- Imposed standards and regulatory constraints

::: info Key Insight
Greater detail reduces the risk of getting something unexpected, but increases the cost of the specification. This is a trade-off that must be consciously managed.
:::

### 3.1.4 Aspects to be Considered in Work Products (L1)

When specifying requirements, different aspects must be considered:

1. **Kind of requirement:** functional requirements, quality requirements, constraints
2. **Functional aspects:** structure and data, function and flow, state and behavior
3. **Context aspects:** system context and external actors, system boundary and external interfaces

These aspects are interrelated. Some work products focus on a specific aspect (especially models), while others (like system requirements specifications) cover all aspects. When different aspects are in separate work products, they must be kept **consistent** with each other.

### 3.1.5 General Documentation Guidelines (L1)

Regardless of the techniques used:

1. **Select** a work product type that fits the intended purpose
2. **Avoid redundancy** by referencing content instead of repeating it
3. **Ensure consistency** between work products that cover different aspects
4. **Use terms consistently** as defined in the glossary
5. **Structure** work products appropriately

### 3.1.6 Plan the Work Products to be Used (L1)

The work products to be used should be defined at an early stage. The following must be agreed upon:

- In which work products shall the requirements be recorded and for what purpose?
- Which abstraction levels need to be considered?
- Up to which level of detail must requirements be documented?
- How shall the requirements be represented?

Early planning helps to plan efforts, ensures appropriate notations, avoids redundancy, and prevents major reshuffling of information later.

## 3.6 Requirements Documents and Documentation Structures (L2)

**Frequently used documents:**

- Stakeholder Requirements Specification
- User Requirements Specification
- System Requirements Specification
- Business Requirements Specification
- Vision Document

**Frequently used alternative documentation structures:**

- Product backlog
- Sprint backlog
- Story map

The selection of a documentation structure depends on the chosen development process, the development type and domain, any customer-imposed structure, and the size of the document.

## 3.7 Prototypes in Requirements Engineering (L1)

Prototypes are a means of specifying requirements by example and of validating requirements.

### Exploratory Prototypes

Exploratory prototypes are used to create shared understanding, clarify requirements, or validate requirements. They are **discarded after use**.

| Type | Fidelity | Purpose |
|------|----------|---------|
| **Wireframes** | Low | Discussing and validating design ideas and UI concepts |
| **Mock-ups** | Medium | Specifying and validating user interfaces (real screens, click flows, no real functionality) |
| **Native prototypes** | High | Verifying whether prototyped parts of the system will work as expected |

### Evolutionary Prototypes

Evolutionary prototypes are **pilot systems** that form the core of a system to be developed. The final system evolves by incrementally extending and improving the pilot system in several iterations.

## 3.8 Quality Criteria for Work Products and Requirements (L1)

In modern RE with value-oriented approaches (Principle 1), the degree of fulfillment for a quality criterion should correspond to the value created by the requirement.

### Quality Criteria for Single Requirements

**Adequacy** and **understandability** are the most important. Without them, a requirement is useless or even harmful.

- **Adequate** — describes true and agreed stakeholder needs
- **Necessary**
- **Unambiguous**
- **Complete** (self-contained)
- **Understandable**
- **Verifiable**

### Quality Criteria for Work Products (Multiple Requirements)

- **Consistent** — no contradictions between requirements
- **Non-redundant** — no unnecessary duplication
- **Complete** — no known relevant requirements missed
- **Modifiable** — can be changed without excessive effort
- **Traceable** — requirements can be followed to sources and downstream artifacts
- **Conformant** — adheres to applicable standards and guidelines

## Practice Quiz

<Quiz :questions="questions" />
