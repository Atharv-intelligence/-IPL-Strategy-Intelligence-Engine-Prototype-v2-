import pandas as pd


def load_data(filepath):
    """
    Load IPL deliveries dataset.
    """

    df = pd.read_csv(filepath)

    return df


def basic_info(df):
    """
    Display basic dataset information.
    """

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)


if __name__ == "__main__":

    file_path = "data/raw/deliveries (2).csv"

    data = load_data(file_path)

    basic_info(data)
