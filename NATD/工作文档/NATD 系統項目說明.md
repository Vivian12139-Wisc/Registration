# NATD 考試管理系統 — 項目說明文件

> 本文件說明 NATD 考試管理系統的完整業務流程、各功能模塊及相關數據格式，並附有對應的樣例文件連結供參考。

---

## 目錄

1. [系統概覽](#1-系統概覽)
2. [使用角色](#2-使用角色)
3. [完整業務流程](#3-完整業務流程)
   - [Step 1：配置考試基本資料](#step-1配置考試基本資料)
   - [Step 2：導入申請人及考生資料](#step-2導入申請人及考生資料)
   - [Step 3：核對申請人數據](#step-3核對申請人數據)
   - [Step 4：生成考試費總表](#step-4生成考試費總表)
   - [Step 5a：編排考試時間表](#step-5a編排考試時間表)
   - [Step 5b：生成准考證](#step-5b生成准考證)
   - [Step 6：生成考生評分表](#step-6生成考生評分表)
   - [Step 7：生成考試日程表](#step-7生成考試日程表)
   - [Step 8：輸入考生成績](#step-8輸入考生成績)
   - [Step 9：生成統計及財務報告](#step-9生成統計及財務報告)
4. [數據格式說明](#4-數據格式說明)
5. [功能代碼一覽](#5-功能代碼一覽)

---

## 1. 系統概覽

NATD 考試管理系統負責處理舞蹈考試從報名到出成績的全週期管理，包括考試配置、考生資料導入、准考證及評分表生成、成績錄入及財務報表輸出。

系統由以下兩種操作方式構成：

| 類型 | 說明 |
|---|---|
| **管理員操作** | 由管理員在系統中手動完成的步驟（如數據導入、模板上傳、資料核對） |
| **系統自動運行** | 系統根據導入數據自動完成的步驟（如生成证件、日程表、報告等） |

考生報名流程透過外部 **MIP 報名系統**完成，報名數據以 TXT 文件形式導出後導入本系統。

---

## 2. 使用角色

| 角色 | 職責 |
|---|---|
| **管理員** | 配置考試資料、導入數據、上傳模板、核對信息、錄入成績 |
| **考官** | 使用考官版日程表主持考試、填寫評分表 |
| **監考員** | 使用監考員版日程表協助考場管理 |

---

## 3. 完整業務流程

### Step 1：配置考試基本資料

**執行方式：** 管理員操作

管理員在系統中輸入或更新本次考試所需的基礎配置資料，包括：

- 各考試專業及級別的**考試費**與**場地附加費**
- **考試場地**資料（名稱及地址）
- **舞蹈種類**資料

| 功能代碼 | 功能名稱 | 必要性 |
|---|---|---|
| NATD003 | Maintain Exams | Must have |
| NATD005 | Maintain Grade Code | Must have |
| NATD015 | Maintain Centre | Must have |
| NATD025 | Maintain Dance Types | Must have |
| NATD130 | Maintain Centre Arrangement Fee For Teachers | Must have |

**配置樣例：**
- 📄 [考試專業及級別（配置）](./考试专业级别（配置）.pdf)
- 📄 [舞蹈種類（配置）](./舞蹈种类（配置）.pdf)
- 🖼️ [考場信息（配置）](./考场信息（配置）.png)

---

### Step 2：導入申請人及考生資料

**執行方式：** 管理員操作 → 系統自動處理

管理員將由 MIP 報名系統導出的 **TXT 文件**上傳至本系統，系統自動讀取並生成申請人及考生數據。

**功能：** NATD105 — Load and Validate Entry Data

TXT 文件每個申請人包含以下字段：

| # | 字段 |
|---|---|
| 1 | 申請人編號 |
| 2 | 申請人姓名 |
| 3 | 申請人聯絡電話 |
| 4 | 申請人聯絡電郵 |
| 5 | 申請人聯絡地址 |
| 6 | 各考生姓名、性別、身份證明文件號碼及出生日期 |
| 7 | 各考生組別編號 |
| 8 | 各考生考生編號 |
| 9 | 各考生報考專業、級別及舞蹈種類 |
| 10 | 申請人已付費用總額 |

**導入樣例：**
- 🖼️ [申請人及考生資料（導入）](./申请人及考生资料（导入）.png)

---

### Step 3：核對申請人數據

**執行方式：** 管理員操作 → 系統驗證

管理員在系統中**手動再次輸入**每位申請人的以下數據，系統將自動與 Step 2 導入的 TXT 數據進行比對驗證：

1. 申請人編號
2. 申請人姓名
3. 已付費的考試專業及級別
4. 各專業及級別的報考人數

**功能：** NATD110 — Validate Entry Data（Must have）

> ⚠️ 此步驟為雙重核對機制，確保報名數據的準確性。如數據不一致，系統將提示錯誤。

---

### Step 4：生成考試費總表

**執行方式：** 系統自動運行

系統根據 Step 1–3 的數據，自動計算並生成**考試費總表**，供管理員查閱及下載。

**功能：** NATD210 — Print Fee Statement Summary（Must have）

報表內容包含每位申請人的：
- 申請人編號
- 申請人姓名
- 各考試專業及級別的報考人數
- 考試費總額
- 場地附加費總額

報表同時顯示：
- **Total Amount (Sys Gen)**：由系統自動匯總的總金額
- **Total Amount (Entry Data)**：由管理員導入數據時輸入的金額（用於核對）

**輸出樣例：**
- 📄 [申請人繳費統計（導出）](./申请人缴费统计（导出）.pdf)

---

### Step 5a：編排考試時間表

**執行方式：** 管理員操作 → 系統處理

系統提供 **Excel 模板**，管理員在模板中填入每位考生的考試地點、日期及時間後上傳，系統自動完成考生編排。

| 功能代碼 | 功能名稱 | 必要性 |
|---|---|---|
| NATD323 | Generate Candidate List for Inputting Exam Date and Time Data | Must have |
| NATD324 | Load Exam Date and Time Data | Must have |

> 📝 若申請人事後提出更改考試日期、時間或地點，管理員須**重新編排所有考生**。

Excel 模板字段說明：

| 字段 | 說明 |
|---|---|
| REFNO | 申請人編號 |
| GROUPNO | 組別編號 |
| CANDNO | 考生編號 |
| CANDNAME | 考生姓名 |
| EXAMS_CODE | 考試專業代碼 |
| GRADE_CODE | 級別代碼 |
| CENTRE_CODE | 考試場地代碼 |
| EXAM_DATE (DD/MM/YYYY) | 考試日期 |
| START_TIME (HH:MI) | 考試開始時間 |

---

### Step 5b：生成准考證

**執行方式：** 管理員上傳模板 → 系統自動生成

管理員上傳**准考證模板文件**，系統自動將考生資料導入模板對應位置，批量生成准考證。

| 功能代碼 | 功能名稱 | 必要性 |
|---|---|---|
| NATD405F | Upload Template | Must have |
| NATD405 | Print Admission Form | Must have |

**輸出樣例：**
- 📄 [准考證（導出）](./准考证（导出）.pdf)

---

### Step 6：生成考生評分表

**執行方式：** 管理員上傳模板 → 系統自動生成

由於不同考試專業使用**不同的評分表模板**，管理員上傳模板時須指定該模板所屬的考試專業，系統再自動將對應考生的資料導入模板。

| 功能代碼 | 功能名稱 | 必要性 |
|---|---|---|
| NATD410F | Upload Template | Must have |
| NATD410 | Print Mark Report | Must have |

評分表分為兩種類型：

| 種類 | 適用範圍 |
|---|---|
| **第一種** | Amateur（業餘組）— Ballroom、Latin、Popular Social Dance Test、Country & Western Line Dancing、Rainbow |
| **第二種** | Professional（專業組）— Pro Ballroom、Pro Latin |

**輸出樣例：**
- 📄 [評分表（導出）](./评分表（导出）.pdf)

---

### Step 7：生成考試日程表

**執行方式：** 管理員上傳模板 → 系統自動生成

考試日程表分為**兩個版本**，管理員上傳模板時須指明版本，系統分別生成：

| 版本 | 適用對象 |
|---|---|
| 考官版 | 考官使用，含詳細評核安排 |
| 監考員版 | 監考員使用，含場次及時間安排 |

| 功能代碼 | 功能名稱 | 必要性 |
|---|---|---|
| NATD415F | Upload Template | Must have |
| NATD415 | Print Day Sheet | Must have |

**輸出樣例：**
- 📄 [考官日程表（導出）](./考官日程表（导出）.pdf)
- 📄 [監考員日程表（導出）](./监考员日程表（导出）.pdf)

---

### Step 8：輸入考生成績

**執行方式：** 管理員操作 → 系統處理

考試完結後，系統提供 **Excel 模板**，管理員填入每位考生的成績後上傳，系統自動完成登分。

| 功能代碼 | 功能名稱 | 必要性 |
|---|---|---|
| NATD430 | Generate Candidate List for Inputting Exam Result | Must have |
| NATD501 | Load Exam Result Data | Must have |

Excel 模板在 Step 5a 的字段基礎上新增：

| 字段 | 說明 |
|---|---|
| RESULT | 考試成績代碼（如 `HC` = Honours with Credit） |

**導入樣例：**
- 📊 [考生成績（導入）](./考生成绩（导入）.xlsx)

---

### Step 9：生成統計及財務報告

**執行方式：** 系統自動運行

考試結束後，系統自動生成以下兩份報告：

#### 報告一：Entry Statistics（NATD215）

統計每個考試專業及級別的考生人數。

**輸出樣例：** 詳見填寫樣本文件夾中的 `Entry Statistics樣本.pdf`

#### 報告二：Fee Statement Summary（NATD210）

按申請人匯總費用明細，包含：
- 申請人編號
- 申請人姓名
- 各考試專業及級別的報考人數
- 考試費總額
- 場地附加費總額

**輸出樣例：** 詳見填寫樣本文件夾中的 `Fee statement summary樣本.pdf`

---

## 4. 數據格式說明

### 考生成績 Excel 文件（NATD430 / NATD501）

文件格式為標準 `.xlsx`，工作表命名格式：`natd430s_DDMMYYYYHHMMSS`

| 欄位 | 類型 | 說明 | 示例 |
|---|---|---|---|
| REFNO | 數字 | 申請人編號 | `2510001` |
| GROUPNO | 字串 | 組別編號（兩位） | `"01"` |
| CANDNO | 字串 | 考生編號（兩位） | `"01"` |
| CANDNAME | 字串 | 考生姓名 | `"SAMPLE"` |
| EXAMS_CODE | 字串 | 考試專業代碼 | `"JV"` / `"ADB"` / `"PL"` |
| GRADE_CODE | 字串 | 級別代碼 | `"JVOD"` / `"ADBNA"` |
| CENTRE_CODE | 字串 | 考試場地代碼 | `"002"` |
| EXAM_DATE | 日期 | 格式 DD/MM/YYYY | `26/10/2025` |
| START_TIME | 時間 | 格式 HH:MI | `15:30` |
| RESULT | 字串 | 成績代碼 | `"HC"` |

---

## 5. 功能代碼一覽

| 功能代碼 | 功能名稱 | 所屬步驟 |
|---|---|---|
| NATD003 | Maintain Exams | Step 1 |
| NATD005 | Maintain Grade Code | Step 1 |
| NATD015 | Maintain Centre | Step 1 |
| NATD025 | Maintain Dance Types | Step 1 |
| NATD130 | Maintain Centre Arrangement Fee For Teachers | Step 1 |
| NATD105 | Load and Validate Entry Data | Step 2 |
| NATD110 | Validate Entry Data | Step 3 |
| NATD210 | Print Fee Statement Summary | Step 4 / Step 9 |
| NATD323 | Generate Candidate List for Inputting Exam Date and Time Data | Step 5a |
| NATD324 | Load Exam Date and Time Data | Step 5a |
| NATD405F | Upload Template (Admission Form) | Step 5b |
| NATD405 | Print Admission Form | Step 5b |
| NATD410F | Upload Template (Mark Report) | Step 6 |
| NATD410 | Print Mark Report | Step 6 |
| NATD415F | Upload Template (Day Sheet) | Step 7 |
| NATD415 | Print Day Sheet | Step 7 |
| NATD430 | Generate Candidate List for Inputting Exam Result | Step 8 |
| NATD501 | Load Exam Result Data | Step 8 |
| NATD215 | Print Entry Statistics | Step 9 |

---

*文件最後更新：2026 年 5 月*
