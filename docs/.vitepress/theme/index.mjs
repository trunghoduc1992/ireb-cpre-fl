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
  setup() {
    useMermaid()
  },
}
