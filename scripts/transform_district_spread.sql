DROP VIEW IF EXISTS vw_district_price_spread;

CREATE VIEW vw_district_price_spread AS
SELECT
    commodity_name,
    DATE_TRUNC('week', price_date) AS price_week,
    MAX(modal_price) - MIN(modal_price) AS price_spread,
    MAX(modal_price) AS highest_price,
    MIN(modal_price) AS lowest_price,
    COUNT(DISTINCT district) AS districts_compared
FROM stg_mandi_prices
WHERE modal_price > 0
GROUP BY commodity_name, DATE_TRUNC('week', price_date)
HAVING COUNT(DISTINCT district) >= 5
ORDER BY price_spread DESC;