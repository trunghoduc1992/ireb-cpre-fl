"""Fix internal links and import paths after directory restructure."""
import os, re

DOCS = r'D:\Projects\ireb_cpre_fl\docs'

def fix_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# ── Fix v3 files (now at root): remove /v3/ prefix from links ──
v3_replacements = [
    ('(/v3/', '(/'),
    ("link: '/v3/", "link: '/"),
    ("link: /v3/", "link: /"),
]

# Fix v3 import paths: files moved UP one level (v3/chapters/ -> chapters/)
v3_import_fix = [
    ("from '../../.vitepress/theme/Quiz.vue'", "from '../.vitepress/theme/Quiz.vue'"),
    ("from '../../.vitepress/theme/ExamQuiz.vue'", "from '../.vitepress/theme/ExamQuiz.vue'"),
]

count = 0
for root, dirs, files in os.walk(DOCS):
    # Skip v2 directory for v3 fixes, skip .vitepress
    if 'v2' in root or '.vitepress' in root:
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        if fix_file(path, v3_replacements + v3_import_fix):
            count += 1
            print(f'  [v3->root] {os.path.relpath(path, DOCS)}')

# ── Fix v2 files (now at /v2/): add /v2/ prefix to internal links ──
# v2 links currently point to /chapters/..., /glossary, /study-plan, /exam-tips, /exams/...
# They need to become /v2/chapters/..., /v2/glossary, etc.
# BUT: links to external sites or /v3/ should NOT be changed

v2_link_patterns = [
    ('(/chapters/', '(/v2/chapters/'),
    ('(/exams/', '(/v2/exams/'),
    ('(/glossary)', '(/v2/glossary)'),
    ('(/study-plan)', '(/v2/study-plan)'),
    ('(/exam-tips)', '(/v2/exam-tips)'),
    ("link: /chapters/", "link: /v2/chapters/"),
    ("link: /exams/", "link: /v2/exams/"),
    ("link: /glossary", "link: /v2/glossary"),
    ("link: /study-plan", "link: /v2/study-plan"),
    ("link: /exam-tips", "link: /v2/exam-tips"),
]

# Fix v2 import paths: files moved DOWN one level (chapters/ -> v2/chapters/)
v2_import_fix = [
    ("from '../.vitepress/theme/Quiz.vue'", "from '../../.vitepress/theme/Quiz.vue'"),
    ("from '../.vitepress/theme/ExamQuiz.vue'", "from '../../.vitepress/theme/ExamQuiz.vue'"),
]

for root, dirs, files in os.walk(os.path.join(DOCS, 'v2')):
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        if fix_file(path, v2_link_patterns + v2_import_fix):
            count += 1
            print(f'  [v2->/v2/] {os.path.relpath(path, DOCS)}')

# ── Fix v2 index.md link to v3 ──
v2_index = os.path.join(DOCS, 'v2', 'index.md')
if os.path.exists(v2_index):
    # The v2 index had a link to /v3/ which should now be /
    fix_file(v2_index, [('(/v3/)', '(/)')])

print(f'\nFixed {count} files')
