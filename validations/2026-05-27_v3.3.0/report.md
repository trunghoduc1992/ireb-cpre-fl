# Validation Report: IREB CPRE-FL Study Guide vs. Official Resources

**Date:** 2026-05-27
**Official syllabus version:** 3.3.0 (April 1, 2026) — validated against v3.2.0 text (structurally identical; v3.3.0 is layout/typo fixes only)
**Official practice exam:** Set_Public_EN_v3.3.1 (45 questions, 70 points)
**Official glossary:** v2.2.0 (English)
**Official exam regulations:** v5.6.2

---

## 1. Syllabus Version — NOT DECLARED

The repo does not state which syllabus version it covers. The current official syllabus is **v3.3.0** (April 2026). Based on the 9-chapter structure, the repo follows the older **v2-era** training layout rather than the v3 syllabus's 7 Educational Units.

**Action:** Declare the syllabus version. Mark current content as "v2-era" and create a v3.3.0-aligned version.

---

## 2. Structural Mismatch (Critical)

### Official v3 Syllabus Structure (7 EUs)

| EU | Title | Level | Duration | Repo Mapping |
|----|-------|-------|----------|-------------|
| EU 1 | Introduction and Overview of Requirements Engineering | L2 | 1h | Ch 1 + Ch 2 (partial) |
| **EU 2** | **Fundamental Principles of Requirements Engineering** | **L2** | **1h 30m** | **NOT COVERED** |
| EU 3 | Work Products and Documentation Practices | L3 | 6h | Ch 4 + Ch 5 + Ch 6 |
| EU 4 | Practices for Requirements Elaboration | L3 | 4h 30m | Ch 2 (partial) + Ch 3 + Ch 7 |
| **EU 5** | **Process and Working Structure** | **L3** | **2h** | **NOT COVERED** |
| EU 6 | Management Practices for Requirements | L2 | 2h 30m | Ch 8 |
| EU 7 | Tool Support | L2 | 1h | Ch 9 |

### Official v3 Syllabus — Full Table of Contents

```
EU 1  Introduction and Overview of Requirements Engineering (L2) — 1h
  1.1  Requirements Engineering: What (L1)
  1.2  Requirements Engineering: Why (L2)
  1.3  Requirements Engineering: Where (L2)
  1.4  Requirements Engineering: How (L1)
  1.5  The Role and Tasks of a Requirements Engineer (L1)
  1.6  What to Learn about Requirements Engineering (L1)

EU 2  Fundamental Principles of Requirements Engineering (L2) — 1h 30m
  2.1  Overview of Principles (L1)
  2.2  The Principles Explained (L2)
       — Nine principles: value orientation, stakeholders, shared understanding,
         context & problem, requirement & solution, validation, evolution,
         innovation, systematic & disciplined work

EU 3  Work Products and Documentation Practices (L3) — 6h
  3.1  Work Products in Requirements Engineering (L2)
    3.1.1  Characteristics of Work Products (L1)
    3.1.2  Abstraction Levels (L2)
    3.1.3  Level of Detail (L2)
    3.1.4  Aspects to be Considered in Work Products (L1)
    3.1.5  General Documentation Guidelines (L1)
    3.1.6  Plan the Work Products to be Used (L1)
  3.2  Natural-Language-Based Work Products (L2)
  3.3  Template-Based Work Products (L3)
  3.4  Model-Based Work Products (L3)
    3.4.1  The Role of Models in Requirements Engineering (L2)
    3.4.2  Modeling Context (L2)
    3.4.3  Modeling Structure and Data (L3)
    3.4.4  Modeling Function and Flow (L3)
    3.4.5  Modeling State and Behavior (L2)
    3.4.6  Further Model Types in Requirements Engineering (L1)
  3.5  Glossaries (L2)
  3.6  Requirements Documents and Documentation Structures (L2)
  3.7  Prototypes in Requirements Engineering (L1)
  3.8  Quality Criteria for Work Products and Requirements (L1)

EU 4  Practices for Requirements Elaboration (L3) — 4h 30m
  4.1  Sources for Requirements (L3)
  4.2  Elicitation of Requirements (L2)
  4.3  Resolving Conflicts regarding Requirements (L2)
  4.4  Validation of Requirements (L2)

EU 5  Process and Working Structure (L3) — 2h
  5.1  Influencing Factors (L2)
  5.2  Requirements Engineering Process Facets (L2)
  5.3  Configuring a Requirements Engineering Process (L3)

EU 6  Management Practices for Requirements (L2) — 2h 30m
  6.1  What is Requirements Management? (L1)
  6.2  Life Cycle Management (L2)
  6.3  Version Control (L2)
  6.4  Configurations and Baselines (L1)
  6.5  Attributes and Views (L2)
  6.6  Traceability (L1)
  6.7  Handling Change (L1)
  6.8  Prioritization (L1)

EU 7  Tool Support (L2) — 1h
  7.1  Tools in Requirements Engineering (L1)
  7.2  Introducing Tools (L2)
```

### Missing Content (Critical)

**EU 2 — Fundamental Principles:** The nine principles are completely absent. These are: value orientation, stakeholders, shared understanding, context and problem, requirement and solution, validation, evolution, innovation, systematic and disciplined work. The official practice exam has **4 questions (6 points, 8.6%)** on this EU.

**EU 5 — Process and Working Structure:** RE process facets, influencing factors (plan-driven vs agile), and process configuration are not covered. The repo has only a single passing mention that RE activities are "not sequential." The official practice exam has **2 questions (3 points, 4.3%)** on this EU.

---

## 3. Exam Format Details

| Detail | Repo (exam-tips.md) | Official (Practice Exam v3.3.1) | Status |
|--------|--------------------|---------------------------------|--------|
| Questions | ~46 | 45 | Minor discrepancy |
| Duration | 75 min | 75 min (+15 for non-native speakers) | Missing non-native info |
| Total points | ~70 | 70 | Correct |
| Passing score | 70% (~49/70) | 70% (49/70) | Correct |
| Points per question | 1 or 2 | 1 or 2 | Correct |
| Question types | A-type, P-type, K-type | A-type, P-type, K-type | Correct |
| Allowed aids | None | None | Correct |

### Exam Weight by EU (from official practice exam)

| EU | Questions | Points | Weight | Repo's Approximate Weight |
|----|-----------|--------|--------|--------------------------|
| EU 1 — Introduction | 3 | 4 | 5.7% | Ch 1: ~7% |
| EU 2 — Principles | 4 | 6 | 8.6% | **Not shown (missing chapter)** |
| EU 3 — Work Products | 18 | 30 | 42.9% | Ch 4-6: ~40% |
| EU 4 — Practices | 10 | 14 | 20.0% | Ch 2+3+7: ~37% (split across 3 chapters) |
| EU 5 — Process | 2 | 3 | 4.3% | **Not shown (missing chapter)** |
| EU 6 — Management | 6 | 10 | 14.3% | Ch 8: ~13% |
| EU 7 — Tools | 2 | 3 | 4.3% | Ch 9: ~3% |

---

## 4. Practice Exams — Format OK, Scope Incomplete

Both repo sample exams (46 questions, 70 pts, A/P/K types) closely match the official format. However:

- They are custom-written, not sourced from the official practice exam (Set_Public_EN_v3.3.1)
- They contain **no questions on EU 2 (Principles) or EU 5 (Process)** since those chapters don't exist
- The official practice exam is free to download in 12 languages — not mentioned or linked
- Repo has 46 questions vs. official's 45

---

## 5. Glossary — No Version Reference

The repo has ~70 custom glossary terms. The official IREB Glossary is **v2.2.0** with standardized definitions in 13 languages. Issues:

- Definitions are paraphrases, not verbatim from the official glossary
- No version reference or link to official glossary
- May miss terms added in the v2.2.0 glossary
- The official syllabus states: "all terms in the glossary which are designated as foundational terms must be known (L1), even if they are not explicitly mentioned in the educational objectives"

---

## 6. Content Accuracy (Spot Checks)

What the repo covers is largely accurate:

| Topic | Status | Notes |
|-------|--------|-------|
| Requirement definition | Correct | Matches IREB definition |
| Three requirement types | Correct | Functional, quality, constraints |
| Four core RE activities | Correct | Elicitation, documentation, validation & negotiation, management |
| Elicitation techniques (8) | Correct | Interview, workshop, observation, questionnaire, document analysis, brainstorming, prototyping, perspective-based reading |
| Kano model | Correct | Properly placed in prioritization (Ch 8) |
| MoSCoW / Pairwise comparison | Correct | |
| UML diagrams | Correct | Use case, activity, state machine, class diagrams |
| Validation vs. verification | Correct | |
| Traceability types | Correct | Pre/post/inter-requirements |
| Natural language defects | Correct | Ambiguity, nominalization, passive voice, etc. |
| Sentence templates | Correct | |
| Quality criteria for requirements | Correct | |

---

## 7. No Links to Official Resources

The repo contains **zero references** to any official IREB resource:

| Resource | Version | URL |
|----------|---------|-----|
| Syllabus | v3.3.0 | [IREB Download Center](https://cpre.ireb.org/en/downloads-and-resources/downloads) |
| Handbook | v1.3.1 (EN) | [IREB Download Center](https://cpre.ireb.org/en/downloads-and-resources/downloads) |
| Glossary | v2.2.0 (EN) | [IREB Download Center](https://cpre.ireb.org/en/downloads-and-resources/downloads) |
| Practice Exam | Set_Public_EN_v3.3.1 | [IREB Download Center](https://cpre.ireb.org/en/downloads-and-resources/downloads) |
| Exam Regulations | v5.6.2 | [IREB Download Center](https://cpre.ireb.org/en/downloads-and-resources/downloads) |
| Nine Principles | v1.0.0 | [IREB Download Center](https://cpre.ireb.org/en/downloads-and-resources/downloads) |

---

## Summary of Issues by Severity

### Critical (exam coverage gaps)

1. **Missing EU 2 — Nine Fundamental Principles** (new in v3, 8.6% of exam points)
2. **Missing EU 5 — Process and Working Structure** (4.3% of exam points)
3. **No declared syllabus version** — readers don't know if the content is current

### Medium (exam detail inaccuracies)

4. **Exam question count:** repo says ~46, official is 45
5. **No mention of +15 min for non-native speakers**
6. **Practice exams don't cover all 7 EUs**
7. **Exam weight table doesn't map to the official 7-EU structure**

### Low (completeness / polish)

8. No links to any official IREB resources
9. Glossary not tied to official IREB glossary version or verbatim definitions
10. Chapter numbering follows v2-era layout, not v3 EU numbering
