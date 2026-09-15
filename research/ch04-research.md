# ch04 研究筆記（1866–1873）

方法說明：本章研究分兩輪完成（2026-09）。方法：英文／德文／法文 Wikipedia API 全文擷取（en/de/fr）＋直接頁面擷取；NY Fed Liberty Street Economics（Crisis Chronicles 系列，Klitgaard & Narron，2016-02）；1873-09-19《紐約時報》（TimesMachine，經 NY Fed 轉引）；1911 Encyclopaedia Britannica（Wikisource）；以 Python 交叉驗證關鍵日期之日曆星期（1873-09-18 為週四、09-19 為週五、10-18 為週六；1873-05-09 為週五；1875-01-14 為週四；1879-01-01 為週三）。主要來源：en-wiki「Panic of 1873」「Long Depression」「Jay Cooke」「Jay Cooke & Company」「Northern Pacific Railway」「Coinage Act of 1873」「Specie Payment Resumption Act」「Black Friday (1869)」「Greenback (1860s money)」「Crédit Mobilier scandal」「Coal miners' strike of 1873」「1873 in the United States」「List of recessions in the United States」「Reconstruction era」；de-wiki「Gründerkrach」；fr-wiki「Crise bancaire de mai 1873」；NY Fed Crisis Chronicles（Crisis Chronicles: The Panic of 1873 之 Jay Cooke & Company 條目）；1911 EB「Cooke, Jay」；本書第三章（ch03）回指來源。

## 關鍵事件與日期

- 1864-07-02：第 38 屆國會特許北太平洋鐵路（連接五大湖與普吉特灣）；國會原撥 6,000 萬英畝土地撥賜，該路最終接受近 4,000 萬英畝；「間隔地段」（alternate section）分配。（來源：en-wiki「Northern Pacific Railway」）
- 1865-04：停戰；綠背自 150 兌 100 開始回升；國會把綠背發行上限設為 4.5 億美元。（來源：en-wiki「Greenback (1860s money)」）
- 1866-04-12《收縮法》；1866-05-10 奧凡德·格尼（Overend, Gurney）停兌——已寫入 ch03，本章不重述，僅回指。（來源：ch03 §5/§6）
- 1867：奧匈妥協（Austro-Hungarian Compromise）；妥協後奧匈帝國進入重建與投資期，維也納證券交易所熱度同步攀升。（來源：en-wiki「Austro-Hungarian Compromise of 1867」）
- 1868：約翰遜（Andrew Johnson）彈劾案（參議院一票幸免）；第十四修正案通過；格蘭特（Ulysses S. Grant）當選總統，1869–77 兩任。（來源：en-wiki「Reconstruction era」；「1868 in the United States」）
- 1869：格蘭特簽署《公共信貸法》（Public Credit Act of 1869），建立 10 年復返金本位時間表，公債以「黃金或其等價物」償付。（來源：en-wiki「Black Friday (1869)」）
- 1869-04 起：財務部長鮑威爾（George S. Boutwell）開始雙週出售財政部黃金贖回戰債；出售命令以電報發給美聯社公開；至 9 月 1 日國債已減 5,000 萬美元。（來源：en-wiki「Black Friday (1869)」）
- 1869-09-24（週五）：黃金圈（Gold Ring）壟斷破滅——格蘭特下令釋放 400 萬美元黃金、購入 400 萬美元公債；數分鐘內金價自 160 美元跌至 138 美元；該日史稱「黑色星期五」，為美國史上第一個黑色星期五。（來源：en-wiki「Black Friday (1869)」；NY Fed Liberty Street Economics「The Gold Panic of 1869, America's First Black Friday」）
- 1870-02-15：北太平洋鐵路（Northern Pacific Railway）在明尼蘇達州德盧斯（Duluth）附近破土。（來源：en-wiki「Panic of 1873」）
- 1870：北太平洋鐵路指定庫克公司（Jay Cooke & Company）為獨家債券代理。（來源：en-wiki「Jay Cooke & Company」）
- 1890-07-10：科羅拉多州參議員亨利·M·泰勒（Henry M. Teller）在國會辯論中首次使用「1873 年之罪」（Crime of 1873）一詞。（來源：en-wiki「Coinage Act of 1873」）
- 1870-03：德意志銀行（Deutsche Bank）成立。（來源：fr-wiki「Crise bancaire de mai 1873」）
- 1871-01-18：德意志帝國宣告成立；法國賠款 2 億英鎊流入德奧資本市場，為「創業者時代」（Gründerzeit）投機熱潮的主要燃料。（來源：en-wiki「Long Depression」）
- 1871-11-23：德國開始廢除銀幣法償地位（1873-07-09 金馬克正式確立金本位）。（來源：en-wiki「Panic of 1873」）
- 1872-02：《紐約太陽報》（The New York Sun）於 1872 年大選期間曝光 Crédit Mobilier 醜聞。（來源：en-wiki「Crédit Mobilier scandal」）
- 1872-09：美國近恐慌（near-panic）——1870 年代第一次流動性危機；庫克公司倫敦合夥人 Fahnestock 於 1872 年秋警告「用存款人的錢支持北太平洋債券是殘酷的」。（來源：NY Fed Crisis Chronicles，引 Kindleburger《Crashes and Panics》p.80）
- 1873-01-01：俄亥俄州東北部煤田（馬霍寧、申岡戈、塔斯卡瓦薩河谷）逾 6,000 名工會化煤礦工人為抵制 25% 減薪罷工（1872 年工資為每噸 1.10 美元）；罷工歷時數月，以輸入替代工人（300 名來自維吉尼亞的黑人工人、200 名意大利移民）告敗。（來源：en-wiki「Coal miners' strike of 1873」）
- 1873-02-12：《鑄幣法》（Coinage Act of 1873）由格蘭特簽署；1873-04-01 生效。（來源：en-wiki「Coinage Act of 1873」；「1873 in the United States」）
- 1873-04-13：路易斯安那州格蘭特派考爾法克斯大屠殺（Colfax massacre），62 至 153 名自由民與州民兵死亡。（來源：en-wiki「1873 in the United States」）
- 1871-10-08 芝加哥大火（Great Chicago Fire）；1872-03 波士頓大火（Great Boston Fire of 1872）；1872–73 馬流感（equine influenza）流行——巨額財產損失與流行病，是銀行準備金受壓的貢獻因素之一。（來源：en-wiki「Panic of 1873」）
- 1873-05-01：維也納世界博覽會開幕。（來源：de-wiki「Gründerkrach」）
- 1873-05-08 至 10：維也納證券交易所崩潰，交易所停市（一說崩潰自 5 月 9 日開始，德文來源稱 5 月 9 日為「黑色星期五」）；5 月 13 日重開，恐慌「似乎已經消退」，被判斷為僅限於奧匈帝國。（來源：en-wiki「Long Depression」；de-wiki「Gründerkrach」；en-wiki「Panic of 1873」）
- 1873-05-09 清晨：「仲介生意之王」阿道夫·佩茨克（Adolf Petschek）率先破產，同日上午 120 家銀行倒閉，13 點維也納交易所被警察關閉；普拉克特銀行（Placht und Fels）負債 276 萬佛羅林、資產僅 9,000 佛羅林。（來源：de-wiki「Gründerkrach」；fr-wiki「Crise bancaire de mai 1873」）
- 1873-06-04：北太平洋鐵路線東段軌道抵達密蘇里河。（來源：en-wiki「Northern Pacific Railway」）
- 1873-07：克利夫蘭（Cleveland）等工業城市鐵路工人減薪罷工（具體日期未核實，見「待核實項」第 5 條）。（來源：見待核實項；背景：en-wiki「Panic of 1873」之 1877 年大罷工為其後續）
- 1873-09-18（週四）：庫克公司在紐約、費城兩辦事處停止兌付。（來源：NY Fed Crisis Chronicles「on September 18, 1873, it suspended withdrawal of deposits at its New York and Philadelphia offices」；en-wiki「Panic of 1873」「On 18 September, the firm declared bankruptcy」；en-wiki「Northern Pacific Railway」；fr-wiki「panique du 18 septembre 1873」；en-wiki「1873 in the United States」）
- 庫克停兌公告原文（NY Fed Crisis Chronicles）：「large drawing upon them by the Philadelphia house and their own depositors during the last fortnight」（過去兩週費城分行與其存款人的大額提款）。（來源：NY Fed Crisis Chronicles）
- 1873-09-19（週五）：衝擊抵達紐約交易所；1873-09-19《紐約時報》：「第一個傳到交易所的關於任何變化的消息，是一則簡短通知：賈伊·庫克公司已停止兌付。街頭陷入興奮狀態……」；德文來源稱「9 月 19 日，危機抵達紐約」（無「黑色星期五」標籤之來源）。（來源：NY Fed Crisis Chronicles 引 NYT 1873-09-19；de-wiki「Gründerkrach」）
- 1873-09-18 當時即稱「黑色星期四」（Black Thursday）。（來源：en-wiki「Long Depression」）
- 1873-09-20（週六）：紐約證券交易所（NYSE）起關閉 10 天（9 月底重開；德文來源稱至 9 月 29 日）。（來源：en-wiki「Panic of 1873」；fr-wiki；de-wiki「Gründerkrach」）
- 1873-09-26：德文日報《Das Vaterland》文章已使用「Gründerkrach」一詞。（來源：de-wiki「Gründerkrach」）
- 庫克失敗後，紐約經紀商行亨利·克魯斯（Henry Clews）隨後倒閉，引發連鎖銀行倒閉與交易所暫時關閉。（來源：en-wiki「Panic of 1873」）
- 1873-10-04：紐約納蘇街第四國家銀行（Fourth National Bank）發生搶存（Frank Leslie's Illustrated Newspaper 1873-10-04 圖像標題）。（來源：en-wiki「Panic of 1873」）
- 1873-11：至 1873 年 11 月，55 家鐵路破產；一年內另 60 家。（來源：en-wiki「Panic of 1873」）
- 1873-10 至 1879-03：NBER 計量之收縮期，65 個月，為 NBER 體系最長收縮（大蕭條為 43 個月）。（來源：en-wiki「Long Depression」；「List of recessions in the United States」）
- 1874：民主黨在國會議員選舉中取得眾議院（內戰以來首次）；格蘭特否決「費里通膨法案」（Ferry Bill）。（來源：en-wiki「Panic of 1873」；「Long Depression」）
- 1877-07：木材市場崩盤，密西根多家木材公司破產。（來源：en-wiki「Panic of 1873」）
- 1875-01-14：《硬幣兌付復原法》（Specie Payment Resumption Act）通過——1874 年大選後 lame-duck 共和黨國會所通過。（來源：en-wiki「Specie Payment Resumption Act」；ch03 §6）
- 1878-12：綠背與金幣平價。（來源：en-wiki「Greenback (1860s money)」；ch03 §6）
- 1879-01-01：自由兌付正式恢復，美國回到金本位。（來源：en-wiki「Specie Payment Resumption Act」；「Long Depression」；ch03 §6）
- 1879：俾斯麥（Bismarck）德國通過保護關稅（容克地主推動，國家自由黨反對）；法國第三共和國（蒂爾總統）轉向保護主義，最終至 1892 年梅蘭關稅；1887 年法意關稅戰。（來源：en-wiki「Long Depression」）
- 1882：法國聯合銀行（Union Générale）倒閉，法國衰退延至 1897–99。（來源：en-wiki「Long Depression」）
- 1896：英國「長蕭條」（1873–96）終結。（來源：en-wiki「Long Depression」）

## 關鍵數據

- 綠背對金溢價（金溢價）走勢：1862-12 為 129 兌 100（溢價 29%）；1863 春 152 兌 100；葛底斯堡後 131 兌 100；1864-07 最低點 258 兌 100；1865-04 回升 150 兌 100；1878-12 平價。（來源：en-wiki「Greenback (1860s money)」；已寫入 ch03 §6/§9，本章僅回指）
- 綠背流通量：戰末 4.31 億美元（另有 5,000 萬美元零用紙幣「shinplasters」授權）。（來源：en-wiki「Specie Payment Resumption Act」）
- 美國國債：6,400 萬美元（1860）→28 億美元（約翰遜政府末，1868）。（來源：en-wiki「Black Friday (1869)」）
- 1869 黃金圈：金價 132.50（09-06）→137（09-06 後）；09-22 收 141；09-24 釋放 400 萬美元黃金後金價 160→138（數分鐘內）；古德（Gould）與菲斯克（Fisk）合計持有 5,000 萬至 6,000 萬美元黃金（約為紐約公共供給的三倍）；股價 09-24 至 10-01 下跌 20%；小麥 1.40→0.77 美元/蒲式耳；玉米 0.95→0.68。（來源：en-wiki「Black Friday (1869)」）
- 美國鐵路：1868–73 鋪設 33,000 英里；鐵路業為最大非農業僱主；高峰時吸收最多 20% 的美國資本投資；鐵路里程 1867–73 增長 50%。（來源：en-wiki「Panic of 1873」；「Long Depression」）
- 北太平洋鐵路：4,000 萬英畝公共土地撥賜；1873 年仍尋求 1 億美元資本；1870-02-15 破土；1873-06-04 軌道達密蘇里河；1873 年 9 月庫克公司「無法銷售數百萬美元北太平洋債券」（原文「several million dollars」）。（來源：en-wiki「Long Depression」；「Northern Pacific Railway」；「Panic of 1873」）
- 紐約市銀行準備金：1873 年 9–10 月自 5,000 萬美元跌至 1,700 萬美元。（來源：en-wiki「Panic of 1873」）
- 銀行綠背準備金：1873 年 9 月 3,400 萬美元 → 10 月 500 萬美元。（來源：en-wiki「Specie Payment Resumption Act」）
- 財政部 1873 年夏前售金 1,400 萬美元；國家銀行券發行增 4,400 萬美元。（來源：en-wiki「Specie Payment Resumption Act」）
- 破產：18,000 家企業破產（一說 1873–75，一說 1873–79；其中 89 家鐵路）；至 1873 年 11 月 55 家鐵路破產＋一年內另 60 家；鐵路年新建 7,500 英里（1872）→1,600 英里（1875）。（來源：en-wiki「Long Depression」；「Panic of 1873」）
- 失業：1878 年峰值 8.25%；恐慌影響在紐約快速顯現（25% 工人失業），在芝加哥、內華達州維吉尼亞城（銀礦區）、舊金山較慢；全國約 100 萬人失業。（來源：en-wiki「Panic of 1873」；「Long Depression」）
- 工資：1870 年代名義工資下跌四分之一，賓州等地達一半；實質工資 1865–73 增長近四分之一後停滯至 1880 年代。（來源：en-wiki「Long Depression」）
- 價格：棉花 1872–77 下跌近 50%；小麥 1894 年僅為 1867 年的三分之一；鐵價 1870–90 減半。（來源：en-wiki「Long Depression」）
- 產量（1870–90，五大生產國）：鐵 1,100 萬噸→2,300 萬噸（倍增）；鋼 50 萬噸→1,100 萬噸（二十倍）。（來源：en-wiki「Long Depression」）
- 貨幣（Friedman & Schwartz 數字）：1869–79 名義國民生產 +3%/年、實質 +6.8%/年、實質人均 +4.5%/年；貨幣供給 +2.7%/年；銀行存款 1873–78 自 19.64 億→22.21 億美元（+13.1%）。（來源：en-wiki「Long Depression」，引 Friedman & Schwartz）
- 復甦：軌道新建 2,665 英里（1878）→11,568 英里（1882）；建築許可 1878–83 增至 2.5 倍；失業率回落至 2.5%。（來源：en-wiki「Long Depression」）
- 《復原法》：綠背流通 3.82 億美元（1874 年末）→3 億美元（法案後）；1879-01-01 兌付準備 1.33 億美元（對歐債券銷售＋財政盈餘）；最終復匯日定在黃金溢價跌回峰值十分之一之後。（來源：en-wiki「Specie Payment Resumption Act」；ch03 §6）
- 1877 牛肉出口：前四個月售英量等於此前全年。（來源：en-wiki「Specie Payment Resumption Act」）
- 1877 年大鐵路罷工：1877-07-14 始於西維吉尼亞州馬丁斯堡（B&O 鐵路一年內第三次減薪），歷時 45 天，涉及逾 10 萬工人；州民兵初期同情工人，西維吉尼亞州州長亨利·M·馬修斯（Henry M. Mathews）向海斯（Hayes）總統請求聯邦援助，海斯派聯邦軍隊；巴爾的摩卡姆登碼頭（Camden Yards）對峙中民兵開火，10 人死亡、25 人受傷；密蘇里州至少 18 人死於衝突。（來源：en-wiki「Panic of 1873」；「History of rail transport in the United States」）
- 1877 年 7 月木材市場崩盤，密西根州破產的木材公司包括 Danaher & Melendy 與 Oliver O. Stanchfield（Ludington）、Cushman, Calkins & Co. 與 Tyson, Sweet & Co.（Manistee）。（來源：en-wiki「Panic of 1873」註 58）
- 1873 年《鑄幣法》的連鎖效應：減少國內貨幣供給、推高利率、傷害負債農民；「對美國貨幣政策不穩定的認知使投資人迴避長期債務，尤其是長期債券；問題因已進入後期的鐵路熱潮而加劇」；銀價崩落被貿易銀元與 1873 年內華達州維吉尼亞城（Virginia City）大銀礦發現（新投資）部分抵消；「廢銀因此是太平洋兩岸危機的共同要素」。（來源：en-wiki「Panic of 1873」）
- 自由人儲蓄銀行（Freedman's Savings Bank，1865 年設立）1874 年倒閉。（來源：en-wiki「Long Depression」）
- 柏林交易所 1871–73 接納 95 家新銀行；德意志銀行 1870-03 成立；百餘家金融公司專營城市建設與裝修。（來源：fr-wiki「Crise bancaire de mai 1873」）
- 維也納交易所熱度：帝國奧地利半部的證券銀行自 1867 年的 11 家增至 1873 年 5 月的 141 家；博覽會前數月股價升到「天文數字的高度」；股票可以只繳部分款項購買（即今日的「保證金」）、餘款期待股價繼續上漲時再付，連流動性不足的人也能建立龐大持股。（來源：de-wiki「Gründerkrach」）
- 歐洲泡沫頂峰：維也納房地產價格數月內翻了三倍；柏林 1872 年增長 8%、德意志銀行業平均股息率 10.75%。（來源：法文「Crise bancaire de mai 1873」）
- 復甦不對稱：崩潰後歐洲的復甦遠比美國快，且德國企業避開了深度減薪。（來源：en-wiki「Panic of 1873」）
- 「鄉村貨幣」：銀被視為對鄉村比對大城市銀行更有利的貨幣，廢銀對礦區與農民是打擊。（來源：en-wiki「Long Depression」）
- 「1873 年之罪」標籤：廢銀的礦區利益集團早已以「The Crime of '73」稱呼《鑄幣法》；斯圖爾特 1889 年稱「罪行」；1890-07-10 泰勒（Teller）首次在國會辯論使用「Crime of 1873」。（來源：en-wiki「Panic of 1873」；「Coinage Act of 1873」）
- 金溢價回落不能全歸於《復匯法》本身：1877 年南部產量擴張對總價格水平有下行壓力。（來源：en-wiki「Specie Payment Resumption Act」）
- 法國賠款 2 億英鎊。（來源：en-wiki「Long Depression」）
- 英格蘭銀行 1870 年代利率高達 9%。（來源：en-wiki「Panic of 1873」；「Long Depression」）
- 羅特席德家族與巴林銀行（Barings Bank）1850 年後為世界最大債券發行機構（一說發行全球約 70% 的債券）。（來源：en-wiki「Panic of 1873」，單一來源，見待核實項第 9 條）
- 庫克（Jay Cooke，1821–1905）：庫克公司 1861 年創立於費城；內戰期銷售 5 億美元「五-二十」債券（Five-Twenties，1862-02-25 授權之 6% 20 年期公債），2,500 名分銷代理；美國第一家「電線經紀行」（wire house）。（來源：en-wiki「Jay Cooke」；「Jay Cooke & Company」）
- 1911 EB 記庫克歿於 1905-02-18；en-wiki 記 1905-02-16。（來源：1911 EB；en-wiki「Jay Cooke」，見待核實項第 6 條）

## 關鍵人物與決策

- 賈伊·庫克（Jay Cooke，1821–1905）：俄亥俄州桑達斯基（Sandusky）人，費城起家；1861-01-01 創立庫克公司；內戰債券銷售起家（5 億美元「五-二十」）；1869 年後轉向鐵路融資；1870 年成為北太平洋獨家債券代理；深度捲入加拿大太平洋鐵路建設融資，引發 1873 年加拿大「太平洋醜聞」（Pacific Scandal），使麥基倫（John A. Macdonald）總理在 1873 年大選敗選；1873-09-18 公司停兌；其後以猶他州霍恩銀礦（Horn Silver Mine）重建身家，至 1880 年代已重償債務並再度富甲。（來源：en-wiki「Jay Cooke」；NY Fed Crisis Chronicles）
- 庫克公司（Jay Cooke & Company，1861–73）：總部費城，紐約與華盛頓設分行；第一家「電線經紀行」；1869 年黑色星期五後自公債轉向鐵路融資（北太平洋，將連接德盧斯與西雅圖）；1870 年成為北太平洋獨家債券代理，其後吸收該路發行的絕大多數債券，庫克最終持有該路 75% 股權（見待核實項第 11 條）；1873 年為「國家銀行體系的主要組成部分」（原文 a major component of the country's banking establishment）。（來源：en-wiki「Jay Cooke & Company」；「Panic of 1873」；NY Fed Crisis Chronicles）
- 亨利·克魯斯（Henry Clews）：紐約經紀商行，1873 年庫克失敗後隨即倒閉，是連鎖倒閉的第二環。（來源：en-wiki「Panic of 1873」）
- 尤利西斯·S·格蘭特（Ulysses S. Grant，1869–77）：簽署《公共信貸法》（1869）；1869-09-24 下令釋放 400 萬美元黃金打破黃金圈；1874 年否決費里通膨法案；其政府以「癱瘓與失信」收場（Nevins 評語）。（來源：en-wiki「Black Friday (1869)」；「Panic of 1873」；「Long Depression」）
- 鮑威爾（George S. Boutwell）：1869–73 財務部長；售金還債政策；雙週售金以電報公開；1873 年辭任競選參議員。（來源：en-wiki「Black Friday (1869)」）
- 古德與菲斯克（Jay Gould、James Fisk）：1869 黃金圈主謀；以柯賓（Abel Corbin，格蘭特小姨子之夫）的總統關係為槓桿；逃過刑事追訴（1870 年 Garfield 國會調查洗清格蘭特，但譴責古德與柯賓；坦慕尼環（Tweed Ring）法官庇護）；菲斯克 1872-01-06 遭槍擊身亡。（來源：en-wiki「Black Friday (1869)」）
- 麥卡洛克（Hugh McCulloch）：1865–73 財務部長；收縮主義——認為恢復硬幣兌付的最好方式是「盡快撤回綠背」，直至國會叫停（國會認為其收縮正在傷害經濟）。（來源：en-wiki「Panic of 1873」）
- 約翰·謝爾曼（John Sherman）：1866–67 財務部長（1866《收縮法》最大推手，見 ch03）；1873 年以參議員身分提出《鑄幣法》；1875–77 海斯（Hayes）政府財務部長，推動復匯，1879-01-01 前累積 1.33 億美元兌付準備。（來源：en-wiki「Coinage Act of 1873」；「Specie Payment Resumption Act」；ch03）
- 柯利斯·P·亨廷頓（Collis P. Huntington）等鐵路領袖：軟貨幣陣營，公開呼籲多發綠背。（來源：en-wiki「Specie Payment Resumption Act」）
- Crédit Mobilier 醜聞當事人：聯合太平洋鐵路（Union Pacific）與建設公司 Crédit Mobilier of America，1864–67 年間「兩段式詐欺」侵吞東段（密蘇里河至猶他領地）建設利潤；「賊股息」（thief's dividend）受領者包括副總統斯庫勒·考爾法克斯（Schuyler Colfax）、參議員約翰·羅根（John A. Logan）、戰爭部長約翰·A·迪克斯（John A. Dix）、歐克斯·埃姆斯（Oakes Ames）、湯瑪斯·杜蘭特（Thomas Durant）等。（來源：en-wiki「Crédit Mobilier scandal」）
- 亨利·維拉爾（Henry Villard）：德裔，前戰爭記者與報人；1871–73 在歐洲（尤其新統一的德意志帝國）為西部鐵路募資；1881–84 任北太平洋第 6 任總裁。（來源：en-wiki「Northern Pacific Railway」）
- 約翰·傑伊·諾克斯（John Jay Knox）：副幣務長；奉財長鮑威爾（Boutwell）之命起草 1873 年《鑄幣法》；法案在國會審議了大約三年，「很少被公開提及，但並未隱藏它將確立金本位」。（來源：en-wiki「Coinage Act of 1873」）
- 威廉·M·斯圖爾特（William M. Stewart，內華達參議員）：1889 年在一篇演說中七次稱《鑄幣法》是一樁「罪行」（他本人 1873 年投了贊成票）。（來源：en-wiki「Coinage Act of 1873」）
- 貝塞爾·亨利·斯特勞斯伯格（Bethel Henry Strousberg，1823–1884）：普魯士奈登堡（Neidenburg）出身的德意志猶太實業家；以槓桿資本在德意志帝國境內大興鐵路，鐵路帝國一度僱用 10 萬名工人。（來源：de-wiki「Gründerkrach」；en-wiki「Bethel Henry Strousberg」）
- 格爾松·馮·布萊希羅德（Gerson von Bleichröder）：俾斯麥的銀行家；1873 年復甦過程中出現反猶成分：德國工人協會（ADAV）報紙《Neuer Sozial-Demokrat》發表文章指責崩盤是其之過，10 月 29 日的文章稱他為「俾斯麥的猶太人」。（來源：en-wiki「Panic of 1873」）
- 施特凡·克格列維奇（Stephan Keglevich）：維也納人，曾任哈布斯堡王室金庫長（1842–48）的加博爾·克格列維奇（Gábor Keglevich）的親屬；1845 年共同創立一家為匈牙利工業擴張融資的金融聯合；1873 年破產。（來源：en-wiki「Panic of 1873」）
- 喬治·史蒂芬（George Stephen）與唐納德·史密斯（Donald Smith）：庫克破產後以低價收購庫克持有的北太平洋股份，完成加拿大太平洋鐵路。（來源：en-wiki「Jay Cooke」）
- 愛爾文·費雪（Irving Fisher）：以債務-通縮解釋 1873 年恐慌的嚴重性（恐慌觸發去槓桿螺旋）。（來源：en-wiki「Long Depression」）
- 米爾頓·弗里德曼（Milton Friedman）與安納·史華茲（Anna Schwartz）：貨幣史數字（1869–79 實質 +6.8%/年等）；批評「1873 年之罪」；（來源：en-wiki「Long Depression」）
- 倫迪格斯·菲爾斯（Rendigs Fels）：1879 年復金本位「為通縮設定下限」。（來源：en-wiki「Long Depression」）
- 麥瑞·羅斯巴德（Murray Rothbard）：「長蕭條」是「被誤解的衰退」——實質工資與產出其實在增加。（來源：en-wiki「Long Depression」）
- 大衛·艾姆斯·韋爾斯（David Ames Wells，1891）：第二次工業革命的過渡成本／產能過剩論述。（來源：en-wiki「Long Depression」）
- 艾倫·涅夫斯（Allan Nevins）：格蘭特政府收場評語「沒有任何其他政府在如此癱瘓與失信中收場」。（來源：en-wiki「Long Depression」，引 Nevins）
- 奧托·馮·俾斯麥（Otto von Bismarck）：德意志帝國宰相；其政府把法國賠款主要用於贖還國債，德意志帝國同樣受崩盤波及（受創程度輕於奧匈帝國）。（來源：de-wiki「Gründerkrach」）
- 亨利·M·泰勒（Henry M. Teller）：科羅拉多州參議員；1890-07-10 在國會辯論中首次使用「1873 年之罪」（Crime of 1873）一詞。（來源：en-wiki「Coinage Act of 1873」）

## 比較與分析素材

- 1873 年恐慌被英文來源稱為「第一個真正的國際性危機」（the first truly international crisis）。（來源：en-wiki「Long Depression」）
- 三向傳導迴路：維也納（1873-05）→ 紐約（1873-09-18/19）→ 歐洲第二波（維也納第二次恐慌、德國銀行倒閉）——危機「環行」一圈。（來源：de-wiki「Gründerkrach」；en-wiki「Long Depression」）
- 傳導機制：金本位（固定匯率）＋世界債券市場（北太平洋債券經維拉爾網絡在歐洲尤其德國募集、德文來源記德國私人資本流入維也納）＋電報網絡——1857/1866 的三條傳導管道（見 ch03 §7）在 1873 年首次覆蓋「全球」而非「大西洋兩岸」。（來源：en-wiki「Northern Pacific Railway」；de-wiki「Gründerkrach」；ch03 §7）
- 蘇伊士成因：蘇伊士運河 1869 年通航是 1873 年恐慌成因之一——遠東商品原經好望角運至英國倉庫，通航使英國轉口貿易受損；英國自 1873 年起進入約二十年經濟停滯。（來源：en-wiki「Panic of 1873」）
- 阿哈邁德（Ahamed，en-wiki「Panic of 1873」轉引）：德國各邦償清了債務、贖回了全部公債，持有公債的儲蓄者手裡只剩下現金——「問題是這些現金怎麼辦」；答案是股市，資金湧入鐵路、工廠、碼頭與蒸汽船投機，與美國不可持續擴張的產業完全重疊。（來源：en-wiki「Panic of 1873」，引 Ahamed）
- 德國放寬的公司法刺激了上市潮，新企業成立與老企業改組並進。（來源：en-wiki「Panic of 1873」）
- 維也納與柏林兩熱點的結構相同：準銀行機構（各邦儲蓄銀行、抵押銀行與建設銀行）＋房地產抵押＋股票投機；抵押品正是被同一批資本推高價格的樓房與鐵路股。（來源：法文「Crise bancaire de mai 1873」）
- 《鑄幣法》因果鏈：廢銀→銀價崩落→礦區危機；貨幣供給減少→利率上升→農民受損；貨幣政策不穩定感→投資人迴避長期債券→後期鐵路債券（北太平洋）賣不掉——「問題因已進入後期的鐵路熱潮而加劇」。（來源：en-wiki「Panic of 1873」）
- 廢銀與銀價機制：美國與德國相繼廢銀，世界對銀的貨幣需求驟減；德國廢銀後拋售銀庫存，銀價崩落，被貿易銀元與維吉尼亞城銀礦新發現部分抵消。（來源：en-wiki「Coinage Act of 1873」；「Panic of 1873」）
- 投機結構：土地撥賜（4,000 萬英畝，主權信用背書）→鐵路債券（包銷商賺價差）→外資（德國市場，維拉爾網絡）→庫克公司資產負債表（吸收未售債券）→存款（紐約、費城兩城）。任何一環斷裂即為系統性危機。（來源：en-wiki「Long Depression」；「Northern Pacific Railway」；「Jay Cooke & Company」）
- 長蕭條機制三說：貨幣論（弗里德曼：「1873 年之罪」——廢銀＋金本位壓縮世界貨幣供給）；結構論（韋爾斯：第二次工業革命過渡成本、產能過剩）；債務-通縮論（費雪：去槓桿螺旋）。（來源：en-wiki「Long Depression」）
- 反證：1869–79 實質國民生產 +6.8%/年、貨幣供給 +2.7%/年（弗里德曼與史華茲）——「長蕭條」是價格通縮而非產出崩潰；1873–79 的 65 個月 NBER 收縮是「商業活動」意義的收縮。（來源：en-wiki「Long Depression」）
- 硬貨幣 vs 軟貨幣政治：債權人（復匯＝補償十年貶值損失）vs 農民勞工（通膨＝稀釋債務）；復匯＝債務實際值上升最多 50%；1874 大選（民主黨取得眾議院）→1875 法案（lame-duck 共和黨國會）→1878 布蘭德-艾利森法（Bland-Allison Act，國會推翻海斯否決，要求財政部每月購買白銀）→1896 年《黃金十字架》（Cross of Gold，布萊恩）。（來源：en-wiki「Specie Payment Resumption Act」；「Coinage Act of 1873」；「Long Depression」；ch03 §8）
- 1873 vs 2008：觸發（包銷商賣不掉債券而倒閉）；投機載體（土地＋鐵路 vs 住房＋房貸證券，皆為主權信用背書資產）；傳導（電報＝天級 vs 電子交易＝毫秒級）；制度回應（無最後貸款人、NYSE 關閉 10 天 vs 聯準會全面救市）；時長（65 個月 vs 18 個月）。（來源：en-wiki「Panic of 1873」；「Long Depression」；「Jay Cooke & Company」）
- 1929 對照：1873 年 Depression 一度被稱為「Great Depression」，該稱謂隨 1929 年崩盤而讓位。（來源：en-wiki「Panic of 1873」）
- 金本位的「通縮下限」：1879 年復金本位結束通縮、但固定了 1873–79 通縮的分配成本（菲爾斯）。（來源：en-wiki「Long Depression」，引 Fels）
- 1873 年後的全球保護主義轉向：1879 年德國關稅、法國第三共和國保護主義、1887 年法意關稅戰；1870–90 全球商船隊無顯著增長。（來源：en-wiki「Long Depression」）
- 南方政治：雄心勃勃的南方鐵路建設計劃破產，使大多數州陷入重債與重稅，南方各州一個接一個落入民主黨之手。（來源：en-wiki「Panic of 1873」）
- 1877 年妥協（Compromise of 1877）：1876 年總統選舉的和解；重建時代終結。（來源：en-wiki「Compromise of 1877」）
- 《復匯法》＝硬貨幣與軟貨幣兩陣營的妥協（謝爾曼-埃德蒙茲（Edmunds）妥協）：硬貨幣陣營得到「日期」（1879-01-01），軟貨幣陣營得到「空間」（自由銀行條款）；弗里德曼與史華茲：法案的主要經濟產出是「信心」——市場需要一個可信的日期。（來源：en-wiki「Specie Payment Resumption Act」）
- 《馬丁斯堡政治家報》（Martinsburg Statesman）：「寧可被子彈打死，也不願被一寸一寸餓死」（starve to death by inches），記下 1877 年罷工中一名工人的話。（來源：en-wiki「Panic of 1873」）
- 1873 為「原型」：第一次以「全球化資本」為主角的崩盤；第一次完成「環行」傳導；第一次開啟「通縮時代」（長蕭條）而非「衰退」（1857/1866 型）。（來源：en-wiki「Long Depression」；de-wiki「Gründerkrach」）

## 待核實項（研究後應清空；寫入章節時不得保留未核實數字）

1. 庫克公司倒閉日期：任務書預設 1873-10-18。核實結果：五個獨立來源一致為 09-18/09-19——en-wiki「Panic of 1873」「On 18 September, the firm declared bankruptcy」；en-wiki「Northern Pacific Railway」「Cooke and Company went bankrupt on September 18, 1873」；NY Fed Crisis Chronicles「on September 18, 1873, it suspended withdrawal of deposits」（並引 1873-09-19《紐約時報》當日記述）；fr-wiki「panique du 18 septembre 1873」；en-wiki「1873 in the United States」「September 18 – The New York stock market crash triggers the Panic of 1873」。且 1873-10-18 為週六（Python 驗證），銀行停兌於週六不合邏輯。已決：不採 1873-10-18；採 1873-09-18（週四）為停止兌付日、1873-09-19（週五）為紐約交易所衝擊日（德文來源稱「危機抵達紐約」，無「黑色星期五」標籤之來源）。
2. 紐約崩盤日期：任務書預設 1873-11?。核實結果：初始衝擊為 09-18/19；NYSE 自 09-20 起關閉 10 天（9 月底重開）；10 月仍有銀行搶存（1873-10-04 第四國家銀行）。已決：不採「11 月」；正文以「9 月 18/19 日為衝擊、9 月 20 日起交易所關閉 10 天、10 月初銀行搶存」為時間軸。
3. NYSE 重開日：de-wiki 記 09-29；en-wiki「Panic of 1873」記「自 9 月 20 日起關閉 10 天」（＝09-30）。已決：說法不一；正文以定性「9 月底重開」表述，不寫具體重開日。
4. 維也納崩潰起始日：en-wiki「Panic of 1873」記 05-09；en-wiki「Long Depression」記「5 月 8 日開始，至 5 月 10 日交易所停市，三日後（5 月 13 日）重開」。已決：正文以「1873 年 5 月 8 至 10 日維也納證券交易所崩潰（5 月 9 日最劇烈，德文來源稱該日為『黑色星期五』），交易所停市，5 月 13 日重開」表述，起始日 08/09 之微差在 §9 註記。
5. 克利夫蘭鐵路罷工日期：任務書預設 1873-07-16。核實結果：多輪檢索未獲免費可靠來源（en-wiki 無獨立條目；「1873 in the United States」未載；「Coal miners' strike of 1873」為 1 月 1 日起的煤礦罷工，屬不同事件）。已決：不採 07-16 具體日期；正文改定性為「1873 年夏，克利夫蘭等工業城市鐵路工人減薪罷工」，不給具體日期；俄亥俄煤田罷工（1873 年 1 月 1 日，6,000 餘名工人，25% 減薪）有源，可給日期。
6. 庫克歿日：en-wiki 記 1905-02-16；1911 EB 記 1905-02-18。已決：說法不一；正文僅給歿年（1905），不給具體日期。
7. en-wiki「Panic of 1873」載「北太平洋鐵路已向庫克公司借逾 150 萬美元（more than $1.5 million）無法償還」：該數字與公司業務規模明顯不符（疑似原文筆誤）。已決：不採該數字；改定性「庫克公司曾向北太平洋大額放款，該路無以為償」。
8. en-wiki「Panic of 1873」載「1873 年 9 月庫克公司即將取得 3 億美元政府貸款」：數字明顯不合理（當時國債約 20 億級）。已決：不採，正文不使用。
9. en-wiki「Panic of 1873」載羅特席德家族與巴林銀行「1850 年後發行全球 70% 的債券」：單一來源、數字偏高。已決：正文採定性「當時世界最大的兩家債券發行機構」，數字註「一說約七成」。
10. 「黑色星期五」多指涉已釐清：1869-09-24（黃金圈潰敗，首用）、1873-05-09（維也納，de-wiki）；1873-09-19 之「黑色星期五」標籤於 de-wiki/en-wiki/fr-wiki/NY Fed 皆無來源，不採用。已決：正文對 09-19 僅記「危機抵達紐約」。
11. en-wiki「Jay Cooke & Company」載「庫克因銷售困難最終持有該路 75%（wound up owning 75 percent of the company）」：上下文 the company 指北太平洋鐵路、owning 即股權。已決：採；正文 §3 記「庫克因銷售困難最終持有該路 75% 股權」。
12. 維吉尼亞城（Virginia City）銀礦「新發現」之年份：正文僅定性「引發新一輪開礦投資」，未標 1873 年（en-wiki 未給年份）；若日後補年份來源，同步更新 §3。

無未決項。
