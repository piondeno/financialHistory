#!/usr/bin/env python3
"""章節驗證腳本（spec §6）。

用法: verify_chapter.py FILE [FILE ...]
- 每檔: 去空白字數 >= 24000 且 9 個 H2 節齊全
- 渲染健檢: 同一行成對的「~」會被 GFM 當刪除線、未配對的「**」、
  「<」緊接字母（會被吃掉變成 HTML 標籤）
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
MIN_CHARS = 24000
FILENAME_RE = re.compile(r"^ch(\d{2})-(\d{4})-(\d{4})-.+\.md$")


def count_chars(text):
    """去除空白與 markdown 強調記號（*）後的字元總數（spec §6.1）。

    粗體記號 ** 不視為內容字元；「」（含引文）仍計入。
    """
    return len(re.sub(r"[\s*]", "", text))


def missing_sections(text):
    h2 = [ln for ln in text.splitlines() if ln.startswith("## ")]
    return [name for name in REQUIRED_SECTIONS if not any(name in ln for ln in h2)]


INLINE_CODE = re.compile(r"`[^`]*`")
TAG_LIKE = re.compile(r"<[A-Za-z/]")
FENCE = "```"


def render_issues(text):
    """markdown 渲染健檢，回傳 [(行號, 訊息)]。

    GFM 的刪除線延伸接受「單一」~（remark-gfm 預設 singleTilde），
    所以一行裡第二個 ~ 一出現，兩個 ~ 之間就成了刪除線內容：
    「1980-01~07、1981-07~1982-11」會把「07、1981-07」劃掉、
    純文字複製出來則黏成「1980-0107、1981-071982-11」。
    區間該寫「至」，約略該寫「約」。行內程式碼與圍欄不查。
    """
    out, in_fence = [], False
    for num, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith(FENCE):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        body = INLINE_CODE.sub("", line)
        if "~~" in body:
            out.append((num, "「~~」會渲染成刪除線"))
        elif body.count("~") >= 2:
            out.append((num, "同一行兩個「~」被 GFM 湊成刪除線，中間文字會被劃掉"))
        if body.count("**") % 2:
            out.append((num, "粗體 ** 未配對"))
        if TAG_LIKE.search(body):
            out.append((num, "「<」緊接字母會被當成 HTML 標籤"))
    return out


def check_file(path):
    text = path.read_text(encoding="utf-8")
    return count_chars(text), missing_sections(text), render_issues(text)


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
        n, missing, issues = check_file(path)
        ok = n >= MIN_CHARS and not missing and not issues
        print(f"{'PASS' if ok else 'FAIL'} {path.name}: "
              f"chars={n} (>= {MIN_CHARS}: {'ok' if n >= MIN_CHARS else 'too short'})")
        if missing:
            print(f"     缺少節: {missing}")
        for num, msg in issues:
            print(f"     渲染 第 {num} 行: {msg}")
        failed = failed or not ok
    for err in check_chain(Path(argv[0]).resolve().parent):
        print(f"FAIL chain: {err}")
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
