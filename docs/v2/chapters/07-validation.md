<script setup>
import Quiz from '../../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'What is the primary goal of requirements validation?',
    options: [
      'To verify that the code correctly implements the requirements',
      'To ensure that documented requirements correctly reflect stakeholder intentions and meet quality criteria',
      'To prioritize requirements for the next sprint',
      'To create test cases from requirements',
    ],
    answer: 1,
    explanation: 'Validation checks that requirements correctly capture what stakeholders actually want and that the specification meets quality criteria. Verification of code is a different activity (done during testing).',
  },
  {
    text: 'What is the difference between validation and verification in the IREB context?',
    options: [
      'They are the same thing with different names',
      'Validation checks requirements against stakeholder intentions; verification checks artifacts against specifications',
      'Validation is done by testers; verification is done by BAs',
      'Validation uses models; verification uses natural language',
    ],
    answer: 1,
    explanation: 'Validation = "Are we building the right thing?" (do requirements match what stakeholders need?). Verification = "Are we building the thing right?" (does the artifact conform to specifications?).',
  },
  {
    text: 'Which validation technique involves a formal, structured review with defined roles (author, moderator, reviewer, scribe)?',
    options: [
      'Walkthrough',
      'Ad-hoc review',
      'Inspection',
      'Perspective-based reading',
    ],
    answer: 2,
    explanation: 'An inspection is the most formal review technique, with defined roles (moderator, author, reviewers, scribe), a structured process, entry/exit criteria, and documented findings.',
  },
  {
    text: 'What is a requirements conflict?',
    options: [
      'A missing requirement that no stakeholder has identified',
      'A requirement that cannot be implemented due to technical limitations',
      'A situation where two or more requirements contradict each other or stakeholders have incompatible expectations',
      'A requirement that fails validation',
    ],
    answer: 2,
    explanation: 'A conflict exists when requirements contradict each other (e.g., one says "encrypt all data" while a constraint says "use a system that doesn\'t support encryption") or when stakeholders have incompatible expectations that cannot all be satisfied.',
  },
  {
    text: 'Which of the following is NOT a typical conflict resolution strategy?',
    options: [
      'Compromise — both parties give up something',
      'Voting — majority decides',
      'Ignoring — pretend the conflict doesn\'t exist',
      'Overruling — a person with authority decides',
    ],
    answer: 2,
    explanation: 'Ignoring a conflict is not a resolution strategy — it leads to problems later when the contradiction surfaces during development or testing. IREB lists agreement, compromise, voting, overruling, and other structured approaches.',
  },
  {
    text: 'Which quality aspect is being checked when a reviewer asks: "Can we write a test for this requirement?"',
    options: [
      'Completeness',
      'Correctness',
      'Verifiability',
      'Traceability',
    ],
    answer: 2,
    explanation: 'Verifiability means a requirement is testable — you can determine objectively whether it has been fulfilled. If you can\'t write a test for it, the requirement needs to be made more specific.',
  },
]
</script>

# Chapter 7: Validation & Negotiation

<div class="exam-tip">
  <strong>Exam weight:</strong> ~15% of questions. Focus on the difference between validation/verification and know the review techniques.
</div>

## Fundamentals of Validation

<div class="key-concept">

**Requirements Validation** ensures that documented requirements:
1. Correctly reflect stakeholder intentions (are we capturing the right needs?)
2. Meet quality criteria (are they complete, consistent, unambiguous?)
3. Are agreed upon by relevant stakeholders

</div>

### Validation vs. Verification

This is a critical distinction:

| | Validation | Verification |
|---|-----------|-------------|
| **Question** | "Are we building the **right** thing?" | "Are we building the thing **right**?" |
| **Checks** | Requirements against stakeholder intentions | Artifact against its specification |
| **When** | During RE, before development starts | During development and testing |
| **Who** | Stakeholders + requirements engineers | Developers + testers |

::: warning Exam Tip
Remember: **Validation** = right product. **Verification** = product right. The exam tests this distinction frequently.
:::

::: tip From Your Experience
As a tester, you do verification when you test code against requirements. As a BA, you do validation when you review specs with stakeholders. Understanding both sides makes the distinction intuitive.
:::

## Quality Aspects to Check

During validation, check requirements against these quality aspects:

### For Individual Requirements

| Quality Aspect | Question to Ask |
|---------------|-----------------|
| **Correct** | Does this requirement accurately reflect the stakeholder's intention? |
| **Complete** | Does it contain all necessary information? Are edge cases covered? |
| **Unambiguous** | Is there only one possible interpretation? |
| **Consistent** | Does it contradict any other requirement? |
| **Verifiable** | Can we write a test to determine if this is fulfilled? |
| **Traceable** | Can we trace it back to its source and forward to design/test artifacts? |
| **Necessary** | Is there a justified need for this requirement? |
| **Feasible** | Can it realistically be implemented within constraints? |

### For the Entire Specification

| Quality Aspect | Question to Ask |
|---------------|-----------------|
| **Complete** | Are all relevant requirements documented? Are there gaps? |
| **Consistent** | Are there contradictions between requirements? |
| **Unambiguous** | Is terminology used consistently (glossary)? |
| **Modifiable** | Can the spec be changed without cascading side effects? |
| **Traceable** | Do all requirements have unique IDs? Are cross-references in place? |

## Validation Techniques

### 1. Review (General)

Structured examination of requirements by one or more reviewers. Reviews range from informal to highly formal.

### 2. Walkthrough

The **author** leads reviewers through the document, explaining the content.

| Aspect | Detail |
|--------|--------|
| **Formality** | Low to medium |
| **Led by** | Author |
| **Goal** | Understanding, education, finding major issues |
| **Preparation** | Reviewers may or may not prepare in advance |

**Pros:** Easy to organize, author can explain context.
**Cons:** Author bias — they may steer reviewers away from problems.

### 3. Inspection

The most **formal** review technique with defined roles, processes, and metrics.

| Aspect | Detail |
|--------|--------|
| **Formality** | High |
| **Led by** | Moderator (not the author) |
| **Roles** | Author, moderator, reviewer(s), scribe |
| **Goal** | Systematic defect detection |
| **Preparation** | Mandatory — reviewers prepare individually before the meeting |
| **Process** | Planning → individual preparation → meeting → rework → follow-up |

**Pros:** Most effective at finding defects; produces measurable results.
**Cons:** Time-consuming, requires trained moderators.

<div class="key-concept">

**Inspection roles:**
- **Moderator** — facilitates the meeting, ensures process is followed (NOT the author)
- **Author** — answers questions but does NOT lead the review
- **Reviewer(s)** — examine the document and report findings
- **Scribe** — records defects and decisions

</div>

### 4. Perspective-Based Reading

Each reviewer examines the specification from a **specific stakeholder perspective**.

<div class="example-box">

**Example perspectives:**
- **User perspective**: Can I perform all my tasks? Are the workflows logical?
- **Developer perspective**: Is this implementable? Are there enough technical details?
- **Tester perspective**: Can I derive test cases? Are success and failure scenarios defined?
- **Operator perspective**: Can I deploy, monitor, and maintain this system?
</div>

This technique systematically increases coverage — each perspective catches different types of issues.

### 5. Prototyping (for Validation)

Using a prototype to validate requirements with stakeholders. Let them interact with a concrete representation of the system.

**When useful:**
- Stakeholders can't evaluate abstract text requirements
- UI/UX requirements need visual confirmation
- Complex workflows need hands-on validation

### Comparison of Techniques

| Technique | Formality | Defect Detection | Effort | Best For |
|-----------|----------|-------------------|--------|----------|
| Walkthrough | Low | Low-Medium | Low | Understanding, education |
| Inspection | High | High | High | Critical or high-risk specs |
| Perspective-based | Medium | Medium-High | Medium | Completeness checks |
| Prototyping | Low | Medium (UX-focused) | Medium-High | UI/workflow validation |

## Conflict and Negotiation

### Types of Conflicts

Conflicts arise when stakeholders have **incompatible requirements** or expectations.

| Conflict Type | Example |
|--------------|---------|
| **Data conflict** | Different stakeholders cite different facts ("We have 1,000 users" vs. "We have 5,000 users") |
| **Interest conflict** | Sales wants rapid delivery; Security wants thorough review |
| **Value conflict** | Stakeholders fundamentally disagree on priorities (cost vs. quality) |
| **Relationship conflict** | Personal tensions between stakeholders affect discussions |
| **Structural conflict** | Organizational constraints create conflicting goals |

### Conflict Resolution Strategies

<div class="key-concept">

IREB describes several resolution strategies:

1. **Agreement (consensus)** — all parties reach a solution everyone supports. Best outcome but hardest to achieve.
2. **Compromise** — each party gives up something. Acceptable but may leave everyone partially unsatisfied.
3. **Voting** — the majority decides. Democratic but may alienate the minority.
4. **Overruling** — a person with authority (sponsor, manager) makes the decision. Fast but can create resentment.
5. **Mediation** — a neutral third party helps facilitate resolution.

</div>

### The Requirements Engineer's Role in Conflicts

The RE acts as a **neutral mediator**:
- Surface conflicts early (don't hide them)
- Ensure all perspectives are heard
- Document conflicting positions objectively
- Facilitate resolution using appropriate strategies
- Escalate to decision-makers when needed

<div class="example-box">

**Practical example:**

Marketing wants: "The user registration form should have minimal fields (name and email only) to maximize sign-ups."

Legal wants: "The registration form must collect full address and date of birth for regulatory compliance."

**Resolution approach:** The RE facilitates a session to understand the underlying goals. The compromise: a two-step registration — minimal fields for initial sign-up (marketing satisfied), with additional fields collected before the first transaction (legal satisfied).
</div>

## Practice Quiz

<Quiz :questions="questions" />

---

**Previous:** [← Chapter 6: Model-Based Documentation](/v2/chapters/06-models)
| **Next:** [Chapter 8: Requirements Management →](/v2/chapters/08-management)
