
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
