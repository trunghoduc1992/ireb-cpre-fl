import re, json

with open(r'D:\Projects\ireb_cpre_fl\validations\2026-05-27_v3.3.0\downloads\ireb_cpre_glossary_EN_v2.2.0.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove page headers and page breaks
text = re.sub(r'--- PAGE \d+ ---', '', text)
text = re.sub(r'Glossary of Requirements Engineering Terminology\s*\n\s*\d+ \| 39', '', text)
text = re.sub(r'Term \(English\)\nDefinition', '', text)

# Extract the definitions section
m = re.search(r'Definitions of Terms\s*\n(.+?)List of Abbreviations', text, re.DOTALL)
if not m:
    print('Could not find definitions section')
    exit(1)

defs_text = m.group(1)
lines = defs_text.strip().split('\n')

terms = []
current_term = None
current_def_lines = []

def save_current():
    if current_term and current_def_lines:
        defn = ' '.join(current_def_lines).strip()
        defn = re.sub(r'\s+', ' ', defn)
        # Remove cross-reference arrows
        defn = defn.replace('↑', '')
        terms.append({'term': current_term, 'definition': defn})

for line in lines:
    stripped = line.strip()
    if not stripped:
        continue

    # Detect term headers: short lines that look like titles
    # Terms are typically < 60 chars, start with uppercase, don't end with period
    is_term = (
        len(stripped) < 60 and
        stripped[0].isupper() and
        not stripped.endswith('.') and
        not stripped.endswith(',') and
        not stripped.startswith(('Note:', 'Notes:', 'Abbreviation:', 'Synonym', 'Abbreviation')) and
        not stripped.startswith(('1.', '2.', '3.', '4.', 'a.', 'b.', 'c.', 'd.')) and
        not stripped.startswith(('The ', 'A ', 'An ', 'Any ', 'That ', 'Those ', 'In ', 'For ')) and
        not stripped.startswith(('→',)) and
        '.' not in stripped[:-1] and  # no period mid-text
        not any(w in stripped.lower() for w in ['which', 'that is', 'when', 'where'])
    )

    if is_term:
        save_current()
        current_term = stripped
        current_def_lines = []
    else:
        if current_term is not None:
            current_def_lines.append(stripped)

save_current()

# Remove entries that are just cross-references or too short
filtered = []
for t in terms:
    d = t['definition'].strip()
    if len(d) > 10 and t['term'] not in ('Terms formatted in bold are key terms',):
        filtered.append(t)

with open(r'D:\Projects\ireb_cpre_fl\validations\2026-05-27_v3.3.0\downloads\glossary_terms_raw.json', 'w', encoding='utf-8') as f:
    json.dump(filtered, f, indent=2, ensure_ascii=False)

print(f'Extracted {len(filtered)} terms, saved to glossary_terms_raw.json')
