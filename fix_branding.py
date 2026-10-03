import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

target = r'<div className="brand-mark">\s*<Boxes size=\{19\} />\s*</div>\s*<div>\s*<strong>NOVA</strong>\s*<span>FLEET</span>\s*</div>'

replacement = '''<img src="/logo.png" alt="Midas Logo" style={{ width: '40px', height: '40px', objectFit: 'contain' }} />
            <div>
              <strong>MİDAS</strong>
              <span>YAZICI KONTROL</span>
            </div>'''

content = re.sub(target, replacement, content)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
