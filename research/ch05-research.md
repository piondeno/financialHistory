# ch05 研究筆記（1873–1893）

方法說明：本章研究分兩輪完成（2026-09）。方法：英文／法文 Wikipedia 全文擷取（en/fr）＋直接頁面擷取；NY Fed Liberty Street Economics（Crisis Chronicles 系列，Klitgaard & Narron，2016-05-13）；Federal Reserve History（Richardson & Sablik）；Yale New Bagehot Project 案例研究；以 Python 交叉驗證關鍵日期。主要來源：en-wiki「Long Depression」「Depression of 1882–85」「Panic of 1884」「Union générale」「Panic of 1893」「Baring crisis」「Barings Bank」「Dakota boom」「Gold standard」「Bank Charter Act 1844」「Specie Payment Resumption Act」「Bland–Allison Act」「Sherman Silver Purchase Act」「German tariff of 1879」「Méline tariff」「Protectionism」「Populist Party」「1892 United States presidential election」「Standard Oil」「Trust (business)」「Gilded Age」「Industrial Revolution in the United States」「J.P. Morgan」「Drexel Burnham Lambert」「1889 in the United States」「1890 in the United States」「Deflation」「Cross of Gold speech」；fr-wiki「Grande Dépression」；NY Fed Liberty Street Economics「Crisis Chronicles: Gold, Deflation, and the Panic of 1893」（Klitgaard & Narron，2016-05-13）；Fed History「Banking Panics of the Gilded Age」（Richardson & Sablik）；Yale New Bagehot Project「United States: New York Clearing House Association, the Panic of 1890」；本書第三章／第四章（ch03/ch04）回指來源。

## 關鍵事件與日期

- 1871-12-04：德國通過把帝國新金幣十分之一命名為馬克、授權鑄造 10、20 馬克金幣之法律；1873-07-09《鑄幣法》（Münzgesetz）使馬克成為帝國貨幣單位、取代各邦貨幣；1875-09-22 帝國條例規定 1876-01-01 正式生效——德國轉入金本位，是「古典金本位時代」（classical gold standard，通算 1821–1931）的開端事件。（來源：en-wiki「Gold standard」）
- 1873：法國賠款 50 億金法郎（＝40.5 億金馬克，折約 1,451 公噸黃金）；1873-09-05 法國付清賠款，巴黎造幣廠隔日即限制鑄造銀幣；法國銀聯（LMU）1873 年停止無限鑄造 5 法郎銀幣。（來源：en-wiki「Gold standard」）
- 1873-04-01：美國《鑄幣法》生效（「1873 年之罪」），見 ch04 §2；同年內華達州康斯托克礦脈（Comstock Lode，1859 年發現）進入大規模開發期。（來源：en-wiki「Gold standard」「Coinage Act of 1873」，ch04 已引用）
- 1873-10 至 1879-03：NBER 計量收縮期 65 個月，為 NBER 體系最長收縮（大蕭條 43 個月）；1873–79 間 18,000 家企業破產（含 89 家鐵路）；1878 年失業率峰值 8.25%。（來源：en-wiki「Long Depression」）
- 1874：民主黨取得眾議院（見 ch04 §5）；1875-01-14《硬幣兌付復原法》、1878-12 綠背平價、1879-01-01 復兌（見 ch03 §6，本章不重述）。（來源：en-wiki「Long Depression」「Specie Payment Resumption Act」）
- 1876：德國「稅收與經濟改革協會」與「德國工商業中央協會」成立，關稅改革運動組織化；同年底「鋼鐵與黑麥之婚」（marriage of iron and rye，Carr 1934 年用語）——工業與容克地主結成保護主義聯盟。（來源：en-wiki「German tariff of 1879」）
- 1878 秋：204 名帝國議會議員（中樞 87、保守派 36、國家自由派 27）組成跨黨派保護主義集團；1878-10 中樞黨（Centre Party）宣布支持關稅。（來源：en-wiki「German tariff of 1879」）
- 1879-02-24：「德國地主大會」（top 250 地主）通過保護主義綱領。（來源：en-wiki「German tariff of 1879」）
- 1879-03-31：俾斯麥（Bismarck）與中樞黨領袖溫德霍斯特（Windthorst）達成交易：放寬文化鬥爭（Kulturkampf）換取中樞黨支持關稅。（來源：en-wiki「German tariff of 1879」）
- 1879-07-09：帝國議會以 211 比 122 通過「弗蘭肯施泰因條款」（Franckenstein clause）；1879-07-12 關稅法案以 100 票多數通過。條款內容：中央政府關稅與菸草稅收入上限 1.3 億馬克，超額部分歸邦（州）。（來源：en-wiki「German tariff of 1879」）
- 1879-05-19：德國停止拋售銀庫存（此前賠款換來的黃金流入使德國成為金本位國）。（來源：en-wiki「Gold standard」）
- 1879：俾斯麥關稅生效，德國由自由貿易轉保護主義；法國推出弗雷西內計畫（plan Freycinet，全國交通建設）。（來源：en-wiki「German tariff of 1879」；fr-wiki「Grande Dépression」）
- 1872：洛克菲勒（Rockefeller）加入「南方改良公司」（South Improvement Company）——秘密運輸協議，可對競爭對手輸送之石油收取回扣；說服克利夫蘭煉油廠以現金或股票出售給 Standard Oil。（來源：en-wiki「Standard Oil」）
- 1878–1887：達科他淘金潮與土地熱（Dakota Boom）：達科他領地人口 11,766（1870）→32 萬以上（1890）；農戶 1,700 →5 萬以上；城鎮 6 →310；小麥產量至 1880 年代末僅次於明尼蘇達州；1887 年為頂峰（乾旱、小麥跌價、信貸過度）。（來源：en-wiki「Dakota boom」）
- 1882：Standard Oil Trust 成立（41 名受託人、40 家公司證券集中）；此前 1870 年洛克菲勒將 1863 年合夥改組為 Standard Oil（Ohio，資本 100 萬美元）；1904 年控制美國 91% 煉油與 85% 最終銷售；「Standard Oil 的組織概念如此成功，其他巨型企業相繼採用這種『托拉斯』形式」。（來源：en-wiki「Standard Oil」）
- 1882-01：法國聯合銀行（Union Générale）停止兌付——該行為天主教君主立憲色彩之銀行，1875 年創於里昂，1878-06-03 正式改組（資本 2,500 萬法郎增至 5,000 萬），銀行家邦圖（Bontoux，羅特席德兄弟銀行前部門主管、奧地利鐵路公司前董事）1878 年接掌；停兌後邦圖與費德爾（Feder）被判五年監禁，羅特席德家族、巴黎—荷蘭銀行（Banque de Paris et des Pays-Bas）等大財團設 2,000 萬法郎特別基金救援。同年巴黎股市崩潰。（來源：en-wiki「Union générale」；en-wiki「Long Depression」）
- 1882：美國鐵路建設由 11,568 英里（一說 11,569）（1882）轉入下滑；鐵路「費率戰」（rate wars）與管理失當使獲利與投資吸引力轉弱。（來源：en-wiki「Depression of 1882–85」）
- 1884-05：馬林國家銀行（Marine National Bank，詹姆斯·費雪（James Fish））與證券商格蘭特與沃德（Grant & Ward，斐迪南·沃德（Ferdinand Ward）＋尤利西斯「巴克斯」·格蘭特（Ulysses "Buck" Grant Jr.））破產——沃德以月息 10% 向存戶吸金（龐氏結構）、向市府借款 160 萬美元後逃往加拿大。（來源：en-wiki「Panic of 1884」）
- 1884：第二國家銀行（Second National Bank）遭搶存——銀行總裁約翰·切斯特·伊諾（John Chester Eno）挪兌逾 300 萬美元潛逃，其父艾莫斯·伊諾（Amos Eno）補足窟窿；大都會國家銀行（Metropolitan National Bank）遭不實傳言（稱其總裁挪用銀行資金投機鐵路證券，後被證實不實）引發搶存，紐約結算所（NYCH）審計後認定其資力健全、公開廣告並貸予 300 萬美元，恐慌遂止——危機限於紐約及其結算所網絡（紐澤西、賓州）。（來源：en-wiki「Panic of 1884」；Fed History「Banking Panics of the Gilded Age」）
- 1882–1885：NBER 計 38 個月，為第三長收縮；1882–84 年間逾 1.5 億美元黃金流出美國；1884-07-01 至 1885-07-01 約 5% 工廠與礦場完全停業、另有 5% 部分停業；谷底約 100 萬工人失業。（來源：en-wiki「Depression of 1882–85」「Panic of 1884」）
- 1884：法國德卡茲維爾「大礦工罷工」（Decazeville），煤價與工資崩落背景下的勞資衝突。（來源：en-wiki「Union générale」）
- 1887：美國《州際商務法》（Interstate Commerce Act），禁止鐵路低於成本價銷售與市場分割——長蕭條期間罕見的國家監管立法。（來源：fr-wiki「Grande Dépression」）
- 1889-04-22：奧克拉荷馬領土「土地衝」（Oklahoma Land Rush）——奧克拉荷馬城（Oklahoma City）與古特里（Guthrie）兩城於數小時內出現逾萬人。（來源：en-wiki「1889 in the United States」）
- 1889：北達科他、南達科他、蒙大拿、華盛頓四州同入聯邦（自 1788 年來最繁忙的建州年）。（來源：en-wiki「1889 in the United States」）
- 1889-12：美國農民聯盟（Farmers' Alliance）聖路易平台（St. Louis Platform）：麥克尤恩（Macune）提出「準財政部計畫」（Sub-Treasury Plan，政府倉庫以農產市值 80% 為限放款）。（來源：en-wiki「Populist Party」）
- 1890：農民聯盟候選人於 1890 年大選中成功當選（與兩黨的保守態度一起，促使聯盟領導人決定建立正式第三黨）；Ocala 要求（Ocala Demands）＝農民聯盟綱領：集體議價、聯邦鐵路費率監管、擴張性貨幣政策、準財政部計畫（聯邦控制的倉庫支援農民）；其他支持措施：雙本位、累進所得稅、參議員直選、縮短工時、郵政儲蓄制度。（來源：en-wiki「Populist Party」）
- 1890-12：農民聯盟大會重申 Ocala 要求；並同意 1892 年初再開大會討論建黨可能（若民主黨不採納其政策目標）；支持建黨者：聯盟主席波爾克（Leonidas L. Polk）、喬治亞報人沃森（Tom Watson）、明尼蘇達前眾議員唐尼利（Ignatius L. Donnelly）。（來源：en-wiki「Populist Party」）
- 1892-02：聖路易農民聯盟大會（貝拉米（Bellamy）與亨利·喬治（Henry George）支持者、綠背／禁酒／反壟斷／勞工改革等多黨人士出席）；唐尼利收尾演說：「我們集會於一個已臨道德、政治與物質破產邊緣的國家……我們要把共和國的政府還給它起源時所在的『平民』之手。我們的門向四面八方敞開……鄉村與城市勞工的利益相同，敵人相同」；大會隨後決定建立「人民黨」（People's Party），並於 07-04 在奧馬哈開提名大會；記者稱之為「Populist Party」。（來源：en-wiki「Populist Party」）
- 1892-07-04：奧馬哈大會；初領頭者波爾克於大會數週前病逝；威弗（前北軍將軍、1880 年綠背黨總統候，愛荷華）＋菲爾德（前南軍軍官，維吉尼亞）；《奧馬哈平台》：準財政部及其他農民聯盟長期目標、累進所得稅、參議員直選、縮短工時、限制移民、鐵路與通信線國營。（來源：en-wiki「Populist Party」）
- 1890-07-02：《雪曼反托拉斯法》（Sherman Antitrust Act）成為法律（參議院 51 比 1、眾議院 242 比 0）——針對 1870–90 年代托拉斯（trust）壟斷之反壟斷立法，禁止一切「限制貿易」之契約與陰謀。（來源：en-wiki「1890 in the United States」「Standard Oil」；fr-wiki「Grande Dépression」）
- 1890-07-10：科羅拉多參議員泰勒（Teller）在國會首次使用「1873 年之罪」一詞（見 ch04 §2）。（來源：en-wiki「Coinage Act of 1873」，ch04 已引用）
- 1890-07-14：《雪曼購銀法》（Sherman Silver Purchase Act）由哈林（Harrison）簽署：財政部每月強購 450 萬盎司銀（參議院 1890-06-17 以 42 比 25 通過、眾議院 06-25 以 145 比 28 通過）；購銀以「可兌銀或金」的紙鈔支付；法案與麥金利關稅（McKinley Tariff，平均關稅升至 49%）打包。（來源：en-wiki「Sherman Silver Purchase Act」；fr-wiki「Grande Dépression」）
- 1890 秋：阿根廷「公園革命」（Revolución del Parque），總統塞爾曼（Miguel Juárez Celman）被迫下台；阿根廷債務危機爆發。（來源：en-wiki「Barings Bank」）
- 1890-11-06：英格蘭銀行（BoE）獲悉巴林銀行（Barings）困境（未公開）；11-07 貼現率由 5% 升至 6%（市場「普遍出現戒心與警覺」）；11-15 對外公佈。（來源：Yale New Bagehot Project「The Panic of 1890」；en-wiki「Baring crisis」）
- 1890-11-11：證券商迪克、豪威（Decker, Howell & Co.）現金斷鏈；其欠美國銀行（Bank of North America，NYCH 會員、費城）140 萬美元，該行結算短缺 90 萬美元；摩根（J.P. Morgan）集九家 NYCH 銀行行長（含本人）同意以證券為抵押共同墊付該行 90 萬美元結算缺口；NYCH 當日授權發行結算所貸款憑證（CLC）。（來源：Yale New Bagehot Project「The Panic of 1890」；Fed History）
- 1890-11-12：NYCH CLC 首次發行；12-22 最後一批；至 1891-02-07 全數贖回。峰值 1,521 萬美元（1890-12-12）；24 家會員行（共 66 家）動用；利率 6% 加月費 0.25%、抵押至少 25% 折價。（來源：Yale New Bagehot Project）
- 1890-11-19：費城、波士頓結算所同步發行 CLC；峰值分別 887 萬、507 萬美元；波士頓一個月內結束，費城發行持續至 1891-05。（來源：Yale New Bagehot Project，引 Cannon 1910a）
- 1890 全年：股價自 5 月至 11 月平均下跌約一半（NYT 1890a）；1890 年銀行倒閉共 18 家（Wicker 2000）；紐約無一銀行停止兌付存款人；1890 年危機被後世定性為「有限範圍」（limited scope）的「萌芽性恐慌」（incipient panic）。（來源：Yale New Bagehot Project；Fed History）
- 1892：法國梅蘭關稅（Méline tariff）通過——「法國第三共和國最重要的經濟立法」，以保護主義終結 1860 年《科本–謝瓦利埃條約》（Cobden–Chevalier）開啟的自由貿易時代；命名自法國第 65 任總理朱爾·梅蘭（Jules Méline）。（來源：en-wiki「Méline tariff」）
- 1892-11：美國總統大選：投票率 75.8%；克利夫蘭（Cleveland）46.0%、哈里森（Harrison）43.0%、威弗（Weaver）8.5%（《Populist Party》條目；《1892 election》條目作 8.6%，說法不一）；禁酒黨（Prohibition Party）的比德爾（Bidwell）2.2%；選舉人票 277 比 145、威弗 22 票；威弗贏得 100 萬以上選票，勝出科羅拉多、愛達荷、堪薩斯、北達科他四州（22 張選舉人票全數來自此四州；「1892 United States presidential election」條文明載 won the first four of these states）——內戰後首個贏得選舉人票的第三黨；在密西西比河以東、梅森–狄克森線以北的任何州，威弗得票率均未逾 5%；儘管有鄧斯（Debs）、鮑德利（Powderly）等勞工組織者支持，該黨在中西部與東北的城市勞工中未能取得多大支持；此役為在位黨三連敗（1884、1888、1892）之第三次。（來源：en-wiki「1892 United States presidential election」「Populist Party」）
- 1893–94（ch06 背景，僅存檔）：克利夫蘭就任後國家陷入 1893 恐慌；克利夫蘭及其民主黨盟友廢除雪曼購銀法、通過 Wilson–Gorman 關稅法（小幅降稅）；人民黨譴責克利夫蘭政府的金本位立場，並「憤怒攻擊」其向摩根（J. P. Morgan）領銜的辛迪加購金的決定；考克西之軍（Coxey's Army）等組織在華盛頓抗議遊行；人民黨在數州成長（Goodwyn 估計 1890 年代中期有 25–45% 選民在二十多個州支持該黨）；1894 年大選：民主黨慘敗，人民黨在西部／中西部（共和黨主導）表現不佳、在阿拉巴馬等州獲勝；主席陶貝內克（Taubeneck）主張廢棄《奧馬哈平台》、以雙本位「團結全國改革力量」；1894-12 大會反而把平台擴大（加入市政公用事業市營）；1894–96 民粹浪潮席捲南方棉花與煙草帶（北卡：貧困白人農民與共和黨聯盟，1894 與 1896 控制州議會、1896 贏得州長）。（來源：en-wiki「Populist Party」）
- 1896（ch06 背景，僅存檔）：人民黨提名布萊恩（Bryan），拒絕民主黨副候、改推沃森（Tom Watson）；布萊恩席捲南方與西部、以決定性差距敗給麥金利；1900 年該黨另提巴克（Wharton Barker）與唐尼利，隨後解散。（來源：en-wiki「Populist Party」）
- 1893-02-20：費城與雷丁鐵路（Philadelphia & Reading Railroad）因過度擴張被任命受託人——1893 年恐慌的最早信號（克利夫蘭就任 1893-03-04 前 12 天）。（來源：en-wiki「Panic of 1893」）
- 1893：小麥價格崩落；財政部黃金儲備自 1.9 億美元（1890）跌至約 1 億美元。（來源：en-wiki「Panic of 1893」；Fed History）
- 1893-04-22：財政部長卡萊爾（Carlisle）宣布政府黃金儲備降至異常低點；04-24 克利夫蘭發聲強調只以黃金兌付（NYT 1893-04-24）；兩週內股市崩潰、5 月恐慌全面爆發（本章止於「1893 前夜」，1893 年 5 月以後屬 ch06）。（來源：NY Fed「Crisis Chronicles: Gold, Deflation, and the Panic of 1893」）
- 1893-08：國會以壓倒性票數廢除《雪曼購銀法》（NYT 1893-08-30：「華盛頓昨夜最沮喪的人，是那些與銀運動結盟的人」）。（來源：NY Fed；en-wiki「Panic of 1893」）
- 1896：布萊恩（Bryan）《黃金十字架》（Cross of Gold）——本章至多回指一句，其內容屬 ch06。（來源：NY Fed；en-wiki「Cross of Gold speech」）
- 1899/1897–99：法國衰退終結（en-wiki「Long Depression」稱法國衰退延至 1897–99）；英國「長蕭條」（1873–96）終結。（來源：en-wiki「Long Depression」）
- 1907-09-30：德國 3 馬克塔勒（thaler，1879 年起與金馬克按 1:3 並存之「跛足標準」limping standard）退出法償。（來源：en-wiki「Gold standard」）
- 1913：凱因斯（Keynes）回溯性提出金本位「遊戲規則」（rules of the game）說——實為事後概括而非當時共識。（來源：en-wiki「Gold standard」）

## 關鍵數據

- NBER 收縮：1873-10 至 1879-03 共 65 個月（最長；大蕭條 43 個月）；1882–85 共 38 個月（第三長）。（來源：en-wiki「Long Depression」「Depression of 1882–85」）
- 通縮（Friedman，轉引自 Grant's Interest Rate Observer）：1875–96 美國年均物價 −1.7%、英國 −0.8%。（來源：en-wiki「Deflation」）
- 成長率（Tylecote，1873–90 年均，%）：德國 2.9、英國 1.7、美國 4.7、法國 1.3、瑞典 3.1、意大利 0.9；對比 1850s–73：德國 4.3、英國 3.0、美國 6.2、法國 1.7。（來源：en-wiki「Long Depression」）
- GNP（Kennedy，1960 年億美元，1870→1890）：英國 19.6→29.4、法國 16.8→19.7、美國（同期大幅上升）、俄羅斯 22.9→21.1。（來源：en-wiki「Long Depression」）
- 價格：小麥 1894 年約為 1867 年的三分之一（Hobsbawm）；棉花 1872–77 下跌近 50%；鐵價 1870–90 減半。（來源：en-wiki「Long Depression」）
- 產量（1870–90）：鐵 1,100 萬噸→2,300 萬噸；鋼 50 萬噸→1,100 萬噸（二十倍）。（來源：en-wiki「Long Depression」）
- 1882–85：鐵路年新建 2,665 英里（1878）→11,568（1882）→6,741（1883）→2,866（1885）；約 5% 工廠與礦場完全停業（1884-07 至 1885-07）；谷底約 100 萬工人失業。（來源：en-wiki「Depression of 1882–85」）
- 1873–79 通縮：18,000 家企業破產（含 89 家鐵路）；1878 年失業率峰值 8.25%；名義工資 1870 年代跌約 1/4（賓州達 1/2）。（來源：en-wiki「Long Depression」）
- 實質工資：1860–90 增幅 40%（一說 60%，同一條目兩說）；普查局 1892 年：工業工人平均年工資 380 美元（1880）→564 美元（1890）（+48%）；Long（1914 年美元）：375（1870）/395（1880）/519（1890）/573（1900），三十年 +53%。（來源：en-wiki「Gilded Age」）
- 專利：1860–90 共 50 萬件（超過此前 70 年總和的十倍）。（來源：en-wiki「Gilded Age」）
- 勞動力組織：騎士團（Knights of Labor）峰值 70 萬（1880 年代）→1890 年不足 10 萬。（來源：en-wiki「Gilded Age」）
- 農業：農戶 200 萬（1860）→600 萬（1905）；農業人口 1,000 萬（1880）→3,100 萬（1905）；農地價值 80 億美元（1860）→300 億（1906）。（來源：en-wiki「Gilded Age」）
- 財富集中（1860–1900）：前 2% 持有逾 1/3 財富、前 10% 約 3/4、後 40% 接近於零。（來源：en-wiki「Gilded Age」）
- 美國佔世界製造業產值：23%（1870）→36%（1913）（Irwin）；1870 年代中期關稅成本約為 GDP 的 0.5%。（來源：en-wiki「Industrial Revolution in the United States」）
- 金本位機制：1717 年牛頓（Newton）把金銀比定得過低（事實金本位之始）；法國以無限鑄造較廉金屬將比值錨定 15.5；美國法定雙本位至 1900（比值 15.0，1837 年修訂 15.99）；1876-01-01 德國金馬克；1879-05-19 德國停售銀；金銀比 18（約 1880）→20（1880s）→30 以上（1890 後）；1893 年印度盧比 10.69 克＝16 便士（比值 21.9）；1906 年海峽元（Straits dollar）。（來源：en-wiki「Gold standard」）
- 《布蘭德–艾利森法》（Bland–Allison Act）：眾議院 1877-11-05 以 163 比 34、參議院 1878-02-15 以 48 比 21 通過；海斯（Hayes）1878-02-28 否決；眾議院 196 比 73、參議院 46 比 19 覆議；財政部每月強購 200–400 萬美元銀。（來源：en-wiki「Bland–Allison Act」）
- 《雪曼購銀法》：每月 450 萬盎司（約 3,400 萬美元）；銀價 1.16 美元/盎司（1890 初）→0.69（1890 底）→0.60（1894-12）；美國為英國印度之外世界第二大銀買家。（來源：en-wiki「Sherman Silver Purchase Act」）
- 1884 恐慌：1882–84 逾 1.5 億美元黃金流出；伊諾挪兌逾 300 萬美元；NYCH 貸大都會銀行 300 萬美元。（來源：en-wiki「Panic of 1884」）
- 1890 危機：8–9 月信用收縮約 1,400 萬美元；財政部 07-19 至 11-01 以盈餘贖回 9,900 萬美元債券（OCC 1891 年事後評：不夠）；股價 5–11 月平均 −50%；NYCH CLC 峰值 1,521 萬（12-12）、費城 887 萬、波士頓 507 萬；24/66 家會員行動用；1890 年全美的銀行倒閉 18 家（1893 年為 503 家）。（來源：Yale New Bagehot Project；en-wiki「Panic of 1893」）
- 巴林危機：1890 年美股單日跌幅居歷史第 17 位（Morningstar 統計）；阿根廷實質 GDP 1890–91 −11%（Mitchener）。（來源：en-wiki「Baring crisis」）
- 1892 大選：投票率 75.8%；46.0/43.0/8.5（8.6）%；選舉人票 277/145/22（過半數需 223）。（來源：en-wiki「1892 United States presidential election」「Populist Party」）
- 1893 前夜：財政部黃金 1.9 億（1890）→約 1 億（1893）。（來源：Fed History「Banking Panics of the Gilded Age」）
- 1893（對照，屬 ch06）：500+ 銀行（一說 503）、15,000+ 企業破產、失業率峰值 17–19%、工業產值 1892–94 −15.3%（Jalil & Hoffman）。（來源：en-wiki「Panic of 1893」；Fed History）
- 紐約恐慌史：1863–1913 間曼哈頓金融中心共發生八次銀行恐慌；1884、1890、1899、1901、1908 限於紐約及鄰近地區，1873、1893、1907 蔓延全國。（來源：Fed History）
- 《1844 銀行章程法》：7 & 8 Vict. c. 32，1844-07-19 御準（「皮爾銀行法」）；銀行券發行權集中於英格蘭銀行；1,400 萬英鎊「虛擬發行」（fictitious issue）不需金準備，超額發行須以黃金支持；1844-05-06 未發行者不得再發行（發鈔權中央化）。（來源：en-wiki「Bank Charter Act 1844」；ch01 §4 已述 1847 年應用）
- 德國 1879 關稅稅率：小麥/黑麥/燕麥 1 馬克/100 公斤、大麥/玉米 0.5 馬克、麵粉 2 馬克、肉 12 馬克、豬 25 馬克；生鐵 1 馬克、鋼鐵 2–15 馬克、紡織 15–30%；原料免稅。（來源：en-wiki「German tariff of 1879」）
- 關稅大時代：1846 年《穀物法》廢除＝英國決定性轉向自由貿易；1860 年《科本–謝瓦利埃條約》後法、比（1861）、普（1862）、意（1863）、瑞（1864）、瑞典挪威西丹漢薩（1865）、奧（1866）相繼簽約，1877 年前德國幾乎成為自由貿易國；1860 年前已全面自由貿易者：荷、丹、葡、瑞（比、瑞典存疑）。（來源：en-wiki「Protectionism」）
- 美國關稅三時代（Irwin）：1790–1860 以籌收入為主（關稅約佔聯邦收入 90%）；1861–1933 以保護為重。（來源：en-wiki「Protectionism」）
- 麥金利關稅 49%（1890）、57%（1897）；1890 年代僅英國（及荷）維持低關稅。（來源：fr-wiki「Grande Dépression」）

## 關鍵人物與決策

- 俾斯麥（Bismarck）：1879 關稅決策者——以間接稅取代直接稅的財政設計＋文化鬥爭放寬換中樞黨支持＋弗蘭肯施泰因條款分利於邦；「鋼鐵與黑麥之婚」的締造者。（來源：en-wiki「German tariff of 1879」）
- 溫德霍斯特（Windthorst）：中樞黨領袖，1879-03-31 與俾斯麥的交易對象。（來源：同上）
- 弗蘭肯施泰因（Franckenstein）：條款以其命名——中央關稅收入上限 1.3 億馬克，超額歸邦，是中央與邦財政分利的關鍵設計。（來源：同上）
- 朱爾·梅蘭（Jules Méline）：法國第 65 任總理，1892 關稅以其命名；克拉克漢（Clapham）評：工業資產階級、大地主與自耕農利益的匯流。（來源：en-wiki「Méline tariff」）
- 約翰·謝爾曼（John Sherman，俄亥俄參議員、財政委員會主席）：《雪曼購銀法》（S. 2348，1890-01-28 提出）提案人——注意：非起草者，亦非「雪曼」本名之誤傳；法案與麥金利關稅打包通過。（來源：en-wiki「Sherman Silver Purchase Act」）
- 威廉·麥金利（William McKinley，眾議院ways & means委員會主席）：1890 關稅（49%）之父，1897 年再升至 57%（ch06 背景）。（來源：fr-wiki「Grande Dépression」；en-wiki「Sherman Silver Purchase Act」）
- 切斯特·A·亞瑟（Chester A. Arthur）：1878 年簽署《布蘭德–艾利森法》（海斯否決後覆議）；本名法案提出者為眾議員布蘭德（Bland，密蘇里民主黨）＋參議員艾利森（Allison，愛荷華共和黨）——「limping bimetallism（跛足雙本位）」的立法化。（來源：en-wiki「Bland–Allison Act」）
- 拉瑟福德·海斯（Rutherford B. Hayes）：1878-02-28 否決《布蘭德–艾利森法》（被覆議）。（來源：同上）
- 本傑明·哈里森（Benjamin Harrison）：1890-07-14 簽署《雪曼購銀法》。（來源：en-wiki「Sherman Silver Purchase Act」）
- A·J·德雷克塞爾（A. Jay Drexel，1838–1892）：其兄弗朗西斯·M·德雷克塞爾（Francis M. Drexel）1838 年創立德雷克塞爾公司（Drexel & Company）；A. J. 1847 年入夥、1863 年弗朗西斯去世後接掌；1871 年按 J. S. 摩根（J. P. 之父）之託成為 J. P. 摩根的導師，合夥更名 Drexel, Morgan & Co.（1871–1895，1895 年改名 J. P. Morgan & Company）——創造工業公司全國資本市場（此前僅鐵路與運河可發行）、1877 年包銷全美陸軍薪資、1895 年（ch06）為美國政府 bailout。（來源：en-wiki「J.P. Morgan」「Drexel Burnham Lambert」）
- J. P. 摩根（J. P. Morgan）：1890-11-11 集九家 NYCH 銀行行長（含本人）共同墊付美國銀行 90 萬美元結算缺口——「私人最後貸款人」的原型行動。（來源：Yale New Bagehot Project；Fed History）
- 約翰·D·洛克菲勒（John D. Rockefeller）：1863 年合夥、1870 年 Standard Oil（Ohio）成立（資本 100 萬美元）；1872 年南方改良公司；1882 年 Trust（41 名受託人）；1904 年控制 91% 煉油、85% 最終銷售；其「信託」組織形式被其他巨型企業相繼模仿——托拉斯時代的定義者。（來源：en-wiki「Standard Oil」）
- 威廉·里德爾代爾（William Lidderdale）：英格蘭銀行行長，組建巴林救援財團。（來源：en-wiki「Baring crisis」）
- 亨利·赫克斯·吉布斯／安東尼·吉布斯公司（Henry Hucks Gibbs / Antony Gibbs & Sons）：里德爾代爾組建的國際救援財團主導者之一（財團另含羅特席德家族與倫敦各大銀行）。（來源：en-wiki「Barings Bank」「Baring crisis」）
- 斐迪南·沃德（Ferdinand Ward）與「巴克斯」格蘭特（Buck Grant Jr.）：Grant & Ward 的 10% 月息龐氏結構（1884 破產）。（來源：en-wiki「Panic of 1884」）
- 詹姆斯·費雪（James Fish）：馬林國家銀行主（1884 破產）。（來源：同上）
- 約翰／艾莫斯·伊諾（John / Amos Eno）：第二國家銀行挪兌案（1884）。（來源：同上）
- 邦圖（Bontoux）：Union Générale 接掌者（1878；羅特席德兄弟銀行前部門主管、奧地利鐵路公司前董事），1882-01 停兌後與費德爾（Feder）同判五年；羅特席德家族、巴黎—荷蘭銀行等大財團設 2,000 萬法郎特別基金。（來源：en-wiki「Union générale」）
- 詹姆斯·B·威弗（James B. Weaver）：前北軍將軍、1880 年綠背黨候選人；1892 年人民黨總統候選人（逾百萬票、勝出科羅拉多、愛達荷、堪薩斯、北達科他四州、22 張選舉人票）。（來源：en-wiki「Populist Party」「1892 United States presidential election」）
- 詹姆斯·G·菲爾德（James G. Field）：前南軍將領，1892 年人民黨副候——1872 年以來首個贏得選舉人票的南方候選人。（來源：en-wiki「Populist Party」）
- 麥克尤恩（Macune）／威爾（Weir）：Ocala 要求（1890）與準財政部計畫（1889 聖路易平台）之設計者。（來源：en-wiki「Populist Party」）
- 唐尼利（Donnelly）：1892-02 聖路易「平民」演說（「我們集會於一個已臨道德、政治與物質破產邊緣的國家」）。（來源：同上）
- 亨利·M·泰勒（Henry M. Teller）：1890-07-10「1873 年之罪」入國會（見 ch04）。（來源：en-wiki「Coinage Act of 1873」，ch04 已引用）
- 弗里德曼（Milton Friedman）：1.7%/0.8% 通縮數據之原始出處（轉引 Grant's IRO）；其對雙本位的同情見 NY Fed 轉述（「雙本位總比至少一個單本位給出更穩定的物價」）。（來源：en-wiki「Deflation」；NY Fed）
- 威克爾（Elmus Wicker）：1890 年銀行倒閉 18 家 vs 1893 年 503 家；NYCH「以快於歐洲任何央行的準備金權力扮演央行」（轉引 Fed History）；「萌芽性恐慌」定性。（來源：Yale New Bagehot Project；Fed History）
- 戈頓與托爾曼（Gorton & Tallman）：NYCH 的 CLC 發行「本身即足以阻止擠兌」（研究結論）。（來源：Yale New Bagehot Project）

## 比較與分析素材

- 「長蕭條」vs「停滯」：Fels 1949 年定名「長波蕭條」（1873–97），其結論：1882–85（及 1873–79）「是價格與工資的蕭條，而非產出的蕭條」；Tylecote 成長率表顯示美德英法 1873–90 仍正成長（美國 4.7%/年）；Kennedy GNP 表顯示英法絕對值上升；但相對速度明顯放緩（美德英對半減）。故本章採「停滯性通縮」框架：價格與工資下跌、產出仍在成長但放緩，1882–85 與 1893 才是產出蕭條。（來源：en-wiki「Long Depression」「Depression of 1882–85」）
- 通縮機制：黃金供給增速落後於產出增速 → 金價相對上升 → 物價下跌；「通縮懲罰債務人」（deflation punishes debtors）——實質債務負擔上升，借款人削減支出或違約，貸方變富但傾向儲蓄，GDP 受抑（en-wiki「Gold standard」引 The Economist 2009）；Wells 1891 年反論：1879–89 美國貨幣供給 +60%，通縮主因是生產力（「溫和的通縮」）。（來源：en-wiki「Gold standard」「Deflation」）
- 「自動調整」神話：價格— specie 流動機制（price–specie flow）在理論上應自動平復國際失衡，但 1870–90 年代央行行為比機制更強（囤金、停兌銀），失衡未自動修正；1913 年凱因斯的「遊戲規則」是事後概括。（來源：en-wiki「Gold standard」）
- 金本位是「政治選擇」：1873 年德國轉金是俾斯麥的財政決策（賠款以金馬克吸收、停止拋銀），不是 inexorable 的市場力量；美國 1873《鑄幣法》是低調立法（見 ch04 §2）；法國 1873 年限制銀幣是賠款時程的副產品。三國相繼「選」金，銀價崩落是結果而非原因——1870s 銀本位崩解的敘事需修正為「金本位擴張」的敘事。（來源：en-wiki「Gold standard」；ch04）
- 銀的政治經濟學：銀＝鄉村與礦區貨幣（見 ch04），《布蘭德–艾利森法》（1878）是「跛足妥協」（每月 200–400 萬美元，遠不足以影響銀價）；《雪曼購銀法》（1890）放大到 450 萬盎司/月並以「可兌銀或金」紙鈔支付＝不增加金準備的貨幣擴張 → 金本位棄守疑慮 → 囤金與黃金外流 → 1893 前夜（本章 §6 主線）。NYT 1893-05-04：「銀購法引起的普遍不信任，與昨日猛攻有相當關係」。（來源：en-wiki「Bland–Allison Act」「Sherman Silver Purchase Act」；NY Fed）
- 1890 危機＝「央行前夜」的實驗：NYCH 池化會員準備金＋CLC 抵押放貸，Wicker 稱其「準備金權力大於任何歐洲央行」；Gorton & Tallman 結論 CLC「本身即足以阻止擠兌」；1890 年僅 18 家銀行倒閉（1893 年 503 家）、紐約無行停兌——但這是私人自發的、無法律授權的、無常設制度的安排：1907 年（ch07）將重演且險些失控，最終催生聯準會。（來源：Yale New Bagehot Project；Fed History）
- 保護主義是長蕭條的「政策產物」：1879 德、1890 美（49%）、1892 法（Méline）、1897 美（57%）；1860–77 自由貿易網絡（科本–謝瓦利埃）瓦解；僅英（荷）維持低關稅；但 Irwin 估算 1870s 關稅成本僅 GDP 的 0.5%，美國成長主要由資源與開放度驅動——保護主義是「結果」多於「原因」。（來源：en-wiki「German tariff of 1879」「Méline tariff」「Protectionism」「Industrial Revolution in the United States」；fr-wiki「Grande Dépression」）
- 第二次工業革命：50 萬件專利（1860–90）、電（愛迪生直流照明）、西屋空氣制動、貝爾／韋爾 AT&T、奧的斯電梯；美國佔世界製造業 23%（1870）→36%（1913）；企業集中＝卡特爾（德）與托拉斯（美）（Standard Oil 為典型，見 §3）；財富集中（前 2% 逾 1/3）與勞工組織瓦解（騎士團 70 萬→<10 萬）並存。（來源：en-wiki「Gilded Age」「Industrial Revolution in the United States」「Standard Oil」「Trust (business)」）
- 達科他熱＝「第二次鐵路熱」的西部變體：人口 11,766（1870）→32 萬（1890）、農戶 1,700→5 萬、城鎮 6→310；1887 頂峰（乾旱＋跌價＋信貸過度）；1889 年建州（北達科他、南達科他）。（來源：en-wiki「Dakota boom」「1889 in the United States」）
- 1892 大選＝銀金之爭的「中間站」：克利夫蘭（金）勝出但民主黨內銀派坐大；威弗 8.5%＋22 選舉人票＝第三黨首次入局；1896 布萊恩（ch06）是此路線的終局。（來源：en-wiki「1892 United States presidential election」「Populist Party」；NY Fed）
- 1844《銀行章程法》回指（ch01）：英國把發鈔權集中於央行＋金準備錨，1847 年危機一週內平息（ch01 §4/§8）；本章 1890 年的紐約結算所＝「沒有央行時，銀行群體自組央行」的對照案例——同一個制度問題，兩種答案。（來源：en-wiki「Bank Charter Act 1844」；ch01；Yale New Bagehot Project）
- 韋爾斯（David Ames Wells，1891）與弗里德曼（1960s）對 1870s 通縮的解釋分歧：生產力通縮 vs 貨幣/黃金供給不足——本章 §7 以此為分析軸。（來源：en-wiki「Deflation」）

## 待核實項

1. 大綱提及「1890-05-19 費城國家銀行（Philadelphia National Bank）關門」——無可靠來源檢得此事件；1890 年危機之來源敘事全為 11 月事件（Decker Howell → 美國銀行 → NYCH CLC）。已決：不寫入正文。
2. 大綱提及「1890 年 Drexel, Parke & Co. 倒閉」——來源顯示當時摩根之合夥名為 Drexel, Morgan & Co.（1871–1895），1890 年危機未涉該行倒閉。已決：不寫入正文；改寫「摩根 1890 年率九銀行救美國銀行」。
3. 大綱提及「1890 年 NYSE 關閉 11 日」——無可靠來源檢得；NYSE 史上首次 10 日關閉為 1873-09-20（見 ch04 §5）。已決：不寫入正文。
4. 大綱提及「1889–90 維也納崩盤」——維也納崩盤屬 1873（見 ch04 §5）；1889–90 來源無維也納崩盤記錄。已決：不寫入正文。
5. 大綱提及「法國 1880 年通過保護關稅」——fr-wiki「Protectionnisme」條目為通論、en-wiki「Protectionism」條目未檢得 1880 年法國關稅法；來源中法國保護主義軌跡為「第三共和國（蒂爾）轉向 → 1892 梅蘭關稅」。已決：正文以定性描述過渡（1880 年代法國漸進保護化），不引用 1880 年為具體立法年。
6. 大綱提及「鋼軌價格 1880 年 71 美元/噸 → 1884 年 20 美元/噸」——en-wiki「Depression of 1882–85」「Long Depression」均未檢得此組數字。已決：不寫入正文與數據表。
7. 1892 年大選威弗得票率：「1892 United States presidential election」條目 8.6%、「Populist Party」條目 8.5%。已決：正文用 8.5%（引 Populist Party 條目），§9 註「說法不一」。
8. 威弗勝州數：「Populist Party」條目「勝科羅拉多、堪薩斯、愛達荷、內華達四州＋俄勒岡與北達科他選舉人票」；「Panic of 1893」條目「勝五州」。已決（經再核）：「1892 United States presidential election」條文明載 won the first four of these states（科羅拉多、愛達荷、堪薩斯、北達科他——民主黨未提議員候選人之四州），22 張選舉人票全數來自此四州；正文改列此四州。
9. Union Générale：初擷取文本 garbled，經再核 en-wiki「Union générale」來源明確：邦圖與費德爾（Feder）判五年監禁；羅特席德家族、巴黎—荷蘭銀行（Banque de Paris et des Pays-Bas）等大財團設 2,000 萬法郎特別基金救援。已決：判五年＋2,000 萬法郎基金已寫入正文。
10. 1889 年世界博覽會（芝加哥）——「1889 in the United States」條目未檢得。已決：不寫入正文。
11. en-wiki「Panic of 1890」為 REDIRECT 至「Baring crisis」；該條無 PNB 關門／Drexel Parke 倒閉／NYSE 關閉記錄，fr-wiki 對應條目擷取為 404 錯誤頁，Wikipedia 全站搜尋無其他相關條目。已決：大綱四項（1890-05-19 PNB、Drexel Parke 倒閉、NYSE 關 11 天、1889–90 維也納崩盤）無可靠來源，維持不寫（NYSE 11 天疑與 1893 年 11 日關閉混淆）。
12. Drexel 創辦人：en-wiki「Drexel Burnham Lambert」載 Francis M. Drexel 1838 年創立德雷克塞爾公司（Drexel & Company），A. J. 為其弟（1847 年入夥、1863 年弗朗西斯去世後接掌）。已決：正文／筆記／細綱統一「其兄弗朗西斯·M」（A. J. 視角）。
13. 鐵路里程：en-wiki「Long Depression」同條目並列 11,568 與 11,568 英里（一說 11,569）（1882）。已決：統一用 11,568（與 ch04 一致），正文標「一說 11,569」一次。
14. Nathan Rothschild 評語：en-wiki「Barings Bank」條目將評語歸 Nathan Rothschild，但 1st Baron Nathan 1876 年已歿。已決：正文改「羅特席德家族成員」。
15. CLC 首日分行金額（200 萬、三行）與「九行各貸 10 萬」：Yale 案例研究僅載匯總（共 1,665 萬、峰 1,521 萬、24 家、1891-02-07 全贖）與「九家行長（含摩根）同意以證券為抵押共同墊付 90 萬」。已決：分行分額不寫，正文用匯總。
16. 1890 年危機命名：en-wiki「Baring crisis」載該危機 became known as the Panic of 1890。已決：正文 §5.1 開頭加命名句。
17. 財政部 1890 年 07-19 至 11-01 之「贖回」（redemption）9,900 萬美元債券（NY Fed 原文，非「售出」）。已決：正文／筆記改「贖回」。
18. LMU 1873 年停止無限鑄造 5 法郎銀幣、1879-05-19 德國停止拋售銀庫存（en-wiki「Gold standard」）。已核：正文原表述正確，保留。

無未決項。
