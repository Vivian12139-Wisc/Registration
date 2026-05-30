# NATD 考试管理系统 — 项目说明文档

> 本文档说明 NATD 考试管理系统的完整业务流程、各功能模块及相关数据格式，并附有对应的样例文件链接供参考。

---

## 目录

1. [系统概览](#1-系统概览)
2. [使用角色](#2-使用角色)
3. [完整业务流程](#3-完整业务流程)
   - [Step 1：配置考试基本资料](#step-1配置考试基本资料)
   - [Step 2：导入申请人及考生资料](#step-2导入申请人及考生资料)
   - [Step 3：核对申请人数据](#step-3核对申请人数据)
   - [Step 4：生成考试费总表](#step-4生成考试费总表)
   - [Step 5a：编排考试时间表](#step-5a编排考试时间表)
   - [Step 5b：生成准考证](#step-5b生成准考证)
   - [Step 6：生成考生评分表](#step-6生成考生评分表)
   - [Step 7：生成考试日程表](#step-7生成考试日程表)
   - [Step 8：输入考生成绩](#step-8输入考生成绩)
   - [Step 9：生成统计及财务报告](#step-9生成统计及财务报告)
4. [数据格式说明](#4-数据格式说明)
5. [功能代码一览](#5-功能代码一览)

---

## 1. 系统概览

NATD 考试管理系统负责处理舞蹈考试从报名到出成绩的全周期管理，包括考试配置、考生资料导入、准考证及评分表生成、成绩录入及财务报表输出。

系统由以下两种操作方式构成：

| 类型 | 说明 |
|---|---|
| **管理员操作** | 由管理员在系统中手动完成的步骤（如数据导入、模板上传、资料核对） |
| **系统自动运行** | 系统根据导入数据自动完成的步骤（如生成证件、日程表、报告等） |

考生报名流程通过外部 **MIP 报名系统**完成，报名数据以 TXT 文件形式导出后导入本系统。

---

## 2. 使用角色

| 角色 | 职责 |
|---|---|
| **管理员** | 配置考试资料、导入数据、上传模板、核对信息、录入成绩 |
| **考官** | 使用考官版日程表主持考试、填写评分表 |
| **监考员** | 使用监考员版日程表协助考场管理 |

---

## 3. 完整业务流程

### Step 1：配置考试基本资料

**执行方式：** 管理员操作

管理员在系统中输入或更新本次考试所需的基础配置资料，包括：

- 各考试专业及级别的**考试费**与**场地附加费**
- **考试场地**资料（名称及地址）
- **舞蹈种类**资料

| 功能代码 | 功能名称 | 必要性 |
|---|---|---|
| NATD003 | Maintain Exams | Must have |
| NATD005 | Maintain Grade Code | Must have |
| NATD015 | Maintain Centre | Must have |
| NATD025 | Maintain Dance Types | Must have |
| NATD130 | Maintain Centre Arrangement Fee For Teachers | Must have |

**配置样例：**
- 📄 [考试专业及级别（配置）](./考试专业级别（配置）.pdf)
- 📄 [舞蹈种类（配置）](./舞蹈种类（配置）.pdf)
- 🖼️ [考场信息（配置）](./考场信息（配置）.png)

---

### Step 2：导入申请人及考生资料

**执行方式：** 管理员操作 → 系统自动处理

管理员将由 MIP 报名系统导出的 **TXT 文件**上传至本系统，系统自动读取并生成申请人及考生数据。

**功能：** NATD105 — Load and Validate Entry Data

TXT 文件每个申请人包含以下字段：

| # | 字段 |
|---|---|
| 1 | 申请人编号 |
| 2 | 申请人姓名 |
| 3 | 申请人联络电话 |
| 4 | 申请人联络电邮 |
| 5 | 申请人联络地址 |
| 6 | 各考生姓名、性别、身份证明文件号码及出生日期 |
| 7 | 各考生组别编号 |
| 8 | 各考生考生编号 |
| 9 | 各考生报考专业、级别及舞蹈种类 |
| 10 | 申请人已付费用总额 |

**导入样例：**
- 🖼️ [申请人及考生资料（导入）](./申请人及考生资料（导入）.png)

---

### Step 3：核对申请人数据

**执行方式：** 管理员操作 → 系统验证

管理员在系统中**手动再次输入**每位申请人的以下数据，系统将自动与 Step 2 导入的 TXT 数据进行比对验证：

1. 申请人编号
2. 申请人姓名
3. 已付费的考试专业及级别
4. 各专业及级别的报考人数

**功能：** NATD110 — Validate Entry Data（Must have）

> ⚠️ 此步骤为雙重核对机制，确保报名数据的准确性。如数据不一致，系统将提示错误。

---

### Step 4：生成考试费总表

**执行方式：** 系统自动运行

系统根据 Step 1–3 的数据，自动计算并生成**考试费总表**，供管理员查阅及下载。

**功能：** NATD210 — Print Fee Statement Summary（Must have）

报表內容包含每位申请人的：
- 申请人编号
- 申请人姓名
- 各考试专业及级别的报考人数
- 考试费总额
- 场地附加费总额

报表同时显示：
- **Total Amount (Sys Gen)**：由系统自动汇总的总金额
- **Total Amount (Entry Data)**：由管理员导入数据时输入的金额（用于核对）

**输出样例：**
- 📄 [申请人缴费统计（导出）](./申请人缴费统计（导出）.pdf)

---

### Step 5a：编排考试时间表

**执行方式：** 管理员操作 → 系统处理

系统提供 **Excel 模板**，管理员在模板中填入每位考生的考试地点、日期及时间后上传，系统自动完成考生编排。

| 功能代码 | 功能名称 | 必要性 |
|---|---|---|
| NATD323 | Generate Candidate List for Inputting Exam Date and Time Data | Must have |
| NATD324 | Load Exam Date and Time Data | Must have |

> 📝 若申请人事后提出更改考试日期、时间或地点，管理员须**重新编排所有考生**。

Excel 模板字段说明：

| 字段 | 说明 |
|---|---|
| REFNO | 申请人编号 |
| GROUPNO | 组别编号 |
| CANDNO | 考生编号 |
| CANDNAME | 考生姓名 |
| EXAMS_CODE | 考试专业代码 |
| GRADE_CODE | 级别代码 |
| CENTRE_CODE | 考试场地代码 |
| EXAM_DATE (DD/MM/YYYY) | 考试日期 |
| START_TIME (HH:MI) | 考试开始时间 |

---

### Step 5b：生成准考证

**执行方式：** 管理员上传模板 → 系统自动生成

管理员上传**准考证模板文件**，系统自动将考生资料导入模板对应位置，批量生成准考证。

| 功能代码 | 功能名称 | 必要性 |
|---|---|---|
| NATD405F | Upload Template | Must have |
| NATD405 | Print Admission Form | Must have |

**输出样例：**
- 📄 [准考证（导出）](./准考证（导出）.pdf)

---

### Step 6：生成考生评分表

**执行方式：** 管理员上传模板 → 系统自动生成

由于不同考试专业使用**不同的评分表模板**，管理员上传模板时须指定該模板所屬的考试专业，系统再自动将对应考生的资料导入模板。

| 功能代码 | 功能名称 | 必要性 |
|---|---|---|
| NATD410F | Upload Template | Must have |
| NATD410 | Print Mark Report | Must have |

评分表分为两种类型：

| 种类 | 適用范圍 |
|---|---|
| **第一种** | Amateur（业余组）— Ballroom、Latin、Popular Social Dance Test、Country & Western Line Dancing、Rainbow |
| **第二种** | Professional（专业组）— Pro Ballroom、Pro Latin |

**输出样例：**
- 📄 [评分表（导出）](./评分表（导出）.pdf)

---

### Step 7：生成考试日程表

**执行方式：** 管理员上传模板 → 系统自动生成

考试日程表分为**两个版本**，管理员上传模板时须指明版本，系统分别生成：

| 版本 | 適用对象 |
|---|---|
| 考官版 | 考官使用，含詳細评核安排 |
| 监考员版 | 监考员使用，含场次及时间安排 |

| 功能代码 | 功能名称 | 必要性 |
|---|---|---|
| NATD415F | Upload Template | Must have |
| NATD415 | Print Day Sheet | Must have |

**输出样例：**
- 📄 [考官日程表（导出）](./考官日程表（导出）.pdf)
- 📄 [监考员日程表（导出）](./监考员日程表（导出）.pdf)

---

### Step 8：输入考生成绩

**执行方式：** 管理员操作 → 系统处理

考试完结后，系统提供 **Excel 模板**，管理员填入每位考生的成绩后上传，系统自动完成登分。

| 功能代码 | 功能名称 | 必要性 |
|---|---|---|
| NATD430 | Generate Candidate List for Inputting Exam Result | Must have |
| NATD501 | Load Exam Result Data | Must have |

Excel 模板在 Step 5a 的字段基础上新增：

| 字段 | 说明 |
|---|---|
| RESULT | 考试成绩代码（如 `HC` = Honours with Credit） |

**导入样例：**
- 📊 [考生成绩（导入）](./考生成绩（导入）.xlsx)

---

### Step 9：生成统计及财务报告

**执行方式：** 系统自动运行

考试结束后，系统自动生成以下两份报告：

#### 报告一：Entry Statistics（NATD215）

统计每个考试专业及级别的考生人数。

**输出样例：** 詳見填写样本文件夾中的 `Entry Statistics样本.pdf`

#### 报告二：Fee Statement Summary（NATD210）

按申请人汇总费用明細，包含：
- 申请人编号
- 申请人姓名
- 各考试专业及级别的报考人数
- 考试费总额
- 场地附加费总额

**输出样例：** 詳見填写样本文件夾中的 `Fee statement summary样本.pdf`

---

## 4. 数据格式说明

### 考生成绩 Excel 文件（NATD430 / NATD501）

文件格式为标准 `.xlsx`，工作表命名格式：`natd430s_DDMMYYYYHHMMSS`

| 栏位 | 类型 | 说明 | 示例 |
|---|---|---|---|
| REFNO | 数字 | 申请人编号 | `2510001` |
| GROUPNO | 字串 | 组别编号（两位） | `"01"` |
| CANDNO | 字串 | 考生编号（两位） | `"01"` |
| CANDNAME | 字串 | 考生姓名 | `"SAMPLE"` |
| EXAMS_CODE | 字串 | 考试专业代码 | `"JV"` / `"ADB"` / `"PL"` |
| GRADE_CODE | 字串 | 级别代码 | `"JVOD"` / `"ADBNA"` |
| CENTRE_CODE | 字串 | 考试场地代码 | `"002"` |
| EXAM_DATE | 日期 | 格式 DD/MM/YYYY | `26/10/2025` |
| START_TIME | 时间 | 格式 HH:MI | `15:30` |
| RESULT | 字串 | 成绩代码 | `"HC"` |

---

## 5. 功能代码一览

| 功能代码 | 功能名称 | 所屬步骤 |
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

*文档最后更新：2026 年 5 月*
