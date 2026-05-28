import { onMounted, onUnmounted } from 'vue'

export function useSearchKeys() {
  if (typeof window === 'undefined') return

  let observer

  // Add hints for our custom shortcuts to the modal's footer row.
  function injectHints() {
    const shortcuts = document.querySelector(
      '.VPLocalSearchBox .search-keyboard-shortcuts'
    )
    if (!shortcuts || shortcuts.querySelector('.custom-search-hint')) return

    // VitePress styles the kbd caps with scoped CSS keyed on a data-v-* hash.
    // Mirror that attribute onto our injected nodes so the styling applies.
    const scopeAttr = shortcuts
      .getAttributeNames()
      .find(n => n.startsWith('data-v-'))
    const scope = scopeAttr ? ` ${scopeAttr}` : ''

    // shortcuts.insertAdjacentHTML(
    //   'beforeend',
    //   `<span${scope} class="custom-search-hint"><kbd${scope}>alt-k</kbd><kbd${scope}>alt-j</kbd> to navigate</span>` +
    //     `<span${scope} class="custom-search-hint"><kbd${scope}>ctrl-\`</kbd> to toggle layout</span>`
    // )
    // shortcuts.insertAdjacentHTML(
    //   'beforeend',
    //   `<span${scope} class="custom-search-hint"><kbd${scope}>Alt</kbd><kbd${scope}>K</kbd> up</span>` +
    //     `<span${scope} class="custom-search-hint"><kbd${scope}>Alt</kbd><kbd${scope}>J</kbd> down</span>` +
    //     `<span${scope} class="custom-search-hint"><kbd${scope}>Ctrl</kbd><kbd${scope}>\`</kbd> to toggle layout</span>`
    // )
    shortcuts.insertAdjacentHTML(
      'beforeend',
      `<span${scope} class="custom-search-hint"><kbd${scope}>alt-k</kbd> up</span>` +
        `<span${scope} class="custom-search-hint"><kbd${scope}>alt-j</kbd> down</span>` +
        `<span${scope} class="custom-search-hint"><kbd${scope}>ctrl-\`</kbd> to toggle layout</span>`
    )
  }

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

  onMounted(() => {
    window.addEventListener('keydown', handler)
    // The modal mounts lazily on open, so watch for it and inject hints.
    observer = new MutationObserver(injectHints)
    observer.observe(document.body, { childList: true, subtree: true })
  })
  onUnmounted(() => {
    window.removeEventListener('keydown', handler)
    observer?.disconnect()
  })
}
