# ch16 研究筆記：大金融海嘯（2007-2012）

## 方法
- 語料：/tmp/opencode/ch16/（46 檔 en-wiki action=raw，~4.7MB）。核心：2008 financial crisis（271K）、Subprime mortgage crisis（316K）、Great Recession（132K）、Eurozone crisis（325K）、Greek government-debt crisis（233K）、AIG（111K）、Lehman（95K）、Washington Mutual（192K）、TARP（80K）、QE（107K）、Dodd–Frank（96K）、ARRA（108K）、CDS（127K）、2011 debt-ceiling crisis（111K）、ECB（214K）、S&P Global Ratings（34K）、FCIC（41K）、Too big to fail（68K）、Moral hazard（46K）、Systemic risk（46K）、Euro（111K）、ESM/EFSF、Bernanke/Paulson/Geithner、FOMC、Fed、US/global 年度檔 2008-2012。
- 重定向修正：European sovereign-debt crisis→Eurozone crisis（2026-10 複查：原目標 Euro area crisis 已改為重定向）；Standard & Poor's→S&P Global Ratings；Dodd-Frank Act→Dodd–Frank Act（en-dash）；IndyMac Bank→IndyMac；Global financial crisis→2008 financial crisis；2011 US debt ceiling→2011 US debt-ceiling crisis。
- subagent 事實清單（task，環境保留）＋主 agent grep 抽驗（6,469.95/14,164/613B/182.3/225–208/440B/whatever it takes/53.5/250,000/10.0%/12.7%/15.4%/1.75T/2.1T/62.2T/$600B 全確認）。

## 矛盾裁定（寫作用）
1. 衰退時長 19 vs 18 個月 → 採 NBER「2007-12 起、2009-06 谷底」事實，不寫月數或註「約 18 個月」。
2. 衰退起點 late/mid-2007 → 以 NBER「December 2007」為準。
3. AIG 救濟 $85B（9/16 首次）→ $182.3B（最終、常稱 $180B；還款 $205B、獲利 $22.7B）→ 寫「$85B 起、最終 $182.3B」。
4. QE1 口徑：初始 MBS 目標 $600B（11/25 2008）→ 2009-03 持有 $1.75T → 2010-06 峰 $2.1T →「注入金融體系 >$4T（含後續 QE）」；Bernanke「$1.3T（2008-11~2010-06）」口徑不同 → 分標。
5. TARP：授權 $700B（10/3）；已分配 $467B/已花 $416B（2012-06）；CBO 2024 最終 disbursements $443.5B、subsidy cost $31.1B；TARP+GSE 合計流出 $620.3B → 依時間點引。
6. ARRA $787B（通過時）→ $831B（2009-2019 修訂）→ 屬修訂，寫「$787B（後修訂 $831B）」。
7. WaMu 接管 9/25（WAMU+2008F 一致；9/26 為控股公司破產日）→ 採 9/25。
8. 希臘 2011 GDP -7.1%（Eurostat）vs -6.9%（EC）→ 採 Eurostat 7.1%。
9. Countrywide 收購 $4.1B（宣布案值）vs $2.5B（Reuters factbox）→ 採 $4.1B（BofA 2008-01-11 全股票案值）。
10. Lehman 申請 9/15（通說；CDS 檔作 9/14）→ 採 9/15（凌晨前申請、15 日生效）。
11. Fed 利率：5.25%→0.0%（非 6.25%）；FOMC 2007-09-18 自 5.25% 峰開始降息；2008-01-22 單次 75bp。
12. S&P 降級：AAA→AA+（2011-08-05，非 Aaa→Aa1 那是 Moody's 口徑）。
13. ESM = 最大貸出 €500B（2012-09-27 成立）；防火牆 €750B = EFSF €440B + EFSM €60B + IMF €250B（非「ESM €700B」）。
14. 未遂買家 = **Barclays**（非 Bank of China；Paulson/Geithner 力促 Barclays 收購 Lehman、英監管否決）。
15. 2008-08-05 降級當日：NASDAQ/ASX/S&P 100 最多 -4%；8/8 道瓊指數 -635 點（-5.6%）→ 以語料數字。
16. Bear 槓桿 35.6:1（2007 底）；FCIC 對五大投行「as high as 40 to 1」→ 分標（Bear 35.6:1、五大投行最高 40:1）。
17. AIG 無「40:1」、無「$850B Fed 承諾」→ 不寫。

## NOT IN CORPUS（禁止引用）
AIG $850B、AIG 40:1、QE1 $2.25T、Bernanke「$18T 全球救濟」、Bain「$2.2T Lehman 衝擊」、Bank of China 競購 Lehman、S&P 500 谷底 676.53（2009-03-09）、IndyMac 資產出售價、Bernanke taper 暗示（2013-06）、PIIGS 縮寫定義、希臘 CDS 具體 bps（僅「Greek/German yield spread >1,000 bps」2010-04-28）、2011-08-05 道瓊指數單日 % 跌幅（僅 8/8 -635/-5.6%）。

## §1 本章摘要
- 大金融海嘯 = 2007-09 美國次貸引爆的系統性金融危機 + 2009-2012 復甦改革 + 2010-2012 歐洲主權債務危機（危機「回歸」為主權/歐元區危機）。
- 投機標的：接 ch15「信用/信貸本身」→ 本章擴為「**系統性槓桿與主權信用**」——槓桿 40:1（五大投行）、CDS $62.2T、影子銀行 $10T；危機從美國信貸蔓延到歐洲主權債務（希臘赤字 6-8%→15.4%、€110B/€130B、53.5% haircut）。
- 主事件：Lehman 9/15（$613B 債、史上最大破產）、AIG（$85B→$182.3B）、TARP $700B（眾院 225-208 否決後 10/3 通過）、QE1（$600B→$1.75T→$2.1T）、ARRA $787B、衰退（NBER 2007-12~2009-06、失業 10%（2009-10）、道瓊指數 14,164→6,469.95（2009-03-06）-53%）、Dodd-Frank（2010-07-21）、希臘（€110B 2010、€130B 2012、53.5% haircut）、Draghi「whatever it takes」（2012-07-26）、S&P 降級美國（2011-08-05、AAA→AA+）。

## §2 歷史背景：2007-08 危機點火與蔓延
- 2.1 次貸引爆與 2007 蔓延：次貸 $35B(1994,5%)→$600B(2006,20%)、$1.3T(2007-03)、option ARM 1/10、teaser rate <4%、2007 40% 自動化核貸；HSBC 2007-02-08 壞帳 $10.5B（首個大規模 subprime 損失）；>100 家房貸機構倒閉（New Century）；2008-01-21 全球股市暴跌、2008-02-05 S&P -3.2%/道瓊指數 -370。
- 2.2 Bear Stearns 兩基金（2007-06-20 救、涉 $20B CDO；7/31 清算）＋ BNP Paribas 8/9「流動性完全蒸發」$2.2B → 危機從「零售」轉「批發」。
- 2.3 倒閉潮：IndyMac（7/11 接管、$32B、股價 $50→$0.44）、WaMu（$307B、9 天提走 $16.7B、9/25 接管、$1.9B 售 JPM）、Wachovia（$23.9B 虧、Wells Fargo $15.1B 全股票）、Countrywide（BofA $4.1B）。
- 2.4 2008 上半年：Fed 2008-01-22 單次 75bp（25 年最大、2001 以來首次緊急）；FOMC 2007-09-18 自 5.25% 開始降息；2008-03-14 Bear 獲 FRBNY $25B/Maiden Lane 買 $30B 資產、JPM $2/股（後 $10）。

## §3 投機的興起：信貸/衍生物投機狂熱
- 3.1 槓桿與影子銀行：五大投行 FY2007 債 >$4.1T（~30% GDP）、Bear 35.6:1、五大投行最高 40:1；影子銀行（SIV $2.2T、repo $2.5T、對沖基金 $1.8T、五大投銀 $4T、整體 ~$10T）。
- 3.2 CDS 與毒資產：CDS $3.7T(2003)→$62.2T(2007)→$38.6T(2008)→$26.3T(2010)；Lehman 債務 $155B 但 CDS 名目 ~$400B；OTC 衍生 $673T；評級 AAA 錯位、無中央清算。
- 3.3 「最後的平靜」與 Minsky：Ponzi 融資的房貸/CDO，Minsky 的 hedge→speculative→Ponzi 已到頂；$70T 可投資資金（Giant Pool of Money）；2008-09 前一切「穩定」＝最大風險。

## §4 頂點與轉折：2008-09 崩潰高潮
- 4.1 Lehman Brothers 9/15：$613B 債/$155B 公司債/$639B 資產、史上最大破產；未遂 Barclays 收購（英監管否決）；Paulson 怕「Mr. Bailout」標籤；Goldman/CS 估其淨值負。
- 4.2 AIG：Fed 9/16 以 $85B 接手（CDS 過度賣保護、損失 >$100B）→ 最終 $182.3B（還款 $205B、獲利 $22.7B）；FCIC「cascading losses」。
- 4.3 TARP 政治：9/29 眾院 225-208 否決 EESA（道瓊指數 -777.68/-6.98%、史上最大點數；金 $900）；9/20 Paulson「heaven help us all」；10/1 參院、10/3 眾院通過、Obama 簽 → $700B TARP。
- 4.4 Minsky moment：批發式恐慌（Gorton「wholesale panic not retail panic」、repo 不展期）；2008-09-07 Fannie/Freddie 接管（$200B 設施）；2008-10-07 存款保險 $100K→$250K。

## §5 崩潰與危機：救市與衰退
- 5.1 Fed 與 TARP 救市：5.25%→0；QE1（11/25 2008、$600B MBS→2009-03 $1.75T→2010-06 $2.1T 峰）；TARP 用途（CPP $204.9B、AIG $67.8B、汽車 $79.7B、Citi/BofA 各 $20B）；存款保險 $250K。
- 5.2 衰退谷底：NBER 2007-12~2009-06（2008-12-01 宣布、道瓊指數 -680）；失 8.7M 工、失業 5%→10%（2009-10、1983 以來最高）；道瓊指數 14,164(2007-10-09)→6,469.95(2009-03-06) -54%；家庭淨值 -$11.5T；貧窮 12.5%→15.1%。
- 5.3 全球蔓延：2009Q1 年化 GDP 德 -14.4%/日 -15.2%/UK -7.4%/拉脫 -18%/歐元區 -9.8%/墨 -21.5%；UK RBS 救市（Darling「離失序僅數小時」）；IMF「自 1930 大蕭條以來最嚴峻」。
- 5.4 規模與代價：一戶四失 75% 淨值；2011 家庭財富中位數 -35%（$106,591→$68,839）；「最嚴重 since 大蕭條」。

## §6 後續與制度變革：復甦、改革與歐洲主權危機
- 6.1 復甦與 ARRA：2009-02-17 簽 ARRA $787B（後 $831B）；2009-06 衰退結束但失業 9.5%；2010 Q1 房貸逾期峰 11.54%；QE2（2010-11-03、$600B 國債）；2010-12 失業 9.3%。
- 6.2 Dodd-Frank（2010-07-21）：CFPB、FSOC、Orderly Liquidation Authority、Volcker Rule、衍生工具中央清算；「one of the most significant financial laws since the New Deal」。
- 6.3 歐洲危機點火（希臘）：2009 末赤字揭露 6-8%→12.7%→15.4%、債務 113%→127% GDP；Goldman FX swap 隱匿債務；2010-05-01/03 Troika €110B（5.5%）、降 junk；2010-05-05 三人死。
- 6.4 歐洲蔓延與收束：愛爾蘭（2010-11）、葡萄牙（2011-05）、西班牙（Bankia €19B 2012-05、EFSM €100B 2012-06）、塞浦勒斯（2012-06）；EFSF €440B→€780B、ESM €500B（2012-09-27）、防火牆 €750B；LTRO €489B（2011-12-22）；2012-07-26 Draghi「whatever it takes」、9/6 OMT → 危機收束；2012 歐元區失業 11.6%。
- 6.5 美國降級：2011-08-05 S&P 降 AAA→AA+（首次、1917 以來）、debt ceiling（BCCA 8/2）、sequestration；2012 底 fiscal cliff 和解。

## §7 深度分析
- 7.1 Minsky 與去槓桿：Minsky meltdown、paradox of deleveraging（Yellen 2009-04-16）、批發式恐慌（Gorton）。
- 7.2 too-big-to-fail 與 moral hazard：五大投行結局（Lehman 破/Bear+Merrill 火賣/Goldman+Morgan 轉銀行）；Schweikhard 隱性補貼省 $120B（Citi $53B/BofA $32B）；Stiglitz「too big to fail are too big to exist」；moral hazard（LTCM 1998 先例、FCIC 認定）；Greenspan put→Bernanke put。
- 7.3 FCIC 與投機標的：FCIC「21 世紀金融體系、19 世紀保障」、五大原因、30 年去管制（Greenspan）、2000 OTC 衍生去管制轉折點；投機標的從「信用/信貸」擴為「系統性槓桿 + 主權信用」（危機從美國信貸回歸為歐洲主權/歐元區危機）。

## §8 評判與評斷（七）
1. Lehman 是「不救」的實驗：Fed 選擇讓 Lehman 破產（避免 Mr. Bailout），結果證明 too-big-to-fail 無法選擇性執行——救 AIG、Fannie 卻不救 Lehman，只加劇恐慌（FCIC）。
2. 危機是「批發式」而非「零售式」恐慌（Gorton）：儲戶沒跑、金融機構 repo 互跑——2008 與 1930 的根本差異。
3. TARP 的政治劇：225-208 否決日 道瓊指數 -777，是「信心」崩潰的極端；政治程序本身成為系統風險。
4. 救市規模史無前例：TARP $700B + GSE + QE（$1.75T→$2.1T）+ ARRA $787B；「self-inflicted」但避免了大蕭條重演（IMF）。
5. Dodd-Frank 是「19 世紀→21 世紀」的制度補丁：CFPB/FSOC/Volcker/清算，但 2018 已部分回滾。
6. 歐洲主權危機 = 危機的「回歸」：銀行救市把私人債務轉為主權債務（EURC），無匯率貶值工具（共享歐元）讓危機無法「內部貶值」——主權信用成為新的投機標的。
7. 本章是 ch17（零利率、QE、資產泡沫 2012-2019）的開場：零利率 + QE 持續、歐洲危機收束但「低成長/低利率」時代開始，資產泡沫在低利率下重燃。

## §9 來源（待引用對齊後定稿，預計 ~28 條）
2008 financial crisis / Great Recession / Subprime mortgage crisis / Bear Stearns / Lehman Brothers / American International Group / Washington Mutual / Wachovia / IndyMac / Troubled Asset Relief Program / Quantitative easing / Dodd–Frank Act / American Recovery and Reinvestment Act of 2009 / Eurozone crisis / Greek government-debt crisis / Credit default swap / Too big to fail / Moral hazard / Ben Bernanke / Henry Paulson / Timothy Geithner / Financial Crisis Inquiry Commission / S&P Global Ratings / European Central Bank / European Stability Mechanism / European Financial Stability Facility / Euro / 2011 United States debt-ceiling crisis / Federal Reserve / Federal Open Market Committee / Systemic risk / Credit rating / Bank of America Home Loans / Financial crisis / 2008-2012 in the United States / 2008-2012（global years）
