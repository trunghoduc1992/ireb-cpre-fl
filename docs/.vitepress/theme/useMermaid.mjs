import { watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'
import { useData } from 'vitepress'

export function useMermaid() {
  if (typeof window === 'undefined') return

  const route = useRoute()
  const { isDark } = useData()

  async function renderAll() {
    await nextTick()
    const blocks = document.querySelectorAll('div.language-mermaid')
    if (!blocks.length) return

    const { default: mermaid } = await import('mermaid')
    mermaid.initialize({
      startOnLoad: false,
      theme: isDark.value ? 'dark' : 'default',
      securityLevel: 'loose',
    })

    for (const block of blocks) {
      const code = block.querySelector('code')?.textContent
      const container = document.createElement('div')
      container.className = 'mermaid-container'
      container.style.cssText = 'display:flex;justify-content:center;margin:1.5rem 0;overflow-x:auto'
      try {
        const id = 'mermaid-' + Math.random().toString(36).slice(2, 9)
        const { svg } = await mermaid.render(id, code)
        container.innerHTML = svg
      } catch (e) {
        container.innerHTML = '<pre style="color:red">' + e.message + '</pre>'
      }
      block.replaceWith(container)
    }
  }

  watch(() => route.path, renderAll, { immediate: true })
  watch(isDark, renderAll)
}
