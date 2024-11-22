import pandas as pd

def load_data(file_path):
    """Load dataset from a CSV file."""
    df_amazon = pd.read_csv('/home/francis/Projects/amazon_data_analysis/data/amazon.csv')
    return df_amazon

def clean_data(df):
    """Clean dataset by handling missing values."""
    df.dropna(inplace=True)
    return df
