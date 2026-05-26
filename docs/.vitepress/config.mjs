import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(
  defineConfig({
    base: '/ireb-cpre-fl/',
    title: 'IREB CPRE-FL Study Guide',
    description: 'Self-study guide for IREB Certified Professional for Requirements Engineering — Foundation Level',
    head: [
      ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0' }],
      ['link', { rel: 'icon', href: '/favicon.svg', type: 'image/svg+xml' }],
    ],
    themeConfig: {
      logo: '/favicon.svg',
      nav: [
        { text: 'Home', link: '/' },
        { text: 'Chapters', link: '/chapters/01-introduction' },
        { text: 'Glossary', link: '/glossary' },
        { text: 'Exam Tips', link: '/exam-tips' },
        { text: 'Study Plan', link: '/study-plan' },
      ],
      sidebar: [
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
          text: 'Reference',
          items: [
            { text: 'Glossary', link: '/glossary' },
          ],
        },
      ],
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
    mermaid: {
      theme: 'default',
    },
  })
)
