-- ============================================================
-- FRAUD DETECTION ANALYTICS
-- BigQuery SQL Analysis
-- Dataset: Synthetic Fraud Detection Transactions
-- ============================================================


-- ============================================================
-- 1. TOTAL TRANSACTIONS
-- Business Question:
-- How many cleaned transactions are in the dataset?
-- ============================================================

SELECT
  COUNT(*) AS total_transactions
FROM `essential-storm-508407-b9.fraud_detection.transactions`;


-- ============================================================
-- 2. TOTAL TRANSACTION VALUE
-- Business Question:
-- What is the total value of all transactions?
-- ============================================================

SELECT
  ROUND(SUM(amount_inr), 2) AS total_transaction_value_inr
FROM `essential-storm-508407-b9.fraud_detection.transactions`;


-- ============================================================
-- 3. FLAGGED TRANSACTIONS AND FLAGGED RATE
-- Business Question:
-- How many transactions are flagged?
-- What percentage of transactions are flagged?
-- ============================================================

SELECT
  COUNTIF(is_fraud = 1) AS flagged_transactions,
  COUNT(*) AS total_transactions,
  ROUND(
    COUNTIF(is_fraud = 1) * 100.0 / COUNT(*),
    2
  ) AS flagged_rate_percent
FROM `essential-storm-508407-b9.fraud_detection.transactions`;


-- ============================================================
-- 4. PAYMENT CHANNEL ANALYSIS
-- Business Question:
-- Which payment channels have the most flagged transactions?
-- ============================================================

SELECT
  COALESCE(payment_channel, 'Unknown') AS payment_channel,
  COUNTIF(is_fraud = 1) AS flagged_transactions,
  COUNT(*) AS total_transactions,
  ROUND(
    COUNTIF(is_fraud = 1) * 100.0 / COUNT(*),
    2
  ) AS flagged_rate_percent
FROM `essential-storm-508407-b9.fraud_detection.transactions`
GROUP BY payment_channel
ORDER BY flagged_transactions DESC;


-- ============================================================
-- 5. LOCATION ANALYSIS
-- Business Question:
-- Which locations have the most flagged transactions?
-- ============================================================

SELECT
  COALESCE(location, 'Unknown') AS location,
  COUNTIF(is_fraud = 1) AS flagged_transactions,
  COUNT(*) AS total_transactions,
  ROUND(
    COUNTIF(is_fraud = 1) * 100.0 / COUNT(*),
    2
  ) AS flagged_rate_percent
FROM `essential-storm-508407-b9.fraud_detection.transactions`
GROUP BY location
ORDER BY flagged_transactions DESC;


-- ============================================================
-- 6. HIGH-VALUE FLAGGED TRANSACTIONS
-- Business Question:
-- Which flagged transactions should be prioritized for review?
-- ============================================================

SELECT
  transaction_id,
  customer_id,
  amount_inr,
  payment_channel,
  merchant_category,
  location,
  risk_level,
  failed_attempts,
  device_trust_score,
  is_fraud
FROM `essential-storm-508407-b9.fraud_detection.transactions`
WHERE is_fraud = 1
ORDER BY amount_inr DESC
LIMIT 20;


-- ============================================================
-- 7. RISK LEVEL ANALYSIS
-- Business Question:
-- Which risk level has the highest flagged rate?
-- ============================================================

SELECT
  risk_level,
  COUNT(*) AS total_transactions,
  COUNTIF(is_fraud = 1) AS flagged_transactions,
  ROUND(
    COUNTIF(is_fraud = 1) * 100.0 / COUNT(*),
    2
  ) AS flagged_rate_percent
FROM `essential-storm-508407-b9.fraud_detection.transactions`
GROUP BY risk_level
ORDER BY flagged_rate_percent DESC;


-- ============================================================
-- 8. MERCHANT CATEGORY ANALYSIS
-- Business Question:
-- Which merchant categories have the most flagged transactions?
-- ============================================================

SELECT
  COALESCE(merchant_category, 'Unknown') AS merchant_category,
  COUNT(*) AS total_transactions,
  COUNTIF(is_fraud = 1) AS flagged_transactions,
  ROUND(
    COUNTIF(is_fraud = 1) * 100.0 / COUNT(*),
    2
  ) AS flagged_rate_percent
FROM `essential-storm-508407-b9.fraud_detection.transactions`
GROUP BY merchant_category
ORDER BY flagged_transactions DESC;


-- ============================================================
-- END OF ANALYSIS
-- ============================================================