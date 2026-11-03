#!/usr/bin/env python3
"""修復 CommonMark 粗體失效：結尾 ** 前為標點、或起始 ** 為 intraword 時，在 ** 前後補半形空格。

CommonMark 的強調規則：
  - 結尾 ** 必須 right-flanking：其前不可為標點（全形 ） ， 。 」 也算標點）
  - 若 ** 前後都是字母/數字（intraword），不可用作強調
最通用的修法是讓 ** 外側出現空白。本腳本只做最小改動：在失效的 ** 前後各補一個半形空格。
"""
import re
import sys
import unicodedata
import glob

WS = set(' \t')
CODE = set('`')


def is_punct(ch):
    if not ch:
        return False
    if ch in '"\'':
        return True
    return unicodedata.category(ch)[0] in ('P', 'S')


def alnum(ch):
    return bool(ch) and (ch.isalnum())


def fix_line(line):
    """逐行處理（跳過列內程式碼 spans）。"""
    if '**' not in line:
        return line, 0
    # 找出行內 inline code 區間，這些區間內的 ** 不動
    code_spans = [(m.start(), m.end()) for m in re.finditer(r'`[^`]*`', line)]

    def in_code(i):
        return any(a <= i < b for a, b in code_spans)

    out = []
    i = 0
    n = 0
    while i < len(line):
        m = re.compile(r'\*\*(?!\s)(.+?)(?<!\s)\*\*', re.S).search(line, i)
        if not m or in_code(m.start()):
            out.append(line[i:])
            break
        s, e = m.start(), m.end()
        inner = m.group(1)
        prev = line[s - 1] if s > 0 else ''
        nxt = line[e] if e < len(line) else ''
        close_before = inner[-1]

        need = False
        # 結尾 ** 前為標點 → 需要空格在 ** 之後（讓其 right-flanking 成立）
        if is_punct(close_before):
            need = True
        # 起始 ** 前非空白/行首 且 前後皆為字母數字 → intraward，需要空格在 ** 之前
        if prev not in WS and prev and alnum(prev) and alnum(inner[0]):
            need = True

        if not need:
            out.append(line[i:e])
            i = e
            continue

        pre = '' if s == 0 or prev in WS else ' '
        post = '' if e == len(line) or nxt in WS else ' '
        out.append(line[i:s])
        out.append(pre)
        out.append(line[s:e])
        out.append(post)
        n += 1
        i = e
    return ''.join(out), n


def fix_text(text):
    lines = text.split('\n')
    out = []
    total = 0
    in_fence = False
    for ln in lines:
        if ln.lstrip().startswith('```'):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence:
            out.append(ln)
            continue
        new, n = fix_line(ln)
        out.append(new)
        total += n
    return '\n'.join(out), total


def count_bad(text):
    """統計仍然「結尾 ** 前為標點」的粗體 spans（粗估）。"""
    bad = 0
    for m in re.finditer(r'\*\*(?!\s)(.+?)(?<!\s)\*\*', text, re.S):
        if is_punct(m.group(1)[-1]):
            bad += 1
    return bad


def main():
    files = sys.argv[1:] or sorted(glob.glob('chapters/*.md'))
    grand = 0
    for f in files:
        t = open(f, encoding='utf-8').read()
        before = count_bad(t)
        new, n = fix_text(t)
        if new != t:
            open(f, 'w', encoding='utf-8').write(new)
        after = count_bad(new)
        grand += n
        print(f'{n:4d} 修正 | 標點結尾 {before:4d} -> {after:4d} | {f}')
    print('total insertions:', grand)


if __name__ == '__main__':
    main()
