SELECT 
  is_fraud,
  ROUND(AVG(TransactionAmount), 2) AS avg_amount,
  ROUND(STDDEV(TransactionAmount), 2) AS std_amount,
  ROUND(AVG(TransactionDuration), 2) AS avg_duration,
  ROUND(STDDEV(TransactionDuration), 2) AS std_duration
FROM `metal-arc-460019-p7.transaction_data.bank_transactions`
GROUP BY is_fraud;