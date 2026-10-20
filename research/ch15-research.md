# ch15 研究筆記：亞幣風暴、網路泡沫與房市泡沫（1997-2007）

## 方法
- 語料：/tmp/opencode/ch15/（en-wiki action=raw，UA research-script/10）。核心：1998 Russian financial crisis（31K）、Long-Term Capital Management（46K）、1998-2002 Argentine great depression（80K）、2001 in Argentina（7K）、1999 in Brazil（15K）、Brazilian real（59K）、Dot-com bubble（56K）、Nasdaq（40K）、2000s United States housing bubble（93K）、Subprime mortgage crisis（316K）、Subprime lending（23K）、Housing bubble（22K）、Negative amortization（15K）、Federal Housing Administration（29K）、Housing and Economic Recovery Act of 2008（22K）、Alan Greenspan（114K）、Federal Reserve（151K）、Greenspan put（53K）、Great Recession（132K）、2008 financial crisis（271K）、Subprime mortgage crisis；美國年度檔 1998-2007（10）、全球年度檔 1998-2007（10）。
- 註：「1999 Brazilian financial crisis」/「2001 Argentine economic crisis」獨立條目 404 → 用 1999 in Brazil + Brazilian real、1998-2002 Argentine great depression；「US housing bubble」→ 2000s United States housing bubble；「Financial crisis of 2007-2008」→ 2008 financial crisis。
- 語料無、不引用（NOT IN CORPUS）：俄羅斯 1998 GDP 萎縮率/失業率/油價水準（僅定性「油價下跌/1999-2000 油價急升」）、巴西 1999 GDP/失業/利率（1999 in Brazil 純事件）、1999-2000 風投美元規模、Nasdaq 綜合指數 2002 谷底與 1995 初值（僅 Nasdaq-100 谷底 1,114）、AOL-Time Warner $164B（語料 $162B）、LTCM 合夥人 Mermin/Litterman/Simons/Vishny（語料僅 Meriwether、Scholes、Merton 語境）、Greenspan Nobel（語料未提）、Greenspan 2026 卒（超時限、不寫）。

## 矛盾裁定（兩值並列，正文取較穩口徑）
1. LTCM 救助：$3.6B（首段）vs $3.65B（9/23 資本重組）→ 正文寫「約 $3.6B（14 家銀行、NY Fed 協調）、資本重組 $3.65B」。
2. dot-com 1995→頂點：+600%（首段）vs +400%（細部段）→ 正文寫「約四成（400%，另有統計達 600%）」。
3. 阿根廷違約規模：$100B（CEPR 史上最大）vs「$132B 中的大部分」→ 正文寫「約 $100B（當時史上最大主權違約，部分統計 $132B）」。
4. 阿根廷 2002-04 月通膨：10.4%（圖表）vs ~20%（文字）→ 正文不寫單月峰值，寫「通膨失序、比索貶值逾七成」。
5. 阿根廷匯兌本位起始：1991-02 vs 1991-04-01 → 正文寫「1991 年（Cavallo 上任經濟部長、austral 換 peso 1:1 釘美元）」。
6. 德國 3G 拍牌「£30 billion」（貨幣符號異常）→ 正文不寫金額，只寫「德國 2000 年 8 月 3G 拍牌」。
7. New Century「負債超過 $100 million」（疑 typo）→ 不寫該數。
8. AIG 救援「>$100B」vs「2008-09 初 >$180B」→ ch15 不寫 AIG 救援額（屬 ch16），只點 AIG COO 2006-01 離職的伏筆。
9. 美國家庭淨資產跌幅 ~$13T(20%) vs $11.5T(17.3%) → 屬 2008 後（ch16），ch15 不寫。
10. 1% 利率時點：Reich「2004」vs 2008 檔「2000-2003」vs Greenspan 檔 2002-11 聽證會 1.25%→1.00% → 正文寫「2001 年 1 月起 13 次降息、2003 年 6 月降至 1%、2004 年 5 月前維持」。
11. Bear「$10 trillion total assets」（語料原文）→ 不採用（數值異常），改用 Bear 2006-11-30 負債 $383.6B vs 股本 $11.8B（~33:1）。

## §1 本章摘要
- 承 ch14（1997 亞幣風暴引爆、1998 俄罗斯引爆 LTCM）。本章三段：(1) 新興市場危機浪潮 1998-2002（俄罗斯、巴西、阿根廷）——亞幣風暴的後續波；(2) 網路泡沫 1995-2002（頂 2000-03-10、跌 78%）；(3) 房市/次貸泡沫 2000-2007（Fed 1% 利率、證券化、2006 見頂、2007 爆發）。
- 投標對象收：從 ch14「資本流動/匯率」擴為「**信用/信貸本身**」——投標對象從「國家貨幣」擴為「**一筆房貸的信用**」，且槓桿從單筆資產（LTCM 25:1）擴為整個金融體系（40:1）。收句引向 ch16（大金融海嘯）。

## §2 歷史背景：新興市場危機的浪潮（1997-2002）
### 2.1 俄罗斯 1998
- 爆發 1998-08-17：盧布貶值、GKO（國內券）違約、外債延期；匯率 6.43/USD → 數週破 21；匯率區間 5.3-7.1 放寬至 6.0-9.5；央行 8/26 停 MICEX 美元交易；9/2 全面自由浮動；9/21 ~21/USD；11/15 解除外債延期。（Russian crisis）
- 1998 通膨 84%；GKO 拍賣利率曾達 ~150%（1998-06，Kirienko 時期）。（Russian crisis）
- 外因：1997 亞幣風暴 + 原油與有色金屬需求/價格下跌 → 重創外匯儲備；車臣戰爭 1995 初 ~$30M/日、總 $5.5B、赤字近 GDP 10%。（Russian crisis）
- 內因：低生產力、高固定匯率避免民怨、財務失當、慢性赤字。（World Bank）
- IMF/世銀 $22.6B 救助（1998-07-13）；1997-10~1998-08-17 耗外儲 ~$27B；約 $5B 國際貸款被挪用。（Russian crisis）
- 政治：Yeltsin 1998-03-23 解 Chernomyrdin、任命 35 歲 Kirienko；Duma 7/15 否決救市；8/23 Kirienko 被解；9/11 Primakov 獲通過；10/7 總罷工。（Russian crisis）
- 傳染：烏克蘭、摩爾多瓦違約；Bankers Trust 危機 → 1998-11 售 Deutsche Bank（~$10B）。（Russian crisis）
- 復甦：1999-2000 油價急升 + 貿易順差 + 貶值紅利；Stiglitz〈The ruin of Russia〉（Guardian，2003-04-09）。（Russian crisis）
- 美國背景：1998-04 失業 4.3%（1970-02 以來最低）。（1998 in US）
### 2.2 LTCM 1998
- 1994-02-24 開盤，資本 $1.01B；首年 21%、次年 43%、三年 41% 年化。（LTCM）
- 1998 初：股本 $4.7B、借入 >$124.5B、資產 ~$129B、債權比 >25:1；表外衍生名目 ~$1.25T（多為利率交換）。（LTCM）
- 策略：相對價值/收斂套利（benchmark Treasury convergence，數 bps 利差）→ 靠槓桿放大；依賴 repo 市場對手方持續融資。（LTCM）
- 1998-08-17 俄罗斯違約為引信：flight to liquidity——流動標的（LTCM 做空者）更貴、非流動標的（持有者）更賤；8 月底虧 $1.85B 股本。（LTCM）
- 9 月：股本自月初 $2.3B 跌至 9/25 的 $400M；負債仍 >$100B → 實際槓桿 >250:1。（LTCM）
- 1998 共虧 $4.6B（不足 4 個月）。（LTCM）
- 9/23 十四家金融機構協議 $3.65B 資本重組、NY Fed/Fed 監督；首段稱「$3.6B bailout」。（LTCM）
- 2000 初清算解散。Buffett/Munger 1993 拒絕投資（槓桿太險）；Samuelson、Fama、Klarman 早有疑慮。（LTCM）
- 意義：「too interconnected to fail」先聲；Greenspan put 大幅擴展到催生網路泡沫（Greenspan put）。
### 2.3 巴西 1999
- Real 1994-07-01 推出（Itamar Franco、Ricupero）；1 real = 2,750 cruzeiros reais；初 1:1 釘美元、受控滑落至 1998 底 ~1.20。（Brazilian real）
- 1999-01 俄罗斯違約後 real 自由浮動（新任央行總裁 Arminio Fraga）；貶至 ~2.00/USD；1999-2002 底波動但總向下。（Brazilian real）
- 2002 底 Lula 競選風波 → 匯率+通膨危機；2003-01-01 Lula 上任時 3.52/USD（Palocci + Fraga 正統路線）。（Brazilian real）
- 註：巴西無 1999 危機獨立條目，1999 in Brazil 純事件列表；正文以 real 放浮 + 新興市場「連鎖反應」框架寫。
### 2.4 阿根廷 2001-02
- 「大蕭條」期 1998Q3-2002Q2；GDP 損失 >20%；2002Q1 GDP 年化 -16.3%（紀錄）；失業 21.5%；實質工資 -18%；貧困 53%、赤貧 25%。（Argentine great depression）
- 匯兌本位：Cavallo 1991-01 任經濟部長、1991-04-01 austral 10,000:1 換 peso、1:1 釘美元（矛盾：另處 1991-02）。（同上）
- 1999 巴西貶值重創（巴西占其貿易 30%）；1999 GDP -3%、2000 GDP -0.8%；De la Rúa 1999 當選時失業 15%。（同上）
- 2001：S&P 7 月降 B-；megaswap（$30B 本金延期至 2005 + $38B 未來利息、涉 $82B 債券 60%）；8 月失業 16.4%（230 萬）；12/5 IMF 拒付 $1.3B；12/4-11 利差 34%→42%。（同上）
- Corralito 2001-12-02：取款限額 $250/週。（同上）
- 總統混戰：De la Rúa → Puerta（12/20-22）→ Rodríguez Saá → Camaño（12/30）；Cavallo 辭職+戒嚴 12/19；12/16-18 搶劫潮；12/20 抗議 26 死；De la Rúa 乘直升機離場。（2001 in Argentina）
- 2001 末違約：$100B（CEPR 史上最大）vs「$132B 大部分」→ 取 ~$100B。（同上）
- 2002-01：1.4:1 脫鉤後崩至 ~4 peso/USD；累計通膨 ~80%；pesificación（存款 1.40、債務 1:1「corralón」）。（同上）
- 復甦：2003-2007 GDP 8.8/9.0/9.2/8.5/8.7%；Kirchner 2003-05-25（Lavagna）；2005 重組 76% 債權 25-35% 平價（~70% 削減）。（同上）
- 教訓：固定匯率＋外幣負債＋財政赤字＝「原罪」極端版；1999 巴西貶值是引爆點（區域傳導）。

## §3 網路泡沫的興起（1995-2000）
### 3.1 技術革命與風投狂潮
- 1991 WWW、1993 Mosaic、1994 首筆安全信用卡交易（NetMarket）、1995 網民 >4,000 萬、Amazon/eBay 成立、1997 資本利得稅降、1996 電信法。（Dot-com）
- PC 普及率 15%（1990）→35%（1997）。（Dot-com）
- 風投易籌、投銀靠 IPO（多在 Nasdaq）獲利、鼓勵科技投資；Aeron 椅 $1,100。（Dot-com）
- Amazon：1997 IPO（營收年增 900%）、1998 估值 >$14B 仍未獲利。（Dot-com）
### 3.2 「新經濟」敘事與估值脫錨
- 投資者願以技術進步取代傳統指標（P/E）；任何「.com」名皆可投資。（Dot-com）
- 1999 末 Nasdaq P/E >200（日經 1991 峰 80 的兩倍多）。（Dot-com）
- 1999：Qualcomm +2,619%、12 只大型股 >+1,000%、7 只 >+900%；Nasdaq 綜合 +85.6%、S&P +19.5%；但跌多於漲（資金從慢成長股轉向網股）。（Dot-com/NYT）
- Shiller《Irrational Exuberance》2000 出書。（Dot-com）
### 3.3 IPO 潮、AOL-Time Warner、電信過載
- 1995-2000 Nasdaq 綜合 +400%（首段另稱 600%）。（Dot-com）
- AOL-Time Warner：2000-01-10 宣布、$162B（語料；常見 $164B 不採用）、史上最大企業合併。（2000 in US）
- 超級碗 XXXIV（2000-01-30）：61 支廣告 12 支 dot-com、30 秒 $1.9M-$2.2M。（Dot-com）
- 1996 電信法後 >$500B 光纖/電信投資；英國 3G 拍牌 2000-04 £22.5B、德國 2000-08（金額語料異常、不寫）。（Dot-com）
- 詐欺伏筆：WorldCom（Ebbers）、Enron（Skilling、Lay）。（Dot-com）
### 3.4 低失業、低利率與 Greenspan put
- 低失業背景：1999-12 美國失業 4.0%（1970-01 以來最低）。（1999 in US）
- Greenspan put：1987 崩盤後交易員命名；工具=大買國債（壓低殖利率→華爾街國債帳簿獲利）、降 funds rate（甚至負實質利率）、可無限展期短天期 repo=「間接 QE」；序列：1987→S&L→波斯灣→1994 墨西哥→1998 LTCM「大幅擴展、催生網路泡沫」→網路後轉 MBS 購買刺激房市。（Greenspan put）
- 「不要與 Fed 作對」；銀行稱其「The Maestro」；Blankfein 2009「動用 Fed put=做上帝的工作（下雨時收傘）」。（Greenspan put）
- Greenspan 1999-2000 升息被認為為刺破泡沫；Templeton 做空。（Dot-com）

## §4 網路泡沫的頂點與崩潰（2000-2002）
### 4.1 2000-03 頂點與刺破
- 頂點 2000-03-10：Nasdaq 綜合歷史高 5,048.62；兩週後 Nasdaq-100、S&P 500、Wilshire 5000 相繼見頂，結束 17+ 年牛市。（2000）
- 破裂軌跡：2000-03-13 日本拋售；03-20 Barron's〈Burning Up〉；03-21 Fed 升息→殖利率曲線倒掛；04-03 微軟判賠（MSFT -15%、Nasdaq -350/-8%）；04-14 Nasdaq 單日 -9%、單週 -25%。（Dot-com）
### 4.2 崩潰軌跡與破產潮
- 谷底 2002-10-09：Nasdaq-100 = 1,114（-78%）；綜合口徑「至 2002-10 跌 78%、回吐全部泡沫期漲幅」。（Dot-com）
- 破產/崩潰：Pets.com（2000-11-09 關門）、Webvan、Boo.com、WorldCom、NorthPoint、Global Crossing；詐欺 Ebbers/Skilling/Lay。（Dot-com）
- 48% dot-com 活到 2004；Cisco 後續 -80%。（Dot-com）
### 4.3 -78% 與 5 兆美元蒸發、電信/光纖
- 2002 底累計市值損失 $5T。（Dot-com）
- 光纖/電信過載：1996 電信法後 >$500B 投資、3G 拍牌狂潮、WorldCom/Global Crossing 破產 → 電信業巨額損失（「overbuild」）。（Dot-com）
### 4.4 對實體經濟與 Fed 回應
- Fed 2000-01 開始 6 次降息（1% 見 §5）；Krugman（NYT 2002-08-02〈Dubya's Double Dip?〉）：2002 信貸已推動房市而非企業投資、Fed「需製造房市泡沫取代 Nasdaq 泡沫」。（2008 financial crisis）
- 網路崩潰未引發大蕭條（消費/銀行體系相對韌），但 2001-09 9/11 + 通縮疑慮 → Fed 降息。（Great Recession 語境）

## §5 房市泡沫與次貸的興起（2001-2006）
### 5.1 Fed 降息到 1%（2001-03）：以房市救網路
- 利率路徑：2000-2003 由 6.5% 降至 1.0%（緩和网络/9-11/通縮風險）；1% 當時紀錄低點；其後升至 5.25%（2006）；2007-09-18 首度從峰頂降 50bp；2008-12 至 0-0.25%。（Greenspan、2008 financial crisis、Subprime）
- 矛盾裁定：1% 時點寫「2003 年 6 月降至 1%、2004 年 5 月前維持」（避開 2004/2000-2003 之爭）。
- Greenspan 2004-02-23 演說建議屋主考慮 ARM、八天後改稱固定利率佳（Fed 態度反覆）。（Greenspan）
- Krugman：Fed 製造房市泡沫取代 Nasdaq 泡沫。（2008 financial crisis）
### 5.2 信貸擴張：次貸、NINJA、負攤還、ARM
- 次貸規模：1994 占新貸 5%（$35B）→2006 20%（$600B）；截至 2007-03 次貸存量 $1.3T、首筆次貸 >750 萬筆（Bernanke 2007-05-17）；2004-06 占新貸 18-21%。（Subprime mortgage crisis）
- NINJA（無收入/工作/資產核實）=「liar loans」；FICO 門檻 2000 初 ≤660 →2005 許多放貸商 620；full doc→low doc→no doc。（2008 financial crisis）
- Citi 吹哨人 Richard M. Bowen III（FCIC）：2006 Citi 自 ~1,600 家 originator 買入房貸 60%「有缺陷」、2007 >80%。（2008 financial crisis）
- 負攤還（NegAm）：付款<利息、餘額增長（遞延利息/漸進付款）；企業版=PIK 貸款。（Negative amortization）
- 非銀行 originator 2002 ~25% →2003-05 房貸信貸成長 ~50%；多數在加州。（Subprime）
- 2006：1/3 房貸為次貸或 no-doc、該類占當年購屋 17%。（2008 financial crisis）
- FHA：HUD 內 Office of Housing、1934（National Housing Act 1934）。（FHA）
### 5.3 證券化：MBS、CDO、評級、影子銀行
- MBS 發行 1996-2007 近三倍至 $7.3T；次貸證券化比例 54%（2001）→75%（2006）；合成 CDO 2006 主導、名目 $5T；私人 MBS/ABS/CDO 2006 峰 ~$2T →2009 <$150B。（Subprime）
- 評級：2007 秋-2008 中下調 ~$2T MBS；2008 底 80% AAA CDO（按價值 $300B）降為垃圾級（FCIC）；銀行減記/損失 $523B（Bloomberg 2008-09-24）。（Subprime）
- 影子銀行（Geithner 2007 初）：SIV/導管 $2.2T、tri-party repo $2.5T、對沖基金 $1.8T、五大投銀 $4T、五大銀行控股剛過 $6T、整個銀行體系 ~$10T；Krugman：repo≈美國銀行體系 60%。（Subprime）
- OTC 衍生名目 $673T（FCIC）；CDS 未償 1998→2008 增 100 倍；2008 無中央清算所。（Subprime）
- Fannie/Freddie：2008-09 被接管時直接負債或擔保近 $5T 房貸。（2008 financial crisis、Subprime）
### 5.4 財富效應、HELOC、房價飆漲
- 房屋權益提取 $627B（2001）→$1,428B（2005）、累計 ~$5T；提取占 GDP 2.3-3.8%（1993-97）→11.5%（2005）。（Subprime）
- HELOC $106B（1996）→$750B（2005）、2/3 用於消費。（2000s US housing bubble）
- 房貸債務占 GDP 46%（1990s 均）→73%（2008，$10.5T）；每戶 $91,500→$149,500（+63%）。（Subprime）
- 家庭負債 $705B（1974，占 DPI 60%）→$7.4T（2000 底）→$14.5T（2008 中，占 DPI 134%）。（Subprime）
- 2001-06 都會區實價漲幅：7 個 >80%（Tampa、Miami、San Diego、LA、Las Vegas、Phoenix、DC）、6 個 <10%。（2000s US housing bubble）
- 建商：D.R. Horton $3（1997）→$42.82（2005-07-20）；Pulte $2.33B（1996）→$14.69B（2005）；2005 單家庭銷售 1,283,000 件（1990-95 年均 609,000）。（2000s US housing bubble）
### 5.5 泡沫頂點：2006 見頂、止損上升
- 頂點 2006 年初；「2006 多年高於平均漲價後、屋價見頂、房貸延誤上升——泡沫破裂第一信號」。（2000s US housing bubble、2008 financial crisis）
- 止損（foreclosure）：2006 1,259,118 件（+42%）；2007 ~1.3M（+79%）；2008 2.3M（+81%）。（2006 in US、Subprime）
- 早期警告：Gramlich（2001）次貸警告、Ron Paul 證詞（2003-09）、2004 CRO 備忘錄（Andrukonis）。（2000s US housing bubble）
- Greenspan 2005-08-27「約 1/3 美國地區房市顯著高估」、2005-04-08「次貸占未償房貸 ~10%（1990s 初 1-2%）」。（Greenspan）

## §6 崩潰前奏：2006-2007 次貸危機爆發（橋段，2008 屬 ch16）
### 6.1 2006 警告
- 2006-05 JPMorgan 警告客戶房市下行、止損上升、尤其次貸；2006-11 UBS 警告「美國房市即將來臨的危機」。（2008 financial crisis）
- 2006-08 殖利率曲線倒掛（Cleveland Fed：一兩年內很可能衰退）。（2008 financial crisis）
- 2006-01-18 AIG COO Donald Kanak「個人原因」辭職（伏筆，不寫救援額）。（2006 in US）
- 2006-10 失業 4.4%（2001-05 以來最低）；道瓊指數 10-03 收 11,727.34（6 年新高）、10-19 首破 12,000。（2006 in US）
### 6.2 2007 爆發：New Century、Bear、BNP Paribas
- 2007-04-02 New Century（次貸 REIT）申請第 11 章——「由此擴散為次貸危機」。（2008 financial crisis）
- 2007-06-20 Bear 在 margin call 後救兩個對沖基金（$20B CDO 曝險）、7/31 兩基金清算（Zandi：「最直接的催化劑」）。（Subprime）
- 2007-08-09 BNP Paribas 凍結三隻基金 $2.2B——「流動性完全蒸發」、銀行拒絕互相做生意。（2008 financial crisis）
- 2007-08-06 American Home Mortgage 破產；2007 全年 >100 家放貸機構倒閉/停業/出售。（Subprime、2008 financial crisis）
### 6.3 Northern Rock、歐洲蔓延、Greenspan 降息
- 2007-07-30 德國 IKB——「危機第一家銀行犧牲品」、KfW 救援（傳至歐洲）。（2008 financial crisis）
- 2007-09-14 Northern Rock 獲英央行支持→銀行擠兌（2008-02-22 國有化、成本 £87B/$150B）。（2008 financial crisis）
- 2007-09-18 Fed 首度從 5.25% 峰頂降 50bp；2007-12-12 TAF 啟用。（2008 financial crisis、Federal Reserve）
- 2007-10-09 道瓊指數收 14,164.53——危機前最後收盤高。（2008 financial crisis）
- Greenspan 2007-09-16/17（FT）承認「房市有泡沫」、2007-09-13「我直到 2005 底 2006 才真正看清」。（Greenspan）
### 6.4 「批發式恐慌」與 Minsky 時刻
- Gorton：2008=「批發式恐慌、非零售式恐慌」——金融機構經 repo 互相跑單。（Great Recession）
- Bear/Lehman 被「恐慌的隔夜 repo 貸方沉默跑單」擊垮（Economist 2010-03）。（Subprime）
- 2007-11-26 美股入 correction、Bear 史上首次季虧損；2007-12「晚 2000s 衰退正式開始」、NBER 定 recession 2007-12~2009-06。（2007 in US、Great Recession）
- 過渡：2008-01-22 緊急降 75bp、2008-03-17 Bear 以 $2/股賣 JPMorgan、2008-09-15 Lehman 破產——「2008 金融危機高潮」（引向 ch16）。（2008 financial crisis）

## §7 深度分析
### 7.1 Minsky：hedge→speculative→Ponzi 在房市重演
- Minsky（1919-1996）：金融脆弱性內生於金融市場；繁榮→現金流上升→投機亢奮→債務超可服務收入→銀行收緊→收縮；三類借款人 hedge/speculative/Ponzi；Minsky moment=資產價值突崩。（ch14 已立框架，本章套用）
- 房市重演：hedge（傳統固定房貸）→speculative（ARM、利息_ONLY）→Ponzi（負攤還、依賴房價漲、NINJA 不靠收入）；2007-07 Bear margin call 連鎖=speculative→Ponzi 的邊際呼叫動態。（Subprime、Greenspan put、2008 financial crisis）
- Janet Yellen〈A Minsky Meltdown: Lessons for Central Bankers〉（FRB 舊金山，2009-04-16）：危機前過度槓桿、Minsky「去槓桿悖論」+節儉悖論。（2008 financial crisis）
### 7.2 Greenspan put 的代價：道德風險、泡沫接力
- Greenspan put 序列：1987→S&L→波斯灣→1994 墨西哥→1998 LTCM「催生網路泡沫」→網路後 MBS 購買「直接刺激房市價格膨脹、直到在大蕭條中崩潰、Greenspan 退休」。（Greenspan put）
- 代價：道德風險（預期 Fed 托底）、單向棘輪（Pearlstein「股債價格的地板、永無天花板」）、不平等擴大。（Greenspan put）
- 泡沫接力：網路（1995-2000）→房市（2000-2006）；Krugman「Fed 需製造房市泡沫取代 Nasdaq 泡沫」。（2008 financial crisis）
### 7.3 金融化：槓桿 40:1、金融業債務 $36T
- 投槓桿最高 40:1（FCIC）；五大投銀 FY2007 負債 >$4.1T（~30% 名目 GDP）；Bear 2006-11-30 負債 $383.6B vs 股本 $11.8B（~33:1）、資產跌 3% 即破產。（Subprime、2008 financial crisis）
- 金融業債務 $3T（1978）→$36T（2007）；2006 金融業利潤占全部企業利潤 27%（1980 年 15%）。（Subprime）
- 21 世紀金融體系、19 世紀保障措施（FCIC）。（Subprime）
### 7.4 從 dot-com 到房市的泡沫接力與全球傳導
- 同一台「Greenspan put 機器」先吹網股、後吹屋價；低利率是共同燃料。（Greenspan put、2008 financial crisis）
- 全球傳導：1997 亞幣→1998 俄罗斯→LTCM→1999 巴西→2001 阿根廷；2007 次貸→2007-08 歐洲（IKB、Northern Rock）。（各年度檔）
- 投標對象演化：國家（ch11-12）→預期（ch12）→槓桿/算法（ch13）→資本流動/匯率（ch14）→**信用/信貸本身**（ch15）：一筆房貸的信用被證券化、槓桿化、全球化，投標對象成為「**一筆房貸的信用**」，槓桿從單筆資產（LTCM 25:1）擴為整個金融體系（40:1）。

## §8 評判與評判（一~七）
- 一、俄罗斯 1998 與 1997 亞幣同構：固定匯率＋外幣負債＋財政赤字＋hot money；不同是俄罗斯以「內幣債（GKO）違約」而非「貶值」引爆，顯示連主權內幣債都可被市場不信任。
- 二、LTCM 是 2008 的藍圖：25:1→250:1、repo 融資、too interconnected to fail；1998 的 Fed 干預（不救價、救流動性）成為 2008 的模板。
- 三、阿根廷是「原罪」極端：1:1 釘美元 + 外幣負債 + 財政赤字，1999 巴西貶值引爆；Corralito 與史上最大違約是「不可能三角」的破產式結局。
- 四、網路泡沫的獨特：估值（P/E 200）脫錨 + 風投/IPO 機制 + 電信物理過載；但銀行體系相對乾淨，故未直接引爆系統危機——是「資產泡沫」而非「信貸泡沫」的初級形態。
- 五、Fed 1% 利率是雙刃：救網路衰退 + 9/11 通縮，卻用「財富效應」與「負實質利率」吹起更大、更系統性的房市/次貸泡沫。
- 六、證券化把「信用」變成可交易、可槓桿、可全球化的商品：放貸（origination）與承險（securitization）分離 + 評級錯位 + 影子銀行，使風險不可見、不可控。
- 七、Minsky 被證明：2007 不是意外而是「穩定→不穩定」的必然收束；Greenspan put 延緩但放大每次危機（泡沫接力）。本章是 ch16 大金融海嘯的完整前奏。

## §9 關鍵數據表（行）
| 事件 | 數據 |
|---|---|
| 俄罗斯盧布 | 6.43→破21/USD（1998-08-17）；9/2 自由浮動 |
| 俄罗斯通膨/GKO | 84%；GKO 利率曾 ~150%（1998-06） |
| 俄罗斯救助 | IMF/世銀 $22.6B（1998-07-13） |
| LTCM | 股本 $4.7B/借 >$124.5B（>25:1）；9 月股本 $2.3B→$400M（>250:1）；虧 $4.6B；$3.65B 重組（9/23，14 行） |
| 巴西 real | 1994-07-01 推出（2,750:1）；1999-01 放浮→~2.00 |
| 阿根廷 GDP | 1998Q3-2002Q2 損失 >20%；2002Q1 年化 -16.3%；失業 21.5%、貧困 53% |
| 阿根廷 Corralito | 2001-12-02、$250/週 |
| 阿根廷違約 | ~$100B（2001 末，當時史上最大） |
| 阿根廷比索 | 2002-01 脫鉤→~4/USD |
| Nasdaq 頂 | 5,048.62（2000-03-10） |
| Nasdaq 底 | -78%（2002-10；Nasdaq-100 1,114，2002-10-09） |
| dot-com 漲幅 | 1995→頂 ~400%（另 600%）；1999 Nasdaq +85.6%、Qualcomm +2,619% |
| dot-com 蒸發 | 2002 底市值 -5T；48% 活到 2004 |
| AOL-Time Warner | $162B（2000-01-10，史上最大） |
| Nasdaq P/E | >200（1999 末，vs 日經 1991 80） |
| Fed 利率 | 6.5%→1%（2003-06）；5.25%（2006）；0-0.25%（2008-12） |
| 次貸規模 | $35B（1994，5%）→$600B（2006，20%）；存量 $1.3T（2007-03） |
| MBS 發行 | $7.3T（1996-2007）；次貸證券化 54%→75%（2001-06） |
| 合成 CDO | 名目 $5T（2006） |
| OTC 衍生 | 名目 $673T；CDS 1998→2008 增 100 倍 |
| 家庭負債 | $7.4T（2000）→$14.5T（2008，DPI 134%） |
| 房貸債務 | 占 GDP 46%→73%（2008，$10.5T） |
| 房屋權益提取 | $627B（2001）→$1,428B（2005） |
| 止損 | 1.26M（2006）→2.3M（2008） |
| 投槓桿 | 最高 40:1；五大投銀 FY2007 負債 >$4.1T |
| 金融業債務 | $3T（1978）→$36T（2007） |
| 2007 危機 | New Century 4/2 破產；BNP Paribas 8/9 流動性蒸發；Northern Rock 9/14 擠兌；道瓊指數最後高 14,164.53（10/9） |

## 參考來源（en-wiki，全部實際引用於正文）
- 1998 Russian financial crisis
- Long-Term Capital Management
- 1998-2002 Argentine great depression
- 2001 in Argentina
- 1999 in Brazil
- Brazilian real
- Dot-com bubble
- Nasdaq
- 2000 in the United States
- 1999 in the United States
- 1998 in the United States
- 2000s United States housing bubble
- Subprime mortgage crisis
- Subprime lending
- Housing bubble
- Negative amortization
- Federal Housing Administration
- Housing and Economic Recovery Act of 2008
- Alan Greenspan
- Federal Reserve
- Greenspan put
- Great Recession
- 2008 financial crisis
- 2005 in the United States
- 2006 in the United States
- 2007 in the United States
- 2000s
