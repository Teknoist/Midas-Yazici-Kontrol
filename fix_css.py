import re

with open('src/styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

target = r'\.top-actions \.primary-button \{ width: 38px; padding: 0; font-size: 0; \}'
replacement = r'.top-actions .primary-button { width: 38px; padding: 0; gap: 0; }\n  .top-actions .primary-button .btn-text { display: none; }'

content = re.sub(target, replacement, content)

with open('src/styles.css', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated CSS")
