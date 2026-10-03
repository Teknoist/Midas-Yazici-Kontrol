import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<Plus size={17} /> {tr("Yazıcı ekle", "Add printer")}', 
    '<Plus size={17} /> <span className="btn-text">{tr("Yazıcı ekle", "Add printer")}</span>'
)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated App.tsx")
