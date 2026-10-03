import re
with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('src="/logo.png"', 'src="./logo.png"')
with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed logo path in App.tsx")
