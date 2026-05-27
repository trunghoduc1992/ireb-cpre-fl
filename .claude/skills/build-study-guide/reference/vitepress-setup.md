# VitePress Setup Reference

## Required Dependencies

```json
{
  "devDependencies": {
    "mermaid": "^11.15.0",
    "vitepress": "^1.6.4",
    "vue": "^3.5.34"
  }
}
```

## Config Template (multi-sidebar versioning)

```js
import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/<repo-name>/',
  title: '<Certification> Study Guide',
  description: 'Self-study guide for <certification full name>',
  head: [
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0' }],
  ],
  themeConfig: {
    nav: [
      {
        text: 'Version',
        items: [
          { text: 'vX.X (Latest)', link: '/' },
          { text: 'vY.Y (Deprecated)', link: '/vY/' },
        ],
      },
      { text: 'Home', link: '/' },
      { text: 'Chapters', link: '/chapters/<first-chapter>' },
      { text: 'Sample Exams', link: '/exams/exam-1' },
      { text: 'Glossary', link: '/glossary' },
      { text: 'Exam Tips', link: '/exam-tips' },
      { text: 'Resources', link: '/resources' },
    ],
    sidebar: {
      '/vY/': [
        // Old version sidebar (frozen)
      ],
      '/': [
        // Latest version sidebar
      ],
    },
    search: { provider: 'local' },
    outline: { level: [2, 3] },
  },
})
```

## Theme Components

### Required files in `docs/.vitepress/theme/`

| File | Purpose |
|------|---------|
| `index.mjs` | Theme entry — registers Quiz, ExamQuiz, ProgressTracker, Mermaid |
| `Quiz.vue` | Chapter quiz component (A-type questions) |
| `ExamQuiz.vue` | Full exam component (A/P/K-type, timer, scoring) |
| `ProgressTracker.vue` | Checkbox progress tracker (version-aware via URL path) |
| `useMermaid.mjs` | Mermaid renderer with dark/light theme and WCAG AA colors |
| `MermaidChart.vue` | Mermaid chart helper for ExamQuiz |
| `custom.css` | Custom styles (key-concept, example-box, exam-tip) |

### Theme entry (`index.mjs`)

```js
import DefaultTheme from 'vitepress/theme'
import Quiz from './Quiz.vue'
import ExamQuiz from './ExamQuiz.vue'
import ProgressTracker from './ProgressTracker.vue'
import { useMermaid } from './useMermaid.mjs'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('ExamQuiz', ExamQuiz)
    app.component('ProgressTracker', ProgressTracker)
  },
  setup() { useMermaid() },
}
```

### Mermaid theme variables (WCAG AA verified)

Dark mode (all pairs >= 6.7:1 contrast ratio):
```js
{
  fontFamily: '"Inter", sans-serif',
  background: '#1e1e1e',
  primaryColor: '#2d4a7a', primaryTextColor: '#e0e0e0', primaryBorderColor: '#5b9bd5',
  secondaryColor: '#3b3b5c', secondaryTextColor: '#e0e0e0', secondaryBorderColor: '#7b7baf',
  tertiaryColor: '#2a3a2a', tertiaryTextColor: '#e0e0e0', tertiaryBorderColor: '#6aaf6a',
  lineColor: '#8ab4f8', textColor: '#e0e0e0',
  mainBkg: '#2d4a7a', nodeBorder: '#5b9bd5',
  clusterBkg: '#1a2744', clusterBorder: '#5b9bd5',
  titleColor: '#e0e0e0', edgeLabelBackground: '#1e1e1e', nodeTextColor: '#e0e0e0',
}
```

Light mode (all pairs >= 11.0:1 contrast ratio):
```js
{
  fontFamily: '"Inter", sans-serif',
  background: '#ffffff',
  primaryColor: '#d4e6f1', primaryTextColor: '#1a1a1a', primaryBorderColor: '#2980b9',
  secondaryColor: '#d5f5e3', secondaryTextColor: '#1a1a1a', secondaryBorderColor: '#27ae60',
  tertiaryColor: '#fef9e7', tertiaryTextColor: '#1a1a1a', tertiaryBorderColor: '#f39c12',
  lineColor: '#2c3e50', textColor: '#1a1a1a',
  mainBkg: '#d4e6f1', nodeBorder: '#2980b9',
  clusterBkg: '#eaf2f8', clusterBorder: '#2980b9',
  titleColor: '#1a1a1a', edgeLabelBackground: '#ffffff', nodeTextColor: '#1a1a1a',
}
```

### Mermaid dark/light toggle pattern

Store mermaid source code in `data-mermaid-source` on the container element when first rendering. On theme toggle, re-initialize mermaid with the new theme and re-render from stored source. Do NOT search for the original code blocks — they have been replaced.

### Custom CSS patterns

```css
.vp-doc .key-concept {
  border-left: 4px solid var(--vp-c-brand-1);
  padding: 0.75rem 1rem;
  margin: 1rem 0;
  background: var(--vp-c-brand-soft);
  border-radius: 0 8px 8px 0;
}

.vp-doc .example-box {
  border: 1px solid var(--vp-c-green-1);
  padding: 0.75rem 1rem;
  margin: 1rem 0;
  border-radius: 8px;
  background: var(--vp-c-green-soft);
}

.vp-doc .exam-tip {
  border: 1px solid var(--vp-c-yellow-1);
  padding: 0.75rem 1rem;
  margin: 1rem 0;
  border-radius: 8px;
  background: var(--vp-c-yellow-soft);
}
```

### ProgressTracker version awareness

The ProgressTracker detects the URL path to determine which version's chapters to show. It uses separate localStorage keys per version (e.g., `progress-v2`, `progress-v3`) so progress does not mix.
