import re
with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace("maxWidth: '160px'", "maxWidth: '80px'")
with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated width")
