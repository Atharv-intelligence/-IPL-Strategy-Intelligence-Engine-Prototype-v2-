import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def basic_info(df):
    print(df.head())
    print(df.shape)
    print(df.columns)
