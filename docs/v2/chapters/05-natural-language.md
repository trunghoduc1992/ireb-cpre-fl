<script setup>
import Quiz from '../../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'Which of the following is an example of a nominalization that should be avoided in requirements?',
    options: [
      '"The system shall validate the input"',
      '"The validation of the input shall be performed"',
      '"The system shall display an error message"',
      '"The user shall enter their credentials"',
    ],
    answer: 1,
    explanation: '"The validation" is a nominalization — it turns the verb "validate" into a noun and obscures who performs the action and when. "The system shall validate the input" is clearer because it has a defined subject and verb.',
  },
  {
    text: 'What is the purpose of a requirements template (sentence template)?',
    options: [
      'To make requirements shorter',
      'To provide a consistent syntactic structure that reduces ambiguity',
      'To eliminate the need for models',
      'To automatically generate test cases',
    ],
    answer: 1,
    explanation: 'Sentence templates provide a consistent structure (e.g., "The system shall <verb> <object> <condition>") that reduces ambiguity by ensuring each requirement has a clear subject, action, and object.',
  },
  {
    text: 'What is the main purpose of a glossary in requirements engineering?',
    options: [
      'To document all system functions',
      'To ensure all stakeholders share the same understanding of key terms',
      'To replace the requirements specification',
      'To list all stakeholders and their roles',
    ],
    answer: 1,
    explanation: 'A glossary defines domain-specific and project-specific terms to avoid ambiguity. When all stakeholders agree on term definitions, the risk of misunderstanding requirements is significantly reduced.',
  },
  {
    text: 'Which phrase indicates a vague, non-verifiable requirement?',
    options: [
      '"The system shall respond within 3 seconds"',
      '"The system shall be user-friendly"',
      '"The system shall encrypt passwords using SHA-256"',
      '"The system shall send a confirmation email within 1 minute"',
    ],
    answer: 1,
    explanation: '"User-friendly" is subjective and cannot be measured or tested. The other options are specific and verifiable. This is a classic example of a vague quality requirement that needs refinement.',
  },
  {
    text: 'According to IREB, what does the keyword "shall" indicate in a requirement?',
    options: [
      'A suggestion that may be ignored',
      'A legally binding obligation that must be fulfilled',
      'A future enhancement for the next release',
      'An optional feature for user convenience',
    ],
    answer: 1,
    explanation: '"Shall" indicates a mandatory requirement — it must be fulfilled. "Should" indicates a recommended requirement, and "may" or "can" indicate optional features. This follows the RFC 2119 convention.',
  },
  {
    text: 'Which of the following requirements contains a passive voice problem?',
    options: [
      '"The system shall log all failed login attempts"',
      '"Failed login attempts shall be logged"',
      '"The security module shall log each failed login attempt with timestamp and IP address"',
      '"An administrator shall review logged login attempts weekly"',
    ],
    answer: 1,
    explanation: '"Failed login attempts shall be logged" uses passive voice — it doesn\'t specify WHO or WHAT does the logging. The active alternatives clearly state the subject (system, security module, administrator).',
  },
]
</script>

# Chapter 5: Natural Language Documentation

<div class="exam-tip">
  <strong>Exam weight:</strong> Part of the ~40% documentation block. Focus on language pitfalls, sentence templates, and the glossary.
</div>

## Natural Language: Strengths and Weaknesses

Natural language is the most common form of requirements documentation because everyone can read it. But it comes with inherent risks.

| Strengths | Weaknesses |
|-----------|------------|
| Universally readable | Ambiguous by nature |
| Flexible, expressive | Prone to incompleteness |
| No special tools needed | Inconsistent terminology |
| Natural for stakeholder review | Hard to analyze automatically |

The goal is not to *avoid* natural language, but to **use it carefully** with rules and patterns that reduce its weaknesses.

## Common Language Defects

### 1. Ambiguity

A requirement that can be interpreted in more than one way.

<div class="example-box">

**Ambiguous:** "The system shall display the customer's recent orders."

- How recent? Last 7 days? Last 10 orders?
- Display where? On the dashboard? In a separate page?
- Which customer? The logged-in user? Any customer an admin selects?

**Clear:** "The system shall display the 10 most recent orders for the currently logged-in customer on the customer dashboard page."
</div>

### 2. Nominalization

Turning verbs into nouns, which hides the actor and action.

<div class="example-box">

**Nominalization:** "The *calculation* of the total shall occur after *addition* of all items."

Who calculates? When does it happen? What triggers it?

**Clear:** "The system shall *calculate* the order total after the customer *adds* the last item to the cart."
</div>

### 3. Passive Voice (Missing Subject)

Omitting who performs the action.

<div class="example-box">

**Passive:** "The report shall be generated weekly."

Who generates it? The system automatically? An admin manually?

**Active:** "The system shall automatically generate the sales report every Monday at 06:00."
</div>

### 4. Vague Adjectives and Adverbs

Words like "fast", "user-friendly", "easy", "adequate", "appropriate" are not measurable.

<div class="example-box">

**Vague:** "The system shall be fast."

**Measurable:** "The system shall respond to any user action within 2 seconds under normal load (up to 500 concurrent users)."
</div>

### 5. Incomplete Conditions

Missing boundary cases, error handling, or exception scenarios.

<div class="example-box">

**Incomplete:** "The system shall apply a 10% discount for premium customers."

What about customers who became premium mid-order? What if the discount conflicts with another promotion? What is a "premium customer" exactly?

**Better:** "The system shall apply a 10% discount to the order total for customers whose account type is 'Premium' at the time of order submission. This discount shall not be combined with promotional discounts; the higher discount applies."
</div>

## Requirement Keywords (Legal Obligation Levels)

IREB uses keywords (following RFC 2119 conventions) to indicate the obligation level of a requirement:

| Keyword | Obligation | Meaning |
|---------|-----------|---------|
| **shall** | Mandatory | Must be fulfilled — non-negotiable |
| **should** | Recommended | Expected to be fulfilled unless there's a justified reason not to |
| **may** / **can** | Optional | Nice to have; implementation is at discretion |

::: warning Exam Tip
If a question asks about the difference between "shall", "should", and "may" — "shall" is always mandatory. This is tested frequently.
:::

## Sentence Templates

Sentence templates (also called requirement patterns or boilerplates) provide a **consistent syntactic structure** for writing requirements.

### Basic Template

```
The <system/component> shall <verb> <object> <condition/qualifier>.
```

**Examples:**
- "The system **shall display** the account balance **when the user opens the dashboard**."
- "The payment module **shall encrypt** all credit card numbers **using AES-256 encryption**."

### Extended Templates

For more complex requirements, templates can include conditions, events, and temporal aspects:

```
<Condition>, the <system> shall <verb> <object>.
```
- "**When the session has been inactive for 30 minutes**, the system shall **log out the user automatically**."

```
The <system> shall be able to <verb> <object> <quality measure>.
```
- "The system shall be able to **process up to 10,000 transactions per hour**."

### Benefits of Templates

1. **Consistency** — all requirements follow the same structure
2. **Completeness** — the template prompts authors to fill in subject, verb, object, condition
3. **Reduced ambiguity** — clear structure makes requirements easier to parse
4. **Easier review** — reviewers can quickly check if all parts are filled in

## The Glossary

<div class="key-concept">

A **glossary** is a collection of term definitions that ensures all stakeholders share a common understanding of domain-specific and project-specific vocabulary.

</div>

### Why a Glossary is Essential

- **Different stakeholders use different terms** for the same concept (synonyms)
- **The same term can mean different things** to different people (homonyms)
- **Technical jargon** may not be understood by all stakeholders
- Without agreed definitions, requirements are inherently ambiguous

<div class="example-box">

**Real-world confusion:**

The term "order" might mean:
- A customer's purchase request (e-commerce team)
- A work order for manufacturing (operations team)
- A database record in the orders table (development team)

The glossary entry would define which meaning applies in this project and note the alternatives.
</div>

### Glossary Entry Structure

A good glossary entry contains:

| Field | Purpose |
|-------|---------|
| **Term** | The word or phrase being defined |
| **Definition** | Clear, unambiguous meaning in this project's context |
| **Synonyms** | Other terms that mean the same thing |
| **Abbreviation** | Short form, if any |
| **Source** | Where the definition comes from |

### Glossary Best Practices

1. **Start the glossary early** — from the first elicitation session
2. **Involve stakeholders** — they must agree on definitions
3. **Use glossary terms consistently** — every occurrence in the spec should match the glossary definition
4. **Highlight glossary terms** in requirements (e.g., bold, italics, or links)
5. **Maintain it throughout the project** — add new terms as they emerge

::: info Key Exam Point
The exam treats the glossary as a **mandatory artifact** for quality requirements documentation. Expect at least one question about its purpose and usage.
:::

## Practical Guidelines Summary

| Guideline | Why |
|-----------|-----|
| Use **active voice** | Makes the responsible actor clear |
| Avoid **nominalizations** | Keeps actions and actors visible |
| Use **requirement keywords** (shall/should/may) | Clarifies obligation level |
| Avoid **vague terms** (fast, easy, etc.) | Ensures verifiability |
| Use **sentence templates** | Ensures consistency and completeness |
| Maintain a **glossary** | Eliminates term ambiguity |
| **One requirement per sentence** | Makes requirements traceable and testable |
| Write **complete conditions** | Covers all cases including exceptions |

## Practice Quiz

<Quiz :questions="questions" />

---

**Previous:** [← Chapter 4: Documentation Basics](/v2/chapters/04-documentation)
| **Next:** [Chapter 6: Model-Based Documentation →](/v2/chapters/06-models)
