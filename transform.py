import pandas as pd
from source.py import df

def clean_and_transform_data(df):
    """
    Cleans and transforms a pandas DataFrame by handling missing values, 
    removing duplicates, converting a date column, and adding a new calculated column.

    """
    # Clean missing values by replacing NaN with "Unknown"
    df = df.fillna("Unknown")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert a column to datetime objects
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    
    # Add a calculated column for total sales
    df['total_sale'] = df['quantity'] * df['price']
    
    return df