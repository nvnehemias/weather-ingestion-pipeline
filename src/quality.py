import pandas as pd 

def validate_quality(df: pd.DataFrame):

    """
    
    Run data quality assertions before loading to warehouse.
    
    """

    assert not df.empty, "Data Quality Alert: DataFrame is empty"
    assert df["temp_celsius"].isnull().sum() == 0, "Data Quality Alert: Null values found in temp_celsius"
    assert (df["temp_celsius"] > -70).all() and (df["temp_celsius"] < 60).all(), "Data Quality Alert: Temperature out of physical bounds!"
    print(" :) All Data Quality checks passed successfully. ")