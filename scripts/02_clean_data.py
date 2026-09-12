import pandas as pd

# ==================================================
# 1. LOAD RAW DATA
# ==================================================

input_file = "data/financial_fraud_transactions_10000.csv"
output_file = "data/cleaned_fraud_transactions.csv"

df = pd.read_csv(input_file)

print("=" * 70)
print("FRAUD DETECTION - DATA CLEANING")
print("=" * 70)

print("\nOriginal shape:")
print(df.shape)


# ==================================================
# 2. CHECK ORIGINAL DATA QUALITY
# ==================================================

print("\nOriginal missing values:")
print(df.isnull().sum())

print(
    "\nOriginal duplicate transaction IDs:",
    df["transaction_id"].duplicated().sum()
)


# ==================================================
# 3. CONVERT TIMESTAMP
# ==================================================

df["transaction_timestamp"] = pd.to_datetime(
    df["transaction_timestamp"],
    errors="coerce",
    dayfirst=True
)

invalid_timestamps = df["transaction_timestamp"].isna().sum()

print(
    "\nInvalid timestamps found:",
    invalid_timestamps
)
# Remove rows with invalid timestamps
df = df.dropna(
    subset=["transaction_timestamp"]
).copy()

print(
    "Rows remaining after removing invalid timestamps:",
    len(df)
)


# ==================================================
# 4. HANDLE MISSING CATEGORICAL VALUES
# ==================================================

categorical_columns = [
    "payment_channel",
    "merchant_category",
    "location",
    "device_type"
]

for column in categorical_columns:
    df[column] = df[column].fillna("Unknown")

print("\nMissing categorical values replaced with 'Unknown'.")


# ==================================================
# 5. HANDLE INVALID TRANSACTION AMOUNTS
# ==================================================

invalid_amounts = df["amount_inr"] < 0

print(
    "\nNegative transaction amounts found:",
    invalid_amounts.sum()
)

# Remove transactions with invalid negative amounts
df = df[df["amount_inr"] >= 0].copy()


# ==================================================
# 6. HANDLE INVALID FAILED ATTEMPTS
# ==================================================

invalid_failed_attempts = df["failed_attempts"] < 0

print(
    "\nNegative failed attempts found:",
    invalid_failed_attempts.sum()
)

# Replace invalid values with 0
df.loc[
    invalid_failed_attempts,
    "failed_attempts"
] = 0


# ==================================================
# 7. HANDLE INVALID DEVICE TRUST SCORES
# ==================================================

invalid_trust_score = (
    (df["device_trust_score"] < 0) |
    (df["device_trust_score"] > 100)
)

print(
    "\nInvalid device trust scores found:",
    invalid_trust_score.sum()
)

# Replace invalid values with the median
median_trust_score = df.loc[
    ~invalid_trust_score,
    "device_trust_score"
].median()

df.loc[
    invalid_trust_score,
    "device_trust_score"
] = median_trust_score


# ==================================================
# 8. REMOVE DUPLICATE TRANSACTION IDs
# ==================================================

duplicate_ids = df["transaction_id"].duplicated()

print(
    "\nDuplicate transaction IDs before removal:",
    duplicate_ids.sum()
)

df = df.drop_duplicates(
    subset=["transaction_id"],
    keep="first"
)


# ==================================================
# 9. FINAL DATA QUALITY CHECK
# ==================================================

print("\nFinal missing values:")
print(df.isnull().sum())

print(
    "\nFinal duplicate transaction IDs:",
    df["transaction_id"].duplicated().sum()
)

print(
    "\nFinal negative amounts:",
    (df["amount_inr"] < 0).sum()
)

print(
    "\nFinal negative failed attempts:",
    (df["failed_attempts"] < 0).sum()
)

print(
    "\nFinal invalid device trust scores:",
    (
        (df["device_trust_score"] < 0) |
        (df["device_trust_score"] > 100)
    ).sum()
)


# ==================================================
# 10. SAVE CLEANED DATA
# ==================================================

df.to_csv(
    output_file,
    index=False
)

print("\nFinal shape:")
print(df.shape)

print("\nCleaned dataset saved to:")
print(output_file)

print("=" * 70)
print("DATA CLEANING COMPLETE")
print("=" * 70)