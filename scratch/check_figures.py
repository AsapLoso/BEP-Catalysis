import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('research/literature/schbib_1996_extracted_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'Figure \d.*', text):
    print(m.group(0))

for m in re.finditer(r'Figure 3\..*?(?=\n\n|\Z)', text, re.DOTALL):
    print("--- FULL FIG 3 ---")
    print(m.group(0))

for m in re.finditer(r'Figure 4\..*?(?=\n\n|\Z)', text, re.DOTALL):
    print("--- FULL FIG 4 ---")
    print(m.group(0))

