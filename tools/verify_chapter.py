#!/usr/bin/env python3
"""章節驗證腳本（spec §6）。

用法: verify_chapter.py FILE [FILE ...]
- 每檔: 去空白字數 >= 20000 且 9 個 H2 節齊全
- 年份鏈: 以第一個檔案所在目錄視為 chapters/，解析 chNN-YYYY-YYYY-*.md，
  驗證相鄰章起年=前章迄年、ch01 起年=1837、ch20 迄年=2026
退出碼: 0=全通過, 1=有失敗, 2=用法錯誤
"""
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "本章摘要",
    "歷史背景",
    "投機的興起",
    "頂點與轉折",
    "崩潰與危機",
    "後續與制度變革",
    "深度分析",
    "評判與評斷",
    "關鍵數據表",
]
MIN_CHARS = 20000
FILENAME_RE = re.compile(r"^ch(\d{2})-(\d{4})-(\d{4})-.+\.md$")


def count_chars(text):
    """去除所有空白字元後的字元總數（spec §6.1）。"""
    return len(re.sub(r"\s", "", text))


def missing_sections(text):
    h2 = [ln for ln in text.splitlines() if ln.startswith("## ")]
    return [name for name in REQUIRED_SECTIONS if not any(name in ln for ln in h2)]


def check_file(path):
    text = path.read_text(encoding="utf-8")
    return count_chars(text), missing_sections(text)


def check_chain(chapters_dir):
    entries = []
    for p in sorted(Path(chapters_dir).glob("*.md")):
        m = FILENAME_RE.match(p.name)
        if m:
            entries.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), p.name))
    entries.sort(key=lambda e: e[0])
    errors = []
    for num, start, end, name in entries:
        if num == 1 and start != 1837:
            errors.append(f"ch01 起年應為 1837（實際 {start}）: {name}")
        if num == 20 and end != 2026:
            errors.append(f"ch20 迄年應為 2026（實際 {end}）: {name}")
    for (n1, _s1, e1, f1), (n2, s2, _e2, f2) in zip(entries, entries[1:]):
        if n2 != n1 + 1:
            errors.append(f"章號不連續: ch{n1:02d} 之後應為 ch{n1+1:02d}（實際 ch{n2:02d}）: {f2}")
        elif s2 != e1:
            errors.append(f"年份鏈斷裂: ch{n1:02d} 迄 {e1}，ch{n2:02d} 起 {s2}")
    return errors


def main(argv):
    if not argv:
        print("usage: verify_chapter.py FILE [FILE ...]", file=sys.stderr)
        return 2
    failed = False
    for arg in argv:
        path = Path(arg)
        if not path.is_file():
            print(f"FAIL {arg}: 檔案不存在")
            failed = True
            continue
        n, missing = check_file(path)
        ok = n >= MIN_CHARS and not missing
        print(f"{'PASS' if ok else 'FAIL'} {path.name}: "
              f"chars={n} (>= {MIN_CHARS}: {'ok' if n >= MIN_CHARS else 'too short'})")
        if missing:
            print(f"     缺少節: {missing}")
        failed = failed or not ok
    for err in check_chain(Path(argv[0]).resolve().parent):
        print(f"FAIL chain: {err}")
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
