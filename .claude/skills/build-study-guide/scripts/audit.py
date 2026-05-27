"""Audit study guide chapters against syllabus Educational Objectives and key terms.

Usage: python audit.py <eo-definition.json> <chapters-dir> <glossary-terms.json> <output-report.md>

The EO definition JSON has the structure:
{
  "units": {
    "EU 1": {
      "files": ["01-introduction.md"],
      "terms": ["requirement", "stakeholder", ...],
      "eos": [
        {"id": "EO 1.1.1", "level": "L1", "desc": "...", "keywords": ["kw1", "kw2"]}
      ]
    }
  }
}
"""
import sys, os, json

def audit(eo_json_path, chapters_dir, glossary_json_path, output_path):
    with open(eo_json_path, 'r', encoding='utf-8') as f:
        eo_def = json.load(f)

    with open(glossary_json_path, 'r', encoding='utf-8') as f:
        glossary_terms = {t['term'].lower() for t in json.load(f)}

    chapters = {}
    for fname in os.listdir(chapters_dir):
        if fname.endswith('.md'):
            with open(os.path.join(chapters_dir, fname), 'r', encoding='utf-8') as f:
                chapters[fname] = f.read().lower()

    report = ['# Audit Report\n']
    total_eos = 0
    covered_eos = 0
    issues = []

    for unit_name, unit in eo_def.get('units', {}).items():
        content = '\n'.join(chapters.get(f, '') for f in unit.get('files', []))
        report.append(f'\n## {unit_name}\n')

        # Check EOs
        report.append('### Educational Objectives\n')
        for eo in unit.get('eos', []):
            total_eos += 1
            keywords = eo.get('keywords', [])
            found = sum(1 for kw in keywords if kw.lower() in content)
            coverage = found / max(len(keywords), 1)
            if coverage >= 0.5:
                covered_eos += 1
                status = 'PASS'
            elif coverage > 0:
                covered_eos += 0.5
                status = 'PARTIAL'
            else:
                status = 'MISSING'

            report.append(f'- [{status}] **{eo["id"]}** ({eo["level"]}): {eo["desc"]} ({found}/{len(keywords)} keywords)')
            if status != 'PASS':
                missing = [kw for kw in keywords if kw.lower() not in content]
                issues.append(f'{eo["id"]}: missing keywords: {missing}')

        # Check key terms
        report.append('\n### Key Terms\n')
        for term in unit.get('terms', []):
            in_chapter = term.lower() in content
            in_glossary = any(term.lower() in g for g in glossary_terms)
            status = 'PASS' if (in_chapter and in_glossary) else 'WARN' if in_chapter else 'FAIL'
            report.append(f'- [{status}] **{term}** — chapter: {"yes" if in_chapter else "NO"}, glossary: {"yes" if in_glossary else "NO"}')
            if not in_chapter:
                issues.append(f'{unit_name}: term "{term}" not found in chapter')

    report.append(f'\n## Summary\n')
    report.append(f'- EO coverage: {covered_eos}/{total_eos}')
    report.append(f'- Issues: {len(issues)}')
    if issues:
        report.append('\n### Issues\n')
        for i in issues:
            report.append(f'- {i}')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

    print(f'Audit: {covered_eos}/{total_eos} EOs covered, {len(issues)} issues')
    print(f'Report: {output_path}')
    return len(issues) == 0

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage: python audit.py <eo-definition.json> <chapters-dir> <glossary.json> <output.md>')
        print()
        print('EO definition JSON format:')
        print('  {"units": {"EU 1": {"files": [...], "terms": [...], "eos": [{...}]}}}')
        sys.exit(1)
    success = audit(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    sys.exit(0 if success else 1)
