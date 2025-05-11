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

## Visuals

### Aging Days Based On:
- **Board Creation Date**
- **Project Start Date (Actual Work Commencement)**

---

### Project Tasks Overview:
- **Status Distribution:**
  - To Do
  - In Progress
  - Completed
  
- **Phase-wise Progress:**
  - Phase 01 to Phase 07

---

### Individual Dashboards per Assignee:
- Number of tasks completed, pending, and overdue
- Personalized workload summaries

---

### Overall Project Status View:
- High-level implementation stage for each customer
- **Traffic-light Indicators:**
  - 🔴 **Red** – Overdue
  - 🟡 **Yellow** – On Track
  - 🟢 **Green** – Go-Live

---

### Quarterly Cohort Segmentation:
- Customers grouped based on onboarding quarter
- Used to track lifecycle and delivery aging
---

## 📁 Supporting Assets

| Path                            | Description                        |
|---------------------------------|------------------------------------|
| `docs/documentation.pdf`        | Full project documentation         |
| `docs/Workflow_Schema.jpg`      | Project Workflow Structure         |
| `docs/Automation.jpg`           | Project Automation                 |

---

## 📈 Results

- 📅 **30% reduction** in manual follow-ups through task tracking automation (due dates, reminders, status updates).
- 🕒 **40% decrease** in missed deadlines due to streamlined workflows and automatic status updates.
- 🔍 **Increased project visibility** with real-time status and due date tracking, empowering teams to stay on top of progress.
- 📈 **Boosted team efficiency**, leading to faster task completion and improved accountability.

---

## 👤 Authors & Maintainers

**[Avinash M]** – Business Analyst  
📧 Email: [avinashsolai@gmail.com]  
🔗 LinkedIn: [www.linkedin.com/in/avinash-m-va73]  

**Mentor: [Ashray Kiran]** – Senior Associate Revops  
📧 Email: [ashrayking94@gmail.com]  
🔗 LinkedIn: [www.linkedin.com/in/ashray-kiran-927932b4]  

---
