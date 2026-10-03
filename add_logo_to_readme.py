with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = '<img src="public/logo.png" height="80" align="right" />\n\n' + content

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
