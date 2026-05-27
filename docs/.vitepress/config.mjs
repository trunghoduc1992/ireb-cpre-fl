import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/ireb-cpre-fl/',
  title: 'IREB CPRE-FL Study Guide',
  description: 'Self-study guide for IREB Certified Professional for Requirements Engineering — Foundation Level',
  head: [
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0' }],
    ['link', { rel: 'icon', href: '/ireb-cpre-fl/favicon.svg', type: 'image/svg+xml' }],
  ],
  themeConfig: {
    logo: '/favicon.svg',
    nav: [
      {
        text: 'Version',
        items: [
          { text: 'v3.3.0 (Syllabus v3)', link: '/v3/' },
          { text: 'v2 (Legacy)', link: '/' },
        ],
      },
      { text: 'Home', link: '/v3/' },
      { text: 'Chapters', link: '/v3/chapters/01-introduction' },
      { text: 'Sample Exams', link: '/v3/exams/exam-1' },
      { text: 'Glossary', link: '/v3/glossary' },
      { text: 'Exam Tips', link: '/v3/exam-tips' },
      { text: 'Resources', link: '/v3/resources' },
    ],
    sidebar: {
      '/v3/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Study Plan', link: '/v3/study-plan' },
            { text: 'Exam Tips', link: '/v3/exam-tips' },
            { text: 'Official Resources', link: '/v3/resources' },
          ],
        },
        {
          text: 'Educational Units',
          items: [
            { text: 'EU 1. Introduction & Overview', link: '/v3/chapters/01-introduction' },
            { text: 'EU 2. Fundamental Principles', link: '/v3/chapters/02-principles' },
            {
              text: 'EU 3. Work Products & Documentation',
              collapsed: false,
              items: [
                { text: '3.1 Work Product Basics', link: '/v3/chapters/03a-work-product-basics' },
                { text: '3.2 Natural Language & Templates', link: '/v3/chapters/03b-natural-language' },
                { text: '3.4 Model-Based Work Products', link: '/v3/chapters/03c-models' },
              ],
            },
            {
              text: 'EU 4. Practices for Elaboration',
              collapsed: false,
              items: [
                { text: '4.1 Sources & Elicitation', link: '/v3/chapters/04a-sources-and-elicitation' },
                { text: '4.3 Conflicts & Validation', link: '/v3/chapters/04b-conflicts-and-validation' },
              ],
            },
            { text: 'EU 5. Process & Working Structure', link: '/v3/chapters/05-process' },
            { text: 'EU 6. Management Practices', link: '/v3/chapters/06-management' },
            { text: 'EU 7. Tool Support', link: '/v3/chapters/07-tools' },
          ],
        },
        {
          text: 'Sample Exams',
          items: [
            { text: 'Exam 1 (45 questions)', link: '/v3/exams/exam-1' },
            { text: 'Exam 2 (45 questions)', link: '/v3/exams/exam-2' },
          ],
        },
        {
          text: 'Reference',
          items: [
            { text: 'Glossary', link: '/v3/glossary' },
          ],
        },
      ],
      '/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Study Plan', link: '/study-plan' },
            { text: 'Exam Tips', link: '/exam-tips' },
          ],
        },
        {
          text: 'Chapters',
          items: [
            { text: '1. Introduction & Foundations', link: '/chapters/01-introduction' },
            { text: '2. System & System Context', link: '/chapters/02-system-context' },
            { text: '3. Requirements Elicitation', link: '/chapters/03-elicitation' },
            { text: '4. Documentation Basics', link: '/chapters/04-documentation' },
            { text: '5. Natural Language', link: '/chapters/05-natural-language' },
            { text: '6. Model-Based Documentation', link: '/chapters/06-models' },
            { text: '7. Validation & Negotiation', link: '/chapters/07-validation' },
            { text: '8. Requirements Management', link: '/chapters/08-management' },
            { text: '9. Tool Support', link: '/chapters/09-tools' },
          ],
        },
        {
          text: 'Sample Exams',
          items: [
            { text: 'Exam 1 (46 questions)', link: '/exams/exam-1' },
            { text: 'Exam 2 (46 questions)', link: '/exams/exam-2' },
          ],
        },
        {
          text: 'Reference',
          items: [
            { text: 'Glossary', link: '/glossary' },
          ],
        },
      ],
    },
    search: {
      provider: 'local',
    },
    outline: {
      level: [2, 3],
    },
    footer: {
      message: 'Study guide for IREB CPRE Foundation Level exam preparation.',
    },
  },
})
