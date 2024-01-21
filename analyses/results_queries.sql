--1- How did the average revenue (base price + consumption * energy price , Grundpreis +
--Verbrauch * Arbeitspreis) per contract develop between 01.10.2020 and 01.01.2021?
SELECT
    c."ID" AS contract_id,
    AVG(
        (CASE
            WHEN pr."PRICECOMPONENTID" = 1 THEN pr."PRICE"
            ELSE 0
        END)
        +
        (c."USAGE" * 
            CASE
                WHEN pr."PRICECOMPONENTID" = 2 THEN pr."PRICE" / 100
                ELSE 0
            END
        )
        
    ) AS average_revenue
FROM
    CUSTOMER_CONTRACTS_SNAPSHOT c
JOIN
    PRODUCTS_SNAPSHOT p ON c."PRODUCTID" = p."ID"
JOIN
    PRICES_SNAPSHOT pr ON p."ID" = pr."PRODUCTID"
WHERE
    DATE(c."STARTDATE") >= '2020-10-01'
    AND DATE(c."ENDDATE") <= '2021-01-01'
GROUP BY
    c."ID";






--2- How many contracts were on delivery on 01.01.2021?
select count(distinct "ID") as contracts_on_delivery
from raw.analytics.CUSTOMER_CONTRACTS_SNAPSHOT
where 
"STATUS" = 'indelivery'
and DATE("MODIFICATIONDATE") = '2021-01-01'

--- Zero

--- 3. How many new contracts were loaded into the DWH on 01.12.2020?
WITH ContractCounts AS (
    SELECT
        "ID",
        DBT_UPDATED_AT,
        DBT_VALID_FROM,
        DBT_VALID_TO,
        COUNT(*) OVER (PARTITION BY "ID") AS id_count
    FROM raw.analytics.CUSTOMER_CONTRACTS_SNAPSHOT
)
SELECT
    COUNT(*) AS new_contracts
FROM ContractCounts
WHERE
    DATE(DBT_UPDATED_AT) = '2020-12-01'
    AND DATE(DBT_VALID_FROM) = '2020-12-01'
    AND DBT_VALID_TO IS NULL
    AND id_count = 1;



--1720
