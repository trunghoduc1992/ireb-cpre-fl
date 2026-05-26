<script setup>
import Quiz from '../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'What is the primary advantage of model-based documentation over pure natural language?',
    options: [
      'Models are always more complete than text',
      'Models reduce ambiguity for structural and behavioral aspects',
      'Models do not require any training to read',
      'Models replace the need for natural language documentation',
    ],
    answer: 1,
    explanation: 'Models use well-defined notations that reduce ambiguity, especially for structure and behavior. However, they complement — not replace — natural language, and they do require training to read.',
  },
  {
    text: 'In a use case diagram, what does an "include" relationship mean?',
    options: [
      'The included use case optionally extends the base use case',
      'The base use case always incorporates the behavior of the included use case',
      'The included use case replaces the base use case',
      'The included use case is an alternative to the base use case',
    ],
    answer: 1,
    explanation: 'An <<include>> relationship means the base use case ALWAYS incorporates the included use case — it\'s mandatory. The included behavior is factored out because it\'s shared by multiple base use cases.',
  },
  {
    text: 'In an activity diagram, what does a fork (thick horizontal bar splitting into multiple paths) represent?',
    options: [
      'A decision point where only one path is taken',
      'The start of parallel activities that execute concurrently',
      'The end of the activity',
      'An error handling branch',
    ],
    answer: 1,
    explanation: 'A fork splits the flow into concurrent paths — all outgoing branches execute in parallel. A join (another thick bar) synchronizes them. A decision (diamond) is where only one path is taken.',
  },
  {
    text: 'In a state machine diagram, what triggers a transition between states?',
    options: [
      'A class association',
      'An event, optionally with a guard condition',
      'A use case include relationship',
      'A data flow between entities',
    ],
    answer: 1,
    explanation: 'Transitions in state machines are triggered by events. A guard condition (in square brackets) can make the transition conditional: event [guard] / action.',
  },
  {
    text: 'In a class diagram, what does a multiplicity of "0..*" on an association mean?',
    options: [
      'Exactly zero instances',
      'Zero or more instances (optional, unbounded)',
      'At least one instance',
      'Exactly one instance',
    ],
    answer: 1,
    explanation: '"0..*" means zero or more — the association is optional and can have any number of instances. "1..*" means at least one. "1" means exactly one. "0..1" means zero or one.',
  },
  {
    text: 'Which diagram type is MOST suitable for documenting the data structure and relationships in a domain?',
    options: [
      'Activity diagram',
      'State machine diagram',
      'Class diagram / data model',
      'Use case diagram',
    ],
    answer: 2,
    explanation: 'Class diagrams (or entity-relationship diagrams) model the data structure — entities, their attributes, and relationships. Activity diagrams show processes, state machines show state changes, and use case diagrams show functionality overview.',
  },
  {
    text: 'What does an "extend" relationship in a use case diagram represent?',
    options: [
      'A mandatory behavior that is always executed',
      'An optional behavior that extends the base use case under certain conditions',
      'Inheritance between two actors',
      'A data flow between use cases',
    ],
    answer: 1,
    explanation: 'An <<extend>> relationship means the extending use case optionally adds behavior to the base use case — it\'s only triggered under specific conditions (at an extension point). Compare with <<include>> which is always executed.',
  },
]
</script>

# Chapter 6: Model-Based Documentation

<div class="exam-tip">
  <strong>Exam weight:</strong> This is the heaviest part of the ~40% documentation block. Expect many questions on UML diagram types, notation, and interpretation.
</div>

## Why Use Models?

Models complement natural language by providing:

- **Precision** — formal notation reduces ambiguity
- **Abstraction** — focus on relevant aspects, hide details
- **Different perspectives** — structure, behavior, interaction
- **Communication** — visual representations are easier to discuss

<div class="key-concept">

Models don't replace natural language — they supplement it. Use natural language for context, rationale, and details that models can't express. Use models for structure and behavior that text describes poorly.

</div>

## Overview of Model Types

| Model Type | Purpose | Shows |
|-----------|---------|-------|
| **Use case diagram** | Functional overview | What the system does for its actors |
| **Activity diagram** | Process/workflow | Step-by-step flow with decisions and parallelism |
| **State machine diagram** | Object lifecycle | How an entity changes state over time |
| **Class diagram** | Data structure | Entities, attributes, and relationships |
| **Goal model** | Motivation | Why requirements exist, stakeholder goals |

## Use Case Diagrams

Use case diagrams show **what the system does** from the user's perspective — a high-level functional overview.

### Elements

| Element | Symbol | Meaning |
|---------|--------|---------|
| **Actor** | Stick figure | A person or external system interacting with the SuD |
| **Use case** | Oval/ellipse | A function the system provides |
| **System boundary** | Rectangle | The boundary of the SuD |
| **Association** | Solid line | An actor participates in a use case |

<MermaidChart code="graph%20LR%0A%20%20%20%20subgraph%20Online%20Shop%20-%20SuD%0A%20%20%20%20%20%20%20%20UC1((Browse%5CnProducts))%0A%20%20%20%20%20%20%20%20UC2((Place%5CnOrder))%0A%20%20%20%20end%0A%20%20%20%20Customer%20--%3E%7Cuses%7C%20UC1%0A%20%20%20%20Customer%20--%3E%7Cuses%7C%20UC2" />

### Relationships Between Use Cases

#### Include (<<include\>\>)
The base use case **always** executes the included use case.

<MermaidChart code="graph%20LR%0A%20%20%20%20PO((Place%20Order))%20--%20%22%C2%ABinclude%C2%BB%22%20--%3E%20VP((Verify%20Payment))" />

"Place Order" always includes "Verify Payment" — you can't place an order without payment verification.

#### Extend (<<extend\>\>)
The extending use case **optionally** adds behavior to the base use case.

<MermaidChart code="graph%20RL%0A%20%20%20%20AC((Apply%20Coupon))%20--%20%22%C2%ABextend%C2%BB%22%20--%3E%20PO((Place%20Order))" />

"Apply Coupon" optionally extends "Place Order" — the customer may or may not have a coupon.

#### Actor Generalization
One actor inherits the use cases of another.

<MermaidChart code="graph%20BT%0A%20%20%20%20Admin%20--%3E%7Cinherits%7C%20User" />

Admin is a specialized User — Admin can do everything a User can, plus admin-specific functions.

::: warning Key Exam Distinction
**Include** = always, mandatory. **Extend** = optional, conditional. The arrow directions are different: include points FROM base TO included; extend points FROM extending TO base.
:::

### Use Case Description (Textual)

A use case diagram gives an overview but not details. Each use case should have a **textual description**:

| Field | Content |
|-------|---------|
| **ID** | UC-03 |
| **Name** | Place Order |
| **Actor** | Customer |
| **Precondition** | Customer is logged in and has items in cart |
| **Main flow** | 1. Customer selects "Checkout" 2. System displays order summary 3. Customer confirms order 4. System processes payment 5. System confirms order |
| **Alternative flows** | 3a. Customer modifies quantity → return to step 2 |
| **Exception flows** | 4a. Payment fails → System displays error, return to step 3 |
| **Postcondition** | Order is recorded; confirmation email sent |

## Activity Diagrams

Activity diagrams model **processes and workflows** — the step-by-step flow of activities with decisions and parallelism.

### Elements

| Element | Symbol | Meaning |
|---------|--------|---------|
| **Initial node** | Filled circle ● | Start of the process |
| **Activity/Action** | Rounded rectangle | A step in the process |
| **Decision** | Diamond ◇ | Branch point (one path taken) |
| **Merge** | Diamond ◇ | Reconnects decision branches |
| **Fork** | Thick bar ━ | Splits into parallel paths |
| **Join** | Thick bar ━ | Synchronizes parallel paths |
| **Final node** | Circle with inner filled circle ◉ | End of the process |
| **Swim lane** | Vertical/horizontal partition | Assigns activities to responsible actors |

### Example: Order Processing

<MermaidChart code="flowchart%20TD%0A%20%20%20%20Start((%20))%20--%3E%20Receive%5BReceive%20Order%5D%0A%20%20%20%20Receive%20--%3E%20Check%7BStock%20available%3F%7D%0A%20%20%20%20Check%20--%3E%7CYes%7C%20Fork1%5B%20%5D%0A%20%20%20%20Check%20--%3E%7CNo%7C%20Notify%5BNotify%20Customer%5D%0A%20%20%20%20Notify%20--%3E%20End1((%20))%0A%20%20%20%20Fork1%20--%3E%20Pack%5BPack%20Items%5D%0A%20%20%20%20Fork1%20--%3E%20Invoice%5BSend%20Invoice%5D%0A%20%20%20%20Pack%20--%3E%20Join1%5B%20%5D%0A%20%20%20%20Invoice%20--%3E%20Join1%0A%20%20%20%20Join1%20--%3E%20Ship%5BShip%20Order%5D%0A%20%20%20%20Ship%20--%3E%20End2((%20))%0A%0A%20%20%20%20style%20Start%20fill%3A%23000%2Cstroke%3A%23000%2Ccolor%3A%23000%0A%20%20%20%20style%20End1%20fill%3A%23000%2Cstroke%3A%23000%2Ccolor%3A%23000%0A%20%20%20%20style%20End2%20fill%3A%23000%2Cstroke%3A%23000%2Ccolor%3A%23000%0A%20%20%20%20style%20Fork1%20fill%3A%23333%2Cstroke%3A%23333%2Ccolor%3A%23333%0A%20%20%20%20style%20Join1%20fill%3A%23333%2Cstroke%3A%23333%2Ccolor%3A%23333" />

### Swim Lanes

Swim lanes partition activities by **responsibility** — who performs each step.

<MermaidChart code="flowchart%20LR%0A%20%20%20%20subgraph%20Customer%0A%20%20%20%20%20%20%20%20A%5BSubmit%20Order%5D%0A%20%20%20%20%20%20%20%20F%5BReceive%20Email%5D%0A%20%20%20%20end%0A%20%20%20%20subgraph%20System%0A%20%20%20%20%20%20%20%20B%5BValidate%20Order%5D%0A%20%20%20%20%20%20%20%20E%5BSend%20Confirmation%20Email%5D%0A%20%20%20%20end%0A%20%20%20%20subgraph%20Warehouse%0A%20%20%20%20%20%20%20%20C%5BPick%20Items%5D%0A%20%20%20%20%20%20%20%20D%5BPack%20%26%20Ship%5D%0A%20%20%20%20end%0A%0A%20%20%20%20A%20--%3E%20B%20--%3E%20C%20--%3E%20D%0A%20%20%20%20B%20--%3E%20E%20--%3E%20F" />

::: tip From Your Experience
As a tester, activity diagrams map directly to test scenarios — each path through the diagram is a test case. As a BA, swim lanes help you assign responsibilities to roles.
:::

## State Machine Diagrams

State machine diagrams show how an **entity changes state** in response to events over its lifecycle.

### Elements

| Element | Symbol | Meaning |
|---------|--------|---------|
| **State** | Rounded rectangle | A condition the entity is in |
| **Transition** | Arrow → | Change from one state to another |
| **Event** | Label on transition | What triggers the transition |
| **Guard** | [condition] | Condition that must be true for transition |
| **Action** | /action | What happens during the transition |
| **Initial state** | Filled circle ● | Starting state |
| **Final state** | ◉ | End of lifecycle |

### Transition Syntax

```
event [guard] / action
```

### Example: Order Lifecycle

<MermaidChart code="stateDiagram-v2%0A%20%20%20%20%5B*%5D%20--%3E%20New%0A%20%20%20%20New%20--%3E%20Confirmed%20%3A%20payment%20received%0A%20%20%20%20New%20--%3E%20Cancelled%20%3A%20cancelled%0A%20%20%20%20Confirmed%20--%3E%20Shipped%20%3A%20shipped%0A%20%20%20%20Shipped%20--%3E%20Delivered%20%3A%20delivered%0A%20%20%20%20Cancelled%20--%3E%20%5B*%5D%0A%20%20%20%20Delivered%20--%3E%20%5B*%5D" />

With guard conditions:
<MermaidChart code="stateDiagram-v2%0A%20%20%20%20Delivered%20--%3E%20Returned%20%3A%20return%20requested%20%5Bwithin%2030%20days%5D%20%2F%20create%20return%20label" />

<div class="exam-tip">
  <strong>Exam tip:</strong> Be able to read transition labels in the format <code>event [guard] / action</code>. Questions often ask what event triggers a specific transition or what guard condition applies.
</div>

## Class Diagrams (Data Models)

Class diagrams model the **data structure** of the domain — what entities exist, their attributes, and how they relate to each other.

### Elements

| Element | Meaning |
|---------|---------|
| **Class** | A domain entity (rectangle with name, attributes, operations) |
| **Association** | A relationship between classes (line) |
| **Multiplicity** | How many instances participate (numbers at ends of association) |
| **Generalization** | Inheritance (triangle arrow pointing to parent) |
| **Aggregation** | "Has-a" relationship, parts can exist independently (hollow diamond) |
| **Composition** | "Has-a" relationship, parts cannot exist without the whole (filled diamond) |

### Multiplicity Notation

| Notation | Meaning |
|----------|---------|
| `1` | Exactly one |
| `0..1` | Zero or one (optional) |
| `*` or `0..*` | Zero or more |
| `1..*` | One or more (at least one) |
| `2..5` | Between 2 and 5 |

### Example: E-Commerce Domain Model

<MermaidChart code="classDiagram%0A%20%20%20%20Customer%20%221%22%20--%3E%20%220..*%22%20Order%20%3A%20places%0A%20%20%20%20Order%20%221%22%20--%3E%20%221..*%22%20OrderItem%20%3A%20contains%0A%20%20%20%20OrderItem%20%220..*%22%20--%3E%20%221%22%20Product%20%3A%20refers%20to%0A%0A%20%20%20%20class%20Customer%20%7B%0A%20%20%20%20%20%20%20%20name%0A%20%20%20%20%20%20%20%20email%0A%20%20%20%20%20%20%20%20address%0A%20%20%20%20%7D%0A%20%20%20%20class%20Order%20%7B%0A%20%20%20%20%20%20%20%20orderDate%0A%20%20%20%20%20%20%20%20status%0A%20%20%20%20%20%20%20%20totalAmount%0A%20%20%20%20%7D%0A%20%20%20%20class%20OrderItem%20%7B%0A%20%20%20%20%20%20%20%20quantity%0A%20%20%20%20%20%20%20%20unitPrice%0A%20%20%20%20%7D%0A%20%20%20%20class%20Product%20%7B%0A%20%20%20%20%20%20%20%20name%0A%20%20%20%20%20%20%20%20description%0A%20%20%20%20%20%20%20%20price%0A%20%20%20%20%7D" />

Reading: "One Customer places zero or more Orders. Each Order contains one or more OrderItems. Each OrderItem refers to one Product."

### Generalization (Inheritance)

<MermaidChart code="classDiagram%0A%20%20%20%20Payment%20%3C%7C--%20CreditCard%0A%20%20%20%20Payment%20%3C%7C--%20BankTransfer%0A%0A%20%20%20%20class%20Payment%20%7B%0A%20%20%20%20%20%20%20%20amount%0A%20%20%20%20%20%20%20%20date%0A%20%20%20%20%7D%0A%20%20%20%20class%20CreditCard%20%7B%0A%20%20%20%20%20%20%20%20cardNumber%0A%20%20%20%20%20%20%20%20expiry%0A%20%20%20%20%7D%0A%20%20%20%20class%20BankTransfer%20%7B%0A%20%20%20%20%20%20%20%20accountNumber%0A%20%20%20%20%20%20%20%20bankCode%0A%20%20%20%20%7D" />

CreditCard and BankTransfer are specialized types of Payment — they inherit `amount` and `date`.

### Aggregation vs. Composition

<MermaidChart code="classDiagram%0A%20%20%20%20Department%20o--%20Employee%20%3A%20aggregation%0A%20%20%20%20Order2%20*--%20OrderItem2%20%3A%20composition%0A%0A%20%20%20%20class%20Department%20%7B%20%7D%0A%20%20%20%20class%20Employee%20%7B%20%7D%0A%20%20%20%20class%20Order2%5B%22Order%22%5D%20%7B%20%7D%0A%20%20%20%20class%20OrderItem2%5B%22OrderItem%22%5D%20%7B%20%7D" />

::: warning Key Exam Distinction
**Aggregation** (hollow diamond): the part can exist independently of the whole.
**Composition** (filled diamond): the part cannot exist without the whole — if the whole is deleted, the parts are deleted too.
:::

## Goal Models

Goal models capture the **why** behind requirements — what stakeholders want to achieve.

Goals are decomposed into sub-goals, which eventually lead to concrete requirements.

<MermaidChart code="graph%20TD%0A%20%20%20%20G1%5BIncrease%20online%20sales%5D%0A%20%20%20%20G1%20--%3E%20G2%5BImprove%20user%20experience%5D%0A%20%20%20%20G1%20--%3E%20G3%5BReduce%20cart%20abandonment%5D%0A%20%20%20%20G2%20--%3E%20R1%5B%22Fast%20page%20loads%20(%3C%202%20sec)%22%5D%0A%20%20%20%20G3%20--%3E%20R2%5B%22Simplified%20checkout%20(3%20steps)%22%5D" />

Goal models help:
- **Justify** requirements — every requirement traces back to a business goal
- **Prioritize** — requirements supporting high-priority goals get higher priority
- **Detect conflicts** — conflicting goals produce conflicting requirements

## Choosing the Right Model

| If you need to show... | Use... |
|----------------------|--------|
| What the system does for users | Use case diagram |
| How a process flows step by step | Activity diagram |
| How an entity's state changes over time | State machine diagram |
| The data structure and relationships | Class diagram |
| Why requirements exist | Goal model |

## Practice Quiz

<Quiz :questions="questions" />

---

**Previous:** [← Chapter 5: Natural Language](/chapters/05-natural-language)
| **Next:** [Chapter 7: Validation & Negotiation →](/chapters/07-validation)
