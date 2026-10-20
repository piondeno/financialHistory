#!/usr/bin/env python3
"""中英夾雜掃描器：抓「未經定義就夾在中文裡的英文詞」。

用法:
    scan_codeswitch.py [FILE|DIR ...] [--show N] [--count-only]

    不給參數 → 掃 <repo>/chapters/*.md
    給目錄    → 掃該目錄下的 *.md
    給檔案    → 只掃那些檔案（可混給多檔）

    --show N      每個詞最多列幾處上下文（預設 2）
    --count-only  只列「詞＋次數」，不列上下文

判定規則（與全書文字規則一致）：英文只能出現在
    1. 「」／『』引文內
    2. `來源：` 引用行內
    3. （）括註內
    4. 首次出現即附中文括註（`xxx（中文定義）`）或以「，即／，此指／，就是／，指的是」引出定義
    5. 專有名詞與縮寫（首字母大寫者、長度 <3 的詞）一律豁免
其餘「中文夾層裡的小寫英文詞」視為待處理，依上下文逐詞人工分級。

合法術語表（allowlist）一律從全書 `chapters/` 建立，即使只掃單一章——
任何術語只要在書中某處加過中文括註，即全書放行。
已知取捨：也因此會**低估重複使用**（同一術語只在首次附註時，後續不重複報）。
本工具抓的是「未定義就使用」，不是「使用太多次」。

退出碼: 0=無待處理命中, 1=有命中, 2=用法錯誤
"""
import argparse
import collections
import re
import sys
from pathlib import Path

CJK = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf]")
TOKEN = re.compile(r"[A-Za-z][A-Za-z'’\-\.]*[A-Za-z]")
# 緊接中文括註／中文定義引出的英文 → 視為已定義
GLOSS = re.compile(
    r"((?:[A-Za-z][A-Za-z'’\-\.]*\s+){0,6}[A-Za-z][A-Za-z'’\-\.]*)"
    r"\s*(?:（[^）\n]*[\u4e00-\u9fff][^）\n]*）|，(?:即|此指|就是|指的是)[^，。；\n]*[\u4e00-\u9fff])"
)
QUOTED = re.compile(r"「[^」]*」|『[^』]*』")
SRC = re.compile(r"來源：.*$")
PAREN = re.compile(r"（[^）\n]*）|\([^)\n]*\)")


def chapters_dir():
    """<repo>/chapters，供建立全書合法術語表。"""
    return Path(__file__).resolve().parent.parent / "chapters"


def expand(targets):
    """把檔名／目錄參數展開成 md 檔清單。"""
    files = []
    for arg in targets:
        p = Path(arg)
        if p.is_dir():
            files.extend(sorted(p.glob("*.md")))
        elif p.is_file():
            files.append(p)
        else:
            print(f"錯誤: 路徑不存在: {arg}", file=sys.stderr)
            return None
    return files


def add_phrase(allowlist, phrase):
    for tok in TOKEN.findall(phrase):
        if len(tok) >= 2:
            allowlist.add(tok.lower())


def build_allowlist(corpus):
    """全書合法術語表：括註、「」引文、來源行、（）註解內的英文。"""
    allow = set()
    for path in corpus:
        for line in path.read_text(encoding="utf-8").splitlines():
            for m in GLOSS.finditer(line):
                add_phrase(allow, m.group(1))
            for q in QUOTED.findall(line):
                add_phrase(allow, q)
            for s in SRC.findall(line):
                add_phrase(allow, s)
            for p in PAREN.findall(line):
                add_phrase(allow, p)
    return allow


def scan(path, allow, limit):
    """回傳 {小寫詞: {"n": 次數, "where": [上下文, ...]}}。"""
    hits = collections.defaultdict(lambda: {"n": 0, "where": []})
    name = path.name.split("-")[0]
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        scanline = SRC.sub("", line)
        scanline = QUOTED.sub(lambda m: "＊" * len(m.group(0)), scanline)
        for m in TOKEN.finditer(scanline):
            tok = m.group(0)
            low = tok.lower()
            if len(tok) < 3 or low in allow:
                continue
            if tok != low:  # 首字母大寫：專有名詞／標題
                continue
            around = scanline[max(0, m.start() - 3):m.start()] + scanline[m.end():m.end() + 3]
            if not CJK.search(around):  # 未緊貼中文 → 純英文術語串
                continue
            hit = hits[low]
            hit["n"] += 1
            if len(hit["where"]) < limit:
                lo = max(0, m.start() - 18)
                hi = m.end() + 14
                hit["where"].append(f"{name}:{lineno} …{scanline[lo:hi].strip()}…")
    return hits


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="scan_codeswitch.py",
        description="抓未經定義就夾在中文裡的英文詞",
        epilog="合法術語表取自全書 chapters/；退出碼 0=乾淨, 1=有命中, 2=用法錯誤",
    )
    parser.add_argument("targets", nargs="*", metavar="FILE|DIR", help="預設 <repo>/chapters/*.md")
    parser.add_argument("--show", type=int, metavar="N", default=2, help="每詞最多列幾處上下文（預設 2）")
    parser.add_argument("--count-only", action="store_true", help="只列詞與次數")
    args = parser.parse_args(argv)

    files = expand(args.targets) if args.targets else sorted(chapters_dir().glob("*.md"))
    if files is None:
        return 2
    if not files:
        print("錯誤: 找不到任何 .md", file=sys.stderr)
        return 2

    limit = max(1, args.show)
    base = chapters_dir()
    corpus = sorted(base.glob("*.md")) if base.is_dir() else files
    allow = build_allowlist(corpus)

    total = collections.defaultdict(lambda: {"n": 0, "where": []})
    for path in files:
        for low, hit in scan(path, allow, limit).items():
            total[low]["n"] += hit["n"]
            room = limit - len(total[low]["where"])
            if room > 0:
                total[low]["where"].extend(hit["where"][:room])

    ordered = sorted(total.items(), key=lambda kv: -kv[1]["n"])
    for low, hit in ordered:
        if args.count_only:
            print(f"{hit['n']:>3}  {low}")
        else:
            print(f"{hit['n']:>3}  {low}  |  " + "  ||  ".join(hit["where"]))
    spots = sum(h["n"] for h in total.values())
    print(f"\n{len(files)} 檔／{len(ordered)} 詞／{spots} 處"
          f"（合法表 {len(allow)} 詞，取自 {len(corpus)} 檔）")
    return 1 if spots else 0


if __name__ == "__main__":
    sys.exit(main())
