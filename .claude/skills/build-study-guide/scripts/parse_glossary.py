"""Parse extracted glossary text into a JSON array of {term, definition} pairs."""
import sys, os, re, json

def parse(txt_path, output_json):
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()

    text = re.sub(r'--- PAGE \d+ ---', '', text)
    # Remove common headers (adapt pattern to the specific glossary format)
    text = re.sub(r'Glossary of .+?Terminology\s*\n\s*\d+ \| \d+', '', text)
    text = re.sub(r'Term \(English\)\nDefinition', '', text)

    m = re.search(r'Definitions of Terms\s*\n(.+?)(?:List of Abbreviations|References|Sources)', text, re.DOTALL)
    if not m:
        print('Warning: could not find definitions section markers, using full text')
        defs_text = text
    else:
        defs_text = m.group(1)

    lines = defs_text.strip().split('\n')
    terms = []
    current_term = None
    current_def_lines = []

    def save():
        if current_term and current_def_lines:
            defn = ' '.join(current_def_lines).strip()
            defn = re.sub(r'\s+', ' ', defn)
            defn = defn.replace('↑', '')  # remove cross-ref arrows
            if len(defn) > 10:
                terms.append({'term': current_term, 'definition': defn})

    for line in lines:
        s = line.strip()
        if not s:
            continue
        is_term = (
            len(s) < 60 and s[0].isupper() and
            not s.endswith('.') and not s.endswith(',') and
            not s.startswith(('Note:', 'Notes:', 'Abbreviation:', 'Synonym')) and
            not s.startswith(('1.', '2.', '3.', '4.', 'a.', 'b.', 'c.', 'd.')) and
            not s.startswith(('The ', 'A ', 'An ', 'Any ', 'That ', 'Those ', 'In ', 'For ')) and
            not s.startswith(('→',)) and
            '.' not in s[:-1]
        )
        if is_term:
            save()
            current_term = s
            current_def_lines = []
        elif current_term is not None:
            current_def_lines.append(s)

    save()

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(terms, f, indent=2, ensure_ascii=False)

    print(f'Parsed {len(terms)} terms -> {output_json}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python parse_glossary.py <extracted-text.txt> <output.json>')
        sys.exit(1)
    parse(sys.argv[1], sys.argv[2])
