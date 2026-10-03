import os

replacements = [
    ("Nova 3D Printer Manager", "Midas Yazıcı Kontrol"),
    ("Nova-3D-Printer-Manager", "Midas-Printer-Control"),
    ("Nova Fleet", "Midas Yazıcı Kontrol"),
    ("nova-fleet", "midas-printer-control"),
    ("nova-3d-printer-manager", "midas-printer-control")
]

include_exts = {'.ts', '.tsx', '.json', '.html', '.md', '.css', '.js', '.xml', '.java', '.gradle', '.properties'}

for root, dirs, files in os.walk('.'):
    # Skip node_modules and .git (though we deleted them, just in case)
    if 'node_modules' in dirs: dirs.remove('node_modules')
    if '.git' in dirs: dirs.remove('.git')
    if 'build' in dirs: dirs.remove('build') # Don't touch binaries
    
    for file in files:
        if os.path.splitext(file)[1] in include_exts:
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                continue # Skip binary/weird files
            
            new_content = content
            for old, new in replacements:
                new_content = new_content.replace(old, new)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {path}")
