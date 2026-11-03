#!/usr/bin/env python3
"""列出渲染後仍殘留字面 ** 的行（markdown-it 逐行渲染，方便定位）。"""
import glob
import re
import subprocess
import sys


def render(line):
    r = subprocess.run(['markdown-it'], input=line, capture_output=True, text=True)
    return r.stdout


def main():
    files = sys.argv[1:] or sorted(glob.glob('chapters/*.md'))
    for f in files:
        lines = open(f, encoding='utf-8').read().split('\n')
        hits = []
        fence = False
        for i, ln in enumerate(lines, 1):
            if ln.lstrip().startswith('```'):
                fence = not fence
                continue
            if fence or '**' not in ln:
                continue
            html = render(ln)
            html_no_code = re.sub(r'<code>.*?</code>', '', html, flags=re.S)
            if '**' in html_no_code:
                hits.append((i, ln))
        if not hits:
            continue
        print(f'=== {f}  ({len(hits)} 行)')
        for i, ln in hits:
            print(f'{i}: {ln[:220]}')
        print()


if __name__ == '__main__':
    main()
