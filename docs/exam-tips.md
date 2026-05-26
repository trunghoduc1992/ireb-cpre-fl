# Exam Tips

## About the Exam

| Detail | Value |
|--------|-------|
| **Duration** | 75 minutes |
| **Questions** | 45 multiple-choice |
| **Passing score** | 60% (27 of 45 correct) |
| **Question types** | Single-select and multiple-select |
| **Allowed aids** | None (closed book) |
| **Languages** | Multiple (English, German, etc.) |

## Question Weighting by Chapter

| Chapter | Approx. Weight |
|---------|---------------|
| 1. Introduction & Foundations | ~7% |
| 2. System & System Context | ~7% |
| 3. Requirements Elicitation | ~15% |
| 4–6. Documentation (all parts) | ~40% |
| 7. Validation & Negotiation | ~15% |
| 8. Requirements Management | ~13% |
| 9. Tool Support | ~3% |

Documentation chapters carry the most weight — focus your study there.

## Key Strategies

### Read the Question Carefully
- Watch for qualifiers like "always", "never", "can", "must" — they change the meaning.
- For multi-select questions, the number of correct answers is stated (e.g., "select two").

### Know the IREB Definitions
The exam uses IREB's specific definitions. For example:
- **Requirement** = a condition or capability needed by a stakeholder to solve a problem or achieve an objective, *that must be met or possessed by a system*.
- **Stakeholder** = a person or organization that influences or is influenced by the system requirements.
- Don't rely on informal definitions from your work experience.

### Distinguish Similar Concepts
Common traps:
- **Verification vs. Validation** — Verification checks the spec against standards; Validation checks the spec against stakeholder intentions.
- **System context vs. System boundary** — Context includes relevant environment; boundary separates system from context.
- **Requirements specification vs. System specification** — Requirements spec describes *what*; System spec describes *how* (at solution level).

### Models Are Heavily Tested
Expect questions about:
- **Use case diagrams**: actors, use cases, relationships (include, extend, generalization)
- **Activity diagrams**: actions, decisions, forks/joins, swim lanes
- **State machine diagrams**: states, transitions, events, guards
- **Class diagrams**: classes, associations, multiplicities, inheritance
- **Entity-relationship models**: entities, relationships, cardinalities

You need to *read* these diagrams, not draw them from scratch.

### Process of Elimination
- If stuck, eliminate obviously wrong answers first.
- Look for answers that are too absolute ("always", "never") — they're often wrong.
- Prefer answers that match IREB terminology over generic software engineering terms.

### Time Management
- 75 minutes for 45 questions = ~100 seconds per question.
- Don't spend more than 2 minutes on any single question.
- Flag difficult questions and return to them.

## Common Mistakes to Avoid

1. **Confusing functional and quality requirements.** "The system shall respond within 2 seconds" is a *quality* requirement, not functional.
2. **Mixing up elicitation techniques.** Know which technique is best for which situation.
3. **Forgetting about constraints.** Constraints are requirements imposed by the organizational or technological environment — they are not negotiable.
4. **Ignoring the glossary role.** In IREB's view, a glossary is essential for avoiding ambiguity. Questions often test this.
5. **Overlooking traceability types.** Pre-traceability (requirement ← source) vs. post-traceability (requirement → artifact) vs. inter-requirement traceability.
