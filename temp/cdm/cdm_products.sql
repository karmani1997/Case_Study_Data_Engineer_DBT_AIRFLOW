
--select * from {{ref('products')}}
select * from {{source('raw_db','products')}}