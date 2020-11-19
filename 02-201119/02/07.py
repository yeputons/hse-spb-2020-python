#!/usr/bin/env python3
import pathlib
from pathlib import Path

with open('a.txt', 'r') as f:
    print(f.read().split())

print(Path('a.txt').read_text().split())
print(pathlib.Path('a.txt').read_text().split())
# os.listdir/glob.glob/sys... old and uncozy.

with open('b1.txt', 'w', encoding='utf-8') as f:
    f.write('Привет!')
Path('b2.txt').write_text('Привет!', encoding='utf-8')
