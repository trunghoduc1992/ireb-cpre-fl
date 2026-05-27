---
name: build-study-guide
description: Generate a VitePress self-study guide from an official certification syllabus
argument-hint: <downloads-page-url> <version>
arguments: [downloads_url, version]
when_to_use: When producing self-study material for a certification exam from official syllabus and glossary PDFs
allowed-tools: WebFetch WebSearch Read Write Bash Edit Glob Grep
user-invocable: true
effort: high
---

# Build Self-Study Guide

Generate a complete VitePress self-study guide from an official certification syllabus.

**Input:**
- `$downloads_url` — URL of the certification body's downloads/resources page
- `$version` — target syllabus version (e.g., `v3.3.0`)

## Workflow

Execute these 8 phases in order. Each phase produces artifacts that subsequent phases depend on. Reference the files in `${CLAUDE_SKILL_DIR}/reference/` for detailed instructions and `${CLAUDE_SKILL_DIR}/scripts/` for automation.

### Phase 1: Validate and Inventory

1. Fetch `$downloads_url` and inventory ALL available resources (syllabus, glossary, practice exam, exam regulations, handbook, supplementary materials)
2. For each resource, record: title, version, language, file format, download URL
3. Download the syllabus, glossary, and practice exam PDFs
4. Extract text from each PDF using: `python ${CLAUDE_SKILL_DIR}/scripts/extract_pdf.py <pdf-path> <output-dir>`
5. Save all downloads and extracted text to `validations/<date>_<version>/downloads/`
6. Save a `downloads.json` manifest with provenance (URL, version, date, why downloaded)
7. Produce a validation report (`report.md` + `report.html`) comparing existing content against the official resources

**Output:** `validations/<date>_<version>/` directory with report, PDFs, extracted text, and manifest.

### Phase 2: Scaffold Site Structure

If this is a new project:
1. Initialize VitePress with `package.json`, `docs/.vitepress/config.mjs`, and theme components
2. Copy the theme components from `${CLAUDE_SKILL_DIR}/reference/vitepress-setup.md` (Quiz, ExamQuiz, ProgressTracker, Mermaid with WCAG AA themes)

If this is a version update (existing content exists):
1. Move previous version's content under `/vN/` (where N is the old version)
2. Latest version content goes at root `/`
3. Add version dropdown to nav bar
4. Update sidebar config with multi-sidebar (one per version)
5. Add deprecation banner to old version's index page

See `${CLAUDE_SKILL_DIR}/reference/vitepress-setup.md` for config templates.

### Phase 3: Write Chapters

1. Parse the extracted syllabus text to identify:
   - Chapter/unit structure (names, numbers, cognitive levels, durations)
   - Educational Objectives (EO numbers, descriptions, levels)
   - Key terms listed at the start of each chapter
2. For each chapter, create a markdown file with:
   - Official reference info box (syllabus version, unit number, download link)
   - Exam weight tip (percentage of exam points, from practice exam analysis)
   - Content covering every Educational Objective at its cognitive level
   - Mermaid diagrams where the content involves processes, structures, or states
   - Instructional captions on every diagram (one sentence: what to learn)
   - Practice quiz questions (mix of A-type, P-type, K-type matching exam weight)
3. Split large chapters into sub-pages if they exceed ~6 hours of syllabus duration

See `${CLAUDE_SKILL_DIR}/reference/workflow.md` for chapter writing guidelines.

### Phase 4: Write Practice Exams

1. Parse the official practice exam to determine:
   - Total questions, total points, passing score
   - Question type distribution (A-type, P-type, K-type) and points per type
   - Questions per chapter/unit and points per chapter/unit
2. Create an exam tips page with: format table, weight-by-unit table, question type descriptions, strategies
3. Create two practice exams matching the official distribution exactly
4. Tag each question with its chapter/unit in source code comments
5. Link to the official practice exam download

### Phase 5: Build Glossary

1. Extract glossary text: `python ${CLAUDE_SKILL_DIR}/scripts/extract_pdf.py <glossary-pdf> <output-dir>`
2. Parse into JSON: `python ${CLAUDE_SKILL_DIR}/scripts/parse_glossary.py <extracted-text> <output-json>`
3. Generate searchable markdown: `python ${CLAUDE_SKILL_DIR}/scripts/build_glossary_md.py <json> <output-md>`
4. The generated markdown uses h4 headings (for VitePress search indexing + anchor scrolling) with a Vue filter component for on-page search
5. Add DO-NOT-EDIT header with regeneration instructions
6. Add source attribution (glossary version, author, download link)

The JSON file is the source of truth. The markdown is generated and should not be edited directly.

### Phase 6: Build Supporting Pages

1. **Study plan** — weekly schedule based on syllabus durations, exam weight annotations, study tips
2. **Resources page** — all official documents with versions, descriptions, and download links
3. **Index page** — landing page with feature highlights, version badge, link to deprecated version

### Phase 7: Audit

Run: `python ${CLAUDE_SKILL_DIR}/scripts/audit.py <syllabus-text> <chapters-dir> <glossary-json>`

This verifies:
- Every Educational Objective is addressed in chapter content (keyword coverage)
- Every key term appears in both its chapter and the glossary
- Quiz question distribution matches exam weight table

Fix any gaps found, then re-run until 100% coverage with 0 issues.

### Phase 8: Final Polish

1. Add instructional captions to any diagrams that lack them
2. Verify all internal links resolve (no broken cross-references)
3. Build the site (`npm run build`) and confirm no errors
4. Commit all changes with descriptive messages per phase

## Quality Standards

See `${CLAUDE_SKILL_DIR}/reference/quality-standards.md` for:
- WCAG AA contrast requirements for diagrams
- Instructional caption conventions
- Glossary source-of-truth rules
- Abbreviation handling (spell out on first use)
- Educational Objective cognitive level matching
