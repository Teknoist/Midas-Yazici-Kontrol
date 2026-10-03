import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

target = r'<div className="brand"[^>]*>\s*<img[^>]*>\s*<div[^>]*>\s*<strong>.*?</strong>\s*<span[^>]*>.*?</span>\s*</div>\s*</div>'
replacement = '''<div className="brand" style={{ padding: '16px 20px', display: 'flex', justifyContent: 'center' }}>
            <img src="./logo.png" alt="Midas Logo" style={{ width: '100%', maxWidth: '160px', height: 'auto', objectFit: 'contain' }} />
          </div>'''

content = re.sub(target, replacement, content)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated logo")
