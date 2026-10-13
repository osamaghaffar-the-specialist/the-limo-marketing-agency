from pathlib import Path
import re

text = Path('index.html').read_text(encoding='utf-8')
tags = re.findall(r'<img\b[^>]*>', text, flags=re.I | re.S)
print(f'IMG_COUNT={len(tags)}')
missing=[]
empty=[]
for i, tag in enumerate(tags, start=1):
    srcm = re.search(r'\bsrc\s*=\s*["\']([^"\']*)["\']', tag, flags=re.I)
    altm = re.search(r'\balt\s*=\s*["\']([^"\']*)["\']', tag, flags=re.I | re.S)
    src = srcm.group(1) if srcm else '(no src)'
    if not altm:
        missing.append((i, src, ' '.join(tag.split())))
    elif not altm.group(1).strip():
        empty.append((i, src, ' '.join(tag.split())))

print(f'MISSING_ALT_ATTRIBUTE={len(missing)}')
print(f'EMPTY_ALT_VALUE={len(empty)}')
for row in missing:
    print('MISSING', row)
for row in empty:
    print('EMPTY', row)
