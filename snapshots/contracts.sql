{% snapshot contracts_snapshot %}

 {{
        config(
          target_schema='analytics',
          strategy='check',
          unique_key='\"id\"',
          check_cols='all',
        )
    }}


select * from {{ ref('contracts') }}

{% endsnapshot %}