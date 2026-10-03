import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST", "localhost")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://postgres:{db_password}@{db_host}:5432/{db_name}")

sql_files = [
    "sql/transform_mandi_prices.sql",
    "sql/transform_district_spread.sql",
]

with engine.begin() as conn:
    for file_path in sql_files:
        print(f"Running {file_path}...")
        with open(file_path, "r") as f:
            sql_content = f.read()
        conn.execute(text(sql_content))
        print(f"  Done.")

print("All transformations applied successfully.")