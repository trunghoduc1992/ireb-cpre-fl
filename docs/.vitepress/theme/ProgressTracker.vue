<script setup>
import { ref, onMounted, computed } from 'vue'

const chapters = [
  { id: 'ch01', title: '1. Introduction & Foundations', link: '/chapters/01-introduction' },
  { id: 'ch02', title: '2. System & System Context', link: '/chapters/02-system-context' },
  { id: 'ch03', title: '3. Requirements Elicitation', link: '/chapters/03-elicitation' },
  { id: 'ch04', title: '4. Documentation Basics', link: '/chapters/04-documentation' },
  { id: 'ch05', title: '5. Natural Language', link: '/chapters/05-natural-language' },
  { id: 'ch06', title: '6. Model-Based Documentation', link: '/chapters/06-models' },
  { id: 'ch07', title: '7. Validation & Negotiation', link: '/chapters/07-validation' },
  { id: 'ch08', title: '8. Requirements Management', link: '/chapters/08-management' },
  { id: 'ch09', title: '9. Tool Support', link: '/chapters/09-tools' },
]

const completed = ref({})

onMounted(() => {
  const saved = localStorage.getItem('cpre-progress')
  if (saved) {
    completed.value = JSON.parse(saved)
  }
})

function toggle(id) {
  completed.value[id] = !completed.value[id]
  localStorage.setItem('cpre-progress', JSON.stringify(completed.value))
}

const progress = computed(() => {
  const done = Object.values(completed.value).filter(Boolean).length
  return Math.round((done / chapters.length) * 100)
})
</script>

<template>
  <div class="progress-tracker">
    <h3>Study Progress</h3>
    <div class="progress-bar-container">
      <div class="progress-bar" :style="{ width: progress + '%' }"></div>
    </div>
    <p class="progress-label">{{ progress }}% complete</p>
    <ul class="chapter-list">
      <li v-for="ch in chapters" :key="ch.id" class="chapter-item">
        <label class="chapter-label">
          <input
            type="checkbox"
            :checked="completed[ch.id]"
            @change="toggle(ch.id)"
          />
          <a :href="ch.link">{{ ch.title }}</a>
        </label>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.progress-tracker {
  margin: 1.5rem 0;
  padding: 1.25rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
}
.progress-tracker h3 {
  margin-top: 0;
}
.progress-bar-container {
  width: 100%;
  height: 10px;
  background: var(--vp-c-divider);
  border-radius: 5px;
  overflow: hidden;
}
.progress-bar {
  height: 100%;
  background: var(--vp-c-brand-1);
  border-radius: 5px;
  transition: width 0.3s ease;
}
.progress-label {
  font-size: 0.9em;
  color: var(--vp-c-text-2);
  margin-top: 0.3rem;
}
.chapter-list {
  list-style: none;
  padding: 0;
  margin: 0.5rem 0 0 0;
}
.chapter-item {
  padding: 0.3rem 0;
}
.chapter-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}
.chapter-label input {
  width: 1.1em;
  height: 1.1em;
  cursor: pointer;
}
.chapter-label a {
  color: var(--vp-c-text-1);
  text-decoration: none;
}
.chapter-label a:hover {
  color: var(--vp-c-brand-1);
}
</style>
