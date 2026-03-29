# 💳 Financial Fraud Detection & Risk Analytics System

![Tools](https://img.shields.io/badge/Tools-MySQL%20%7C%20Excel%20%7C%20Power%20BI%20%7C%20Python-blue)
![ML Model](https://img.shields.io/badge/ML%20Model-Logistic%20Regression-purple)
![Accuracy](https://img.shields.io/badge/Accuracy-99.91%25-brightgreen)
![Domain](https://img.shields.io/badge/Domain-Banking%20%26%20Fintech-red)
![Dataset](https://img.shields.io/badge/Dataset-284%2C807%20Transactions-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

A complete **end-to-end fraud detection analytics system** built on real European bank transaction data. This project identifies fraudulent credit card transactions using SQL-based anomaly detection, Excel risk modeling, an interactive Power BI dashboard, and a Python Machine Learning model — replicating the exact workflow used by risk analysts at top consulting firms like Deloitte.

---

## 🎯 Business Problem

A European bank processes **2,84,807 transactions daily**. Hidden within them are fraudulent ones made using stolen card details. Manual review is impossible at this scale. This project builds a data-driven system that:

- Flags suspicious transactions automatically using SQL patterns
- Scores each transaction by risk level (High / Medium / Low)
- Identifies behavioral patterns used by fraudsters
- Predicts fraud probability using Machine Learning (0% to 100%)
- Delivers executive-ready insights via interactive Power BI dashboard

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **MySQL 8.0** | Data loading, querying, anomaly detection |
| **Microsoft Excel** | Risk scoring model, pivot analysis, conditional formatting |
| **Power BI Desktop** | Interactive dashboard, KPI cards, visualizations |
| **Python 3.13** | Machine Learning model — Logistic Regression |
| **Scikit-learn** | ML library for training, testing, evaluation |
| **Pandas & NumPy** | Data manipulation and mathematical operations |

---

## 📊 Dataset

- **Source:** [Kaggle — Credit Card Fraud Detection by ULB](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Size:** 2,84,807 transactions · 31 columns
- **Fraud cases:** 492 (0.17%)
- **Features:** Time, Amount, V1-V28 (PCA anonymized), Class (0=Legit, 1=Fraud)

---

## 🔍 Complete Methodology

```
Raw Data (CSV — 284,807 rows)
          ↓
    MySQL — SQL Analysis
    Pattern detection, risk scoring, time analysis
          ↓
    Excel — Risk Modeling
    IF formula scoring, Pivot Table, Conditional formatting
          ↓
    Power BI — Executive Dashboard
    KPI cards, bar chart, donut chart, slicer filters
          ↓
    Python ML — Logistic Regression
    Train → Test → 99.91% accuracy → Fraud probability scores
          ↓
    fraud_predictions.csv — Exported Results
    Each transaction scored with fraud probability %
```

---

## 🗄️ SQL Analysis — 5 Queries

### Query 1 — Fraud vs Legitimate Count
```sql
SELECT Class, COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM transactions), 2) AS percentage
FROM transactions GROUP BY Class;
```
**Result:** 2,84,315 legitimate (99.83%) · 492 fraud (0.17%) — extreme class imbalance

---

### Query 2 — Average Amount Analysis
```sql
SELECT CASE WHEN Class = 1 THEN 'Fraud' ELSE 'Legitimate' END AS transaction_type,
    ROUND(AVG(Amount), 2) AS avg_amount,
    ROUND(MAX(Amount), 2) AS max_amount
FROM transactions GROUP BY Class;
```
**Result:** Fraud avg €122.21 vs Legitimate avg €88.29 — fraudsters avoid large amounts to blend in

---

### Query 3 — Fraud Rate by Time of Day
```sql
SELECT
    CASE WHEN (Time % 86400) BETWEEN 0 AND 21599 THEN 'Late Night (12am-6am)'
         WHEN (Time % 86400) BETWEEN 21600 AND 43199 THEN 'Morning (6am-12pm)'
         WHEN (Time % 86400) BETWEEN 43200 AND 64799 THEN 'Afternoon (12pm-6pm)'
         ELSE 'Evening (6pm-12am)' END AS time_of_day,
    COUNT(*) AS total, SUM(Class) AS fraud_count,
    ROUND(100.0 * SUM(Class) / COUNT(*), 3) AS fraud_rate_pct
FROM transactions GROUP BY time_of_day ORDER BY fraud_rate_pct DESC;
```
**Result:** Late night fraud rate = 0.518% — 4x higher than evening (0.124%)

---

### Query 4 — Risk Scoring Model
```sql
SELECT Time, Amount,
    CASE WHEN Amount > 1000 THEN 'HIGH RISK'
         WHEN Amount > 200  THEN 'MEDIUM RISK'
         ELSE 'LOW RISK' END AS risk_level
FROM transactions WHERE Class = 1 ORDER BY Amount DESC;
```
**Result:** Detected card testing behavior — clusters of €0-€1 transactions

---

### Query 5 — Executive Summary
```sql
SELECT CASE WHEN Amount > 1000 THEN 'HIGH RISK'
            WHEN Amount > 200  THEN 'MEDIUM RISK'
            ELSE 'LOW RISK' END AS risk_level,
    COUNT(*) AS fraud_cases,
    ROUND(SUM(Amount), 2) AS total_loss
FROM transactions WHERE Class = 1
GROUP BY risk_level ORDER BY total_loss DESC;
```
**Result:** Medium Risk causes maximum damage at €33,728 — more than High Risk (€13,237)

---

## 🤖 Python Machine Learning Model

### Why ML was added
SQL risk scoring only used 1 column (Amount). The dataset has 30 columns. Logistic Regression uses ALL 30 columns together — giving each transaction a fraud probability between 0% and 100%.

### Model Code
```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# Separate features and target
X = df.drop('Class', axis=1)
y = df['Class']

# Split — 80% train, 20% test (stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train and evaluate
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)
print("Accuracy:", round(accuracy_score(y_test, model.predict(X_test)) * 100, 2), "%")
```

### Model Results

| Metric | Score | Business Meaning |
|--------|-------|-----------------|
| **Overall Accuracy** | **99.91%** | Correctly classifies 99.91% of all transactions |
| **Fraud Precision** | **83%** | When flagged as fraud — correct 83% of the time |
| **Fraud Recall** | **63%** | Catches 63% of all real fraud cases |
| **F1-Score** | **72%** | Balanced fraud detection performance |
| **Training rows** | **2,27,845** | 80% of dataset |
| **Testing rows** | **56,962** | 20% of dataset |

### Sample Fraud Probability Predictions

| Transaction | Actual | Predicted | Fraud Probability | Risk Level |
|-------------|--------|-----------|-------------------|------------|
| #1146 | Fraud | Fraud | **100.00%** | HIGH RISK |
| #3287 | Fraud | Fraud | **98.94%** | HIGH RISK |
| #7299 | Fraud | Fraud | **100.00%** | HIGH RISK |
| #840 | Fraud | Fraud | **67.40%** | MEDIUM RISK |

### Risk Level Distribution from ML Model
- HIGH RISK (70-100% probability): **71 transactions**
- MEDIUM RISK (30-70% probability): **22 transactions**
- LOW RISK (0-30% probability): **56,869 transactions**

---

## 💡 Key Findings

### Finding 1 — Class Imbalance
Only 0.17% of transactions are fraudulent — making detection extremely challenging and requiring high system sensitivity.

### Finding 2 — Late Night Fraud Surge
Late night (12am-6am) shows fraud rate of 0.518% — nearly **4x higher** than evening hours (0.124%). Fraudsters target low-monitoring windows.

### Finding 3 — Card Testing Behavior
Clusters of €1.00 and €0.00 transactions detected — criminals verify stolen cards before making larger purchases.

### Finding 4 — Medium Risk = Maximum Damage
Medium Risk transactions (€200-€1000) caused highest total loss at **€33,728** — more than High Risk (€13,237). Most conventional systems miss this.

### Finding 5 — ML Probability Scoring
Logistic Regression assigns precise fraud probabilities — 3 transactions scored **100% fraud probability**, giving investigators clear priority targets.

---

## 📋 Results Summary

| Risk Level | Cases | Avg Amount | Total Loss | % of Fraud |
|------------|-------|-----------|------------|------------|
| HIGH RISK | 9 | €1,470.81 | €13,237.33 | 1.83% |
| MEDIUM RISK | 76 | €443.80 | €33,728.56 | 15.45% |
| LOW RISK | 407 | €32.34 | €13,162.08 | 82.72% |
| **TOTAL** | **492** | **€122.21** | **€60,127.97** | **100%** |

| Time Period | Transactions | Fraud Cases | Fraud Rate |
|-------------|-------------|-------------|------------|
| Late Night (12am-6am) | 23,934 | 124 | **0.518%** |
| Morning (6am-12pm) | 70,912 | 118 | 0.166% |
| Afternoon (12pm-6pm) | 96,435 | 134 | 0.139% |
| Evening (6pm-12am) | 93,526 | 116 | 0.124% |

---

## 🏢 Business Recommendations

1. **Late night authentication** — Implement 2FA for all 12am-6am transactions
2. **Medium Risk focus** — Redirect fraud prevention to €200-€1000 transactions
3. **Card testing alerts** — Flag multiple €0-€1 transactions in short windows
4. **ML probability scoring** — Flag transactions above 70% probability for immediate review
5. **Real-time dashboard** — Deploy Power BI to fraud operations team

---

## 📁 Repository Structure

```
📦 financial-fraud-detection-analytics
 ┣ 🐍 fraud_ml_model.py              — Python Logistic Regression ML model
 ┣ 📊 fraud_analysis_final.xlsx      — Excel risk model & pivot analysis
 ┣ 📈 Fraud_Detection_Dashboard.pdf  — Power BI executive dashboard
 ┣ 📄 Fraud_Detection_Portfolio.docx — Complete project case study
 ┗ 📝 README.md                      — Project documentation
```

---

## 🚀 How to Run the Python Model

```bash
# Install libraries
pip install pandas numpy scikit-learn

# Run model
python fraud_ml_model.py
```

**Expected Output:**
```
Step 1 - Libraries loaded!
Step 2 - Data loaded! Total rows: 284807
Step 6 - Training model... please wait!
Model trained successfully!
Accuracy: 99.91 %
Step 8 - Exported fraud_predictions.csv successfully!
```

---

## 🎓 About

Built as part of an **MBA in Business Analytics** portfolio — demonstrating end-to-end analytics capability from raw data to machine learning, aligned with Deloitte's Risk Advisory practice.

**Skills:** SQL · Excel · Power BI · Python · Logistic Regression · Scikit-learn · Risk Scoring · Anomaly Detection · Executive Dashboarding

---

⭐ *If you found this project useful, please give it a star!*
