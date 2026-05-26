<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  questions: {
    type: Array,
    required: true,
  },
})

const answers = ref({})
const submitted = ref(false)

function select(qi, oi) {
  if (submitted.value) return
  answers.value[qi] = oi
}

const score = computed(() => {
  let correct = 0
  props.questions.forEach((q, i) => {
    if (answers.value[i] === q.answer) correct++
  })
  return correct
})

function submit() {
  submitted.value = true
}

function reset() {
  answers.value = {}
  submitted.value = false
}
</script>

<template>
  <div class="quiz-container">
    <h3>Practice Quiz</h3>
    <div v-for="(q, qi) in questions" :key="qi" class="quiz-question">
      <p class="question-text"><strong>Q{{ qi + 1 }}.</strong> {{ q.text }}</p>
      <div
        v-for="(opt, oi) in q.options"
        :key="oi"
        class="quiz-option"
        :class="{
          selected: answers[qi] === oi,
          correct: submitted && oi === q.answer,
          wrong: submitted && answers[qi] === oi && oi !== q.answer,
        }"
        @click="select(qi, oi)"
      >
        <span class="option-letter">{{ String.fromCharCode(65 + oi) }}</span>
        <span>{{ opt }}</span>
      </div>
      <p v-if="submitted" class="explanation">{{ q.explanation }}</p>
    </div>
    <div class="quiz-actions">
      <button v-if="!submitted" class="quiz-btn" :disabled="Object.keys(answers).length < questions.length" @click="submit">
        Check Answers
      </button>
      <div v-else class="quiz-result">
        <p>Score: <strong>{{ score }}/{{ questions.length }}</strong></p>
        <button class="quiz-btn" @click="reset">Retry</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.quiz-container {
  margin: 2rem 0;
  padding: 1.5rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
}
.quiz-container h3 {
  margin-top: 0;
}
.quiz-question {
  margin-bottom: 1.5rem;
}
.question-text {
  margin-bottom: 0.5rem;
}
.quiz-option {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  padding: 0.6rem 0.8rem;
  margin: 0.3rem 0;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.15s;
}
.quiz-option:hover:not(.correct):not(.wrong) {
  background: var(--vp-c-bg-mute);
}
.quiz-option.selected {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.quiz-option.correct {
  border-color: var(--vp-c-green-1);
  background: var(--vp-c-green-soft);
}
.quiz-option.wrong {
  border-color: var(--vp-c-red-1);
  background: var(--vp-c-red-soft);
}
.option-letter {
  font-weight: 600;
  min-width: 1.5em;
  color: var(--vp-c-text-2);
}
.explanation {
  margin-top: 0.5rem;
  padding: 0.5rem 0.75rem;
  background: var(--vp-c-default-soft);
  border-radius: 6px;
  font-size: 0.9em;
  color: var(--vp-c-text-2);
}
.quiz-actions {
  margin-top: 1rem;
}
.quiz-btn {
  padding: 0.5rem 1.5rem;
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 8px;
  background: var(--vp-c-brand-1);
  color: var(--vp-c-white);
  font-size: 0.95em;
  cursor: pointer;
  transition: opacity 0.15s;
}
.quiz-btn:hover {
  opacity: 0.85;
}
.quiz-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.quiz-result {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.quiz-result p {
  margin: 0;
}
</style>
