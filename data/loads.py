import os
import pandas as pd
from sqlalchemy import create_engine


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


csv_files = {
    os.path.join(BASE_DIR, "sales_data.csv"): "sales_data",
   
}  


db_user = "postgres"
db_password = "1234"
db_host = "localhost"
db_port = "5432"
db_name = "sales_db"


engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")


for file_path, table_name in csv_files.items():
    print(f"جارٍ استيراد {file_path} إلى جدول {table_name}...")
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    df.to_sql(table_name, engine, if_exists="replace", index=False)

print("✅ Done!") 
