# 🛡️ Fraud-Detection-ML-Pipeline

## Overview  
Fraud-Detection-ML-Pipeline is an end-to-end machine learning pipeline for detecting fraudulent transactions using a synthetic banking dataset.

The pipeline:
- 📥 Pulls transactional data directly from BigQuery
- 🧪 Engineers both row-level and account-level features with Polars and DuckDB
- 🤖 Trains a highly-performant XGBoost classifier
- 📈 Evaluates the model using AUPRC with impressive results

✅ **Achieved AUPRC: 0.917** — meaning the model is highly effective at identifying fraud in an imbalanced dataset. A random classifier would have ~0.01 AUPRC due to only 1% fraud.

---

## ✨ Features

- 🧹 Data extraction from BigQuery to Parquet using `pull_bigquery.py`
- 🏗️ Feature engineering with Polars + DuckDB in `build_features.py`
- 🔢 One-hot encoding of categorical columns using `ColumnTransformer`
- ⚖️ Class imbalance handling via `scale_pos_weight`
- 🤖 XGBoost model training and pipeline encapsulation
- 📊 AUPRC scoring to reflect fraud detection accuracy
- 💾 Saved model as `models/fraud_xgb.json`
- 📁 Organized, GitHub-ready project structure with reproducible SQL EDA

---

## 📂 Project Structure
fraud-detection-ml-pipeline/
├── data/
│ ├── features_raw.parquet
│ ├── features_eng.parquet
│ └── bank_transactions.csv
├── models/
│ └── fraud_xgb.json
├── notebooks/
│ └── 01_train_xgb.ipynb
├── sql/
│ └── [saved EDA queries].sql
├── src/
│ └── data/
│ ├── build_features.py
│ └── pull_bigquery.py
├── bqgrid.json # (credentials excluded from repo)
├── requirements.txt
└── README.md

---

## 🛠 Tech Stack

- **BigQuery** – data warehousing
- **DuckDB** – fast SQL-style feature engineering
- **Polars** – fast dataframe transformations
- **Parquet** – columnar data storage
- **XGBoost** – robust gradient boosting model
- **scikit-learn** – pipeline, train/test split, evaluation
- **Jupyter Notebook** – training + evaluation visualization

---

## 📈 Evaluation Metric: AUPRC

AUPRC (Area Under the Precision-Recall Curve) is ideal for highly imbalanced datasets like fraud detection.

- A perfect model has **AUPRC = 1.0**
- A random model has **AUPRC ≈ 0.01** (because only ~1% are fraud)

> 🎯 This model scored **0.917** — indicating high precision and recall even on rare fraud cases!

---

## 🚀 How to Run

1. Set up your environment:
    ```bash
    pip install -r requirements.txt
    ```

2. Pull data from BigQuery:
    ```bash
    python src/data/pull_bigquery.py
    ```

3. Build features:
    ```bash
    python src/data/build_features.py
    ```

4. Train model inside Jupyter:
    ```bash
    jupyter notebook notebooks/01_train_xgb.ipynb
    ```

---

## 🔒 Notes

- `bqgrid.json` (credentials) is excluded for security reasons.
- The dataset is fully synthetic.

---

## 🤝 Contributing

Pull requests and suggestions are welcome!
