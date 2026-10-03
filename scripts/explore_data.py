import pandas as pd

df = pd.read_csv("data/agridata_csv_202110311352.csv")

print("Shape (rows, columns):", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nFirst 5 rows:")
print(df.head())
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nUnique states:", df['State'].nunique() if 'State' in df.columns else "no 'State' column found")

print("\nRow(s) with missing data:")
print(df[df.isnull().any(axis=1)])

print("\nDate range:", df['date'].min(), "to", df['date'].max())
print("Unique commodities:", df['commodity_name'].nunique())
print("Unique states:", df['state'].nunique())
print("Unique markets:", df['market'].nunique())

# Drop the two corrupted/incomplete rows
df_clean = df.dropna()

# Properly parse dates - let pandas figure out mixed formats
df_clean['date_parsed'] = pd.to_datetime(df_clean['date'], format='mixed', errors='coerce')

# Check if any dates failed to parse
print("\nRows where date parsing failed:", df_clean['date_parsed'].isnull().sum())

# Now get the REAL date range
print("Actual date range:", df_clean['date_parsed'].min(), "to", df_clean['date_parsed'].max())

# Check for exact duplicate rows
print("\nExact duplicate rows:", df_clean.duplicated().sum())

print("\nFinal clean shape:", df_clean.shape)