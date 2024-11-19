from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Export both dimension tables (_dim) and the fact table to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.
    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    
    # Path to the configuration file
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Define the dimension tables (_dim) mapping
    table_map = {
        'datetime_id': 'datetime_dim',
        'passenger_count_id': 'passenger_count_dim',
        'trip_distance_id': 'trip_distance_dim',
        'pickup_location_id': 'pickup_location_dim',
        'drop_location_id': 'drop_location_dim',
        'rate_code_id': 'rate_code_dim',
        'payment_type_id': 'payment_type_dim',
    }

    # Export the dimension tables
    for key, table_name in table_map.items():
        if key in data:
            # Generate the table ID dynamically
            table_id = f'uber-project-438005.uber_data_103.{table_name}'

            # Export the dimension table data to BigQuery
            BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
                DataFrame(data[key]),  # Convert the data to a DataFrame
                table_id,  # Use the dynamic table ID for dimensions
                if_exists='replace',  # Specify resolution policy if table name already exists
            )
    
    # Export the fact table
    if 'fact_table' in data:
        fact_table_id = 'uber-project-438005.uber_data_103.fact_table'
        
        # Export the fact table data to BigQuery
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(data['fact_table']),  # Convert fact table data to a DataFrame
            fact_table_id,  # Use the table ID for the fact table
            if_exists='replace',  # Specify resolution policy if table name already exists
        )
