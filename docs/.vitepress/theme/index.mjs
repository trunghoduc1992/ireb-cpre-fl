import DefaultTheme from 'vitepress/theme'
import Quiz from './Quiz.vue'
import ProgressTracker from './ProgressTracker.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('ProgressTracker', ProgressTracker)
  },
}
