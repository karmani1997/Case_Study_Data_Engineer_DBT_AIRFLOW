
--select * from {{ref('prices')}}
select * from {{source('raw_db','prices')}}