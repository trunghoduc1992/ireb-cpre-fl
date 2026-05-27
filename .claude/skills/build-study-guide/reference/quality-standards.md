# Quality Standards

## WCAG AA Contrast

All text/background pairs in Mermaid diagrams must meet WCAG AA: minimum 4.5:1 contrast ratio for normal text, 3:1 for large text.

Verify with this Python function:
```python
def contrast(fg_hex, bg_hex):
    def luminance(hex_color):
        r, g, b = int(hex_color[1:3], 16)/255, int(hex_color[3:5], 16)/255, int(hex_color[5:7], 16)/255
        def lin(c): return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
        return 0.2126*lin(r) + 0.7152*lin(g) + 0.0722*lin(b)
    l1, l2 = luminance(fg_hex), luminance(bg_hex)
    lighter, darker = max(l1,l2), min(l1,l2)
    return (lighter+0.05) / (darker+0.05)
```

Do NOT use hardcoded inline `style` directives in Mermaid diagram source. Use the theme variables only — they adapt to dark/light mode automatically.

## Diagram Captions

Every diagram gets an instructional caption — one sentence in italics immediately below the code fence.

**Convention:** The caption tells the reader what to learn from the diagram, not just what it shows.

| Bad (descriptive only) | Good (instructional) |
|----------------------|---------------------|
| *System context diagram.* | *The three nested boundaries: the system boundary encloses the SuD, the context boundary encloses everything relevant.* |
| *UML class diagram.* | *The filled diamond on Order-to-OrderItem is composition: an OrderItem cannot exist without its Order.* |

## Glossary Source of Truth

```
glossary_terms_raw.json  ←  SOURCE OF TRUTH (committed)
        ↓
glossary.md              ←  GENERATED (committed with DO-NOT-EDIT header)
```

Rules:
- Never edit `glossary.md` directly — regenerate from JSON
- The JSON is produced by `parse_glossary.py` from extracted PDF text
- The markdown is produced by `build_glossary_md.py` from JSON
- Every generated file starts with: `<!-- DO NOT EDIT — generated from <json-path> -->`
- Glossary terms render as h4 markdown headings (for VitePress search indexing and anchor scrolling)
- HTML entities must be escaped in definitions (`<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`)

## Abbreviation Handling

Spell out every abbreviation on its first use, then use the short form thereafter.

**Example:** "Educational Unit (EU)" on first mention, then "EU" in subsequent text.

This applies to:
- Chapter content
- The implementation plan
- The validation report
- Exam questions and explanations

## Educational Objective Coverage

Every Educational Objective (EO) listed in the syllabus must be addressed in its corresponding chapter. The content must match the cognitive level:

| EO Level | Content Requirement |
|----------|-------------------|
| L1 (Know) | The concept is named, defined, or listed |
| L2 (Understand) | The concept is explained with reasoning or comparison |
| L3 (Apply) | A worked example or template is provided |

The audit script (`audit.py`) verifies coverage by checking for keywords associated with each EO. Run it after writing chapters and fix any gaps before finalizing.

## Exam Question Standards

- Question types, point values, and per-unit distribution must match the official practice exam exactly
- K-type questions are all-or-nothing (2 points, all 4 statements must be correct)
- P-type questions state how many answers to select
- Every question includes an explanation
- Every question is tagged with its unit/chapter for distribution tracking
- Practice exams use the `ExamQuiz` component with timer, scoring, and pass/fail
