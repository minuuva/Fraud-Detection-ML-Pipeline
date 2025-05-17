SELECT 
  is_fraud,
  COUNT(*) AS count,
  ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM `metal-arc-460019-p7.transaction_data.bank_transactions`
GROUP BY is_fraud;