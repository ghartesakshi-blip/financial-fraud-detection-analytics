# ============================================
# FINANCIAL FRAUD DETECTION — ML MODEL
# Logistic Regression | By: Your Name
# ============================================

# Step 1 — Import libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

print("✅ Step 1 — Libraries loaded!")

# Step 2 — Load data
df = pd.read_csv(r'C:\Users\sakshi gharte\Downloads\creditcard.csv (1)\creditcard.csv')

print("✅ Step 2 — Data loaded!")
print("Total rows:", len(df))
print("Fraud cases:", df['Class'].sum())
print("Legitimate cases:", len(df) - df['Class'].sum())

# Step 3 — Prepare the data
# Separate features (X) and target (y)
X = df.drop('Class', axis=1)  # Everything except fraud label
y = df['Class']               # Just the fraud label (0 or 1)

print("Step 3 - Data prepared!")
print("Features:", X.shape[1], "columns")
print("Target: Class column (0=Legit, 1=Fraud)")

# Step 4 — Split data into Training and Testing
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

print("\nStep 4 - Data split done!")
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))

# Step 5 — Scale the data
# Makes all numbers same scale so model learns better
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nStep 5 - Data scaled!")

# Step 6 — Train the ML Model
print("\nStep 6 - Training model... please wait!")
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

print("Model trained successfully!")

# Step 7 — Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nStep 7 - Model tested!")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("\nDetailed Report:")
print(classification_report(y_test, y_pred, target_names=['Legitimate', 'Fraud']))

# Step 8 — Export fraud probability scores
print("\nStep 8 - Generating fraud probability scores...")

# Get probability of fraud for each transaction
fraud_proba = model.predict_proba(X_test)[:, 1]

# Create results dataframe
results = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': y_pred,
    'Fraud_Probability_%': (fraud_proba * 100).round(2),
    'Risk_Level': pd.cut(
        fraud_proba * 100,
        bins=[0, 30, 70, 100],
        labels=['LOW RISK', 'MEDIUM RISK', 'HIGH RISK']
    )
})

# Save to CSV
results.to_csv(r'C:\Users\sakshi gharte\Downloads\fraud_predictions.csv', index=False)

print("Exported successfully!")
print("\nSample predictions:")
print(results[results['Actual'] == 1].head(10))
print("\nRisk Level Summary:")
print(results['Risk_Level'].value_counts())