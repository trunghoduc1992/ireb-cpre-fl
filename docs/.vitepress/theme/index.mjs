import DefaultTheme from 'vitepress/theme'
import Quiz from './Quiz.vue'
import ProgressTracker from './ProgressTracker.vue'
import MermaidChart from './MermaidChart.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('ProgressTracker', ProgressTracker)
    app.component('MermaidChart', MermaidChart)
  },
}
