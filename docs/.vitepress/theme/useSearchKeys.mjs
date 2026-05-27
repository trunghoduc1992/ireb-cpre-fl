import { onMounted, onUnmounted } from 'vue'

export function useSearchKeys() {
  if (typeof window === 'undefined') return

  function handler(e) {
    const modal = document.querySelector('.VPLocalSearchBox')
    if (!modal) return

    // Alt+K → navigate up
    if (e.altKey && e.key === 'k') {
      e.preventDefault()
      navigateResults(modal, -1)
      return
    }

    // Alt+J → navigate down
    if (e.altKey && e.key === 'j') {
      e.preventDefault()
      navigateResults(modal, 1)
      return
    }

    // Ctrl+` → toggle detailed list
    if (e.ctrlKey && e.key === '`') {
      e.preventDefault()
      const btn = modal.querySelector('.toggle-layout-button')
      if (btn) btn.click()
      return
    }
  }

  function navigateResults(modal, direction) {
    const items = modal.querySelectorAll('.result')
    if (!items.length) return

    let current = -1
    items.forEach((el, i) => {
      if (el.classList.contains('selected')) current = i
    })

    let next = current + direction
    if (next < 0) next = items.length - 1
    if (next >= items.length) next = 0

    items.forEach(el => el.classList.remove('selected'))
    items[next].classList.add('selected')
    items[next].scrollIntoView({ block: 'nearest' })

    // Sync with VitePress internal state by dispatching keyboard event
    const input = modal.querySelector('.search-input')
    if (input) {
      input.dispatchEvent(new KeyboardEvent('keydown', {
        key: direction === -1 ? 'ArrowUp' : 'ArrowDown',
        bubbles: true
      }))
    }
  }

  onMounted(() => window.addEventListener('keydown', handler))
  onUnmounted(() => window.removeEventListener('keydown', handler))
}
