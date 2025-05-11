# 🚀 Customer Onboarding Workflow Automation using JIRA & Databricks

This repository documents the end-to-end implementation of a customer onboarding workflow management system built using JIRA, enhanced with automation rules, and integrated with Databricks for analytics and dashboarding.

---

## 📌 Project Overview

Aimed at improving **visibility**, **accountability**, and **efficiency** during the customer onboarding process, this solution leverages:
- JIRA workflows & screen schemes
- Automation rules
- JIRA API integration
- Databricks dashboards

---

## ⚙️ JIRA Configuration

**Workflow Scheme:** `RevOps Implementation`

- **Phases:** `To Do → Phase 01 → ... → Phase 07 → Completed`
- **Rule:** Forward-only progression; no backward transitions
- **Issue Types:** `Epic`, `Task`, `Sub-task`

**Custom Screen & Field Scheme:**
- Implementation Status
- Task Aging (Created Date & Start Date Based)
- Delay Reason (Custom Field)

---

## 🤖 Automation Rules

> Located in `/automation-rules/`

| File Name                                         | Description                                               |
|--------------------------------------------------|-----------------------------------------------------------|
| `RevOps_Reminder_For_Due_Date.json`              | Sends daily reminders for tasks due in 2 days             |
| `RevOps_Due_Date_Update_Customer_Implementation.json` | Auto-updates Due Date based on Start Date               |
| `RevOps_Capture_Due_Date_Reason.json`            | Prompts users to input a reason when Due Date is changed  |
| `RevOps_Default_Label_Assignment.json`           | Adds "Yet-To-Start" label if no label is present          |
| `RevOps_Comment_Due_Date_Reason.json`            | Posts a comment summarizing the reason for date change    |
| `RevOps_Due_Date_Email_Alert.json`               | Sends alerts for overdue tasks at 10:00 AM IST            |


---

## 🔗 JIRA API + Databricks Integration

> Located in `/api-integration/`

- Pulls data from JIRA using Python (REST API)
- Extracts:
  - Epics / Tasks / Sub-tasks
  - Statuses & custom fields
- Data processed in Databricks for dashboarding

### Dashboards Visualize:
- Task Aging (Board Creation & Start Date Based)
- Onboarding Status by Customer
- Delay Reasons (Logged by CSMs/AMs)

## 📊 Dashboard KPIs

- **Implementation Status:**  
  - 🔴 Red – Overdue  
  - 🟡 Yellow – On Track  
  - 🟢 Green – Go-Live  

- **Project Aging:**  
  - Based on board creation date and actual task start

- **Delay Comments:**  
  - Captured manually by CSMs/AMs for context

- **Quarterly Segmentation:**  
  - Customers categorized by onboarding quarter

---

## 📁 Supporting Assets

| Path                            | Description                        |
|---------------------------------|------------------------------------|
| `docs/white-paper.pdf`          | Full project documentation         |
| `docs/onboarding_workflow.pptx` | Visual walkthrough presentation    |
| `dashboard-assets/`             | Dashboard snapshots and graphs     |

---

## 📈 Results

- 📈 **30% increase** in on-time onboarding completions  
- 👁️ **Real-time visibility** into blockers and KPIs  
- 🔄 **Reduced manual follow-ups** via automation  

---

## 👤 Authors & Maintainers

**[Your Name]** – Project Manager & Automation Lead  
📧 Email: [your.email@example.com]  
🔗 LinkedIn: [linkedin.com/in/yourprofile]  

---

## 📃 License

This project is for internal documentation and demonstration purposes.  
Please contact the author before reuse or external distribution.

---

## 📥 Setup Instructions

For replication or integration, refer to:
- `api-integration/setup.md`
- `automation-rules/readme.md`

---
