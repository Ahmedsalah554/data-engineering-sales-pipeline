# scripts/load.py
import pandas as pd
from sqlalchemy import create_engine

def load_data(df: pd.DataFrame, user="postgres", password="password", host="localhost", port=5432, db="sales_db"):
    """Load data into PostgreSQL sales table"""
    
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")

    df.to_sql("sales", con=engine, if_exists="append", index=False)

    print("✅ Data loaded into PostgreSQL successfully")

if __name__ == "__main__":
    df = pd.read_csv("../data/sales_data.csv")
    from transform import transform_data
    df_transformed = transform_data(df)

    load_data(df_transformed, user="postgres", password="1234", host="localhost", port=5432, db="sales_db")
