# CSTD 考试管理系统 — 项目说明文档

> 本文档根据《CSTD - 报名流程》及《CSTD - 考生编排流程》整理，完整涵盖在线报名、考生编排、文件生成、成绩处理及财务报告的全流程，所有步骤均不遗漏。
>
> ⚠️ **重要提示：报名全程以英语进行。**

---

## 目录

1. [系统概览](#1-系统概览)
2. [使用角色](#2-使用角色)
3. [流程一：在线报名流程](#3-流程一在线报名流程)
   - [3.1 报名前系统配置](#31-报名前系统配置)
   - [3.2 申请人基本资料](#32-申请人基本资料)
   - [3.3 上载申请人证明文件](#33-上载申请人证明文件)
   - [3.4 选择考试类别及场地](#34-选择考试类别及场地)
   - [3.5 填写考生资料](#35-填写考生资料)
   - [3.6 年龄验证与特殊考生处理](#36-年龄验证与特殊考生处理)
   - [3.7 上载报名资格证明](#37-上载报名资格证明)
   - [3.8 Mature Candidate 所需文件](#38-mature-candidate-所需文件)
   - [3.9 夏季考试关联（冬季报名专属）](#39-夏季考试关联冬季报名专属)
   - [3.10 费用计算与确认](#310-费用计算与确认)
   - [3.11 缴费及报名完成](#311-缴费及报名完成)
4. [流程二：报名后管理 — 考生编排](#4-流程二报名后管理--考生编排)
   - [4.1 管理员设置阶段](#41-管理员设置阶段)
   - [4.2 上载 TXT 考试日程](#42-上载-txt-考试日程)
   - [4.3 系统派位验证](#43-系统派位验证)
   - [4.4 个别考生临时更改](#44-个别考生临时更改)
5. [流程三：考试文件生成](#5-流程三考试文件生成)
   - [5.1 日程表生成](#51-日程表生成)
   - [5.2 准考证生成及发送](#52-准考证生成及发送)
   - [5.3 分纸（含 Barcode）生成](#53-分纸含-barcode生成)
6. [流程四：考后成绩处理](#6-流程四考后成绩处理)
   - [6.1 OMR 成绩上载](#61-omr-成绩上载)
   - [6.2 人工成绩设置](#62-人工成绩设置)
   - [6.3 生成考生数据文件](#63-生成考生数据文件)
7. [流程五：财务报告](#7-流程五财务报告)
8. [附录 A：考试科目及级别分类](#8-附录-a考试科目及级别分类)
9. [附录 B：每组人数限制](#9-附录-b每组人数限制)
10. [功能代码一览](#10-功能代码一览)

---

## 1. 系统概览

CSTD 考试管理系统处理舞蹈考试从在线报名到成绩发布的完整周期，主要分为以下五个阶段：

| 阶段 | 内容 |
|---|---|
| **在线报名** | 申请人填写资料、上载文件、缴费（全程英语） |
| **考生编排** | 管理员设置考试资料、上载 TXT 日程、系统验证派位 |
| **考试文件生成** | 自动生成日程表、准考证、分纸（含 Barcode）、证书 |
| **考后成绩处理** | 上载 OMR 成绩或人工录入，生成汇总数据 |
| **财务报告** | 生成各类收费及人数统计报告 |

图例说明：

| 标识 | 含义 |
|---|---|
| **Must have** | 必须实现的功能 |
| **Nice to have** | 建议实现的功能 |
| **系统步骤** | 系统自动执行 |
| **步骤分支** | 根据条件进行的分支判断 |
| **视乎情况** | 按实际情况需进行的步骤 |

---

## 2. 使用角色

| 角色 | 职责 |
|---|---|
| **申请人（保送教师/学校）** | 填写报名表（英语）、上载证明文件、缴费 |
| **管理员** | 配置考试资料、上载日程、处理成绩、生成报告、开启/关闭特定功能 |
| **系统** | 自动验证数据、生成文件、发送通知、自动计算编号与费用 |

---

## 3. 流程一：在线报名流程

> 对应文件：`CSTD - 報名流程_11Nov2025.xlsx`
>
> ⚠️ 本流程全程以英语进行。

---

### 3.1 报名前系统配置

管理员在开放报名前须完成以下系统配置：

| 功能代码 | 功能名称 | 必要性 |
|---|---|---|
| COMM30005 | Maintain Exam Information For Online Registration | Must have |
| CSTD005F | Maintain Exam | Must have |
| CSTD025F | Maintain Exam Grade Code | Must have |
| CSTD015F | Maintain Examination Centre | Must have |
| CSTD20035 | Maintain Schedule | Nice to have |

---

### 3.2 申请人基本资料

**步骤 1：** 申请人进入报名页面，阅读报考简章及考试规则。

**步骤 2：** 申请人提供基本资料，以电邮地址开立账户，供日后查阅报名资料及下载文件。

> ⚠️ 如系统没有即时认证功能，系统须要求申请人输入电邮地址两次。

申请人须填写以下资料（字段 2.1）：

| 字段 | 说明 |
|---|---|
| 保送教师英文姓名 / 学校英文名称 | 必填；此字段内容将作为准考证上保送教师姓名/学校名称的依据 |
| 保送教师英文通讯地址 | 必填 |
| 保送教师联络电话 | 必填 |
| 保送教师电邮地址 | 必填，用于开立账户 |

---

### 3.3 上载申请人证明文件

申请人须上载以下三类证明文件（字段 2.2–2.4）：

| 文件 | 字段 | 格式要求 |
|---|---|---|
| HKDF 会员证 | 2.2 | JPEG / JPG / GIF / BMP / PDF / TIFF，≤1MB，**不接受 HEIC** |
| CSTD 会员证 | 2.3 | 同上（系统展示样品） |
| 教师证书 | 2.4 | 同上（系统展示样品） |

- 申请人可即时预览已上载的文件
- 系统展示各类证件的样品供参考

---

### 3.4 选择考试类别及场地

**步骤 3：** 选择考试类别及考试场地（字段 3.1）。

考试场地分为两大类型：

#### 3.4.1 Central Venue（中央考场）

申请人选择以下一种考试类别（字段 3.11）：

| 类别 | 适用级别 | 备注 |
|---|---|---|
| **Pre Grades and General Grades Examinations**（3.1.1） | 各科目 Pre Grades 至 General Grades（详见附录 A） | — |
| **Major Grade Examinations**（3.1.2） | 各科目 Major Grades 级别（详见附录 A） | — |
| **Stage Performance Examinations**（3.1.3） | 各科目 Stage Performance 级别（详见附录 A） | 此类别可由管理员按考试季度开启/关闭 |

选择考试类别后：
- 标示是否与其他老师举行 **Joint Exam**（勾选 Check Box，并填写其他保送教师姓名）
- 选择最多 **3 个考试日期**（第一选择、第二选择、第三选择）

#### 3.4.2 Own Studio（自行安排场地）

1. 提供试场英文地址
2. 选择该场地是否曾获得香港舞蹈总会认可：
   - **是** → 无需上载平面图，继续下一步
   - **否** → 须上载考试场地平面图
3. 选择最多 **3 个考试日期**（第一选择、第二选择、第三选择）

> 管理员可配置是否由考试机构指定考试日期（可按考试机构要求开启/关闭）。

---

### 3.5 填写考生资料

**步骤 4：** 申请人填写每一考试组别的考试级别、考生人数及考生个人资料。

- 系统按照申请人输入的**组别次序**及**考生次序**自动生成考试组别编号及考生编号（管理员其后可作调动）
- 申请人每次可**输入**或**利用模板导入**最多 **30 组**考生资料
- 管理员可自行设定每份考试报名表的**组别上限**

每位考生须填写（字段 4.1）：

| 字段 | 说明 |
|---|---|
| 考生英文姓名 | 必填 |
| 考生性别 | 必填 |
| 身份证明文件类别 | 香港身份证 / 护照 / 出生证明书 / 其他 |
| 身份证明文件编号 | 必填 |

**上载考生身份证明文件副本：**
- 接受格式：JPEG / JPG / GIF / BMP / PDF / TIFF
- 文件大小：≤1MB，**不接受 HEIC**
- 申请人可即时预览已上载的文件

---

### 3.6 年龄验证与特殊考生处理

**步骤 4.2：** 申请人填写考生出生日期，系统自动计算年龄。

> 📌 考生年龄以**考试当年 12 月 31 日**为计算基准，各考试科目及级别的年龄要求不同，详情参考《CSTD - 考试费用、场地费用及附加费用》文件。

**年龄验证流程：**

```
计算年龄
  ├── 符合年龄最低要求 → 可报考 ✅
  └── 不符合年龄最低要求 → 不可报考 ❌
      系统提示申请人：考生不符合考试级别的年龄最低要求
```

**Mature Candidate 判断：**

```
是否为 Mature Candidate？
  ├── 是 → 系统于管理页面生成报告，提示管理员（此选项可由管理员开启/关闭）
  └── 否 → 继续
```

> 管理员可于管理页面查看含有 Mature Candidate 的报名记录。

**同一季度多科报考检查：**

```
是否于同一考试季度报考多于一个考试科目/级别？
  ├── 是 → 系统于管理页面生成报告，提示管理员
  └── 否 → 继续
```

---

### 3.7 上载报名资格证明

部分级别要求申请人上载**报名资格证明**（上一级考试证书或成绩表）。

#### 4.21 Pre Grades / General Grades 考试（需上载文件的级别）

| 科目 | 需上载文件的级别范围 |
|---|---|
| Classical Ballet | Sub Elementary to Advanced |
| Contemporary | Grade 2 to Grade 5 |
| Modern Jazz | Grade 5 to Grade 8 |
| Revised Modern Jazz | Grade 4 to Grade 9 |
| New Tapping | Grade 6 to Grade 9 |
| Theatrical and Performing Arts | Theatrical and Performing Arts 4 to Theatrical and Performing Arts 8 |

#### 4.22 Major Grade 考试（需上载文件的级别）

| 科目 | 需上载文件的级别范围 |
|---|---|
| Classical Ballet | Teacher's Certificate and Full Teacher's Diploma |
| Contemporary | Teacher's Certificate |
| Modern Jazz | Teacher's Certificate and Full Teacher's Diploma |
| Revised Modern Jazz | Teacher's Certificate and Full Teacher's Diploma |
| New Tapping | Teacher's Certificate and Full Teacher's Diploma |
| Theatrical and Performing Arts | Teacher's Certificate and Full Teacher's Diploma |

**上载格式要求：**
- 接受格式：JPEG / JPG / GIF / BMP / PDF / TIFF，≤1MB，**不接受 HEIC**
- 申请人可即时预览已上载的文件

---

### 3.8 Mature Candidate 所需文件

Mature Candidate 须额外上载以下三类文件（格式均为 JPEG / JPG / GIF / BMP / PDF / TIFF，≤1MB，不接受 HEIC）：

| 文件 | 说明 |
|---|---|
| Mentor's Approval Form | 必须上载 |
| Mentor's Working Sheet | 必须上载 |
| Eligible Teaching Certificate / Examination Training Accreditation | 必须上载 |

- 申请人可即时预览所有已上载的文件

---

### 3.9 夏季考试关联（冬季报名专属）

> 此功能可由管理员按考试季度**开启/关闭**，仅在冬季报名时适用。

**步骤（冬季报名时）：** 系统询问考生有否报考**该年度夏季考试**：

```
考生有否报考该年度夏季考试？
  ├── 是 → 申请人上载考生夏季考试准考证作为报名资格证明
  │         接受格式：JPEG / JPG / GIF / BMP / PDF / TIFF，≤1MB
  │         申请人可即时预览已上载的文件
  └── 否 → 上载其他报名资格证明（上一级考试证书或成绩表）
```

---

### 3.10 费用计算与确认

**步骤 5：** 系统列出管理人设定的报名及考试条款，要求申请人确认。

**步骤 6：** 系统判断是否在**逾期报名期间**内递交：

```
报名表递交日期是否于逾期报名期间？
  ├── 是 → 系统收取逾期报名费：港币 $525 / 每位考生
  └── 否 → 按正常费用计算
```

**步骤 7：** 系统自动计算费用，规则如下：

1. **附加费**：按照每组填写的考试级别收取附加费用（按考试科目及级别）
2. **人数不足附加费**：如每组考生人数不足，须额外收取附加费用（详见附录 B）

> 费率详情请参考《CSTD - 考试费用、场地费用及附加费用》文件。

**步骤 8：** 系统列出所有已输入的资料及每项收费明细（每个考试组别的考试收费及附加费用），要求申请人最终确认。

---

### 3.11 缴费及报名完成

**步骤 9：** 申请人缴交考试费及附加费用（如有）。

**步骤 10：** 系统发出**报名确认电邮**。

> - 电邮内容由管理人于系统中设定
> - 管理人可于系统直接查看**个别发送状态**
> - 管理人可于系统**重发**确认电邮

**步骤 11：** 报名完成 ✅

**管理端后台报告（系统自动生成）：**

| 报告 | 触发条件 | 用途 |
|---|---|---|
| Mature Candidate 报告 | 申请人选择 Mature Candidate | 提示管理员相关报名记录 |
| 同一季度多科报考报告 | 考生在同季度报考多科 | 提示管理员进行核查 |

---

## 4. 流程二：报名后管理 — 考生编排

> 对应文件：`CSTD - 考生編排流程_11Nov2025.xlsx`

---

### 4.1 管理员设置阶段

报名截止后，管理员依次完成以下四项设置：

#### 设置 1：管理员设置申请人编号

申请人编号格式为 **AABCCCC**（7 位数字），规则如下：

| 场地类型 | 编号规则 | 示例 |
|---|---|---|
| Central Venue / Major Grade / Stage Performance | AA[考试年份] + B[考试月份] + CCCC[报名顺序] | `2570001` |
| Own Studio | AA[考试年份] + B[考试月份] + CCCC[报名顺序] | `2580001` |

> ⚠️ 两种选项的考试发生在**不同月份**，故可由月份编号区分。

**相关功能：**
- Maintain Entry Data - Teachers（CSTD115F）
- Maintain Entry Data - Candidates（CSTD115F）
- Maintain Applicant Group Data（CSTD150F）
- Batch Upload Allocation（CSTD305F）

#### 设置 2：管理员设置考试资料

| 配置项 | 说明 |
|---|---|
| 考试日期 | 必填 |
| 考试场地名称 | 必填 |
| 考试场地地址 | 必填 |
| 考试场地编号 | 必填 |
| 考试场地类别 | Central Venue / Own Studio / Major Grade Venue / Stage Performance Venue |
| 考官名称 | 必填 |
| 考官编号 | 必填 |

**相关功能：**
- Maintain Schedule（CSTD20035）
- Maintain Examination Centre（CSTD015F）
- Maintain Examiner（CSTD20025）

#### 设置 3：管理员设置/核对考生资料

管理员可于系统对以下考生资料进行更改：

| 类别 | 可更改字段 |
|---|---|
| 编排资料 | 考生组别号码、考生编号、考试科目及级别 |
| 个人资料 | 考生姓名、考生性别、考生出生日期、考生身份证明文件号码 |
| 特殊检查 | 系统生成报告，供管理员查看是否有**考生超过年龄上限** |

**相关功能：**
- Maintain Entry Data - Candidates（CSTD115F）

#### 设置 4：系统验证入场数据

**相关功能：** Validate Entry Data（CSTD110F）— Must have

---

### 4.2 上载 TXT 考试日程

**步骤：** 管理员以 **TXT 格式**上载考试日程。

TXT 文件须按以下次序排列字段：

| 顺序 | 字段 |
|---|---|
| 1 | 考试日期 |
| 2 | 考试场地编号 |
| 3 | 考试场地类别 |
| 4 | 考官编号 |
| 5 | 申请人编号（由管理员编排） |
| 6 | 考试当天全日时间表的次序 |
| 7 | 考试组别 |
| 8 | 每一组考试开始及完结时间 |
| 9 | 考试级别 |
| 10 | 每一考试组别的考试时间长度 |

---

### 4.3 系统派位验证

上载 TXT 后，系统执行**两轮验证**：

#### 第一轮：重复检查

```
系统检查：每一考试日 × 每一考试场地 × 每组考生
         （组别及考生编号有否重复）
  ├── 有重复 → 系统提示管理员重复派位的考生名单
  │            → 管理员重新上载 TXT 档案
  └── 没有重复 → 进入第二轮验证
```

#### 第二轮：派位完整性检查

```
系统检查：所有考生是否已完成派位
  ├── 尚有考生未能派位 → 系统提示未能派位的考生名单
  │                     → 管理员重新上载 TXT 档案
  └── 所有考生成功派位 → 系统再次检查组别及考生编号是否重复
                        → 编排完成 ✅
                        → 编排结果可输出为 Excel 及考试日程
```

---

### 4.4 个别考生临时更改

编排完成后，如有考生需要更改考试安排，管理员可于系统**直接修改个别考生**的以下资料，**无须重新上载 TXT 文件**：

| 可修改项目 |
|---|
| 考试组别 |
| 考生编号 |
| 考试日期 |
| 考试时间 |
| 考试场地 |
| 考试级别 |

---

## 5. 流程三：考试文件生成

管理员须上载以下五类范本，系统据此自动生成对应文件：

| 范本类型 |
|---|
| 1. 考官考试日程表 |
| 2. 监考员考试日程表 |
| 3. 准考证 |
| 4. 分纸 |
| 5. 证书 |

---

### 5.1 日程表生成

管理员上载考官及监考员考试日程表范本，系统根据日程编排**自动生成每个考试日的日程表**。

| 功能代码 | 功能名称 |
|---|---|
| CSTD20065 | Upload Template（上载范本） |
| CSTD420F | Print Day Sheet for Examiners（考官日程表） |
| CSTD421F | Print Day Sheet for WRS（监考员日程表） |

---

### 5.2 准考证生成及发送

**步骤 1：** 管理员上载电邮范本及准考证范本。

| 功能代码 | 功能名称 |
|---|---|
| COMM20115 | Appointment Template（上载电邮范本 & 上载准考证范本）|
| CSTD405F | Print Admission Form（生成考生准考证）|

系统根据日程编排，**自动将考生资料导入准考证范本**，生成每位考生的准考证。

**步骤 2：** 管理员于系统设定准考证电邮**发送日期**。

| 功能代码 | 功能名称 | 说明 |
|---|---|---|
| CSTD20075 | Publish Appointments | 于系统设定日期自动发送电邮予申请人；申请人可于设定日期内登录系统下载考生准考证 |

---

### 5.3 分纸（含 Barcode）生成

管理员上载分纸范本，系统执行以下操作：

1. 根据日程编排将考生资料导入分纸
2. 为每位考生**自动生成独立的 Barcode**
3. 供管理员下载及列印考生分纸

| 功能代码 | 功能名称 |
|---|---|
| CSTD20065 | Upload Template（上载分纸范本） |
| CSTD410F | Print Mark Report（生成含 Barcode 的考生分纸） |

> 📌 分纸（Mark Report）即为考生评分纸，附带唯一 Barcode，用于后续 OMR 成绩扫描。

---

## 6. 流程四：考后成绩处理

### 6.1 OMR 成绩上载

**步骤：** 考试完结后，将所有印有 Barcode 的分纸进行 **OMR 扫描**，完成后将记录所有考生成绩的 TXT 文件上载至系统。

| 功能代码 | 功能名称 |
|---|---|
| CSTD535F | Upload Candidate Results |

---

### 6.2 人工成绩设置

如需对个别考生成绩进行调整，管理员可通过系统**手动设置或修改**考生成绩。

> 此功能为 CSTD535F 上载后的补充操作，无需另行调用独立功能代码。

---

### 6.3 生成考生数据文件

导入所有考生成绩后，系统可生成以下两份 Excel 报告：

| 报告内容 | 功能代码 |
|---|---|
| 所有申请人及考生的全部资料与**成绩** | CSTD520F（Generate Candidate Data File） |
| 所有申请人及考生的全部资料与**日程编排** | CSTD520F（Generate Candidate Data File） |

---

## 7. 流程五：财务报告

所有财务报告均可通过 **Report Repository Explorer（COMM20050）** 统一访问。

| 功能代码 | 报告名称 | 报告内容 |
|---|---|---|
| CSTD215F | Print Entry Statistics | 每项考试级别的报考人数 |
| CSTD210F | Print Fee Statement Summary | 根据各申请人的报名，详细列出付款日期及时间及已付的收费金额（包括组别及场地附加费）；同时列明申请人的缴费日期及时间、付款方式、总考试费及考生姓名 |
| CSTD225 | Print List of Centre Fee Statistics By Teacher | 详细列出各申请人每级有多少组别须缴付场地费 |
| CSTD230F | Print Supplementary Fee Statistics By Teacher | 详细列出各申请人每级有多少组别须缴付附加费 |
| CSTD220F | Print Entry Statistics By Teacher | 详细列出申请人于每项考试级别的考生人数 |

---

## 8. 附录 A：考试科目及级别分类

### Pre Grades and General Grades Exams

| 科目 | 级别范围 |
|---|---|
| Classical Ballet | Pre-Ballet to Grade 6 |
| Contemporary | Nil |
| Modern Jazz | Grade 5 |
| Revised Modern Jazz | Pre Modern Jazz to Grade 5 |
| New Tapping | Foundation Tap to Grade 5 |
| Theatrical and Performing Arts | Pre-Theatrical & Performing Arts to Theatrical & Performing Arts 6 |

### Major Grades Exams

| 科目 | 级别范围 |
|---|---|
| Classical Ballet | Sub Elementary to Full Teacher's Diploma |
| Contemporary | Foundation to Teacher's Certificate |
| Modern Jazz | Grade 6 to Full Teacher's Diploma |
| Revised Modern Jazz | Grade 6 to Full Teacher's Diploma |
| New Tapping | Grade 6 to Full Teacher's Diploma |
| Theatrical and Performing Arts | Theatrical & Performing Arts 7 to Full Teacher's Diploma |

### Stage Performance Exams

| 科目 | 级别 |
|---|---|
| Classical Ballet | Dorothy Gladstone Award、Martin Rubinstein Award、Premier Danseur |
| Contemporary | Dorothy Gladstone Award |
| Modern Jazz | Dorothy Gladstone Award、Modern Jazz Shield |
| Revised Modern Jazz | Dorothy Gladstone Award、Modern Jazz Shield |
| New Tapping | Dorothy Gladstone Award、Gold Cross |
| Theatrical and Performing Arts | Nil |

---

## 9. 附录 B：每组人数限制

| 科目及级别 | 每组人数上限 |
|---|---|
| Classical Ballet: Pre-Grades to Advanced | 1–4 人 |
| Classical Ballet: Teacher's Certificate and Full Teacher's Diploma | 1 人 |
| Contemporary: Foundation Level to Level 4 | 2–4 人 |
| Contemporary: Level 5 | 1–2 人 |
| Contemporary: Teacher's Certificate | 1 人 |
| Modern Jazz: Grade 5 to Grade 8 | 1–4 人 |
| Modern Jazz: Teacher's Certificate and Full Teacher's Diploma | 1 人 |
| Revised Modern Jazz: Pre Modern Jazz to Grade 9 | 1–4 人 |
| Revised Modern Jazz: Teacher's Certificate and Full Teacher's Diploma | 1 人 |
| New Tapping: Foundation Tap to Grade 9 | 1–4 人 |
| New Tapping: Teacher's Certificate and Full Teacher's Diploma | 1 人 |
| Theatrical and Performing Arts: Pre-Theatrical to Grade 6 | 1–4 人 |
| Theatrical and Performing Arts: Grade 7–8 | 1–3 人 |
| Theatrical and Performing Arts: Teacher's Certificate and Full Teacher's Diploma | 1 人 |
| Stage Performance（所有科目） | 每组仅 1 人 |

---

## 10. 功能代码一览

| 功能代码 | 功能名称 | 所属流程 |
|---|---|---|
| COMM30005 | Maintain Exam Information For Online Registration | 流程一：报名前配置 |
| CSTD005F | Maintain Exam | 流程一：报名前配置 |
| CSTD025F | Maintain Exam Grade Code | 流程一：报名前配置 |
| CSTD015F | Maintain Examination Centre | 流程一 & 流程二 |
| CSTD20035 | Maintain Schedule | 流程一 & 流程二 |
| CSTD115F | Maintain Entry Data（Teachers & Candidates） | 流程二：考生编排 |
| CSTD150F | Maintain Applicant Group Data | 流程二：考生编排 |
| CSTD305F | Batch Upload Allocation | 流程二：考生编排 |
| CSTD20025 | Maintain Examiner | 流程二：考生编排 |
| CSTD110F | Validate Entry Data | 流程二：考生编排 |
| CSTD20065 | Upload Template（日程表 / 分纸） | 流程三：文件生成 |
| CSTD420F | Print Day Sheet for Examiners | 流程三：日程表 |
| CSTD421F | Print Day Sheet for WRS | 流程三：日程表 |
| COMM20115 | Appointment Template | 流程三：准考证 |
| CSTD405F | Print Admission Form | 流程三：准考证 |
| CSTD20075 | Publish Appointments | 流程三：准考证发送 |
| CSTD410F | Print Mark Report | 流程三：分纸（含 Barcode） |
| CSTD535F | Upload Candidate Results | 流程四：成绩处理 |
| CSTD520F | Generate Candidate Data File | 流程四：成绩处理 |
| COMM20050 | Report Repository Explorer | 流程五：财务报告 |
| CSTD215F | Print Entry Statistics | 流程五：财务报告 |
| CSTD210F | Print Fee Statement Summary | 流程五：财务报告 |
| CSTD225 | Print List of Centre Fee Statistics By Teacher | 流程五：财务报告 |
| CSTD230F | Print Supplementary Fee Statistics By Teacher | 流程五：财务报告 |
| CSTD220F | Print Entry Statistics By Teacher | 流程五：财务报告 |

---

*文档最后更新：2026 年 5 月*
