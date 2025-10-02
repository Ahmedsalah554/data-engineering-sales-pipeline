# scripts/extract.py
import pandas as pd

def extract_data(file_path: str):
    """Read sales data from CSV file"""
    df = pd.read_csv(file_path)
    print("✅ Data extracted successfully")
    return df

if __name__ == "__main__":
    df = extract_data("../data/sales_data.csv")
    print(df.head())
