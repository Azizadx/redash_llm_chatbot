WITH dim_top10 AS (
SELECT Date, SUM(Views) AS TotalViews
FROM {{ source('youtube', 'raw_total') }}
GROUP BY Date
ORDER BY TotalViews DESC
LIMIT 10
)
SELECT * FROM dim_top10