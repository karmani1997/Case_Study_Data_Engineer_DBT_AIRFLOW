
--select * from {{ref('contracts')}}--{{source('source','contracts')}}
select * from {{source('raw_data','CONTRACTS')}}
