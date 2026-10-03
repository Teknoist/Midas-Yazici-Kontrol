import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

target = r'<div className="brand"[^>]*>\s*<img[^>]*>\s*</div>'
replacement = '''<div className="brand" style={{ gap: '12px', padding: '24px 20px', display: 'flex', alignItems: 'center' }}>
            <img src="./logo.png" alt="Midas Logo" style={{ width: '40px', height: '40px', objectFit: 'contain' }} />
            <div style={{ whiteSpace: 'nowrap', display: 'flex', flexDirection: 'column' }}>
              <strong style={{ fontSize: '18px', fontWeight: '800', lineHeight: '1' }}>MİDAS</strong>
              <span style={{ fontSize: '11px', color: 'var(--soft)', fontWeight: '600', letterSpacing: '1px', textTransform: 'uppercase', marginTop: '2px' }}>TEKNOLOJİ</span>
            </div>
          </div>'''

content = re.sub(target, replacement, content)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated text logo")
