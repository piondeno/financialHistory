# 粗體（`**…**`）未渲染的原因與修法

## 症狀

原文寫 `**flight to liquidity（逃往流動性）**`，讀者看到的是字面的星號，不是粗體。全书 20 章共約 40 處直接失效、並因錯位波及更多。

## 原因：CommonMark 的分隔符規則

多數渲染器（GitHub、markdown-it、markdown-it-py、react-markify/remark、pandoc）實作 CommonMark。
它規定 `**` 要作為**結尾**分隔符，必須是 right-flanking：**前一個字元不能是標點**（Unicode P*／S*，全形 `）`、`，`、`。`、`」`、`：` 與 ASCII `)` 都算）。

實測（markdown-it-py，CommonMark preset）：

| 寫法 | 結果 |
|---|---|
| `**本幣**債務` | ✅ 粗體（結尾 `**` 後是 CJK 字） |
| `**flight to liquidity（逃往流動性）**爆發` | ❌ 不渲染：結尾 `**` 前是 `）` |
| `占比**20%**下滑` | ❌ 不渲染：intraword（`**` 前後都是字母/數字） |
| `名目**$1.25 兆美元**，後續` | ❌ 不渲染：結尾 `**` 前是 `）`（全形） |
| `名目 **$1.25 兆美元** 後續` | ✅ 粗體（`**` 外側有空白） |

注意：python-markdown 這類非 CommonMark 實作會照樣渲染，所以「本地測通過、站上卻壞掉」是常見的誤判來源。本書檢查一律用 CommonMark（`markdown-it-py`）。

## 修法（本書採用：最小改動）

在失效的 `**` 前後補一個半形空格，讓 `**` 外側出現空白，規則即成立：

```
**flight to liquidity（逃往流動性）**爆發
 → **flight to liquidity（逃往流動性）** 爆發
```

- 只補在需要的地方，不做全域加空格
- 已存在的空格不會重複補（可重複執行）
- 跳過程式碼柵欄與行內程式碼

## 工具

| 腳本 | 用途 |
|---|---|
| `tools/fix_bold_delimiters.py` | 批次修復（在失效 `**` 前後補半形空格） |
| `tools/check_bold_render.py` | 用 markdown-it-py 檢查各章未渲染的粗體 span；`--lines` 列出行號與原因 |

```bash
source ~/uvEnv/baseEnv/bin/activate
python3 tools/check_bold_render.py              # 摘要
python3 tools/check_bold_render.py --lines      # 定位到行
python3 tools/fix_bold_delimiters.py            # 修復全部 chapters/*.md
```

## 2026-10-30 執行結果

- 修復 767 處插入（20 章），修復後 `check_bold_render.py` 回報各章未渲染 0，2,070 對粗體全部渲染為 `<strong>`
- 未觸及表格行、未產生連續兩空格或行首空格

## 往後寫作建議

要粗體的片段，**不要把句末標點或全形括號放進 `**` 裡面**：

- `**光是活著就要付錢。**` → `**光是活著就要付錢**。`
- `**MBS（擔保抵押債權）**賣給` → `**MBS（擔保抵押債權）** 賣給`（或 `**MBS**（擔保抵押債權）賣給`）
- 數字夾在中文裡：`占比 **20%** 下滑`

寫完跑一次 `tools/check_bold_render.py` 即可。
