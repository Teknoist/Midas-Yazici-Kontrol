import os

def fix_encoding(filepath):
    try:
        with open(filepath, 'rb') as f:
            raw = f.read()
            
        text = raw.decode('utf-8')
        
        # Test if text contains specific sequences using hex codes
        # 'Ä' is \xc3\x84 in latin1, which becomes \xc3\x83\xc2\x84 in double encoded
        # Wait, if text was double encoded, it would contain character U+00C4 (Ä)
        
        if '\u00c4' in text or '\u00c3' in text or '\u00c5' in text or '\u015e' in text or '\u011e' in text:
            try:
                original_utf8_bytes = text.encode('latin-1')
                fixed_text = original_utf8_bytes.decode('utf-8')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_text)
                print(f"Fixed: {filepath}")
            except Exception as e:
                pass
    except Exception as e:
        pass

for root, _, files in os.walk('electron'):
    for file in files:
        if file.endswith('.ts') or file.endswith('.tsx'):
            fix_encoding(os.path.join(root, file))

for root, _, files in os.walk('src'):
    for file in files:
        if file.endswith('.ts') or file.endswith('.tsx'):
            fix_encoding(os.path.join(root, file))
