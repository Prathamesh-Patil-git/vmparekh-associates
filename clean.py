import re
with open(r'index.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'href=""https://themexriver\.com[^""]*""', 'href=""#""', text)
with open(r'index.html', 'w', encoding='utf-8') as f:
    f.write(text)
