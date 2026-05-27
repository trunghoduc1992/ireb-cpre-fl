"""Phase 5 audit: cross-reference EOs and key terms against v3 chapter content."""
import os, json, re

V3_DIR = r'D:\Projects\ireb_cpre_fl\docs\v3'
GLOSSARY_JSON = r'D:\Projects\ireb_cpre_fl\validations\2026-05-27_v3.3.0\downloads\glossary_terms_raw.json'

# Load all v3 chapter content
chapters = {}
for root, dirs, files in os.walk(os.path.join(V3_DIR, 'chapters')):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                chapters[f] = fh.read().lower()

# Load exam content
exams = {}
for f in ['exam-1.md', 'exam-2.md']:
    path = os.path.join(V3_DIR, 'exams', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fh:
            exams[f] = fh.read().lower()

# Load glossary terms
with open(GLOSSARY_JSON, 'r', encoding='utf-8') as f:
    glossary_terms = {t['term'].lower() for t in json.load(f)}

# All v3 content combined for searching
all_content = '\n'.join(chapters.values())

# ── EO Definitions ──
eos = {
    'EU 1': [
        ('EO 1.1.1', 'L1', 'Remember the fundamental terminology'),
        ('EO 1.1.2', 'L2', 'Understand the different kinds of requirements'),
        ('EO 1.2.1', 'L2', 'Explain the value of RE'),
        ('EO 1.2.2', 'L1', 'Enumerate symptoms of inadequate RE'),
        ('EO 1.3.1', 'L1', 'Know where RE can be applied and where requirements occur'),
        ('EO 1.4.1', 'L1', 'Know the major tasks of RE and that an RE process has to be tailored'),
        ('EO 1.5.1', 'L1', 'Characterize the role and tasks of a Requirements Engineer'),
        ('EO 1.6.1', 'L1', 'Remember what a Requirements Engineer needs to learn'),
    ],
    'EU 2': [
        ('EO 2.1.1', 'L1', 'Enumerate the principles of RE'),
        ('EO 2.2.1', 'L1', 'Remember the terms associated with the principles'),
        ('EO 2.2.2', 'L2', 'Explain the principles and the reasons why they are important'),
    ],
    'EU 3': [
        ('EO 3.1.1', 'L1', 'Know the characteristics of RE work products and enumerate frequently used types'),
        ('EO 3.1.2', 'L1', 'Know what each work product can be used for and know the life span'),
        ('EO 3.1.3', 'L2', 'Explain the different abstraction levels for requirements'),
        ('EO 3.1.4', 'L1', 'Know aspects to be considered in work products and interrelationships'),
        ('EO 3.1.5', 'L1', 'Name the general documentation guidelines'),
        ('EO 3.1.6', 'L1', 'Describe why it is worth planning the work products to be used'),
        ('EO 3.2.1', 'L1', 'Know natural-language-based work products and their advantages and disadvantages'),
        ('EO 3.2.2', 'L2', 'Explain the rules for writing good natural-language requirements'),
        ('EO 3.3.1', 'L1', 'Know the categories of template-based work products and their advantages and disadvantages'),
        ('EO 3.3.2', 'L3', 'Specify an individual requirement and a user story using a phrase template'),
        ('EO 3.3.3', 'L3', 'Specify a use case using a form template'),
        ('EO 3.4.1', 'L2', 'Understand the role, purpose, and use of models in RE'),
        ('EO 3.4.2', 'L2', 'Understand the advantages and limitations of modeling in RE'),
        ('EO 3.4.3', 'L1', 'Know the terms: model, modeling language, activity model, activity diagram, class model, class diagram, context model, context diagram, domain model, goal model, interaction model, process model, sequence diagram, statechart, state machine, state machine diagram, use case, use case diagram'),
        ('EO 3.4.4', 'L2', 'Understand how to select an appropriate model type'),
        ('EO 3.4.5', 'L2', 'Understand and interpret simple models: context models, use cases, domain models, class models, activity models, process models, statecharts'),
        ('EO 3.4.6', 'L3', 'Specify a simple model using a UML class diagram'),
        ('EO 3.4.7', 'L3', 'Specify a simple system function or business process by a UML activity diagram'),
        ('EO 3.5.1', 'L2', 'Explain the purpose of glossaries and how to create one'),
        ('EO 3.6.1', 'L1', 'Know frequently used requirements specification documents'),
        ('EO 3.6.2', 'L2', 'Explain which document structures serve which purpose'),
        ('EO 3.7.1', 'L1', 'Know different kinds of prototypes and what they are used for'),
        ('EO 3.8.1', 'L1', 'Know quality criteria for single requirements'),
        ('EO 3.8.2', 'L1', 'Know quality criteria for work products'),
    ],
    'EU 4': [
        ('EO 4.1.1', 'L3', 'Determine the boundaries of the system'),
        ('EO 4.1.2', 'L1', 'Remember the relevant sources for the system'),
        ('EO 4.1.3', 'L3', 'Identify stakeholders and write a stakeholder list'),
        ('EO 4.1.4', 'L2', 'Understand the benefits of stakeholder management'),
        ('EO 4.2.1', 'L2', 'Understand how the Kano model can help elicit the right requirements'),
        ('EO 4.2.2', 'L2', 'Understand the difference between gathering techniques and design/idea-generating techniques'),
        ('EO 4.2.3', 'L2', 'Understand how to choose a proper elicitation technique'),
        ('EO 4.3.1', 'L1', 'Remember the different types of conflict'),
        ('EO 4.3.2', 'L2', 'Understand what activities are necessary to solve conflicts'),
        ('EO 4.3.3', 'L2', 'Understand how to apply appropriate conflict resolution techniques'),
        ('EO 4.4.1', 'L2', 'Understand why requirements documents need to be validated'),
        ('EO 4.4.2', 'L1', 'Remember the four important aspects for requirements validation'),
        ('EO 4.4.3', 'L2', 'Understand how to apply appropriate techniques for requirements validation'),
    ],
    'EU 5': [
        ('EO 5.1.1', 'L1', 'Know the important factors that influence an RE process'),
        ('EO 5.1.2', 'L2', 'Understand how and why these factors are influencing'),
        ('EO 5.2.1', 'L2', 'Understand the facets to be considered for RE process configuration'),
        ('EO 5.3.1', 'L1', 'Know typical RE process configurations'),
        ('EO 5.3.2', 'L2', 'Understand the steps for configuring an RE process'),
        ('EO 5.3.3', 'L3', 'Select and apply an appropriate RE process configuration'),
    ],
    'EU 6': [
        ('EO 6.1.1', 'L1', 'Know what requirements management is about and why it is needed'),
        ('EO 6.2.1', 'L2', 'Explain why requirements work products need a status/life cycle model'),
        ('EO 6.3.1', 'L2', 'Explain what a requirements versioning concept looks like'),
        ('EO 6.4.1', 'L1', 'Know the use of requirements configurations and baselines'),
        ('EO 6.5.1', 'L1', 'Know the purpose of attributes for requirements'),
        ('EO 6.5.2', 'L2', 'Explain what an appropriate set of attributes looks like'),
        ('EO 6.5.3', 'L2', 'Explain the purpose of views and name the different views'),
        ('EO 6.6.1', 'L1', 'Name reasons for requirements traceability'),
        ('EO 6.6.2', 'L1', 'Summarize the differences between implicit and explicit traceability'),
        ('EO 6.6.3', 'L1', 'Know how explicit traceability can be documented'),
        ('EO 6.7.1', 'L1', 'Know how to handle changes in linear and agile approaches'),
        ('EO 6.8.1', 'L1', 'Know the reason for prioritization and meaningful assessment criteria'),
        ('EO 6.8.2', 'L1', 'Name steps to prioritize requirements'),
        ('EO 6.8.3', 'L1', 'Name different categories of prioritization techniques'),
    ],
    'EU 7': [
        ('EO 7.1.1', 'L1', 'Know the different types of RE tools'),
        ('EO 7.2.1', 'L2', 'Explain what to consider when introducing RE tools'),
    ],
}

# ── Key terms per EU ──
key_terms = {
    'EU 1': ['requirement', 'requirements specification', 'requirements engineering', 'stakeholder', 'system', 'requirements engineer'],
    'EU 2': ['context', 'requirement', 'requirements engineering', 'stakeholder', 'shared understanding', 'validation'],
    'EU 3': ['work product', 'natural-language', 'template', 'model', 'glossary', 'quality criteria', 'requirements specification'],
    'EU 4': ['requirements source', 'system boundary', 'system context', 'requirements elicitation', 'requirements validation', 'stakeholder', 'kano model', 'conflict resolution'],
    'EU 5': ['process', 're process'],
    'EU 6': ['requirements management', 'change management', 'traceability', 'requirements attributes', 'requirements life cycle', 'prioritization'],
    'EU 7': ['tool', 're tool'],
}

# EU -> chapter file mapping
eu_files = {
    'EU 1': ['01-introduction.md'],
    'EU 2': ['02-principles.md'],
    'EU 3': ['03a-work-product-basics.md', '03b-natural-language.md', '03c-models.md'],
    'EU 4': ['04a-sources-and-elicitation.md', '04b-conflicts-and-validation.md'],
    'EU 5': ['05-process.md'],
    'EU 6': ['06-management.md'],
    'EU 7': ['07-tools.md'],
}

# ── Audit ──
report = []
issues = []

def eu_content(eu):
    return '\n'.join(chapters.get(f, '') for f in eu_files.get(eu, []))

# 5.1 Cross-reference EOs
report.append('# Phase 5 Audit Report\n')
report.append('## 5.1 Educational Objective Coverage\n')

eo_keywords = {
    'EO 1.1.1': ['requirement', 'functional', 'quality', 'constraint'],
    'EO 1.1.2': ['functional requirement', 'quality requirement', 'constraint'],
    'EO 1.2.1': ['value', 'risk', 'reducing'],
    'EO 1.2.2': ['symptom', 'inadequate', 'rushing', 'communication'],
    'EO 1.3.1': ['system requirements', 'stakeholder requirements', 'user requirements', 'domain requirements', 'business requirements'],
    'EO 1.4.1': ['elicitation', 'documentation', 'validation', 'management'],
    'EO 1.5.1': ['role', 'requirements engineer', 'mediator'],
    'EO 1.6.1': ['learn', 'skill', 'foundational'],
    'EO 2.1.1': ['nine', 'principle', 'value orientation'],
    'EO 2.2.1': ['shared understanding', 'context', 'evolution', 'innovation'],
    'EO 2.2.2': ['principle', 'important', 'explain'],
    'EO 3.1.1': ['work product', 'purpose', 'representation', 'life span'],
    'EO 3.1.2': ['temporary', 'evolving', 'durable'],
    'EO 3.1.3': ['abstraction level'],
    'EO 3.1.4': ['functional requirements', 'structure and data', 'function and flow', 'state and behavior'],
    'EO 3.1.5': ['documentation guideline', 'redundancy', 'consistency'],
    'EO 3.1.6': ['planning', 'work products to be used'],
    'EO 3.2.1': ['natural language', 'advantage', 'disadvantage'],
    'EO 3.2.2': ['pitfall', 'passive voice', 'nominalization', 'incomplete'],
    'EO 3.3.1': ['phrase template', 'form template', 'document template'],
    'EO 3.3.2': ['phrase template', 'user story'],
    'EO 3.3.3': ['use case', 'form template'],
    'EO 3.4.1': ['model', 'abstract representation'],
    'EO 3.4.2': ['advantage', 'limitation', 'model'],
    'EO 3.4.3': ['activity diagram', 'class diagram', 'context diagram', 'state machine', 'use case diagram'],
    'EO 3.4.4': ['select', 'model type', 'situation'],
    'EO 3.4.5': ['context model', 'class model', 'activity model', 'statechart'],
    'EO 3.4.6': ['class diagram', 'uml'],
    'EO 3.4.7': ['activity diagram', 'uml'],
    'EO 3.5.1': ['glossary', 'purpose', 'create'],
    'EO 3.6.1': ['requirements specification', 'product backlog', 'story map'],
    'EO 3.6.2': ['document structure', 'purpose'],
    'EO 3.7.1': ['prototype', 'wireframe', 'mock-up'],
    'EO 3.8.1': ['adequate', 'unambiguous', 'verifiable'],
    'EO 3.8.2': ['consistent', 'non-redundant', 'traceable'],
    'EO 4.1.1': ['system boundary', 'context boundary'],
    'EO 4.1.2': ['stakeholder', 'document', 'system', 'source'],
    'EO 4.1.3': ['stakeholder list', 'name', 'role'],
    'EO 4.1.4': ['stakeholder management', 'benefit'],
    'EO 4.2.1': ['kano', 'delighter', 'satisfier', 'dissatisfier'],
    'EO 4.2.2': ['gathering technique', 'design', 'idea-generating'],
    'EO 4.2.3': ['choose', 'elicitation technique', 'combination'],
    'EO 4.3.1': ['conflict type', 'subject matter', 'interest', 'value'],
    'EO 4.3.2': ['conflict identification', 'conflict analysis', 'conflict resolution'],
    'EO 4.3.3': ['agreement', 'compromise', 'voting', 'overruling'],
    'EO 4.4.1': ['validate', 'quality'],
    'EO 4.4.2': ['right stakeholders', 'separating', 'different views', 'repeated'],
    'EO 4.4.3': ['walkthrough', 'inspection', 'prototyping'],
    'EO 5.1.1': ['influencing factor', 'complexity', 'volatility'],
    'EO 5.1.2': ['factor', 'constrain', 'influence'],
    'EO 5.2.1': ['linear', 'iterative', 'prescriptive', 'explorative'],
    'EO 5.3.1': ['participatory', 'contractual', 'product-oriented'],
    'EO 5.3.2': ['five-step', 'step', 'configure'],
    'EO 5.3.3': ['configure', 'process', 'apply'],
    'EO 6.1.1': ['requirements management', 'storing', 'changing', 'tracing'],
    'EO 6.2.1': ['life cycle', 'status', 'transition'],
    'EO 6.3.1': ['version', 'version number', 'history'],
    'EO 6.4.1': ['configuration', 'baseline'],
    'EO 6.5.1': ['attribute', 'metadata'],
    'EO 6.5.2': ['attribute', 'appropriate'],
    'EO 6.5.3': ['selective', 'projective', 'aggregating'],
    'EO 6.6.1': ['traceability', 'reason'],
    'EO 6.6.2': ['implicit', 'explicit', 'traceability'],
    'EO 6.6.3': ['hyperlink', 'matri', 'explicit'],
    'EO 6.7.1': ['change control board', 'product owner', 'backlog'],
    'EO 6.8.1': ['prioritization', 'business value', 'assessment criteria'],
    'EO 6.8.2': ['step', 'prioritiz'],
    'EO 6.8.3': ['ad-hoc', 'analytical'],
    'EO 7.1.1': ['management of requirements', 'management of the re process', 'documentation of knowledge'],
    'EO 7.2.1': ['pilot project', 'life cycle cost', 'introducing'],
}

total_eos = 0
covered_eos = 0

for eu, eo_list in eos.items():
    content = eu_content(eu)
    report.append(f'\n### {eu}\n')
    for eo_id, level, desc in eo_list:
        total_eos += 1
        keywords = eo_keywords.get(eo_id, [])
        found = sum(1 for kw in keywords if kw in content)
        coverage = found / max(len(keywords), 1)
        status = 'COVERED' if coverage >= 0.5 else 'PARTIAL' if coverage > 0 else 'MISSING'
        if status == 'COVERED':
            covered_eos += 1
        elif status == 'PARTIAL':
            covered_eos += 0.5
        icon = {'COVERED': 'pass', 'PARTIAL': 'warn', 'MISSING': 'FAIL'}[status]
        report.append(f'- [{icon}] **{eo_id}** ({level}): {desc} — {found}/{len(keywords)} keywords found')
        if status != 'COVERED':
            missing_kws = [kw for kw in keywords if kw not in content]
            issues.append(f'{eo_id}: missing keywords: {missing_kws}')

report.append(f'\n**EO Coverage: {covered_eos}/{total_eos} ({covered_eos/total_eos*100:.0f}%)**\n')

# 5.2 Key terms verification
report.append('\n## 5.2 Key Terms in Chapters and Glossary\n')
term_issues = []
for eu, terms in key_terms.items():
    content = eu_content(eu)
    report.append(f'\n### {eu}\n')
    for term in terms:
        in_chapter = term.lower() in content
        in_glossary = any(term.lower() in g for g in glossary_terms)
        status = 'pass' if (in_chapter and in_glossary) else 'warn' if in_chapter else 'FAIL'
        report.append(f'- [{status}] **{term}** — chapter: {"yes" if in_chapter else "NO"}, glossary: {"yes" if in_glossary else "NO"}')
        if not in_chapter:
            term_issues.append(f'{eu}: term "{term}" not found in chapter content')

# 5.3 Quiz question distribution
report.append('\n## 5.3 Quiz Question Distribution\n')
all_exam_content = '\n'.join(exams.values())
for eu in ['EU 1', 'EU 2', 'EU 3', 'EU 4', 'EU 5', 'EU 6', 'EU 7']:
    tag = eu.lower()
    count = all_exam_content.count(f"chapter: '{tag}'")
    report.append(f'- {eu}: {count} questions across both exams')

# Chapter quizzes
report.append('\n### Chapter Quiz Counts\n')
for fname, content in sorted(chapters.items()):
    quiz_count = content.count("text: '") - content.count("text: 'which")  # rough
    answer_count = content.count('answer:')
    report.append(f'- {fname}: ~{answer_count} quiz questions')

# Summary
report.append('\n## Summary\n')
report.append(f'- Educational Objectives: {covered_eos}/{total_eos} covered')
report.append(f'- Issues found: {len(issues) + len(term_issues)}')
if issues:
    report.append('\n### EO Issues\n')
    for i in issues:
        report.append(f'- {i}')
if term_issues:
    report.append('\n### Term Issues\n')
    for i in term_issues:
        report.append(f'- {i}')

output = '\n'.join(report)
outpath = r'D:\Projects\ireb_cpre_fl\validations\2026-05-27_v3.3.0\phase5-audit.md'
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(output)

print(f'Audit complete: {covered_eos}/{total_eos} EOs covered')
print(f'Issues: {len(issues) + len(term_issues)}')
print(f'Report saved to phase5-audit.md')
