# 第 18 章 研究筆記：疫情與史上最大貨幣擴張（2019-2020）

## 方法
- 語料 `/tmp/opencode/ch18/`（15 檔 en-wiki action=raw，~2.4MB）。核心：2020 stock market crash（300K）、2020 in the United States（280K）、2021 in the United States（280K）、COVID-19 pandemic in the United States（184K）、Paycheck Protection Program（169K）、Federal Reserve（151K）、CARES Act（130K）、United States federal budget（113K）、Quantitative easing（107K）、American Rescue Plan Act of 2021（102K）、Consolidated Appropriations Act 2021（98K）、2020 United States presidential election（453K）、S&P 500（19K）、2020/2021 US federal budget（15K/14K）。
- fetch 修正：「Coronavirus pandemic in the United States」→「COVID-19 pandemic in the United States」（redirect）；「NASDAQ」→「Nasdaq」（redirect，未再抓）；「2020/2021 in finance / economics / in the economy / in world events / in American politics」全數 404（用各年 US 條目 + crash 條目代替）；「United States stock market / 2020 stock market / 2021 stock market」404（用 crash + S&P 500 + 各年 US 條目代替）。
- 本章定位：2020 疫情是「流動性泡沫」（ch17）的極端形態——實體經濟崩塌（Q2 GDP -32.9% 年化、4 月失業 14.7%、2,310 萬人失業）與資產價格「脫鉤」（3/23 低點→3/24 +11%→2020 收盤雙創歷史新高；S&P 2021 +26.89%），靠「央行＋財政無限量印鈔」（12 個月內 >~$5.7T 財政＋Fed $700B→+$2T QE）。核心詞是**脫鉤（decoupling）**。
- 年份鏈：2019-12/2020-01（疫情）→ 2020-03（崩潰＋無限量印鈔）→ 2020 全年（V 形復甦）→ 2021（第二波＋疫苗＋資產再漲＋ARP $1.9T）。ch17 收於 2019 泡沫頂點，ch18 接 2019-12 疫情爆發。

## 投機標的主軸
- ch17「流動性／零利率下的資產價格本身」→ ch18「**無限量央行＋財政印鈔下的資產價格**」（流動性泡影的極限形態）。當「央行＋財政」同時「無限量」印鈔，投機標的不再是「流動性會流向哪裡」，而是「**印鈔會不會停**」——答案在 2020-2021 是「不會」，故資產價格與實體經濟**脫鉤**、數週 V 形復甦。
- 投機者再擴：(a) 選舉結果本身（2020-11-03、306-232、1/6 事件）；(b) **GameStop 逼空**（2021-01、股價較歷史低點漲 900 倍、1/28 券商限單）——投機標的**首次包含交易機制本身**（散戶 vs 對沖基金的槓桿結構）；(c) 債務上限本身（2021-10 61-38/50-48）。
- 收句橋接 ch19：2020-2021 的「無限量印鈔」堆出「萬物泡影」，2021 高通膨期開端（2021-2023）→ 2022 Fed 急升息刺破（見第十九章大輪動）。

## 關鍵事實（逐字取自語料）
### 疫情時間軸（COVID-19 pandemic in the United States）
- 首例：infobox arrival 1/13、正文 1/20 公布；2/2 對中旅行限制；2/6 最早死亡（57 歲女性、Santa Clara County）
- 3/11 WHO 宣布 pandemic；3/12 美國確診破 1,000；3/13 Trump 宣布國家緊急狀態；3/27 美國病例破 100,000
- 5/27 死亡破 100,000；6/11 病例破 200 萬；8/8 破 500 萬；9/22 死亡破 200,000；10/2 Trump 陽性；11/9 病例破 1,000 萬；12/8 破 1,500 萬；12/14 死亡破 300,000
- 2021：1/1 病例破 2,000 萬；2/22 死亡破 500,000；5/6 IHME 估實際死亡 >900,000；7/7 Delta 主導；9/20 死亡破 675,000（>1918 流感估）；10/1 死亡破 700,000；2022/5/4 死亡破 100 萬
- CDC 估計 1,231,440 人死亡；疫苗 2020-12 EUA、首批完整 FDA 批准 2021/8/23

### 2020 年 3 月崩潰（2020 stock market crash）
- 崩盤期間 2/20-4/7；崩前高點 infobox 2/12 vs 正文 2/19；2/28 10 年期 1.12%、30 年期 1.30%
- 3/3 FOMC 緊急降息 50bp
- 3/9 道瓊指數 -2,013.76（-7.79%、收 23,851.02）「Black Monday」；3/10 +4.9%（+1,167 點）；3/11 正式進熊市（11 年首次、史上最長牛市結束）
- 3/12 道瓊指數 -2,352.60（-9.99%、收 21,200.62）、跌 7.2% 觸發首個 circuit breaker、NY Fed 3/12-13 放貸 ≥$1.5T；3/13 +9%
- 3/15 Fed 降至 0-0.25%、準備金比率歸零、啟動 $700B QE
- **3/16 道瓊指數 -2,997.10（-12.93%、收 20,188.52）＝史上最大單日點數跌幅**（大於 1929）、VIX 收 82.69＝史上最高收盤、NY Fed $500B repo
- 3/17 +5%；3/18 道瓊指數跌破 20,000（該週第 4 次 breaker）、ECB €750B PEPP
- 3/23 道瓊指數「closed down 600 points after the government stimulus package failed again」、10 年期 0.82%、30 年期 1.34%
- 3/24 道瓊指數 +11%（1933 年來最佳）、Nasdaq +8%、S&P +9%；3/25 參院 96-0 通過 $2.2T；3/26 最大 3 連漲（1931 以來）
- 2/19-3/23：FTSE All-Share -33%、MSCI World -34%
- 2020 收盤：DJIA 30,606、S&P 500 3,756（雙創 all-time high）；MSCI ACWI 645
- S&P 500 月均（pandemic 檔）：2 月 3,277→3 月 2,652→4 月 2,762→…→11 月 3,694

### Fed / QE（Federal Reserve、Quantitative easing、2020 stock market crash）
- 3/3 緊急降息 50bp 至 1.00-1.25%；3/15 降至 0-0.25%（下界）、準備金歸零、QE4 ≈$700B
- 3/23 第二次緊急降息；「unlimited asset purchases」僅見 crash 檔 3/23 CNBC 引題（QE 檔/Fed 檔全文無「unlimited」）
- 流動性工具：PDCF（2020/3 創設）、CPFF（2020/3/17-2021/3/31）
- Fed 資產負債表（逐字取自語料）：2008 危機前 Fed 僅持 $700-800B 國債、QE1-3 累積 $4.5T 資產（2014-10-29）、QE4 至 2022 年中再增 $2T、2024/8 total $7.139T。（subagent 初報「2021/4/8 $7,708.88B」經 grep 不在語料，棄用）
- 國際：BOJ 2020/3/16 ETF 年度目標加倍 ¥12T；ECB 2020/3/18 €750B PEPP；BoE 峰值 £895B（2020-11）
- 2013 taper 先例：6/19 $85B→$65B/月、3 日 道瓊指數 -4.3%、-659 點（6/19-24）、收 14,660（Quantitative easing）
- 效果爭議：Greenspan 2012-07「very little impact」 vs Stein 2012-10「significant role」（Quantitative easing）

### 財政刺激（CARES Act、PPP、Consolidated Appropriations Act 2021、American Rescue Plan、2020/2021 US federal budget、United States federal budget）
- CARES Act $2.2T（≈GDP 10%、史上最大、大於 2009 ARRA $831B）、2020-03-27 簽署、參院 3/25 96-0；CBO 2020-2030 赤字 +$1.7T
  - 3/22 參院民主黨 47-47 擋案（需 60 票）→ 週一盤前 道瓊指數期貨觸停擺 -600 點（3/23 暴跌原因）；Rand Paul 陽性、另 4 名共和參議員隔離
  - 直接打款 $1,200/人、$2,400/夫妻、$500/17 歲以下小孩；FPUC +$600/週（3/27-7/26）；PEUC +13 週；120 天驅逐禁令（3/27-7/24）
- Consolidated Appropriations Act 2021：$2.3T（$900B 刺激＋$1.4T omnibus）、2020-12-27 簽署、5,593 頁（國會史上最长）；$600 支票 $166B、+$300/週至 2021-03-14（$120B）
- PPP：CARES 檔 $349B+$320B=$669B、PPP 檔 $953B（全 program）；單筆上限 $10M、最高 2.5×平均月薪、利率 1%；初始 $349B 4/3-4/16 全額放完（1.8M 筆、4,975 家機構、平均 $206,000、74% ≤$150K「Of all loans, 74 percent were for $150,000 or less」）；全 program ~11.8M 筆；每保存一個 job-year 成本 $169K-$258K（St. Louis Fed）、~3/4 資金流向收入最高五分位（Autor et al.）
- American Rescue Plan $1.9T、2021-03-11 簽署、PL 117-2；$1,400 打款；州/地方 $350B；學校 $130B；失業 $300B
- 前史：3/6 $8.3B、3/18 $192B Families First；4/21 參院 +$484B、4/24 簽署（新 PPP 申請 4/27 重啟）
- FY2020（budget 檔）：Revenue $3.420T（16.3%）、Expenditures $6.552T（31.3%）、Deficit $3.132T（15.0%）；FY2021：Revenue $4.046T、Expenditures $6.818T、Deficit $2.772T（12.4%）
- 債務：2019 79.4%→2020 **100.3% GDP（首次破 100%）**→2021 99.6%；$21.3T（2020/11）；2021-10-07/08 債務上限提高（參院 61-38/50-48）；2021-11-23 SPR 釋放 5,000 萬桶（史上最大）

### 資產 / 選舉 / 宏觀
- Apple 2020-08-19 首家市值 >$2T 美股公司（2020 in US）
- GameStop 逼空：2021-01-27 基金重大損失、股價較歷史低點漲 900 倍；1/28 多家券商限制交易（2021 in US）
- 2020 大選 2020-11-03：Biden/Harris 306 EV vs Trump/Pence 232；普選 81,283,501（51.31%）vs 74,223,975（46.85%）；總投票 158,429,631；投票率 66.8%（1900 年來最高）；12/14 Electoral College 306-232；2021-01-06 國會山騷亂
- Q1 2020 GDP -4.8% 年化；**Q2 2020 GDP -32.9% 年化（1945 有紀錄以來最劇烈）**；Q3 +33.1%
- 失業率（pandemic 檔月表）：2 月 3.5%→3 月 4.4%→**4 月 14.7%（大蕭條以來最高）**→5 月 13.3%→6 月 11.1%→7 月 10.2%→8 月 8.4%→9 月 7.9%→10 月 6.9%→11 月 6.7%
- 失業申請：3/26 單週 3,280,000（史上最大單週、破 1982 紀錄）；4/6 單月近 22,000,000 人；3 月中旬以來累計 33,000,000+
- 2020 收盤 S&P 500 3,756（all-time high）；S&P 2020 price +16.26%/total +18.40%；S&P 2021 price +26.89%/total +28.71%（S&P 500 檔）
- Nasdaq 2020「best annual return in 11 years」（僅引題，無具體 %）

## 矛盾裁定
1. **最大單日點數跌幅日期**：subagent 初判 -2,997.10（-12.93%、收 20,188.52）屬 **3/16**（crash 檔明載）；3/23 僅「closed down 600 points」→ 採 3/16 為最大單日跌幅，3/23 寫「因 $2.2T 救濟案再遭擋而再跌 ~600 點」。
2. **VIX 82.69 日期**：corpus 為 **3/16** 收盤（史上最高收盤）→ 採 3/16（非 3/12）。
3. **3/15 QE 規模**：corpus 三處（crash、QE 檔、CNBC 標題）皆 **$700B** → 採 $700B（非 $500B）；「unlimited」僅見 crash 檔 3/23 CNBC 引題 → 寫「3/23 Fed 宣布無限量買入（CNBC 引題）」，不寫成 QE 檔/Fed 檔明載。
4. **PPP 總額**：CARES 檔 $349B+$320B=**$669B** vs PPP 檔 **$953B**（全 program）→ 寫「PPP 初始 $349B、擴充後 $669B（CARES 口徑），全 program 最終 ~$953B（PPP 條目口徑）」，不用 $659B。
5. **2020 全年 GDP**：-3.5% NOT IN CORPUS → 改寫 Q1 -4.8% + Q2 -32.9% + Q3 +33.1%（年化），不寫全年 -3.5%。
6. **崩前高點**：infobox 2/12 vs 正文 2/19（同檔）→ 不寫確切崩前高點日，只寫「2 月中高點後開跌」。
7. **ARP 眾院通過日**：正文 line 70「2/26」vs line 36+infobox「2/27」（皆 219-212）→ 採 2/27（infobox 口徑）。
8. **疫情首例日**：infobox arrival 1/13 vs 正文 1/20（同檔）→ 寫「1 月中首例（1/20 公布）」。
9. **FY2020 %GDP**：2020 檔 16.3/31.3/15.0 vs federal budget 檔 CBO 表 16.2/31.1/14.9（微差）→ 採 2020 檔 15.0%。
10. **普選得票**：81,283,501/74,223,975（corpus）→ 用此值。

## NOT IN CORPUS（禁止使用）
- 2020 全年 GDP -3.5%（無；用 Q1 -4.8%/Q2 -32.9%/Q3 +33.1%）
- 2021 全年 GDP 數字（無）
- 2021 CPI 4.7%（無；僅 2021 檔稱 2021 為「period of high inflation (2021-2023)」開端）
- Bitcoin 2020 低點與 2021 ATH $64,863（無；ch18 不寫 BTC 具體價）
- 2021 道瓊指數/Nasdaq 全年回調具體數字（僅 S&P +26.89%、Nasdaq 引題「best annual return in 11 years」）
- 「4/13 最快復甦」（無；crash 檔 4/9 後跳至 6/11）
- S&P 500 3/23 收盤 2,385.14（無）
- 2020-2021 股票回購數據（無）
- 「everything bubble」一詞（無）
- 選後（11/3-4）市場反應（此 15 檔內無）
- Fed 資產負債表 2020 各月數字（僅 2021/4/8 $7,708.88B）

## 來源清單（15，待正文引用後對齊）
2020 in the United States；2021 in the United States；COVID-19 pandemic in the United States；CARES Act；Paycheck Protection Program；2020 stock market crash；Consolidated Appropriations Act, 2021；2020 United States federal budget；2021 United States federal budget；Federal Reserve；Quantitative easing；2020 United States presidential election；American Rescue Plan Act of 2021；S&P 500；United States federal budget。
