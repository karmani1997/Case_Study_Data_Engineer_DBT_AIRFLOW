--1- How did the average revenue (base price + consumption * energy price , Grundpreis +
--Verbrauch * Arbeitspreis) per contract develop between 01.10.2020 and 01.01.2021?
SELECT
    c."id" AS contract_id,
    AVG(
        (CASE
            WHEN pr."pricecomponentid" = 1 THEN pr."price"
            ELSE 0
        END)
        +
        (c."usage" * 
            CASE
                WHEN pr."pricecomponentid" = 2 THEN pr."price" / 100
                ELSE 0
            END
        )
        
    ) AS average_revenue
FROM
    contracts c
JOIN
    products p ON c."productid" = p."id"
JOIN
    prices pr ON p."id" = pr."productid"
WHERE
    DATE(c."startdate") >= '2020-10-01'
    AND DATE(c."enddate") <= '2021-01-01'
GROUP BY
    c."id";



--2- How many contracts were on delivery on 01.01.2021?
select count(distinct "id") as contracts_on_delivery
from raw.analytics.contracts_snapshot
where 
"status" = 'indelivery'
and DATE("modificationdate") = '2021-01-01'

--- 3. How many new contracts were loaded into the DWH on 01.12.2020?
WITH ContractCounts AS (
    SELECT
        "id",
        DBT_UPDATED_AT,
        DBT_VALID_FROM,
        DBT_VALID_TO,
        COUNT(*) OVER (PARTITION BY "id") AS id_count
    FROM raw.analytics.contracts_snapshot
)
SELECT
    COUNT(*) AS new_contracts
FROM ContractCounts
WHERE
    DATE(DBT_UPDATED_AT) = '2024-01-19'
    AND DATE(DBT_VALID_FROM) = '2024-01-19'
    AND DBT_VALID_TO IS NULL
    AND id_count = 1;

