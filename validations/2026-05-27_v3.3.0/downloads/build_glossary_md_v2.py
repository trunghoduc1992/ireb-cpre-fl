"""Build glossary as static markdown content (indexable by VitePress search)
with a Vue filter component for interactive filtering."""
import json, re

with open(r'D:\Projects\ireb_cpre_fl\validations\2026-05-27_v3.3.0\downloads\glossary_terms_raw.json', 'r', encoding='utf-8') as f:
    terms = json.load(f)

lines = []

# Vue script for search filtering
lines.append('<script setup>')
lines.append("import { ref, onMounted, watch } from 'vue'")
lines.append('')
lines.append("const searchTerm = ref('')")
lines.append('')
lines.append('function filterTerms() {')
lines.append('  const q = searchTerm.value.toLowerCase()')
lines.append("  document.querySelectorAll('.vp-doc > h4').forEach(h4 => {")
lines.append("    const p = h4.nextElementSibling")
lines.append("    const text = h4.textContent.toLowerCase() + (p ? p.textContent.toLowerCase() : '')")
lines.append("    const show = !q || text.includes(q)")
lines.append("    h4.style.display = show ? '' : 'none'")
lines.append("    if (p && p.tagName === 'P') p.style.display = show ? '' : 'none'")
lines.append('  })')
lines.append('}')
lines.append('')
lines.append('onMounted(() => { watch(searchTerm, filterTerms) })')
lines.append('</script>')
lines.append('')

# Page header
lines.append('# Glossary (Syllabus v3.3.0)')
lines.append('')
lines.append('::: info Source')
lines.append('Verbatim definitions from the **IREB CPRE Glossary v2.2.0** (October 2025) by Martin Glinz.')
lines.append('[Download official glossary](https://cpre.ireb.org/en/downloads-and-resources/downloads)')
lines.append(':::')
lines.append('')
lines.append(f'A searchable reference of {len(terms)} terms from the official IREB CPRE glossary.')
lines.append('')

# Search input
lines.append('<div style="margin: 1.5rem 0;">')
lines.append('  <input')
lines.append('    v-model="searchTerm"')
lines.append('    type="text"')
lines.append('    placeholder="Search terms..."')
lines.append('    style="')
lines.append('      width: 100%;')
lines.append('      padding: 0.6rem 1rem;')
lines.append('      border: 1px solid var(--vp-c-divider);')
lines.append('      border-radius: 8px;')
lines.append('      background: var(--vp-c-bg);')
lines.append('      color: var(--vp-c-text-1);')
lines.append('      font-size: 1rem;')
lines.append('      outline: none;')
lines.append('    "')
lines.append('  />')
lines.append('</div>')
lines.append('')

# Render each term as an h4 heading (VitePress indexes headings for search anchors)
# h4 is excluded from the sidebar outline by the config (outline.level: [2, 3])
for t in terms:
    raw_term = t['term']
    defn = t['definition'].replace('<', '&lt;').replace('>', '&gt;')
    lines.append(f'#### {raw_term}')
    lines.append('')
    lines.append(f'{defn}')
    lines.append('')

output = '\n'.join(lines)

with open(r'D:\Projects\ireb_cpre_fl\docs\glossary.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f'Generated glossary with {len(terms)} static terms')
