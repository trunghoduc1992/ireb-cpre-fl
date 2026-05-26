<script setup>
import Quiz from '../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'Which of the following is the primary goal of requirements elicitation?',
    options: [
      'To write the requirements specification document',
      'To discover and gather requirements from stakeholders and other sources',
      'To validate that requirements are correct and complete',
      'To prioritize requirements for implementation',
    ],
    answer: 1,
    explanation: 'Elicitation is the activity of discovering and gathering requirements. Documentation, validation, and prioritization are separate RE activities.',
  },
  {
    text: 'In which situation is an interview MOST appropriate?',
    options: [
      'When you need to gather information from a large number of users quickly',
      'When you want to understand a specific stakeholder\'s perspective in depth',
      'When you need to observe how users perform their actual tasks',
      'When stakeholders are unavailable for direct contact',
    ],
    answer: 1,
    explanation: 'Interviews are best for in-depth exploration of individual stakeholder perspectives. For large groups, use questionnaires. For observing tasks, use observation. For unavailable stakeholders, use document analysis.',
  },
  {
    text: 'What is a key advantage of a workshop over individual interviews?',
    options: [
      'It takes less preparation time',
      'It avoids conflicts between stakeholders',
      'It enables group dynamics and builds shared understanding among stakeholders',
      'It produces more detailed requirements than interviews',
    ],
    answer: 2,
    explanation: 'Workshops bring stakeholders together, enabling group dynamics (building on each other\'s ideas) and creating shared understanding. Conflicts may actually surface — which is useful for negotiation.',
  },
  {
    text: 'Which elicitation technique involves examining existing system documentation, forms, and reports?',
    options: [
      'Observation',
      'Prototyping',
      'Document analysis (archaeology)',
      'Brainstorming',
    ],
    answer: 2,
    explanation: 'Document analysis (also called "archaeology") involves studying existing documents, forms, reports, and system interfaces to extract requirements. It\'s especially useful for replacing legacy systems.',
  },
  {
    text: 'What is a major risk of using ONLY questionnaires for elicitation?',
    options: [
      'They are too expensive to create',
      'Respondents may misinterpret questions and you cannot ask follow-up questions',
      'They require too many stakeholders to participate',
      'They always produce ambiguous requirements',
    ],
    answer: 1,
    explanation: 'Questionnaires are one-directional — respondents may misunderstand questions, and the analyst cannot ask for clarification. They lack the interactive feedback loop that interviews and workshops provide.',
  },
  {
    text: 'Which technique is best for discovering requirements that stakeholders cannot articulate?',
    options: [
      'Interviews',
      'Questionnaires',
      'Observation (field observation)',
      'Document analysis',
    ],
    answer: 2,
    explanation: 'Observation allows you to see what stakeholders actually do versus what they say they do. Tacit knowledge — things people do automatically without thinking — is best discovered through observation.',
  },
]
</script>

# Chapter 3: Requirements Elicitation

<div class="exam-tip">
  <strong>Exam weight:</strong> ~15% of questions. Know each technique's strengths, weaknesses, and when to use it.
</div>

## Fundamentals of Elicitation

**Requirements elicitation** is the activity of discovering, gathering, and developing requirements from stakeholders and other sources.

<div class="key-concept">

Elicitation is more than just "asking users what they want." Stakeholders often:
- Cannot articulate their needs clearly
- Don't know what's technically possible
- Have implicit expectations they don't mention
- Disagree with each other

The requirements engineer must actively uncover, clarify, and reconcile these needs.

</div>

## Sources of Requirements

Requirements come from multiple sources — not just stakeholders:

| Source | What It Provides |
|--------|-----------------|
| **Stakeholders** | Explicit needs, expectations, workflows |
| **Existing systems** | Current functionality, known issues, data formats |
| **Documents** | Business rules, regulations, standards, contracts |
| **Domain knowledge** | Industry practices, common patterns |

::: tip From Your Experience
As a BA, you already know that the "real" requirements often emerge between the lines of what stakeholders say. As a tester, you've found requirements gaps when writing test cases. Both perspectives highlight that elicitation is an active, investigative process.
:::

## Elicitation Techniques

IREB defines several elicitation techniques. For each, know **what it is**, **when to use it**, and **its pros and cons**.

### Interview

A structured or semi-structured conversation between the requirements engineer and one or more stakeholders.

**When to use:**
- To explore a stakeholder's domain in depth
- To understand individual perspectives and priorities
- To clarify unclear or conflicting information

**Types of questions:**
- **Open questions**: "How do you handle returns?" — encourages detailed answers
- **Closed questions**: "Do you process more than 100 orders per day?" — gets specific facts

| Pros | Cons |
|------|------|
| Rich, detailed information | Time-consuming per stakeholder |
| Can ask follow-up questions | Interviewer bias can influence answers |
| Builds rapport with stakeholders | Hard to scale to many stakeholders |

<div class="example-box">

**Practical example:**
You interview a warehouse manager about the order fulfillment process. She mentions, "We always check the stock before confirming." This reveals a business rule: *order confirmation requires stock verification* — a requirement you might not find in any document.
</div>

### Workshop

A facilitated group session where multiple stakeholders collaborate to define requirements.

**When to use:**
- To build consensus among stakeholders
- To resolve conflicts early
- To rapidly generate and prioritize ideas
- When group dynamics can produce better results than individual sessions

**Key roles in a workshop:**
- **Facilitator** — guides the process (often the RE)
- **Scribe/recorder** — captures results
- **Participants** — stakeholders who provide input

| Pros | Cons |
|------|------|
| Group dynamics generate new ideas | Dominant personalities can suppress others |
| Builds shared understanding | Requires significant preparation and facilitation skill |
| Efficient for groups (parallel input) | Scheduling many people is difficult |
| Surfaces and resolves conflicts early | Can go off-track without strong facilitation |

### Observation (Field Observation)

Watching stakeholders perform their actual work in their real environment.

**When to use:**
- To understand current workflows and processes
- To discover tacit knowledge (things people do without consciously thinking about them)
- To identify gaps between documented processes and actual practice

**Types:**
- **Active observation** — the observer asks questions while watching
- **Passive observation** — the observer watches silently without interfering

| Pros | Cons |
|------|------|
| Reveals actual behavior vs. stated behavior | Time-consuming |
| Discovers tacit knowledge | Observer's presence may alter behavior (Hawthorne effect) |
| Provides concrete, real-world context | Limited to observable activities |

<div class="example-box">

**Practical example:**
You observe a customer service agent handling complaints. The documented process says they should enter notes in the CRM. You notice they actually write notes on paper first, then batch-enter them at end of day. This reveals a usability issue with the current system and a requirement for the new one: *real-time note entry must be fast and frictionless*.
</div>

### Questionnaire (Survey)

A written set of questions distributed to a large group of stakeholders.

**When to use:**
- To gather input from many stakeholders (dozens or hundreds)
- To collect quantitative data or rank preferences
- When stakeholders are geographically distributed

| Pros | Cons |
|------|------|
| Scalable to large groups | No follow-up questions possible |
| Low cost per respondent | Risk of misinterpretation |
| Results are easy to analyze quantitatively | Low response rates are common |
| Anonymity can encourage honest answers | Cannot discover tacit knowledge |

### Document Analysis (Archaeology)

Studying existing documentation, forms, reports, user manuals, and system interfaces to extract requirements.

**When to use:**
- When replacing or upgrading a legacy system
- To understand existing business rules and data formats
- When stakeholders are unavailable or documentation is the primary source

| Pros | Cons |
|------|------|
| Independent of stakeholder availability | Documents may be outdated or incomplete |
| Reveals formal rules and standards | Cannot capture tacit knowledge |
| Good for understanding data formats and interfaces | May contain contradictions |

### Brainstorming

A creative group technique for generating a large number of ideas in a short time.

**When to use:**
- Early in the project when exploring solution possibilities
- To generate innovative ideas beyond obvious requirements
- To break out of established thinking patterns

**Rules of brainstorming:**
1. No criticism during idea generation
2. Quantity over quality initially
3. Build on others' ideas
4. Wild ideas are welcome

| Pros | Cons |
|------|------|
| Generates many ideas quickly | Ideas need filtering and evaluation afterward |
| Encourages creative thinking | Can be dominated by strong personalities |
| Low formality, easy to run | Results are raw — not directly usable as requirements |

### Prototyping

Creating a preliminary model of the system (or part of it) to help stakeholders understand and refine requirements.

**When to use:**
- When stakeholders cannot visualize the final system
- To validate UI/UX requirements
- To resolve ambiguity in requirements
- To get early feedback on concepts

**Types:**
- **Throwaway prototype** — built quickly to explore ideas, then discarded
- **Evolutionary prototype** — incrementally refined into the final system

| Pros | Cons |
|------|------|
| Makes abstract requirements tangible | Stakeholders may confuse the prototype with the final system |
| Provides early feedback | Can be expensive for complex prototypes |
| Helps discover missing requirements | Risk of premature commitment to a design |

### Perspective-Based Reading

Reviewing existing documentation from different stakeholder perspectives to identify missing or inconsistent requirements.

**When to use:**
- To review existing specifications for completeness
- To identify requirements that are implicit from one perspective but missing from the documentation

<div class="example-box">

**Practical example:**
You review a system specification from three perspectives:
- **User perspective**: "Can I undo my last action?" → Reveals missing undo requirement
- **Admin perspective**: "How do I reset a locked account?" → Reveals missing admin function
- **Tester perspective**: "How do I verify this works correctly?" → Reveals missing acceptance criteria
</div>

## Combining Techniques

In practice, you'll combine multiple techniques. A typical approach:

1. **Document analysis** — understand the current state
2. **Interviews** — deep-dive with key stakeholders
3. **Workshop** — align stakeholders, resolve conflicts
4. **Prototyping** — validate the UI/interaction model
5. **Questionnaire** — confirm priorities with the broader user base

::: info Key Exam Point
No single technique is sufficient. IREB expects you to know which technique to use in which situation and that techniques should be combined.
:::

## Practice Quiz

<Quiz :questions="questions" />

---

**Previous:** [← Chapter 2: System & System Context](/chapters/02-system-context)
| **Next:** [Chapter 4: Documentation Basics →](/chapters/04-documentation)
