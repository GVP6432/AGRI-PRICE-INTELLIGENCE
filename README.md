# Agri Commodity Price Intelligence

Automated data pipeline analyzing wholesale mandi (market) prices across India,
sourced from a government Agmarknet dataset (2019-2021, 836K+ records).

## What it does
- Cleans and standardizes raw mandi price data (mixed date formats, duplicate
  records, invalid zero-price entries)
- Loads into PostgreSQL
- Builds SQL views to surface:
  - Monthly commodity price volatility by district
  - Inter-district price spread per commodity per week

## Key finding
Arecanut (Betelnut/Supari) showed the highest price volatility and inter-district
spread of any commodity in the dataset, with prices ranging from ₹2,600 to
₹66,000 across districts in a single week.

## Stack
Python (pandas, SQLAlchemy) · PostgreSQL · Power BI

## CI/CD
Automated pipeline validation via GitHub Actions — every push spins up a fresh
PostgreSQL instance, installs dependencies, and runs the full load/clean/transform
pipeline end-to-end. [See workflow runs](https://github.com/GVP6432/AGRI-PRICE-INTELLIGENCE/actions)

## How to run
1. `pip install -r requirements.txt`
2. Set up `.env` with your DB credentials (see `.env.example`)
3. `python scripts/load_data.py`
4. Run SQL scripts in `sql/` against your database
5. Open `dashboards/agri_price_dashboard.pbix` in Power BI