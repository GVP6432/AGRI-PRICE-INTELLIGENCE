DROP VIEW IF EXISTS vw_commodity_weekly_volatility;

CREATE VIEW vw_commodity_weekly_volatility AS
SELECT
    commodity_name,
    state,
    district,
    DATE_TRUNC('month', price_date) AS price_month,
    MIN(modal_price) AS min_modal_price,
    MAX(modal_price) AS max_modal_price,
    AVG(modal_price) AS avg_modal_price,
    STDDEV(modal_price) AS price_volatility,
    COUNT(*) AS num_records
FROM stg_mandi_prices
GROUP BY commodity_name, state, district, DATE_TRUNC('month', price_date)
HAVING COUNT(*) >= 5;