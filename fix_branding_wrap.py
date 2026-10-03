import re
with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()
target = '''            <div>
              <strong>MİDAS</strong>
              <span>YAZICI KONTROL</span>
            </div>'''
replacement = '''            <div style={{ whiteSpace: 'nowrap' }}>
              <strong>MİDAS</strong>
              <span style={{ fontSize: '10px' }}>YAZICI KONTROL</span>
            </div>'''
content = content.replace(target, replacement)
with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
