# Workflow Reference

Detailed instructions for each phase of the study guide generation workflow.

## Chapter Writing Guidelines

### Structure per chapter file

```markdown
<script setup>
import Quiz from '../.vitepress/theme/Quiz.vue'

const questions = [
  // A-type: { text, options: [4], answer: number, explanation, chapter }
  // P-type: { text, options: [5], answer: [n, n], multi: true, points: 1|2, explanation, chapter }
  // K-type: { text, type: 'ktype', statements: [{text, answer: bool}x4], points: 2, explanation, chapter }
]
</script>

# Unit Title

::: info Official Reference
**Syllabus vX.X** — Unit N (Level, Duration)
[Download syllabus](URL)
:::

<div class="exam-tip">
  <strong>Exam weight:</strong> ~X% of points (N questions, N points).
</div>

## Section Content

(Cover every Educational Objective at its cognitive level)

## Practice Quiz

<Quiz :questions="questions" />
```

### Cognitive level content mapping

| Level | Verb | Content should... |
|-------|------|-------------------|
| L1 (Know) | Define, list, name, enumerate | State facts, list items, provide definitions |
| L2 (Understand) | Explain, compare, justify, interpret | Explain why, compare alternatives, give reasoning |
| L3 (Apply) | Specify, write, design, develop | Show worked examples, provide templates the reader can use |

### Quiz question distribution

Calculate target questions per unit from the official practice exam:
1. Count questions per unit in the practice exam
2. Count points per unit
3. Calculate weight percentage: `unit_points / total_points * 100`
4. Match this distribution in chapter quizzes and practice exams

### Exam question component API

**A-type (single-select, 1 point):**
```js
{
  text: 'Question text',
  options: ['A', 'B', 'C', 'D'],
  answer: 1,          // 0-indexed correct option
  points: 1,
  explanation: 'Why this is correct',
  chapter: 'EU 1',    // Tag for distribution tracking
}
```

**P-type (pick-two, 1-2 points):**
```js
{
  text: 'Question text (Select two)',
  options: ['A', 'B', 'C', 'D', 'E'],
  answer: [1, 3],     // 0-indexed correct options
  multi: true,
  points: 2,
  explanation: 'Why these are correct',
  chapter: 'EU 1',
}
```

**K-type (true/false matrix, 2 points, all-or-nothing):**
```js
{
  text: 'Which statements are true/false?',
  type: 'ktype',
  statements: [
    { text: 'Statement A', answer: true },
    { text: 'Statement B', answer: false },
    { text: 'Statement C', answer: true },
    { text: 'Statement D', answer: true },
  ],
  points: 2,
  explanation: 'Explanation for all four',
  chapter: 'EU 1',
}
```

## Versioning Convention

- Latest version content lives at root `/`
- Previous versions live at `/vN/` (e.g., `/v2/`)
- When a new version is created:
  1. Move current root content to `/vN/` (freeze it)
  2. Put new content at root
  3. Update config sidebar paths
  4. Add deprecation banner to old version index
  5. Add `/vN+1/` redirect page pointing to root

## Glossary Pipeline

```
Official PDF → extract_pdf.py → .txt file
                                    ↓
                          parse_glossary.py → glossary_terms_raw.json (SOURCE OF TRUTH)
                                                        ↓
                                            build_glossary_md.py → glossary.md (GENERATED)
```

The JSON file is committed to the repo. The markdown is regenerated from it. The markdown file has a DO-NOT-EDIT comment header with regeneration instructions.

## Validation Directory Structure

```
validations/
  <date>_<version>/
    report.md              # Findings in markdown
    report.html            # Findings in standalone HTML
    downloads.json         # Provenance manifest
    phase5-audit.md        # EO coverage audit results
    downloads/
      <syllabus>.pdf       # Downloaded PDF
      <syllabus>.txt       # Extracted text
      <glossary>.pdf
      <glossary>.txt
      <practice-exam>.pdf
      <practice-exam>.txt
      glossary_terms_raw.json
      *.py                 # Processing scripts used
```
