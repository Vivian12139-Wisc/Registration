# 第二阶段 8 个考试项目
## 功能共性分析与统一系统架构建议

**涵盖项目：** AP · BDA · CCMP · CSTD · EMSD · GCE · NATD · UOL

*版本：2025-12  |  机密文件*

---

**图例说明**

| 标记 | 说明 |
|------|------|
| ■ 全部 8 个项目共用 | 所有考试项目共用 |
| ■ 5-7 个项目共用 | 大多数考试项目共用 |
| ■ 2-4 个项目共用 | 部分考试项目共用 |
| 优先级 | 必须 / 建议 / 大部份 |

---

# 一、执行摘要 Executive Summary

透过分析 8 个考试项目的系统工作流程，发现各项目在系统流程、功能模组及操作逻辑上存在高度共性（约 75-85%），可归纳为以下三大功能域：

| 功能域 | 说明 | 共用模组数 |
|--------|------|-----------|
| **管理后台功能** | HKEAA 工作人员使用的系统后台操作，包括系统设置、报名管理、考场编排、文件生成、财务报告等 | ~18 个核心模组 |
| **考生端功能** | 考生透过网上门户（Portal）进行的所有操作，包括报名、付款、下载准考证、接收通知等 | ~8 个核心模组 |
| **集体 / 共用功能** | 跨项目共享的底层基础设施模组，所有考试系统共用，包括 COMM 系列函数、付款引擎、通知引擎等 | ~10 个核心模组 |

---

# 二、管理后台功能（Admin Backend Functions）

以下功能由 HKEAA 系统管理员及工作人员在后台操作，涵盖考试全生命周期的 6 个阶段。

## 2.1 系统设置 System Setup（报名前准备）

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Maintain Application Parameters (UTL010)** | 维护考试年度、系列、联络资讯等全局参数 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Maintain Exam / Subject / Grade Info** | 维护考试名称、科目代码、级别、考试日期时间及费用 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Maintain Exam Centre** | 新增/修改考试中心代码、名称及地址 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Maintain Online Registration Info (COMM30005)** | 设置网上报名开放时间、截止日期、遲报费、URL 连结 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Maintain School / Examiner** | 维护参与学校名单（支援 Excel 上载）及考官资料 | AP·BDA·CCMP·CSTD·GCE·UOL | **必须** |
| **User Role & Menu Maintenance (COMM20035 / COMM20025)** | 管理用户账号、角色及系统菜单访问权限 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Maintain Online Portal User (COMM20060)** | 管理考生门户账号状态及重设密码 | AP·BDA·CCMP·CSTD·GCE·UOL | **必须** |
| **Maintain Forbidden Subjects** | 设置不可同时报考的科目组合（Timetable Clash 规则） | GCE·AP | **建议** |

## 2.2 报名处理 Registration & Entry Processing

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Load & Validate Entry Data** | 批量载入考生报名资料（CSV/Excel/TXT），执行格式及规则校验 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Maintain Entry Data** | 逐一查閱及修改考生报名资料（姓名、科目、身份证、费用） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Validate Entry Data** | 二次校验：费用计算、禁止科目组合、缺失栏位 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Print List of Candidates** | 按考生编号 / 姓名 / 科目生成考生名单报告 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Generate & Print Entry Statistics** | 输出各科目 / 级别的报考人数统计 | AP·BDA·CCMP·CSTD·GCE·UOL | **必须** |
| **Track Entry Amendment Log** | 记录所有后台对考生资料的修改日誌（Audit Trail） | AP·BDA·CCMP·CSTD·GCE·UOL | **必须** |
| **Generate Candidate Data File (XX520F)** | 输出完整考生资料 Excel 檔案，供对外提交或內部核查 | AP·BDA·CCMP·CSTD·GCE·UOL | **必须** |
| **SFAA / EDB Interface** | 生成并提交考试资料至社会福利署（SFAA）及教育局（EDB） | GCE·AP | **必须** |
| **Misc Payment / PLU Table (PAY20015 / PAY20080)** | 为特殊收费（如特殊试场安排费）创建付款连结 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |

## 2.3 考场编排 Centre Allocation

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Load / Maintain Examination Hall** | 上载及维护考试场地资料（房间名称、容量、座位佈局） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Maintain Allocation Parameters** | 为每份试卷设置编排参数（起始座位号、每房人数、场次） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Handle Special Cases (SEN / Back-to-Back)** | 人手处理特殊考生（SEN 额外时间）及连场考试的座位衝突 | AP·GCE·BDA·CSTD | **必须** |
| **Run Centre Allocation (System Auto)** | 系统按参数自动分配候选人至考场及座位 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Check Errors: Unallocated / Duplicate** | 生成未分配考生清单及重复座位报告，供人手復查 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Manually Adjust Seat Numbers (MaintainAllocated Hall/Seat)** | 在系统自动编排后对个别考生进行人手调位 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Print / Export Allocation Summary** | 输出编排摘要、考场报告（PDF + Excel） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |

## 2.4 试卷文件 Exam Stationeries & Dispatch

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Upload Admission Form Template (XX20065)** | 上载准考证 Word/PDF 范本至系统 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Print / Generate Admission Form (XX405F)** | 系统將考生资料自动填入范本，批量生成准考证（PDF） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Print Attendance List (XX410F)** | 按日期/科目/场次列印点名表 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Upload Appointment Email Template (COMM20115)** | 设置准考证发放通知电邮范本 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Publish Admission Form to Portal (Publish Appointments)** | 设定日期后系统自动发邮件通知考生下载准考证 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Print / Export Exam Schedule** | 输出考试时间表（供监考人员使用） | GCE·UOL·CSTD·BDA | **必须** |
| **Upload / Print Day Sheet (Music) (XX420F / XX421F)** | 音樂术科考试專用：上载日程范本并生成每日考试日程表 | BDA·CCMP·CSTD | **必须** |
| **Print Stationery Report** | 统计各考场试卷用量及考试文具需求 | GCE·CSTD | **建议** |

## 2.5 考后处理 Post-Exam Processing

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Upload Candidate Results (XX535F)** | 上载含 Barcode 的成绩单 OMR 掃描结果（TXT/CSV） | BDA·CCMP·CSTD·EMSD | **必须** |
| **Maintain Candidate Results (XX502F)** | 人工核对并修正个别考生成绩（包括缺席标记） | BDA·CCMP·CSTD | **必须** |
| **Print Mark Report (XX410F)** | 生成含个人成绩及 Barcode 的考生成绩单 | BDA·CCMP·CSTD | **必须** |
| **Generate Candidate Data File (XX520F)** | 考试完结后输出所有考生成绩及资料的完整 Excel 报告 | BDA·CSTD·GCE·UOL·AP | **必须** |
| **Generate Subject Data in CSV (XX165)** | 输出考生通讯地址清单（供邮寄成绩通知書） | GCE·UOL | **建议** |

## 2.6 财务报告 Financial Reporting

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Print Fee Statement (XX225)** | 详列每位申请人的缴费日期、方式及金额 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Print List of Fee Payments (XX230)** | 列出所有已付款记录 | AP·BDA·CCMP·CSTD·GCE·UOL | **必须** |
| **Print List of Exam Fee Difference (XX235)** | 列出费用差异（如遲报附加费） | GCE·UOL·BDA·CSTD | **必须** |
| **Print Supplementary Fee Statistics (XX240)** | 详列各申请人应付的场地费及附加费 | BDA·CSTD·GCE | **必须** |
| **Print Entry Statistics By Teacher (XX220F)** | 详列各申请人（老师）旗下每级别的考生人数 | BDA·CSTD | **建议** |
| **Report Repository Explorer (COMM20050)** | 统一报告库：下载所有已生成报告（PDF）的历史记录 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Print Misc. Payment Report (PAY20095)** | 列出所有杂项付款记录（如特殊安排费） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **建议** |

---

# 三、考生端功能（Candidate Portal Functions）

以下功能为考生透过网上门户（Online Portal）直接使用，设计应以用户体验优先，确保流程清晰、操作簡便。

## 3.1 报名流程 Registration Journey

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Create Portal Account / Login** | 考生创建网上账号（或以机构账号登入），完成身份验证 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Submit Registration Application** | 填寫并提交报名表格（科目选择、个人资料、SEN 申请） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Validate Code Verification** | 输入由考试局提供的验证码（Validate Code）确认报名资格 | UOL | **必须** |
| **Subject Change Application** | 提交科目更改申请表（系统校验名额及时间衝突） | AP | **必须** |
| **View Registration Status** | 实时查看报名状态（待審核 / 已确认 / 待付款） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |

## 3.2 付款流程 Payment Journey

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Receive Payment Link via Email** | 报名成功后自动收到付款连结电邮（含付款截止日期） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Complete Online Payment** | 透过付款连结完成考试费缴付（信用卡、FPS、轉数快等） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Receive Payment Confirmation Email** | 付款完成后自动收到付款确认电邮（含参考号码） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Receive Payment Reminder (Auto)** | 临近截止日前一天系统自动发送付款提醒（適用未付款者） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Supplementary Fee Payment** | 收到特殊安排服务费（如 SEN 费用）的付款连结并完成付款 | AP·GCE·CSTD | **必须** |

## 3.3 准考文件 Admission Documents

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Receive Admission Form Release Email** | 准考证发放时收到系统自动通知电邮 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Download E-Admission Form (PDF)** | 登入门户下载电子准考证 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **View / Download Candidate Checklist** | 查看及下载个人报名资料确认清单（核对科目、个人资料） | AP·GCE·UOL·BDA·CSTD | **必须** |
| **Confirm Checklist Details** | 确认清单资料无误或提交更正申请 | GCE·AP | **建议** |

## 3.4 通知系统 Notification System（考生側）

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Registration Confirmation Email** | 报名成功后发送确认电邮（含报名详情） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **Subject Change Outcome Email** | 科目更改審批结果通知（成功 / 失敗 + 原因） | AP | **必须** |
| **Exam Date Reminder** | 考试前发送日期及地点提醒 | AP·BDA·CCMP·CSTD·GCE·UOL | **建议** |
| **Result Release Notification** | 成绩公布后通知考生登入查閱 | BDA·CCMP·CSTD | **建议** |

---

# 四、集体 / 共用功能（Shared & Collective Functions）

以下兩类功能属於「集体」范疇：

- **底层共用基础设施模组（COMM / PAY / UTL 系列）：** 所有 8 个考试系统共用，建议抽离为独立共用服务层（Shared Service Layer）
- **机构 / 集体报名功能：** 由学校、老师或机构代表以集体名义为多名考生办理报名手续

## 4.1 底层共用基础设施 Shared Infrastructure Modules

标记为 **COMM / PAY / UTL** 的函数在所有项目中使用完全相同的功能代码，是最具抽离價值的共用模组。

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **COMM30005 Maintain Exam Info for Online Reg.** | 设置各考试在网上报名系统中的显示资讯、开放时间及相关参数 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **COMM20050 Report Repository Explorer** | 统一报告库：儲存、分类及下载所有考试生成的 PDF 报告 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **COMM20035 User Role Maintenance** | 全系统用户角色及操作权限管理（適用所有考试模组） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **COMM20025 Menu Maintenance** | 系统菜单项目管理（显示 / 隐藏功能入口） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **COMM20060 Maintain Online Portal User** | 统一管理考生门户账号（建立、停用、重设密码） | AP·BDA·CCMP·CSTD·GCE·UOL | **必须** |
| **COMM20115 Appointment Template** | 管理准考证电邮通知范本（支援中英双语） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **COMM20135 Checklist Template** | 管理考生资料确认清单范本 | GCE·UOL·AP·BDA·CSTD | **必须** |
| **UTL010 Application Parameters** | 全局应用参数维护（考试年度、系列、系统联络资讯） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **PAY20015 Misc Payment** | 建立杂项付款连结（用於特殊服务费、遲报费等） | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **PAY20080 Price Look-Up (PLU) Table** | 维护所有考试杂项收费项目及金额 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **必须** |
| **PAY20095 Print Misc. Payment Report** | 输出杂项付款统计报告 | AP·BDA·CCMP·CSTD·EMSD·GCE·NATD·UOL（全部） | **建议** |

## 4.2 机构 / 集体报名功能 Institutional Group Registration

部分考试允许学校或老师以集体名义代表多名考生办理报名，以下功能專为此场景设计：

| Function / 功能 | 描述 Description | 共用项目 Projects | 优先级 |
|----------------|-----------------|-----------------|--------|
| **Maintain Applicant Group Data (XX150F)** | 建立并维护申请人（老师/机构）旗下的考生组别资料 | BDA·CSTD·CCMP | **必须** |
| **Maintain Entry Data (Teachers) (XX115F - Teacher Mode)** | 老师以集体形式管理旗下所有考生的报名资料（科目、级别） | BDA·CSTD·CCMP | **必须** |
| **Validate Entry Data (XX110F - Group Mode)** | 校验集体报名资料的格式及费用正确性 | BDA·CSTD·CCMP | **必须** |
| **Generate School Candidate Online Registration Entry Data in CSV (XX20010)** | 为学校考生生成 CSV 格式报名资料，供后台批量载入 | GCE·UOL | **必须** |
| **Export Online Registration Entry Data for Punching (XX20030)** | 输出 CSV 供工作人员手动补填考生编号、中心代码后重新上载 | GCE·UOL | **必须** |
| **Maintain Examiner (XX20025)** | 为音樂术科考试指派考官至特定时段及考生组别 | BDA·CCMP·CSTD | **必须** |
| **Generate Teacher Centre (BDA305F)** | 系统根据老师资料自动生成考试中心配置 | BDA·CCMP | **建议** |
| **Print Fee Statement Summary By Teacher (XX210F)** | 按老师/申请人列出详細收费（含组别费及场地附加费） | BDA·CSTD | **必须** |
| **Print Entry Statistics By Teacher (XX220F)** | 按老师列出每级别考生人数统计 | BDA·CSTD | **建议** |
| **Print Centre Fee Stats By Teacher (XX225F)** | 统计各申请人应付场地费的组别数量 | BDA·CSTD | **建议** |

---

# 五、统一系统架构优化建议

基於以上功能共性分析，建议將现有 8 个独立系统重新架构为「一个统一平台 + 考试配置模组」的模式：

## 5.1 核心优化方向

| 优化方向 | 具体措施 | 预期效益 |
|---------|---------|---------|
| **共用服务层 (Shared Service Layer)** | 將所有 COMM / PAY / UTL 模组抽离为独立共用服务，所有考试系统调用同一实例，消除重复建设。影響模组：COMM30005, COMM20035, COMM20050, COMM20025, COMM20060, COMM20115, COMM20135, PAY20015, PAY20080, UTL010 | 减少 ~40% 重复代码；统一维护；一次修改全部生效 |
| **配置驱动架构 (Config-Driven)** | 以「考试配置 Profile」替代独立代码库：每个考试（AP/BDA/GCE 等）只需维护一份配置文件，定义其科目结构、费用规则、编排参数、电邮范本及报表格式，核心引擎通用。 | 新增考试类型從「开发新系统」缩短为「填寫配置文件」 |
| **统一工作流引擎 (Unified Workflow Engine)** | 六个阶段（Setup → Registration → Allocation → Dispatch → Post-Exam → Finance）共用同一工作流引擎，每个考试类型通过配置开啟/关閉特定步驟（如音樂考试需要 Day Sheet，筆试不需要）。 | 新增 / 修改业务流程只需改配置，无需动核心代码 |
| **统一通知引擎 (Notification Engine)** | 建立单一电邮通知服务，所有考试类型共用，通过范本（COMM20115/20135）和触发规则配置，支援中英双语及多渠道（Email / SMS）。 | 消除各系统各自维护通知逻辑的问题 |
| **统一考生门户 (Single Candidate Portal)** | 考生只需一个登入账号，可管理旗下所有考试的报名、付款及文件下载，跨考试统一显示付款状态和准考证。 | 提升考生体验；减少账号管理工作量 |
| **统一财务仪表板 (Finance Dashboard)** | 在 Report Repository Explorer (COMM20050) 基础上，建立跨考试的财务总览仪表板，即时显示各考试报考人数、收款状态及费用差异。 | 管理层即时掌握所有考试财务状况 |

## 5.2 建议模组分层架构

| 层次 | 组成模组 |
|------|---------|
| **Layer 1 考试配置层** | AP Config │ BDA Config │ CCMP Config │ CSTD Config │ EMSD Config │ GCE Config │ NATD Config │ UOL Config（每个考试一份配置 Profile，定义业务规则及流程开关） |
| **Layer 2 业务功能层** | 报名管理模组 │ 考场编排模组 │ 文件生成模组 │ 成绩处理模组 │ 财务报告模组 │ 集体报名模组（音樂/学校） |
| **Layer 3 共用服务层** | 统一通知引擎（COMM20115/20135） │ 统一付款服务（PAY系列） │ 统一报告库（COMM20050） │ 用户身份验证（COMM20035/20060） |
| **Layer 4 门户层** | 管理后台 Admin Portal（HKEAA 工作人员） │ 考生门户 Candidate Portal │ 机构门户 Institutional Portal（学校/老师） |

## 5.3 实施优先次序建议

### 第一优先（立即可行）

- 抽离 COMM / PAY / UTL 系列为共用服务层（无业务逻辑，純配置）
- 统一报告库（COMM20050）升级为仪表板
- 考生门户统一登入（SSO）

### 第二优先（中期规划）

- 考场编排引擎通用化（配置驱动取代各系统独立实现）
- 通知引擎统一化（范本管理 + 触发规则配置）
- 集体报名模组独立化（音樂 / 学校共用）

### 第三优先（长期规划）

- 全面配置驱动架构：新考试类型零代码上线
- 统一财务仪表板（跨考试实时数据）
- API 开放：支援第三方机构直接接入系统报名

---

*— 文件完 —*
