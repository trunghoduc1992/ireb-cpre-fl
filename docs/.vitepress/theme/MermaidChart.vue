<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import { useData } from 'vitepress'

const props = defineProps({
  code: { type: String, required: true },
})

const el = ref(null)
const { isDark } = useData()

async function render() {
  await nextTick()
  if (!el.value) return
  try {
    const { default: mermaid } = await import('mermaid')
    mermaid.initialize({
      startOnLoad: false,
      theme: isDark.value ? 'dark' : 'default',
      securityLevel: 'loose',
    })
    const decoded = decodeURIComponent(props.code)
    const id = 'mermaid-' + Math.random().toString(36).slice(2, 9)
    const { svg } = await mermaid.render(id, decoded)
    el.value.innerHTML = svg
  } catch (e) {
    el.value.innerHTML = '<pre style="color:red">' + e.message + '</pre>'
  }
}

onMounted(render)
watch(isDark, render)
</script>

<template>
  <div ref="el" class="mermaid-container" />
</template>

<style scoped>
.mermaid-container {
  display: flex;
  justify-content: center;
  margin: 1.5rem 0;
  overflow-x: auto;
}
</style>
