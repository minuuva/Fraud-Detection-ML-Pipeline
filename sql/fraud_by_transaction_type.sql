SELECT 
  TransactionType,
  COUNT(*) AS total,
  SUM(is_fraud) AS fraud_count,
  ROUND(SUM(is_fraud) * 100.0 / COUNT(*), 2) AS fraud_rate
FROM `metal-arc-460019-p7.transaction_data.bank_transactions`
GROUP BY TransactionType
ORDER BY fraud_rate DESC;