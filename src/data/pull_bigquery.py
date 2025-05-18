import os
from google.cloud import bigquery
import polars as pl       

# --- AUTH ------------------------------------------------------------
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bqgrid.json"

# --- QUERY -----------------------------------------------------------
SQL = """
SELECT
  TransactionID,
  AccountID,
  DeviceID,
  Channel,
  TransactionType,
  TransactionAmount,
  TransactionDuration,
  LoginAttempts,
  AccountBalance,
  CustomerAge,
  CustomerOccupation,
  is_fraud            -- target label
FROM `metal-arc-460019-p7.transaction_data.bank_transactions`
"""

# --- RUN -------------------------------------------------------------
print("Running BigQuery query …")
client = bigquery.Client()
pdf = client.query(SQL).to_dataframe()    # pandas DF
print(f"Rows pulled: {len(pdf):,}")

# --- SAVE ------------------------------------------------------------
pl_df = pl.from_pandas(pdf)
output_path = "data/features_raw.parquet"
pl_df.write_parquet(output_path)
print(f"Saved ➜ {output_path}")
