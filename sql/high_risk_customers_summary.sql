SELECT 
  AccountID,
  COUNT(*) AS total_transactions,
  SUM(CAST(is_fraud AS INT64)) AS fraud_transactions,
  ROUND(SUM(CAST(is_fraud AS FLOAT64)) / COUNT(*) * 100, 2) AS fraud_rate_percentage
FROM 
  `metal-arc-460019-p7.transaction_data.bank_transactions`
GROUP BY 
  AccountID
HAVING 
  fraud_transactions > 0
ORDER BY 
  fraud_rate_percentage DESC, fraud_transactions DESC;