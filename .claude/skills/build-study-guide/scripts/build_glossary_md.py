"""Generate a VitePress glossary page from a JSON array of {term, definition} pairs.

Output uses h4 headings (VitePress indexes these for search + anchor scrolling)
with a Vue filter component for on-page search."""
import sys, json, re

def build(json_path, output_md, source_label='Official Glossary', source_url=''):
    with open(json_path, 'r', encoding='utf-8') as f:
        terms = json.load(f)

    lines = []

    lines.append(f'<!-- DO NOT EDIT -- generated from {json_path} -->')
    lines.append(f'<!-- To regenerate: python {__file__} {json_path} {output_md} -->')
    lines.append('')

    # Vue script for on-page filtering
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
    lines.append('# Glossary')
    lines.append('')
    if source_label:
        lines.append('::: info Source')
        lines.append(f'Verbatim definitions from the **{source_label}**.')
        if source_url:
            lines.append(f'[Download official glossary]({source_url})')
        lines.append(':::')
        lines.append('')
    lines.append(f'A searchable reference of {len(terms)} terms.')
    lines.append('')

    # Search input
    lines.append('<div style="margin: 1.5rem 0;">')
    lines.append('  <input v-model="searchTerm" type="text" placeholder="Search terms..."')
    lines.append('    style="width:100%;padding:0.6rem 1rem;border:1px solid var(--vp-c-divider);')
    lines.append('    border-radius:8px;background:var(--vp-c-bg);color:var(--vp-c-text-1);')
    lines.append('    font-size:1rem;outline:none;" />')
    lines.append('</div>')
    lines.append('')

    # Terms as h4 headings (indexed by VitePress search, scrollable via anchors)
    for t in terms:
        raw_term = t['term']
        defn = t['definition'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        lines.append(f'#### {raw_term}')
        lines.append('')
        lines.append(defn)
        lines.append('')

    with open(output_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f'Generated glossary: {len(terms)} terms -> {output_md}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python build_glossary_md.py <terms.json> <output.md> [source-label] [source-url]')
        sys.exit(1)
    label = sys.argv[3] if len(sys.argv) > 3 else 'Official Glossary'
    url = sys.argv[4] if len(sys.argv) > 4 else ''
    build(sys.argv[1], sys.argv[2], label, url)
