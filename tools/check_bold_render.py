#!/usr/bin/env python3
"""檢查各章 **粗體** 是否真的渲染成粗體（CommonMark 規則），並列出失效的行。

用法：
  python3 tools/check_bold_render.py                # 摘要（全部 chapters/*.md）
  python3 tools/check_bold_render.py --lines        # 同時列出行號與原文
  python3 tools/check_bold_render.py --lines f.md   # 只查指定檔案

原因（CommonMark delimiter rules）：
  1. 結尾 ** 前一個字元是標點（含全形 ）｜，｜。｜」｜： 等 Unicode P*／S*）時，
     該 ** 不是 right-flanking，不能作為結尾分隔符 → 整段不渲染。
  2. ** 前後都是字母／數字（intraword，例如 `占比**20%**下滑`）時，不能用作強調。
  3. 開頭或結尾 ** 內側緊貼空白，也不是有效分隔符。
修法（本倉庫採用的最小改動）：在失效的 ** 前後補一個半形空格。
"""
import glob
import re
import sys
import unicodedata

from markdown_it import MarkdownIt

md = MarkdownIt('commonmark')


def is_punct(ch):
    if not ch:
        return False
    if ch in '"\'':
        return True
    return unicodedata.category(ch)[0] in ('P', 'S')


def bad_reason(inner, prev, nxt):
    """回傳該 **...** span 在 CommonMark 下失效的原因（None 表示沒問題）。"""
    if not inner:
        return '空內容'
    if is_punct(inner[-1]):
        return f'結尾 ** 前是標點「{inner[-1]}」'
    if prev and prev not in ' \t' and prev.isalnum() and inner[0].isalnum():
        return f'intraword（前為「{prev}」）'
    return None


def find_failures(text):
    """回傳 [(line_no_1based, reason, line_text)]。"""
    tokens = md.parse(text)
    src_lines = text.split('\n')
    out = []
    for t in tokens:
        if t.type != 'inline' or not t.children:
            continue
        line = t.map[0] if t.map else None
        kids = t.children
        for i, c in enumerate(kids):
            if c.type != 'text' or '**' not in (c.content or ''):
                continue
            # 對這段文字裡的每個 ** 配對，判斷原因
            content = c.content
            for m in re.finditer(r'\*\*(?!\s)(.+?)(?<!\s)\*\*', content, re.S):
                prev = content[m.start() - 1] if m.start() > 0 else (
                    kids[i - 1].content[-1:] if i > 0 and kids[i - 1].content else '')
                nxt = content[m.end()] if m.end() < len(content) else ''
                r = bad_reason(m.group(1), prev, nxt)
                if r:
                    out.append((line + 1 if line is not None else 0, r, m.group(0)))
            # 單個 **（沒有配對）通常是跨行或被前項吃掉，一併回報
            if len(re.findall(r'\*\*', content)) % 2 == 1:
                out.append((line + 1 if line is not None else 0, '未配對的 **', content[:120]))
    return out


def count_src_pairs(text):
    return text.count('**') // 2


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    show_lines = '--lines' in sys.argv
    files = args or sorted(glob.glob('chapters/*.md'))
    tot_bad = 0
    for f in files:
        text = open(f, encoding='utf-8').read()
        fails = find_failures(text)
        tot_bad += len(fails)
        flag = 'OK ' if not fails else '!! '
        print(f'{flag}{f}: 原始 {count_src_pairs(text):4d} 對 | 未渲染 {len(fails)}')
        if show_lines:
            src = text.split('\n')
            seen = set()
            for ln, reason, frag in fails:
                if ln in seen:
                    continue
                seen.add(ln)
                print(f'    L{ln}: [{reason}]')
                print(f'      {src[ln - 1][:200] if ln <= len(src) else ""}')
    print(f'\n合計未渲染粗體 span：{tot_bad}')


if __name__ == '__main__':
    main()
