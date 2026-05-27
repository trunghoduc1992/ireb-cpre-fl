import { watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'
import { useData } from 'vitepress'

const darkTheme = {
  background: '#1e1e1e',
  primaryColor: '#2d4a7a',
  primaryTextColor: '#e0e0e0',
  primaryBorderColor: '#5b9bd5',
  secondaryColor: '#3b3b5c',
  secondaryTextColor: '#e0e0e0',
  secondaryBorderColor: '#7b7baf',
  tertiaryColor: '#2a3a2a',
  tertiaryTextColor: '#e0e0e0',
  tertiaryBorderColor: '#6aaf6a',
  lineColor: '#8ab4f8',
  textColor: '#e0e0e0',
  mainBkg: '#2d4a7a',
  nodeBorder: '#5b9bd5',
  clusterBkg: '#1a2744',
  clusterBorder: '#5b9bd5',
  titleColor: '#e0e0e0',
  edgeLabelBackground: '#1e1e1e',
  nodeTextColor: '#e0e0e0',
}

const lightTheme = {
  background: '#ffffff',
  primaryColor: '#d4e6f1',
  primaryTextColor: '#1a1a1a',
  primaryBorderColor: '#2980b9',
  secondaryColor: '#d5f5e3',
  secondaryTextColor: '#1a1a1a',
  secondaryBorderColor: '#27ae60',
  tertiaryColor: '#fef9e7',
  tertiaryTextColor: '#1a1a1a',
  tertiaryBorderColor: '#f39c12',
  lineColor: '#2c3e50',
  textColor: '#1a1a1a',
  mainBkg: '#d4e6f1',
  nodeBorder: '#2980b9',
  clusterBkg: '#eaf2f8',
  clusterBorder: '#2980b9',
  titleColor: '#1a1a1a',
  edgeLabelBackground: '#ffffff',
  nodeTextColor: '#1a1a1a',
}

export function useMermaid() {
  if (typeof window === 'undefined') return

  const route = useRoute()
  const { isDark } = useData()
  const stored = []

  async function renderAll() {
    await nextTick()

    const blocks = document.querySelectorAll('div.language-mermaid')
    for (const block of blocks) {
      const code = block.querySelector('code')?.textContent
      if (!code) continue
      const container = document.createElement('div')
      container.className = 'mermaid-container'
      container.dataset.mermaidSource = code
      container.style.cssText = 'display:flex;justify-content:center;margin:1.5rem 0;overflow-x:auto'
      block.replaceWith(container)
      stored.push(container)
    }

    if (!stored.length) return
    await rerender()
  }

  async function rerender() {
    if (!stored.length) return
    const { default: mermaid } = await import('mermaid')
    mermaid.initialize({
      startOnLoad: false,
      theme: 'base',
      securityLevel: 'loose',
      themeVariables: isDark.value ? darkTheme : lightTheme,
    })

    for (const container of stored) {
      const code = container.dataset.mermaidSource
      if (!code) continue
      try {
        const id = 'mermaid-' + Math.random().toString(36).slice(2, 9)
        const { svg } = await mermaid.render(id, code)
        container.innerHTML = svg
      } catch (e) {
        container.innerHTML = '<pre style="color:red">' + e.message + '</pre>'
      }
    }
  }

  watch(() => route.path, () => { stored.length = 0; renderAll() }, { immediate: true })
  watch(isDark, rerender)
}
