import pandas as pd

from preprocessing import load_data


def classify_phase(over):

    if over <= 6:
        return "Powerplay"

    elif over <= 15:
        return "Middle"

    else:
        return "Death"


def create_phase_feature(df):

    df["phase"] = df["over"].apply(classify_phase)

    return df


def create_wicket_feature(df):

    df["is_wicket"] = df["player_dismissed"].notna().astype(int)

    return df


if __name__ == "__main__":

    file_path = "data/raw/deliveries (2).csv"

    data = load_data(file_path)

    data = create_phase_feature(data)

    data = create_wicket_feature(data)

    print(
        data[
            [
                "over",
                "phase",
                "player_dismissed",
                "is_wicket"
            ]
        ].head(20)
    )
