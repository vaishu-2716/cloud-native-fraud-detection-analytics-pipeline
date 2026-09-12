import pandas as pd

# Path to our raw dataset
file_path = "data/financial_fraud_transactions_10000.csv"

# Load the CSV
df = pd.read_csv(file_path)

# -------------------------------
# BASIC DATASET INFORMATION
# -------------------------------

print("=" * 60)
print("FRAUD DETECTION DATASET - INITIAL INSPECTION")
print("=" * 60)

print("\n1. Dataset shape:")
print(df.shape)

print("\n2. Column names:")
print(df.columns.tolist())

print("\n3. First 5 rows:")
print(df.head())

print("\n4. Data types:")
print(df.dtypes)

print("\n5. Missing values:")
print(df.isnull().sum())

print("\n6. Duplicate rows:")
print(df.duplicated().sum())

print("\n7. Duplicate transaction IDs:")
print(df["transaction_id"].duplicated().sum())

print("\n8. Fraud distribution:")
print(df["is_fraud"].value_counts())

print("\n9. Basic statistics:")
print(df.describe())

print("=" * 60)
print("INITIAL INSPECTION COMPLETE")
print("=" * 60)