import pandas as pd
import numpy as np

def simplified_data_cleaner(df):
    """
    Performs essential data cleaning on a pandas DataFrame in two main blocks.

    This function standardizes text data, removes duplicates, and handles missing
    values by dropping columns with too many missing values and imputing the rest.

    """
    df = df.copy()

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    print("Removed duplicate rows.")

    # Standardize text columns (if any)
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.lower().str.strip()
        print(f"Standardized text in column '{col}'.")
    


    # Drop columns with more than 50% missing values
    original_cols = df.shape[1]
    df.dropna(axis=1, thresh=len(df) * 0.5, inplace=True)
    print(f"Dropped {original_cols - df.shape[1]} columns due to high missing values.")

    # Impute remaining missing values
    for col in df.columns:
        if df[col].isnull().any():
            if df[col].dtype in ['int64', 'float64']:
                median_val = df[col].median()
                df[col].fillna(median_val, inplace=True)
                print(f"Imputed missing numeric values in '{col}' with the median.")
            else:
                df[col].fillna('Unknown', inplace=True)
                print(f"Imputed missing text values in '{col}' with 'Unknown'.")

    return df