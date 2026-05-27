# Implementation Plan: Create IREB CPRE-FL v3.3.0 Study Guide

**Based on:** [Validation Report](report.md) (2026-05-27)
**Goal:** Create a new version of the study guide aligned with the official IREB Certified Professional for Requirements Engineering (CPRE) Foundation Level (FL) Syllabus v3.3.0 (April 2026)

## Scope and Versioning Strategy

The existing study guide content (chapters, glossary, sample exams, study plan, exam tips) is frozen as the **v2 version**. It will not be modified.

All work described in this plan produces **new v3.3.0 content** served under a separate URL path. The two versions coexist via a version selector in the site navigation.

| Version | Content | Status |
|---------|---------|--------|
| v2 | Current 9-chapter study guide, glossary, 2 sample exams | Frozen as-is |
| v3.3.0 | New 7-Educational Unit (EU) study guide aligned with Syllabus v3.3.0 | To be created |

---

## Terminology

This plan uses the following abbreviations after their first introduction:

- **CPRE-FL** — Certified Professional for Requirements Engineering, Foundation Level
- **EU** — Educational Unit (the official IREB term for a main chapter of the syllabus; the v3 syllabus has 7 EUs)
- **Educational Objective (EO)** — a numbered learning goal within an EU (e.g., EO 4.2.1)
- **Cognitive levels** — L1 (know/remember), L2 (understand/explain), L3 (apply/design), as defined by the syllabus
- **Requirements Engineering (RE)** — the systematic approach to eliciting, documenting, validating, and managing requirements

---

## Phase 0: Versioning Infrastructure

### 0.1 Set up version dropdown and URL prefixes
- Build a VitePress versioning mechanism with a navbar dropdown (`v2` / `v3.3.0`)
- Copy current content into a `/v2/` URL path (frozen, read-only going forward)
- Create the `/v3/` URL path as the default for new v3.3.0 content
- Update `docs/.vitepress/config.js` with the version selector

### 0.2 Scaffold the v3.3.0 content structure
- Create the v3.3.0 directory layout with empty chapter files matching the 7-EU structure
- Add a prominent banner to the v3.3.0 index page: "Aligned with IREB CPRE-FL Syllabus v3.3.0 (April 2026)"
- Add a notice to the v2 index page: "This version covers an older syllabus. See v3.3.0 for the current exam."

**Files to create:** v3.3.0 directory tree, `docs/.vitepress/config.js` updates
**Files to modify:** v2 `index.md` (add notice banner only)

---

## Phase 1: Write the 7-EU Chapter Content

All chapters are written fresh for v3.3.0. The extracted syllabus text (`downloads/cpre_foundationlevel_syllabus_EN_v3.2.0.txt`) serves as the authoritative source for structure, Educational Objectives, and terminology.

### 1.1 EU 1 — Introduction and Overview of Requirements Engineering (L2, 1 hour)

- **New file:** `v3/chapters/01-introduction.md`
- **Syllabus sections:** 1.1 through 1.6
- **Educational Objectives:** EO 1.1.1 through EO 1.6.1
- **Key terms:** requirement, requirements specification, Requirements Engineering, stakeholder, system, Requirements Engineer
- **Content sources:** Syllabus pages 11-13; may reuse and adapt material from v2 Ch 1
- **Include:** 3-4 quiz questions (matching ~5.7% exam weight)

### 1.2 EU 2 — Fundamental Principles of Requirements Engineering (L2, 1 hour 30 minutes)

- **New file:** `v3/chapters/02-principles.md`
- **Syllabus sections:** 2.1 (Overview of Principles), 2.2 (The Principles Explained)
- **Content:** The nine fundamental principles:
  1. Value orientation
  2. Stakeholders
  3. Shared understanding
  4. Context and problem
  5. Requirement and solution
  6. Validation
  7. Evolution (continuous change)
  8. Innovation
  9. Systematic and disciplined work
- **Source:** Syllabus pages 14-18
- **Include:** 4-5 quiz questions (matching ~8.6% exam weight)
- **Note:** This EU is entirely new — no v2 content to draw from

### 1.3 EU 3 — Work Products and Documentation Practices (L3, 6 hours)

- **New file(s):** `v3/chapters/03-work-products.md` with sub-pages to avoid an excessively long single page:
  - `03a-work-product-basics.md` — sections 3.1, 3.6, 3.7, 3.8
  - `03b-natural-language.md` — sections 3.2, 3.3, 3.5
  - `03c-models.md` — sections 3.4.1 through 3.4.6
- **Syllabus sections:** 3.1 through 3.8
- **Educational Objectives:** EO 3.1.1 through EO 3.8.1
- **Key terms:** work product, natural language, template, model, glossary, requirements document, prototype, quality criteria, abstraction level, class diagram, use case diagram, activity diagram, state machine diagram
- **Source:** Syllabus pages 19-30; may reuse and adapt material from v2 Ch 4, 5, 6
- **Include:** 14-16 quiz questions (matching ~42.9% exam weight)

### 1.4 EU 4 — Practices for Requirements Elaboration (L3, 4 hours 30 minutes)

- **New file(s):** `v3/chapters/04-practices.md` with optional sub-pages:
  - `04a-sources-and-elicitation.md` — sections 4.1, 4.2
  - `04b-conflicts-and-validation.md` — sections 4.3, 4.4
- **Syllabus sections:** 4.1 through 4.4
- **Educational Objectives:** EO 4.1.1 through EO 4.4.3
- **Key terms:** requirements source, system boundary, system context, requirements elicitation, requirements validation, stakeholder, Kano model, conflict, conflict resolution
- **Source:** Syllabus pages 31-35; may reuse and adapt material from v2 Ch 2, 3, 7
- **Include:** 8-10 quiz questions (matching ~20% exam weight)
- **Note:** In the v3 syllabus, system context and stakeholder analysis moved here (from what was a standalone chapter in v2)

### 1.5 EU 5 — Process and Working Structure (L3, 2 hours)

- **New file:** `v3/chapters/05-process.md`
- **Syllabus sections:** 5.1 (Influencing Factors), 5.2 (RE Process Facets), 5.3 (Configuring an RE Process)
- **Educational Objectives:** EO 5.1.1 through EO 5.3.3
- **Key terms:** influencing factor, process facet, plan-driven, agile, iterative, incremental, process configuration
- **Source:** Syllabus pages 36-40
- **Include:** 2-3 quiz questions (matching ~4.3% exam weight)
- **Note:** This EU is entirely new — no v2 content to draw from

### 1.6 EU 6 — Management Practices for Requirements (L2, 2 hours 30 minutes)

- **New file:** `v3/chapters/06-management.md`
- **Syllabus sections:** 6.1 through 6.8
- **Educational Objectives:** EO 6.1.1 through EO 6.8.1
- **Key terms:** requirements management, life cycle, version control, configuration, baseline, attribute, view, traceability, change management, prioritization
- **Source:** Syllabus pages 41-44; may reuse and adapt material from v2 Ch 8
- **Include:** 5-6 quiz questions (matching ~14.3% exam weight)

### 1.7 EU 7 — Tool Support (L2, 1 hour)

- **New file:** `v3/chapters/07-tools.md`
- **Syllabus sections:** 7.1 (Tools in RE), 7.2 (Introducing Tools)
- **Educational Objectives:** EO 7.1.1 through EO 7.2.2
- **Key terms:** RE tool, tool evaluation, tool introduction
- **Source:** Syllabus pages 45-46; may reuse and adapt material from v2 Ch 9
- **Include:** 2 quiz questions (matching ~4.3% exam weight)

---

## Phase 2: Exam Tips and Practice Exams (v3.3.0)

### 2.1 Create v3.3.0 exam tips page
- **New file:** `v3/exam-tips.md`
- **Exam format (from official practice exam Set_Public_EN_v3.3.1):**
  - 45 questions
  - 75 minutes (90 minutes for non-native speakers)
  - 70 total points; passing score 70% (49 points)
  - Question types: A-type (single-select, 1 point), P-type (pick-two, 1-2 points), K-type (true/false matrix, 2 points)
- **Weight table aligned to the 7-EU structure:**

  | Educational Unit | Questions | Points | Weight |
  |------------------|-----------|--------|--------|
  | EU 1 — Introduction and Overview | 3 | 4 | 5.7% |
  | EU 2 — Fundamental Principles | 4 | 6 | 8.6% |
  | EU 3 — Work Products and Documentation | 18 | 30 | 42.9% |
  | EU 4 — Practices for Elaboration | 10 | 14 | 20.0% |
  | EU 5 — Process and Working Structure | 2 | 3 | 4.3% |
  | EU 6 — Management Practices | 6 | 10 | 14.3% |
  | EU 7 — Tool Support | 2 | 3 | 4.3% |

- Include link to official exam regulations v5.6.2 and official practice exam

### 2.2 Create v3.3.0 practice exams
- **New files:** `v3/exams/exam-1.md`, `v3/exams/exam-2.md`
- 45 questions each, 70 total points, matching the official EU distribution above
- All question types represented (A-type, P-type, K-type)
- Each question tagged with its EU in the source code comments
- Must include questions for EU 2 (Principles) and EU 5 (Process)
- Add a prominent link to the official IREB practice exam (free, 12 languages)

---

## Phase 3: Glossary (v3.3.0)

### 3.1 Download and extract the official IREB Glossary v2.2.0
- Download from the [IREB Download Center](https://cpre.ireb.org/en/downloads-and-resources/downloads)
- Extract text using PyMuPDF (same method used for the syllabus)
- Parse into structured term-definition pairs

### 3.2 Create a new v3.3.0 glossary with verbatim definitions
- **New file:** `v3/glossary.md`
- Use verbatim term-definition pairs from the official IREB Glossary v2.2.0
- Include all terms designated as "foundational" (the syllabus states these must be known at L1 even if not explicitly mentioned in Educational Objectives)
- Preserve the Vue component for search and filtering
- Add header: "Source: IREB CPRE Glossary v2.2.0 (English)"
- Add link to the official glossary download page

---

## Phase 4: Study Plan, Resources, and Cross-Links (v3.3.0)

### 4.1 Create a v3.3.0 study plan
- **New file:** `v3/study-plan.md`
- Structure the plan around the 7 EUs with time estimates matching the syllabus durations:
  - EU 1: 1 hour, EU 2: 1.5 hours, EU 3: 6 hours, EU 4: 4.5 hours, EU 5: 2 hours, EU 6: 2.5 hours, EU 7: 1 hour
- Recommend downloading the official syllabus and handbook as companion references

### 4.2 Create a dedicated resources page
- **New file:** `v3/resources.md`
- List all official IREB resources with their versions and download links:

  | Resource | Version | Source |
  |----------|---------|--------|
  | CPRE-FL Syllabus | v3.3.0 | IREB Download Center |
  | CPRE-FL Handbook | v1.3.1 (English) | IREB Download Center |
  | CPRE Glossary | v2.2.0 (English) | IREB Download Center |
  | Practice Exam | Set_Public_EN_v3.3.1 | IREB Download Center |
  | Examination Regulations | v5.6.2 | IREB Download Center |
  | Nine Fundamental Principles | v1.0.0 | IREB Download Center |
  | Requirements Engineering Poster | v1.0.0 | IREB Download Center |

### 4.3 Add EU reference links to every chapter page
- Add a standardized info box to each chapter:
  ```
  Official Reference: IREB CPRE-FL Syllabus v3.3.0, Educational Unit X
  Download: https://cpre.ireb.org/en/downloads-and-resources/downloads
  ```

### 4.4 Create v3.3.0 index page
- **New file:** `v3/index.md`
- Feature overview highlighting the 7-EU structure
- Links to study plan, glossary, exams, and resources

---

## Phase 5: Content Review and Quality Assurance

### 5.1 Cross-reference every Educational Objective
- For each EU, verify that all Educational Objectives listed in the syllabus are addressed in the corresponding chapter
- Ensure the cognitive level of the content matches the EO level:
  - L1 content should define/list/name
  - L2 content should explain/compare/justify
  - L3 content should apply/design/write
- Add coverage of any missing Educational Objectives

### 5.2 Verify key terms per EU
- The syllabus lists key terms at the beginning of each EU
- Confirm every listed term appears in the chapter content and in the glossary

### 5.3 Review quiz questions against Educational Objectives
- Each quiz question should map to a specific Educational Objective
- The cognitive level of a question should not exceed the level of its Educational Objective
- Validate that the EU distribution of quiz questions matches the official exam weight table

### 5.4 Run a second validation
- Repeat the validation process (same method as [this report](report.md)) against the completed v3.3.0 content
- Save results to a new directory under `validations/` for comparison

---

## Execution Order and Dependencies

```
Phase 0 (Versioning) ──► Phase 1 (7 EU Chapters) ──► Phase 2 (Exams)
                                                           │
                                                           ▼
                              Phase 3 (Glossary) ──► Phase 4 (Links & Resources)
                                                           │
                                                           ▼
                                                    Phase 5 (Review)
```

- **Phase 0** must complete first (sets up the versioning infrastructure before any v3.3.0 content is added)
- **Phase 1** is the largest body of work and must be substantially complete before Phase 2 (practice exam questions depend on chapter content)
- **Phase 3** can run in parallel with Phase 1 (glossary extraction is independent of chapter writing)
- **Phase 4** depends on Phase 1 (needs chapter files to exist for cross-linking)
- **Phase 5** runs last as a final quality gate

## Estimated Effort

| Phase | Description | Effort |
|-------|-------------|--------|
| Phase 0 | Versioning infrastructure and scaffolding | 2-3 hours |
| Phase 1 | Write 7 EU chapters with quiz questions | 8-12 hours |
| Phase 2 | Exam tips and 2 practice exams (45 questions each) | 3-4 hours |
| Phase 3 | Glossary extraction and creation | 2-3 hours |
| Phase 4 | Study plan, resources page, cross-links | 2-3 hours |
| Phase 5 | Content review and second validation | 3-4 hours |
| **Total** | | **20-29 hours** |

## Reference Documents

All source documents for this work are stored in `validations/2026-05-27_v3.3.0/downloads/` with extracted text versions. See `downloads.json` for provenance details.

| Document | File | Pages |
|----------|------|-------|
| Syllabus v3.2.0 (English) | `cpre_foundationlevel_syllabus_EN_v3.2.0.txt` | 49 |
| Syllabus v3.0.1 (English) | `cpre_foundationlevel_syllabus_EN_v3.0.1.txt` | 49 |
| Practice Exam v3.3.1 (English) | `IREB_CPRE_FL_Practice_Exam_EN_v3.3.1.txt` | 26 |
