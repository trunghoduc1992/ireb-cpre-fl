<script setup>
import Quiz from '../../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'Which of the following is NOT listed as a main influencing factor for configuring an RE process?',
    options: [
      'Complexity and criticality of the system',
      'The programming language used by the development team',
      'Capability and availability of stakeholders',
      'Volatility of requirements',
    ],
    answer: 1,
    explanation: 'The main influencing factors are: overall process fit, development context, capability and availability of stakeholders, shared understanding, complexity and criticality, constraints, available time and budget, volatility of requirements, and experience of Requirements Engineers. The programming language is not listed.',
  },
  {
    text: 'What are the three process facets that need to be considered when configuring an RE process?',
    options: [
      'Scope, schedule, and budget',
      'Time (linear vs. iterative), purpose (prescriptive vs. explorative), and target (customer-specific vs. market-oriented)',
      'Plan, do, and check',
      'Elicitation, documentation, and validation',
    ],
    answer: 1,
    explanation: 'The three decisive facets are: Time (linear vs. iterative), Purpose (prescriptive vs. explorative), and Target (customer-specific vs. market-oriented).',
  },
  {
    text: 'A company is developing a custom system for a single client. Stakeholders are strongly involved and provide continuous feedback. Which RE process configuration fits best?',
    options: [
      'Contractual RE: linear, prescriptive, customer-specific',
      'Participatory RE: iterative, explorative, customer-specific',
      'Product-oriented RE: iterative, explorative, market-oriented',
      'Waterfall RE: linear, prescriptive, market-oriented',
    ],
    answer: 1,
    explanation: 'A participatory RE process (iterative, explorative, customer-specific) fits when supplier and customer collaborate closely with strong stakeholder involvement in both RE and development.',
  },
]
</script>

# EU 5: Process and Working Structure

::: info Official Reference
**IREB CPRE-FL Syllabus v3.3.0** — Educational Unit 5 (L3, 2 hours)
[Download syllabus](https://cpre.ireb.org/en/downloads-and-resources/downloads)
:::

<div class="exam-tip">
  <strong>Exam weight:</strong> ~4.3% of points (2 questions, 3 points). Know the three process facets and how influencing factors shape the RE process.
</div>

A process is required to shape and structure the RE work to be done in a given context. There is no one-size-fits-all RE process — a tailored RE process must be configured that fits the given development and system context.

The RE process shapes the **information flow** and the **communication model** between participants (customers, users, Requirements Engineers, developers, testers), and also defines the **work products** to be used or produced.

## 5.1 Influencing Factors (L2)

Many factors influence the configuration of an RE process. The main factors are:

| Factor | What It Affects |
|--------|----------------|
| **Overall process fit** | The RE process must fit the overall system development process |
| **Development context** | The environment in which the system is being developed |
| **Capability and availability of stakeholders** | Whether stakeholders can participate and how often |
| **Shared understanding** | The degree of existing shared knowledge among participants |
| **Complexity and criticality** | How complex and safety/mission-critical the system is |
| **Constraints** | Regulatory, organizational, or contractual restrictions |
| **Available time and budget** | Resources allocated for RE activities |
| **Volatility of requirements** | How frequently requirements are expected to change |
| **Experience of Requirements Engineers** | The RE team's skill level |

An analysis of these factors provides information about **how** to configure the RE process. The factors also **constrain** the space of possible process configurations.

<div class="example-box">

If stakeholders are only available at the beginning of the project, no process can be chosen that builds upon continuous stakeholder feedback. The influencing factors narrow down which configurations are feasible.

</div>

## 5.2 Requirements Engineering Process Facets (L2)

There are three decisive facets to consider when configuring an RE process.

### Time Facet: Linear versus Iterative

| Aspect | Linear | Iterative |
|--------|--------|-----------|
| **Approach** | Requirements specified up front in a single phase | Requirements specified incrementally, starting with goals and initial requirements, then refined each iteration |
| **When to use** | Plan-driven process; stakeholders know their requirements up front; comprehensive spec needed for contract or regulation | Agile process; many requirements not known up front; stakeholders available for short feedback loops |

**Criteria for linear:** plan-driven development, stakeholders can specify requirements up front, comprehensive specification required for outsourcing or regulation.

**Criteria for iterative:** agile development, requirements will emerge and evolve, stakeholders available for feedback, ability to change requirements easily is important.

### Purpose Facet: Prescriptive versus Explorative

| Aspect | Prescriptive | Explorative |
|--------|-------------|-------------|
| **Approach** | Requirements specification constitutes a contract — all requirements are binding | Only goals are known a priori; concrete requirements must be explored |
| **When to use** | Customer requires a fixed contract; functionality and scope take precedence over cost and deadlines | Stakeholders initially have a vague idea; continuous feedback; deadlines and cost take precedence |

### Target Facet: Customer-Specific versus Market-Oriented

| Aspect | Customer-Specific | Market-Oriented |
|--------|-------------------|-----------------|
| **Approach** | System ordered by a customer, developed by a supplier | System developed as a product or service for a market |
| **When to use** | Mainly used by the ordering organization; individual stakeholders can be identified | Organization sells the system; prospective users not individually identifiable; personas needed |

### Hints and Caveats

- Linear and prescriptive are frequently chosen together
- Explorative RE processes are typically also iterative (and vice versa)
- Linear processes only work if a sophisticated **change process** is in place
- Linear processes imply long feedback loops — requirements must be validated intensively
- The market-oriented facet does **not** combine well with the linear and prescriptive facets
- In a market-oriented process, user feedback is the only means of validating market fit

## 5.3 Configuring a Requirements Engineering Process (L3)

### Three Typical Process Configurations

#### Participatory RE: Iterative + Explorative + Customer-Specific

| Aspect | Description |
|--------|-------------|
| **Main application** | Supplier and customer collaborate closely; stakeholders strongly involved in both RE and development |
| **Typical work products** | Product backlog with user stories and/or task descriptions, prototypes |
| **Information flow** | Continuous interaction between stakeholders, product owners, Requirements Engineers, and developers; may include user feedback |

#### Contractual RE: Linear (sometimes iterative) + Prescriptive + Customer-Specific

| Aspect | Description |
|--------|-------------|
| **Main application** | Requirements specification is the contractual basis; development by people not involved in specification, with little stakeholder interaction after the requirements phase |
| **Typical work products** | Classic system requirements specification with natural-language requirements and models |
| **Information flow** | Primarily from stakeholders to Requirements Engineers |

#### Product-Oriented RE: Iterative + Explorative + Market-Oriented

| Aspect | Description |
|--------|-------------|
| **Main application** | An organization specifies and develops software to sell or distribute as a product or service |
| **Typical work products** | Product backlog, prototypes |
| **Information flow** | Interaction between product owner, marketing, Requirements Engineers, digital designers, developers, and (maybe) fast feedback from customers/users |

### Five-Step Configuration Procedure

When configuring an RE process, the syllabus recommends the following steps:

1. **Analyze** the influencing factors (5.1)
2. **Assess** the facet criteria (5.2)
3. **Configure** the process (5.3)
4. **Determine** work products (EU 3)
5. **Select** appropriate practices

::: info Key Point
There may be contexts where none of the three typical configurations fit. For example, regulatory constraints may impose the use of a process that conforms to standards such as ISO/IEC/IEEE 29148.
:::

## Practice Quiz

<Quiz :questions="questions" />
