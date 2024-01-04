WITH dim_view_7days AS (
SELECT Date, AVG(Views) OVER (ORDER BY Date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS RollingAverageViews
FROM {{ source('youtube', 'raw_total') }}
ORDER BY Date
)

SELECT * FROM dim_view_7days