{% snapshot contracts_snapshot %}

 {{
        config(
          target_schema='analytics',
          strategy='check',
          unique_key='\"ID\"',
          check_cols='all',
        )
    }}


select * from {{source('cdm_db','cdm_contracts')}}--{{ ref('contracts') }}

{% endsnapshot %}