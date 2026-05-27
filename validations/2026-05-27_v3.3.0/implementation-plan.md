# Implementation Plan: Update to IREB CPRE-FL Syllabus v3.3.0

**Based on:** [Validation Report](report.md) (2026-05-27)
**Goal:** Align the study guide with the official IREB CPRE-FL Syllabus v3.3.0

---

## Phase 0: Versioning Infrastructure

### 0.1 Set up version dropdown + URL prefixes
- Install or build a VitePress versioning mechanism (navbar dropdown with `/v2/` and `/v3/` URL prefixes)
- Snapshot current content as the `v2` version at `/v2/` URL path
- Create the `v3` version at root `/` (default) for new content
- Update `docs/.vitepress/config.js` with version selector in the nav bar

### 0.2 Add syllabus version declaration
- Add a prominent banner/badge to the index page and each chapter page declaring the target syllabus version
- Format: "Aligned with IREB CPRE-FL Syllabus v3.3.0 (April 2026)"

**Files to modify:** `docs/.vitepress/config.js`, `docs/index.md`, all chapter files

---

## Phase 1: Structural Alignment (Critical)

### 1.1 Create EU 2 — Fundamental Principles of Requirements Engineering
- **New file:** `docs/chapters/02-principles.md`
- **Content:** The nine fundamental principles with explanations:
  1. Value orientation
  2. Stakeholders
  3. Shared understanding
  4. Context and problem
  5. Requirement and solution
  6. Validation
  7. Evolution (continuous change)
  8. Innovation
  9. Systematic and disciplined work
- **Source:** Syllabus v3.2.0 pages 14-18 (extracted text available in `downloads/cpre_foundationlevel_syllabus_EN_v3.2.0.txt`)
- **Include:** 5 quiz questions (mix of A/P/K types) matching exam weight (~8.6%)

### 1.2 Create EU 5 — Process and Working Structure
- **New file:** `docs/chapters/05-process.md` (will need renumbering — see 1.3)
- **Content:**
  - 5.1 Influencing factors on RE processes
  - 5.2 RE process facets (plan-driven vs agile, linear vs iterative)
  - 5.3 Configuring an RE process (tailoring)
- **Source:** Syllabus v3.2.0 pages 36-40
- **Include:** 3-4 quiz questions

### 1.3 Restructure chapter numbering to match v3 EUs
- Renumber/rename all chapter files from the v2-era 9-chapter layout to the v3 7-EU layout:

| New File | EU | Content (source from current chapters) |
|----------|-----|---------------------------------------|
| `01-introduction.md` | EU 1 | Current Ch 1 + system context from Ch 2 |
| `02-principles.md` | EU 2 | **NEW** |
| `03-work-products.md` | EU 3 | Current Ch 4 + Ch 5 + Ch 6 (merged or linked) |
| `04-practices.md` | EU 4 | Current Ch 2 (partial: stakeholders, context analysis) + Ch 3 + Ch 7 |
| `05-process.md` | EU 5 | **NEW** |
| `06-management.md` | EU 6 | Current Ch 8 |
| `07-tools.md` | EU 7 | Current Ch 9 |

- **Alternative:** Keep sub-pages within each EU (e.g., EU 3 has sub-pages for natural language, models, etc.) to avoid extremely long single pages
- Update sidebar navigation in VitePress config
- Update all internal links and study plan

**Files to modify:** All `docs/chapters/*.md`, `docs/.vitepress/config.js`, `docs/study-plan.md`, `docs/exam-tips.md`

---

## Phase 2: Exam Format & Practice Exams

### 2.1 Fix exam-tips.md
- Change "~46 questions" to "45 questions"
- Add note about +15 minutes for non-native speakers
- Update weight table to use the 7-EU structure with accurate percentages:
  - EU 1: ~5.7%, EU 2: ~8.6%, EU 3: ~42.9%, EU 4: ~20%, EU 5: ~4.3%, EU 6: ~14.3%, EU 7: ~4.3%
- Add reference link to official exam regulations v5.6.2

### 2.2 Update practice exams
- Add questions for EU 2 (Principles) — approximately 4 questions (6 points) per exam
- Add questions for EU 5 (Process) — approximately 2 questions (3 points) per exam
- Adjust total to 45 questions, keeping 70 total points
- Remove 6 existing questions to maintain the count (reduce from over-represented EUs)
- Map each question to its EU in the question comments

### 2.3 Add link to official practice exam
- Add a prominent link to the official IREB practice exam on the exam-tips page
- Note that it's free and available in 12 languages

**Files to modify:** `docs/exam-tips.md`, `docs/exams/exam-1.md`, `docs/exams/exam-2.md`

---

## Phase 3: Glossary

### 3.1 Download and extract official IREB Glossary v2.2.0
- Download from IREB Download Center
- Extract text using PyMuPDF (same method as syllabus)
- Parse into structured term-definition pairs

### 3.2 Replace glossary with verbatim IREB definitions
- Replace all ~70 paraphrased definitions with official IREB Glossary v2.2.0 text
- Add any missing terms that are designated as "foundational"
- Preserve the Vue component search/filter functionality

### 3.3 Add glossary version reference
- Add header: "Based on IREB CPRE Glossary v2.2.0"
- Add link to official glossary download page

**Files to modify:** `docs/glossary.md`

---

## Phase 4: Official Resource Links

### 4.1 Add IREB resource links to every chapter page
- Add a standardized footer/info box to each chapter:
  ```
  Official Reference: IREB CPRE-FL Syllabus v3.3.0, EU X
  Download: https://cpre.ireb.org/en/downloads-and-resources/downloads
  ```

### 4.2 Add a dedicated resources page
- **New file:** `docs/resources.md`
- List all official resources with versions and download links:
  - Syllabus v3.3.0
  - Handbook v1.3.1
  - Glossary v2.2.0
  - Practice Exam (latest)
  - Exam Regulations v5.6.2
  - Nine Principles v1.0.0
  - RE Poster v1.0.0
- Add to sidebar navigation

### 4.3 Update study plan
- Reference official resources in the study plan
- Recommend downloading syllabus and handbook alongside the guide
- Update week structure to match 7-EU layout

**Files to modify:** All `docs/chapters/*.md`, `docs/study-plan.md`, `docs/index.md`, `docs/.vitepress/config.js`

---

## Phase 5: Content Review

### 5.1 Cross-reference each EU against syllabus learning objectives
- For each EU, verify that all educational objectives (EOs) listed in the syllabus are covered
- Add coverage of any missing EOs
- Ensure cognitive levels match (L1=know, L2=understand, L3=apply)

### 5.2 Verify terms per chapter
- The syllabus lists key terms at the beginning of each EU
- Ensure all listed terms appear in the chapter content and glossary

### 5.3 Review quiz questions against learning objectives
- Each quiz question should map to a specific EO
- Ensure cognitive level of questions matches EO levels

---

## Execution Order & Dependencies

```
Phase 0 (Versioning) ──► Phase 1 (Structure) ──► Phase 2 (Exams)
                                                       │
                                                       ▼
                          Phase 3 (Glossary) ──► Phase 4 (Links)
                                                       │
                                                       ▼
                                                Phase 5 (Review)
```

- **Phase 0** must complete first (snapshots current content before changes)
- **Phases 1-4** can partially overlap but Phase 1 should be mostly done before Phase 2
- **Phase 5** is a final review pass after all content changes

## Estimated Effort

| Phase | Effort | Notes |
|-------|--------|-------|
| Phase 0 | 2-3 hours | VitePress config + snapshot |
| Phase 1 | 6-8 hours | Two new chapters + restructuring |
| Phase 2 | 3-4 hours | Exam updates + new questions |
| Phase 3 | 2-3 hours | Depends on glossary PDF extraction |
| Phase 4 | 1-2 hours | Links + resources page |
| Phase 5 | 3-4 hours | Cross-reference review |
| **Total** | **17-24 hours** | |
