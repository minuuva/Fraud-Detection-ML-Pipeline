import polars as pl
import duckdb

# ------------- Load raw -----------------
raw = pl.read_parquet("data/features_raw.parquet")

# ------------- Row-level features -------
fe = (
    raw
    .with_columns([
        (pl.col("Channel") == "Online").cast(pl.Int8).alias("is_online"),
        (pl.col("TransactionType") == "Debit").cast(pl.Int8).alias("is_debit"),
        (pl.col("LoginAttempts") > 3).cast(pl.Int8).alias("many_login_attempts"),
        (pl.col("TransactionAmount") / (pl.col("AccountBalance") + 1)).alias("amount_ratio")
    ])
)

# ------------- Account aggregates (DuckDB) ------------
con = duckdb.connect()
con.register("fe", fe.to_pandas())

acct_sql = """
SELECT
  AccountID,
  COUNT(*)                AS acct_txn_cnt,
  SUM(is_fraud)           AS acct_fraud_cnt,
  AVG(TransactionAmount)  AS acct_avg_amt
FROM fe
GROUP BY AccountID
"""
acct = pl.from_pandas(con.execute(acct_sql).fetchdf())

# join back
fe = fe.join(acct, on="AccountID", how="left")

# ------------- Save engineered dataset ---------------
fe.write_parquet("data/features_eng.parquet")
print("Saved ➜ data/features_eng.parquet   rows:", fe.shape[0])
