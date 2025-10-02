# scripts/transform.py
import pandas as pd

def transform_data(df: pd.DataFrame):
    """Clean and transform sales data"""
    df = df.dropna()
    df["total_price"] = df["quantity"] * df["unit_price"]
    print("✅ Data transformed successfully")
    return df

if __name__ == "__main__":
    sample_df = pd.read_csv("../data/sales_data.csv")
    transformed = transform_data(sample_df)
    print(transformed.head())
