 {{ config(materialized='table', alias='cdm_client_products', schema='analytics') }}
--select * from {{ref('PRODUCTS')}}
select * from {{source('raw_data','PRODUCTS')}}