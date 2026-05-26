<script setup>
import { ref, computed, onUnmounted } from 'vue'
import MermaidChart from './MermaidChart.vue'

const props = defineProps({
  questions: { type: Array, required: true },
  timeLimit: { type: Number, default: 75 * 60 },
  passingScore: { type: Number, default: 0.7 },
})

const answers = ref({})
const submitted = ref(false)
const timeRemaining = ref(props.timeLimit)
const timerActive = ref(false)
const started = ref(false)
let interval = null

const totalPoints = computed(() =>
  props.questions.reduce((sum, q) => sum + (q.points || 1), 0)
)

const passingPoints = computed(() =>
  Math.ceil(totalPoints.value * props.passingScore)
)

function start() {
  started.value = true
  timerActive.value = true
  interval = setInterval(() => {
    if (timeRemaining.value > 0) timeRemaining.value--
    else submit()
  }, 1000)
}

function toggleTimer() {
  if (timerActive.value) {
    clearInterval(interval)
    timerActive.value = false
  } else {
    timerActive.value = true
    interval = setInterval(() => {
      if (timeRemaining.value > 0) timeRemaining.value--
      else submit()
    }, 1000)
  }
}

onUnmounted(() => { if (interval) clearInterval(interval) })

// ── A-type / P-type selection ──
function select(qi, oi) {
  if (submitted.value) return
  const q = props.questions[qi]
  if (q.multi) {
    const current = answers.value[qi] || []
    const idx = current.indexOf(oi)
    if (idx >= 0) {
      answers.value = { ...answers.value, [qi]: current.filter(i => i !== oi) }
    } else {
      answers.value = { ...answers.value, [qi]: [...current, oi] }
    }
  } else {
    answers.value = { ...answers.value, [qi]: oi }
  }
}

// ── K-type selection ──
function selectKtype(qi, si, value) {
  if (submitted.value) return
  const current = answers.value[qi] || {}
  answers.value = { ...answers.value, [qi]: { ...current, [si]: value } }
}

function isSelected(qi, oi) {
  const q = props.questions[qi]
  if (q.multi) return (answers.value[qi] || []).includes(oi)
  return answers.value[qi] === oi
}

function isCorrectOption(qi, oi) {
  const q = props.questions[qi]
  if (q.multi) return q.answer.includes(oi)
  return oi === q.answer
}

function isWrongSelection(qi, oi) {
  return isSelected(qi, oi) && !isCorrectOption(qi, oi)
}

function isKtypeSelected(qi, si, value) {
  const a = answers.value[qi]
  return a && a[si] === value
}

function isQuestionCorrect(qi) {
  const q = props.questions[qi]
  if (q.type === 'ktype') {
    const a = answers.value[qi] || {}
    return q.statements.every((s, si) => a[si] === s.answer)
  }
  if (q.multi) {
    const sel = answers.value[qi] || []
    return sel.length === q.answer.length && sel.every(s => q.answer.includes(s))
  }
  return answers.value[qi] === q.answer
}

// ── Scoring ──
const score = computed(() => {
  let pts = 0
  props.questions.forEach((q, i) => {
    if (isQuestionCorrect(i)) pts += (q.points || 1)
  })
  return pts
})

const passed = computed(() => score.value >= passingPoints.value)

const answeredCount = computed(() => {
  let count = 0
  props.questions.forEach((q, i) => {
    if (q.type === 'ktype') {
      const a = answers.value[i] || {}
      if (Object.keys(a).length === q.statements.length) count++
    } else if (q.multi) {
      if ((answers.value[i] || []).length > 0) count++
    } else {
      if (answers.value[i] !== undefined) count++
    }
  })
  return count
})

function formatTime(sec) {
  const m = Math.floor(sec / 60)
  const s = sec % 60
  return `${m}:${s.toString().padStart(2, '0')}`
}

function submit() {
  if (interval) clearInterval(interval)
  timerActive.value = false
  submitted.value = true
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function reset() {
  answers.value = {}
  submitted.value = false
  started.value = false
  timeRemaining.value = props.timeLimit
  timerActive.value = false
}

function scrollToQuestion(qi) {
  const el = document.getElementById(`exam-q-${qi}`)
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
}
</script>

<template>
  <!-- Start screen -->
  <div v-if="!started" class="exam-start">
    <div class="exam-start-card">
      <h2>Sample Exam</h2>
      <div class="exam-info-grid">
        <div class="info-item">
          <span class="info-label">Questions</span>
          <span class="info-value">{{ questions.length }}</span>
        </div>
        <div class="info-item">
          <span class="info-label">Time Limit</span>
          <span class="info-value">{{ Math.floor(timeLimit / 60) }} min</span>
        </div>
        <div class="info-item">
          <span class="info-label">Total Points</span>
          <span class="info-value">{{ totalPoints }}</span>
        </div>
        <div class="info-item">
          <span class="info-label">Passing Score</span>
          <span class="info-value">{{ Math.round(passingScore * 100) }}% ({{ passingPoints }}/{{ totalPoints }} pts)</span>
        </div>
      </div>
      <p class="exam-start-note">Three question types — just like the real exam. Single-select (1 pt), pick-two (1–2 pts), and True/False matrix (2 pts). The timer starts when you click the button below.</p>
      <button class="exam-btn exam-btn-primary exam-btn-lg" @click="start">Start Exam</button>
    </div>
  </div>

  <!-- Exam in progress -->
  <div v-else class="exam-container">
    <!-- Sticky header -->
    <div class="exam-header">
      <div class="exam-header-left">
        <span class="exam-progress">{{ answeredCount }}/{{ questions.length }} answered</span>
      </div>
      <div v-if="!submitted" class="exam-header-center">
        <span class="exam-timer" :class="{ 'timer-danger': timeRemaining < 300 }">
          {{ formatTime(timeRemaining) }}
        </span>
        <button class="exam-btn-sm" @click="toggleTimer">
          {{ timerActive ? 'Pause' : 'Resume' }}
        </button>
      </div>
      <div v-if="submitted" class="exam-header-center">
        <span class="exam-result-badge" :class="passed ? 'badge-pass' : 'badge-fail'">
          {{ passed ? 'PASSED' : 'FAILED' }} — {{ score }}/{{ totalPoints }} pts ({{ Math.round(score / totalPoints * 100) }}%)
        </span>
      </div>
      <div class="exam-header-right">
        <button v-if="!submitted" class="exam-btn exam-btn-primary" :disabled="answeredCount === 0" @click="submit">
          Submit Exam
        </button>
        <button v-else class="exam-btn exam-btn-outline" @click="reset">Retake Exam</button>
      </div>
    </div>

    <!-- Question navigation grid -->
    <div v-if="submitted" class="exam-nav-grid">
      <button
        v-for="(q, qi) in questions"
        :key="qi"
        class="nav-dot"
        :class="{
          'nav-correct': isQuestionCorrect(qi),
          'nav-wrong': !isQuestionCorrect(qi),
        }"
        @click="scrollToQuestion(qi)"
      >
        {{ qi + 1 }}
      </button>
    </div>

    <!-- Questions -->
    <div v-for="(q, qi) in questions" :key="qi" :id="`exam-q-${qi}`" class="exam-question">
      <div class="question-header">
        <span class="question-number">Question {{ qi + 1 }}</span>
        <span class="points-badge">{{ q.points || 1 }} {{ (q.points || 1) === 1 ? 'pt' : 'pts' }}</span>
        <span v-if="q.type === 'ktype'" class="multi-badge">True / False</span>
        <span v-else-if="q.multi" class="multi-badge">Select {{ q.answer.length }}</span>
        <span v-else class="multi-badge type-a">1 answer</span>
        <span v-if="q.chapter" class="chapter-badge">{{ q.chapter }}</span>
      </div>
      <p class="question-text">{{ q.text }}</p>

      <!-- Diagram (optional) -->
      <div v-if="q.diagram" class="question-diagram">
        <MermaidChart :code="q.diagram" />
      </div>

      <!-- K-type: True/False matrix -->
      <div v-if="q.type === 'ktype'" class="ktype-container">
        <div class="ktype-header-row">
          <span class="ktype-statement-col"></span>
          <span class="ktype-toggle-col">True</span>
          <span class="ktype-toggle-col">False</span>
        </div>
        <div
          v-for="(stmt, si) in q.statements"
          :key="si"
          class="ktype-row"
          :class="{
            'ktype-correct': submitted && (answers[qi] || {})[si] === stmt.answer,
            'ktype-wrong': submitted && (answers[qi] || {})[si] !== undefined && (answers[qi] || {})[si] !== stmt.answer,
            'ktype-missed': submitted && (answers[qi] || {})[si] === undefined,
          }"
        >
          <span class="ktype-statement-col">{{ String.fromCharCode(65 + si) }}) {{ stmt.text }}</span>
          <span class="ktype-toggle-col">
            <button
              class="ktype-btn"
              :class="{ active: isKtypeSelected(qi, si, true), 'btn-correct': submitted && stmt.answer === true, 'btn-wrong': submitted && isKtypeSelected(qi, si, true) && stmt.answer !== true }"
              @click="selectKtype(qi, si, true)"
            ></button>
          </span>
          <span class="ktype-toggle-col">
            <button
              class="ktype-btn"
              :class="{ active: isKtypeSelected(qi, si, false), 'btn-correct': submitted && stmt.answer === false, 'btn-wrong': submitted && isKtypeSelected(qi, si, false) && stmt.answer !== false }"
              @click="selectKtype(qi, si, false)"
            ></button>
          </span>
        </div>
      </div>

      <!-- A-type / P-type: Option list -->
      <template v-else>
        <div
          v-for="(opt, oi) in q.options"
          :key="oi"
          class="exam-option"
          :class="{
            selected: isSelected(qi, oi) && !submitted,
            correct: submitted && isCorrectOption(qi, oi),
            wrong: submitted && isWrongSelection(qi, oi),
            missed: submitted && isCorrectOption(qi, oi) && !isSelected(qi, oi),
          }"
          @click="select(qi, oi)"
        >
          <span class="option-marker">
            <span v-if="!q.multi" class="radio-marker" :class="{ filled: isSelected(qi, oi) }"></span>
            <span v-else class="check-marker" :class="{ filled: isSelected(qi, oi) }"></span>
          </span>
          <span class="option-letter">{{ String.fromCharCode(65 + oi) }}.</span>
          <span>{{ opt }}</span>
        </div>
      </template>

      <div v-if="submitted" class="explanation" :class="isQuestionCorrect(qi) ? 'explanation-correct' : 'explanation-wrong'">
        <strong>{{ isQuestionCorrect(qi) ? 'Correct!' : 'Incorrect.' }}</strong>
        {{ q.explanation }}
      </div>
    </div>

    <!-- Bottom actions -->
    <div class="exam-footer">
      <button v-if="!submitted" class="exam-btn exam-btn-primary exam-btn-lg" :disabled="answeredCount === 0" @click="submit">
        Submit Exam
      </button>
      <div v-else class="exam-final-result">
        <div class="result-card" :class="passed ? 'result-pass' : 'result-fail'">
          <h3>{{ passed ? 'Congratulations! You passed.' : 'Not quite. Keep studying!' }}</h3>
          <p>Score: <strong>{{ score }}/{{ totalPoints }} points</strong> ({{ Math.round(score / totalPoints * 100) }}%)</p>
          <p>Passing score: {{ passingPoints }}/{{ totalPoints }} points ({{ Math.round(passingScore * 100) }}%)</p>
        </div>
        <button class="exam-btn exam-btn-primary exam-btn-lg" @click="reset">Retake Exam</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.exam-start {
  display: flex;
  justify-content: center;
  padding: 2rem 0;
}
.exam-start-card {
  max-width: 520px;
  padding: 2rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  background: var(--vp-c-bg-soft);
  text-align: center;
}
.exam-start-card h2 {
  margin-top: 0;
}
.exam-info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1.5rem 0;
  text-align: left;
}
.info-item {
  padding: 0.75rem;
  border-radius: 8px;
  background: var(--vp-c-bg);
}
.info-label {
  display: block;
  font-size: 0.8em;
  color: var(--vp-c-text-3);
  margin-bottom: 0.25rem;
}
.info-value {
  font-weight: 600;
  font-size: 0.95em;
}
.exam-start-note {
  font-size: 0.85em;
  color: var(--vp-c-text-2);
  margin-bottom: 1.5rem;
}

.exam-container {
  margin: 0.5rem 0;
}
.exam-header {
  position: sticky;
  top: var(--vp-nav-height, 64px);
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  margin: 0 -0.5rem 1.5rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg);
  backdrop-filter: blur(8px);
  flex-wrap: wrap;
}
.exam-progress {
  font-size: 0.9em;
  color: var(--vp-c-text-2);
}
.exam-timer {
  font-size: 1.4em;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: var(--vp-c-text-1);
}
.timer-danger {
  color: var(--vp-c-red-1);
}
.exam-header-center {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.exam-result-badge {
  font-weight: 700;
  font-size: 0.95em;
  padding: 0.3rem 0.8rem;
  border-radius: 8px;
}
.badge-pass {
  background: var(--vp-c-green-soft);
  color: var(--vp-c-green-1);
}
.badge-fail {
  background: var(--vp-c-red-soft);
  color: var(--vp-c-red-1);
}

.exam-nav-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-bottom: 1.5rem;
  padding: 1rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
}
.nav-dot {
  width: 2rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  font-size: 0.75em;
  font-weight: 600;
  cursor: pointer;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-2);
  transition: all 0.15s;
}
.nav-dot:hover {
  border-color: var(--vp-c-brand-1);
}
.nav-correct {
  background: var(--vp-c-green-soft);
  border-color: var(--vp-c-green-1);
  color: var(--vp-c-green-1);
}
.nav-wrong {
  background: var(--vp-c-red-soft);
  border-color: var(--vp-c-red-1);
  color: var(--vp-c-red-1);
}

.exam-question {
  margin-bottom: 2rem;
  padding: 1.25rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
}
.question-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
  flex-wrap: wrap;
}
.question-number {
  font-weight: 700;
  font-size: 0.85em;
  color: var(--vp-c-brand-1);
}
.points-badge {
  font-size: 0.7em;
  font-weight: 600;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  background: var(--vp-c-default-soft);
  color: var(--vp-c-text-2);
}
.multi-badge {
  font-size: 0.75em;
  font-weight: 600;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}
.type-a {
  background: var(--vp-c-default-soft);
  color: var(--vp-c-text-3);
}
.chapter-badge {
  font-size: 0.7em;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  background: var(--vp-c-default-soft);
  color: var(--vp-c-text-3);
  margin-left: auto;
}
.question-text {
  margin-bottom: 0.75rem;
  font-size: 0.95em;
  line-height: 1.6;
}
.question-diagram {
  margin: 0.5rem 0 1rem;
  padding: 0.5rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg);
}

/* ── K-type True/False matrix ── */
.ktype-container {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  overflow: hidden;
}
.ktype-header-row {
  display: flex;
  align-items: center;
  background: var(--vp-c-bg-mute);
  font-size: 0.8em;
  font-weight: 700;
  color: var(--vp-c-text-2);
  padding: 0.4rem 0;
}
.ktype-statement-col {
  flex: 1;
  padding: 0 0.75rem;
  font-size: 0.9em;
  line-height: 1.5;
}
.ktype-toggle-col {
  width: 60px;
  text-align: center;
  flex-shrink: 0;
}
.ktype-row {
  display: flex;
  align-items: center;
  padding: 0.5rem 0;
  border-top: 1px solid var(--vp-c-divider);
  transition: background 0.15s;
}
.ktype-row:hover:not(.ktype-correct):not(.ktype-wrong) {
  background: var(--vp-c-bg-mute);
}
.ktype-row.ktype-correct {
  background: var(--vp-c-green-soft);
}
.ktype-row.ktype-wrong, .ktype-row.ktype-missed {
  background: var(--vp-c-red-soft);
}
.ktype-btn {
  width: 28px;
  height: 28px;
  border: 2px solid var(--vp-c-divider);
  border-radius: 50%;
  background: var(--vp-c-bg);
  cursor: pointer;
  transition: all 0.15s;
}
.ktype-btn:hover {
  border-color: var(--vp-c-brand-1);
}
.ktype-btn.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-1);
  box-shadow: inset 0 0 0 4px var(--vp-c-bg);
}
.ktype-btn.btn-correct {
  border-color: var(--vp-c-green-1);
  background: var(--vp-c-green-1);
  box-shadow: inset 0 0 0 4px var(--vp-c-bg);
}
.ktype-btn.btn-wrong {
  border-color: var(--vp-c-red-1);
  background: var(--vp-c-red-1);
  box-shadow: inset 0 0 0 4px var(--vp-c-bg);
}

/* ── A-type / P-type options ── */
.exam-option {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  padding: 0.6rem 0.8rem;
  margin: 0.35rem 0;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.15s;
  font-size: 0.93em;
}
.exam-option:hover:not(.correct):not(.wrong):not(.missed) {
  background: var(--vp-c-bg-mute);
}
.exam-option.selected {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.exam-option.correct {
  border-color: var(--vp-c-green-1);
  background: var(--vp-c-green-soft);
}
.exam-option.wrong {
  border-color: var(--vp-c-red-1);
  background: var(--vp-c-red-soft);
}
.exam-option.missed {
  border-color: var(--vp-c-green-1);
  background: var(--vp-c-green-soft);
  opacity: 0.7;
}
.option-marker {
  margin-top: 2px;
}
.radio-marker, .check-marker {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid var(--vp-c-text-3);
  transition: all 0.15s;
}
.radio-marker {
  border-radius: 50%;
}
.check-marker {
  border-radius: 3px;
}
.radio-marker.filled {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-1);
  box-shadow: inset 0 0 0 3px var(--vp-c-bg);
}
.check-marker.filled {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-1);
}
.option-letter {
  font-weight: 600;
  min-width: 1.5em;
  color: var(--vp-c-text-2);
}

.explanation {
  margin-top: 0.75rem;
  padding: 0.6rem 0.8rem;
  border-radius: 6px;
  font-size: 0.88em;
  line-height: 1.5;
  color: var(--vp-c-text-2);
}
.explanation-correct {
  background: var(--vp-c-green-soft);
  border-left: 3px solid var(--vp-c-green-1);
}
.explanation-wrong {
  background: var(--vp-c-red-soft);
  border-left: 3px solid var(--vp-c-red-1);
}

.exam-footer {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--vp-c-divider);
  text-align: center;
}
.exam-final-result {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}
.result-card {
  padding: 1.5rem 2rem;
  border-radius: 12px;
  text-align: center;
}
.result-card h3 {
  margin-top: 0;
}
.result-card p {
  margin: 0.25rem 0;
}
.result-pass {
  background: var(--vp-c-green-soft);
  border: 1px solid var(--vp-c-green-1);
}
.result-fail {
  background: var(--vp-c-red-soft);
  border: 1px solid var(--vp-c-red-1);
}

.exam-btn {
  padding: 0.5rem 1.5rem;
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 8px;
  font-size: 0.95em;
  cursor: pointer;
  transition: opacity 0.15s;
}
.exam-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}
.exam-btn-primary {
  background: var(--vp-c-brand-1);
  color: var(--vp-c-white);
}
.exam-btn-primary:hover:not(:disabled) {
  opacity: 0.85;
}
.exam-btn-outline {
  background: transparent;
  color: var(--vp-c-brand-1);
}
.exam-btn-outline:hover {
  background: var(--vp-c-brand-soft);
}
.exam-btn-lg {
  padding: 0.75rem 2.5rem;
  font-size: 1.05em;
  font-weight: 600;
}
.exam-btn-sm {
  padding: 0.25rem 0.6rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  font-size: 0.8em;
  cursor: pointer;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
}
.exam-btn-sm:hover {
  background: var(--vp-c-bg-mute);
}

@media (max-width: 640px) {
  .exam-header {
    flex-direction: column;
    text-align: center;
  }
  .exam-info-grid {
    grid-template-columns: 1fr;
  }
  .ktype-toggle-col {
    width: 44px;
  }
  .ktype-btn {
    width: 24px;
    height: 24px;
  }
}
</style>
