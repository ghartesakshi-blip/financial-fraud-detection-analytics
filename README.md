# 💳 Financial Fraud Detection & Risk Analytics System

![Tools](https://img.shields.io/badge/Tools-MySQL%20%7C%20Excel%20%7C%20Power%20BI-blue)
![Domain](https://img.shields.io/badge/Domain-Banking%20%26%20Fintech-red)
![Dataset](https://img.shields.io/badge/Dataset-284%2C807%20Transactions-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

A complete end-to-end fraud detection analytics system built on real European bank transaction data. This project identifies fraudulent credit card transactions using SQL-based anomaly detection, Excel risk modeling, and an interactive Power BI dashboard — replicating the exact workflow used by risk analysts at top consulting firms.

---

## 🎯 Business Problem

A European bank processes **284,807 transactions daily**. Hidden within them are fraudulent ones — fake purchases made using stolen card details. Manual review is impossible at this scale. This project builds a data-driven system that:
- Flags suspicious transactions automatically
- Scores each fraud case by risk level
- Identifies behavioral patterns used by fraudsters
- Delivers executive-ready insights via interactive dashboard

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **MySQL 8.0** | Data loading, querying, anomaly detection |
| **Microsoft Excel** | Risk scoring model, pivot analysis, conditional formatting |
| **Power BI Desktop** | Interactive dashboard, KPI cards, visualizations |

---

## 📊 Dataset

- **Source:** [Kaggle — Credit Card Fraud Detection by ULB](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Size:** 284,807 transactions · 31 columns
- **Fraud cases:** 492 (0.17%)
- **Features:** Time, Amount, V1-V28 (PCA anonymized), Class (0=Legit, 1=Fraud)

---

## 🔍 Methodology

```
Raw Data (CSV)
     ↓
MySQL — Data extraction & pattern analysis
     ↓
Excel — Risk scoring model & pivot summary
     ↓
Power BI — Interactive executive dashboard
```

### SQL Analysis
- Transaction volume analysis (fraud vs legitimate)
- Average amount comparison by transaction type
- Fraud rate by time of day (4 time buckets)
- 3-tier risk scoring (High / Medium / Low)
- Top 50 highest risk transaction profiling

### Excel Modeling
- Risk Score column using IF formula (3=High, 2=Medium, 1=Low)
- Pivot Table: Risk Level × Time of Day × Total Amount
- Conditional formatting (Red/Orange/Green risk coding)
- Auto-generated PivotChart for visual summary

### Power BI Dashboard
- 4 KPI Cards: Total Cases, Total Amount, High Risk Cases, Avg Amount
- Bar Chart: Fraud loss by time of day
- Donut Chart: Risk level breakdown
- Data Table: Top fraud transactions with drill-through
- Slicer: Interactive filter by risk level
- Custom dark professional theme

---

## 💡 Key Findings

### Finding 1 — Class Imbalance
> Only **0.17%** of transactions are fraudulent — making detection extremely challenging and requiring high system sensitivity.

### Finding 2 — Late Night Fraud Surge ⚠️
> Late night transactions **(12am–6am)** show a fraud rate of **0.518%** — nearly **4× higher** than evening hours (0.124%). Fraudsters target low-monitoring windows.

### Finding 3 — Card Testing Behavior 🔍
> Clusters of **€1.00 and €0.00** transactions detected — classic card testing pattern where criminals verify stolen cards before making larger purchases.

### Finding 4 — Medium Risk = Maximum Damage 💰
> **Medium Risk transactions (€200–€1000)** caused the highest total loss at **€33,728** — more than High Risk transactions (€13,237). Conventional bank systems miss this segment.

---

## 📈 Results Summary

| Risk Level | Cases | Avg Amount | Total Loss | % of Fraud |
|------------|-------|-----------|------------|------------|
| HIGH RISK | 9 | €1,470.81 | €13,237.33 | 1.83% |
| MEDIUM RISK | 76 | €443.80 | €33,728.56 | 15.45% |
| LOW RISK | 407 | €32.34 | €13,162.08 | 82.72% |
| **TOTAL** | **492** | **€122.21** | **€60,127.97** | **100%** |

---

## 📋 Fraud Rate by Time of Day

| Time Period | Total Transactions | Fraud Cases | Fraud Rate |
|-------------|-------------------|-------------|------------|
| Late Night (12am–6am) | 23,934 | 124 | **0.518%** |
| Morning (6am–12pm) | 70,912 | 118 | 0.166% |
| Afternoon (12pm–6pm) | 96,435 | 134 | 0.139% |
| Evening (6pm–12am) | 93,526 | 116 | 0.124% |

---

## 🏢 Business Recommendations

1. **Strengthen late night authentication** — Implement 2FA for all transactions between 12am–6am to reduce the 0.518% fraud rate
2. **Focus on Medium Risk** — Redirect fraud prevention resources toward €200–€1000 transactions — they cause maximum total damage
3. **Card testing alerts** — Flag accounts making multiple €0–€1 transactions within short windows — reliable early fraud indicator
4. **Real-time monitoring** — Deploy Power BI dashboard to fraud operations team for live transaction monitoring

---

## 📁 Repository Structure

```
📦 financial-fraud-detection-analytics
 ┣ 📊 fraud_analysis_final.xlsx      — Excel risk model & pivot analysis
 ┣ 📈 Fraud_Detection_Dashboard.pdf  — Power BI dashboard export
 ┣ 📄 Fraud_Detection_Portfolio.docx — Complete project case study
 ┗ 📝 README.md                      — Project documentation
```

---

## 🎓 About

Built as part of an MBA in Business Analytics portfolio — demonstrating end-to-end data analytics capability aligned with consulting-grade analytical work.

**Skills demonstrated:** SQL querying · Data cleaning · Risk scoring · Anomaly detection · Executive dashboarding · Business storytelling

---

⭐ *If you found this project useful, please give it a star!*

