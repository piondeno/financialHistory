#!/usr/bin/env python3
"""全書人名中文化：正文英文名 → 繁中慣用譯名，各章首次出現括註英文。

規則
- 只動正文：`來源：` 行與「參考來源」節、「」『』引文、（）括註內的內容一律不碰
  （書中人名多已成「中文名（English）」形，括號內留原文正是全書慣例）；標題層級要改
- 英文名相鄰處若還有英文字母或連字（Goldman Sachs、Volcker-era、J. K. Galbraith）→ 跳過，
  不把多字公司名、縮寫與複合詞拆開；全名與慣用詞寫進 FULL
- 各章首次被替換處加「中文（English）」；該章此前已出現中文形、或原文緊接括註者不加後者，
  改成把英文併進既有括號：「惠洛克（David Wheelock，聖路易斯聯準會）」
- 術語化暱稱（Greenspan put 等「X put」）與一次性學術引用名、公司機構、以人名命名的
  計畫案名（Smoot-Hawley、Teapot Dome）不入替換表

用法：tools/zh_names.py [--dry] [FILE|DIR ...]   預設 <repo>/chapters/*.md
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

# ── 英文姓 → 繁中慣用譯名（書內已有形者沿用書內形）─────────────────────────
SURNAME = {
    "Greenspan": "葛林斯班", "Volcker": "沃克", "Minsky": "明斯基", "Trump": "川普",
    "Nixon": "尼克森", "Bernanke": "柏南克", "Truman": "杜魯門", "Reagan": "雷根",
    "White": "懷特", "Carter": "卡特", "Yellen": "葉倫", "Connally": "康納利",
    "Powell": "鮑爾", "Boutwell": "鮑威爾",
    "Faisal": "費薩爾", "Keynes": "凱因斯", "Paulson": "保爾森", "Eichengreen": "艾肯格林",
    "Milken": "米爾肯", "Shiller": "席勒", "Geithner": "蓋特納", "Friedman": "弗里德曼",
    "Triffin": "特里芬", "Kennedy": "甘迺迪", "Krugman": "克魯曼", "Draghi": "德拉吉",
    "Biden": "拜登", "Baker": "貝克", "Romer": "羅默", "Silber": "席爾伯",
    "Dawes": "道威斯", "Young": "楊格", "Erhard": "艾哈德", "Wilson": "威爾遜",
    "Sadat": "沙達特", "Callaghan": "卡拉漢", "Khomeini": "霍梅尼", "Salinas": "薩利納斯",
    "Buffett": "巴菲特", "Obama": "歐巴馬", "Harris": "賀錦麗", "Polk": "波爾克",
    "Cleveland": "克利夫蘭", "Wicker": "威克爾", "Wheelock": "惠洛克", "Sinclair": "辛克萊",
    "Ferguson": "弗格森", "Ickes": "伊克斯", "Gallup": "蓋洛普", "Galbraith": "加爾布雷斯",
    "Dillon": "狄龍", "Kissinger": "季辛吉", "Witteveen": "威特芬", "Shah": "沙阿",
    "Campeau": "坎波", "Munger": "芒格", "Lula": "盧拉", "Ebbers": "艾伯斯",
    "Skilling": "斯基林", "Lay": "萊", "Blankfein": "布蘭克芬", "Schumer": "舒默",
    "Sanders": "桑德斯", "Warsh": "沃什", "Temin": "泰明", "Bordo": "博多",
    "Schwartz": "史華茲", "Kindleberger": "金德伯格", "Monteagle": "蒙特伊格",
    "Beeching": "比青", "Greider": "格雷德", "Colosio": "科洛西奧", "Soros": "索羅斯",
    "Hoover": "胡佛", "Stillman": "斯蒂爾曼", "Strong": "斯特龍", "Warburg": "沃伯格",
}
# ── 全名與慣用詞形（先於姓替換）───────────────────────────────────────────
FULL = {
    "de Gaulle": "戴高樂", "Charles de Gaulle": "夏爾·戴高樂", "Richard Nixon": "理查·尼克森",
    "Paul Volcker": "保羅·沃克", "Alan Greenspan": "艾倫·葛林斯班", "Ben Bernanke": "班·柏南克",
    "Janet Yellen": "珍妮特·叶倫", "Michael Milken": "麥可·米爾肯", "Huey Long": "休伊·朗",
    "Kevin Warsh": "凱文·沃什", "Martin Wolf": "馬丁·沃爾夫", "Kennedy Sr.": "老甘迺迪",
    "John F. Kennedy": "甘迺迪", "David Wheelock": "大衛·惠洛克", "Robert Triffin": "羅伯特·特里芬",
    "James Baker": "詹姆斯·貝克", "Robert Campeau": "羅伯特·坎波", "Milton Friedman": "米爾頓·弗里德曼",
    "Paul Krugman": "保羅·克魯曼", "Joseph Stiglitz": "約瑟夫·史迪格利茲", "Benjamin Strong": "班傑明·斯特龍",
    "Paul Warburg": "保羅·沃伯格", "Warren Buffett": "華倫·巴菲特", "Charlie Munger": "查理·芒格",
    "Irving Fisher": "愛爾文·費雪", "George Soros": "喬治·索羅斯", "Ted Lieu": "泰德·劉",
    "Jeffrey Skilling": "傑佛瑞·斯基林", "Bernie Sanders": "伯尼·桑德斯", "Chuck Schumer": "查克·舒默",
    "Robert Shiller": "羅伯特·席勒", "Hyman Minsky": "海曼·明斯基", "Ben Shalom Bernanke": "班·柏南克",
    "Taylor rule": "泰勒法則", "Volcker Rule": "沃克規則", "Triffin dilemma": "特里芬兩難",
    "Minsky moment": "明斯基時刻", "Minsky 時刻": "明斯基時刻", "Minsky Meltdown": "明斯基式崩盤",
    "Volcker shock": "沃克衝擊", "Volcker 衝擊": "沃克衝擊", "Keynesians": "凱因斯學派",
    "Keynesian": "凱因斯式",
}
# ── 術語化暱稱：整體保留英文，不動其中人名 ────────────────────────────────
KEEP = ["Greenspan put", "Yellen put", "Powell put", "Bernanke put", "Greenspan Put"]
# ── 書內已有的簡中慣例形 → 繁中慣用形 ─────────────────────────────────────
NORMALIZE = {"伯南克": "柏南克", "格林斯潘": "葛林斯班", "肯尼迪": "甘迺迪",
             "凱恩斯": "凱因斯", "沃克爾": "沃克"}

CJK = "一-鿿"
# ch17-20 正文寫的「鮑威爾」其實是 Fed 主席 Powell；ch04 的「鮑威爾」是財長
# Boutwell。書中替 Powell 另定「鮑爾」，所以這三章既有的中文也要一起改，ch04 不動。
ZH_POWELL = {"鮑威爾": "鮑爾"}
ZH_REWRITE = {f"ch{n}": ZH_POWELL for n in (17, 18, 19, 20)}
_CURRENT = {"file": ""}
CODE = re.compile(r"`[^`]*`")
QUOTED = re.compile(r"[「『][^」』]*[」』]|[「『][^」』]*$")
PAREN = re.compile(r"（[^）]*）|\([^)]*\)|（[^）]*$|\([^)]*$")
KEEP_PAT = re.compile("|".join(re.escape(k) for k in sorted(KEEP, key=len, reverse=True)))
REFHEAD = re.compile(r"^#{2,4}.*參考來源")
NAMES = {**FULL, **SURNAME}
_TOK: dict[str, str] = {}


def transform(text: str, stats: dict) -> str:
    out, glossed, in_ref = [], set(), False
    for line in text.split("\n"):
        if REFHEAD.match(line):
            in_ref = True
        # 一行可以有多個「來源：」（書中很常見）。只處理第一段，其餘原樣保留：
        # 用 head, *tail 再接 tail[0] 會把第二個來源之後的內容整段吃掉。
        parts = line.split("來源：")
        head = parts[0]
        if not in_ref:
            head = _line(head, glossed, stats, "\n".join(out))
            for cn, tw in NORMALIZE.items():
                if cn in head:
                    stats[cn] = stats.get(cn, 0) + head.count(cn)
                    head = head.replace(cn, tw)
            for zh, tw in ZH_REWRITE.get(_CURRENT["file"], {}).items():
                if zh in head:
                    stats[zh] = stats.get(zh, 0) + head.count(zh)
                    head = head.replace(zh, tw)
        out.append("來源：".join([head, *parts[1:]]))
    return "\n".join(out)


def _line(line: str, glossed: set, stats: dict, prior: str) -> str:
    global _TOK
    _TOK = {}
    used, glos = set(), []
    line = KEEP_PAT.sub(lambda m: _stash(m.group(0)), line)
    for pat in (CODE, QUOTED, PAREN):
        line = pat.sub(lambda m: _stash(m.group(0)), line)
    for eng in sorted(NAMES, key=len, reverse=True):
        line, hit = _apply(line, eng, NAMES[eng], glossed, stats, prior, glos)
        if hit:
            used.add(NAMES[eng])
    line = _restore(line)
    for zh in used:                                    # 替換造成的中文間多餘空白
        line = re.sub(rf"(?<=[{CJK}])[ \u00a0]+(?={re.escape(zh)})", "", line)
        line = re.sub(rf"(?<={re.escape(zh)})[ \u00a0]+(?=[{CJK}（）、，。：；「』])", "", line)
    for g in glos:
        # 注意這裡一定要用Lookbehind：寫成「g + 空白」會把整段括註吃掉
        # （Kevin Warsh 那樣的名字就這樣整團消失過）。
        line = re.sub(rf"(?<={re.escape(g)})[ \u00a0]+(?=[{CJK}（）、，。：；「』])", "", line)
        line = re.sub(rf"(?<=[{CJK}])[ \u00a0]+(?={re.escape(g)})", "", line)
    return line


def _apply(line: str, eng: str, zh: str, glossed: set, stats: dict, prior: str, glos: list):
    # 只看「左邊是不是另一個英文字的一部分」；中文緊貼英文名（在Trump）也要換，
    # 引號與括號內的已经在 _line 用 _stash 保掉了，不需要在這裡排除。
    pat = re.compile(rf"(?<![A-Za-z0-9·.]){re.escape(eng)}(?P<poss>'s|’s)?(?![A-Za-z\-])")
    hit = 0

    def rep(m: re.Match) -> str:
        nonlocal hit
        hit += 1
        tail = "的" if m.group("poss") else ""
        if eng in glossed:
            return zh + tail
        glossed.add(eng)
        if zh in prior:                                # 該章已用過中文名
            return zh + tail
        after = line[m.end():]
        mk = re.match(r"(\x00\d+\x00)", after)
        if mk:                                         # 緊接既有括號：英文併進括號內
            key, val = mk.group(1), _TOK.get(mk.group(1), "")
            if val.startswith("（") and val.endswith("）") and len(val) <= 36 \
                    and eng not in val and zh not in val and "\x00" not in val:
                _TOK[key] = f"（{eng}，{val[1:]}"
                return zh + tail
        glos.append(g := f"{zh}（{eng}）")
        return _stash(g) + tail

    new = pat.sub(rep, line)
    if hit:
        stats[eng] = stats.get(eng, 0) + hit
    return new, hit


def _stash(s: str) -> str:
    key = f"\x00{len(_TOK)}\x00"
    _TOK[key] = s
    return key


def _restore(s: str) -> str:
    for _ in range(8):
        s = re.sub(r"\x00(\d+)\x00", lambda m: _TOK.get(m.group(0), ""), s)
    return s


def _dangling(text: str) -> list[int]:
    """每行「開了沒關」的「／（數量。改名不該動到引號與括號的配對，
    所以前後不一致＝有內容被吃掉（來源： 那段就是這樣翻車的）。"""
    out = []
    for ln in text.split("\n"):
        b = ln.split("來源：")[0]
        out.append(max(0, b.count("「") - b.count("」")) + max(0, b.count("（") - b.count("）")))
    return out


def _cjk(line: str) -> int:
    return sum(1 for ch in line if "一" <= ch <= "鿿")


def _integrity(before: str, after: str) -> list[str]:
    bad = []
    # 改名只該「換字」或「加字」，不該讓中文字消失。
    # NORMALIZE／ZH_REWRITE 每處最多少 1 字，留 3 字余裕。
    for i, (a, b) in enumerate(zip(before.split("\n"), after.split("\n")), 1):
        if _cjk(a) - _cjk(b) > 3:
            bad.append(f"第 {i} 行中文字少 {_cjk(a) - _cjk(b)} 字")
    if "\x00" in after:
        bad.append("有沒還原的佔位符")
    if len(before.split("\n")) != len(after.split("\n")):
        bad.append("行數改變")
    if before.count("來源：") != after.count("來源："):
        bad.append("來源： 數改變")
    if _dangling(before) != _dangling(after):
        bad.append("有行的「／（變成未閉合，內容可能被吃掉")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="*", help="預設 <repo>/chapters/*.md")
    ap.add_argument("--dry", action="store_true", help="只列統計不寫檔")
    a = ap.parse_args()
    root = Path(__file__).resolve().parent.parent / "chapters"
    files: list[Path] = []
    for x in a.paths or [root]:
        p = Path(x)
        files += sorted(p.glob("ch*.md")) if p.is_dir() else [p]
    total = errors = 0
    for f in files:
        _CURRENT["file"] = f.name[:4]
        before = f.read_text(encoding="utf-8")
        stats: dict = {}
        after = transform(before, stats)
        bad = _integrity(before, after)
        n = sum(stats.values())
        total += n
        print(f"{f.name[:4]} {n:3d}  " +
              " ".join(f"{k}:{v}" for k, v in sorted(stats.items(), key=lambda kv: -kv[1])[:8]))
        if bad:
            print(f"     ✗ {'；'.join(bad)} → 這檔不寫入")
            errors += 1
            continue
        if not a.dry and after != before:
            f.write_text(after, encoding="utf-8")
    print(f"合計 {total} 處／{len(files)} 檔" + (f"；{errors} 檔完整性檢查失敗" if errors else ""))
    return 3 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
