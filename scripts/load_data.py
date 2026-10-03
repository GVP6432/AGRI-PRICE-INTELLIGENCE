import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

# --- Extract ---
df = pd.read_csv("data/agridata_csv_202110311352.csv")
print(f"Raw rows: {len(df)}")

# --- Clean ---
df = df.dropna()

df['price_date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce')
df = df.drop(columns=['date'])

for col in ['commodity_name', 'state', 'district', 'market']:
    df[col] = df[col].astype(str).str.strip().str.title()

before = len(df)
df = df.drop_duplicates()
print(f"Dropped {before - len(df)} exact duplicate rows")

print(f"Final clean rows: {len(df)}")
print(f"Date range: {df['price_date'].min()} to {df['price_date'].max()}")

# --- Load into Postgres staging table ---
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://postgres:{db_password}@localhost:5432/{db_name}")

df.to_sql("stg_mandi_prices", engine, if_exists="replace", index=False)
print("Loaded into stg_mandi_prices successfully.")