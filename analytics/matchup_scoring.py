from matchup_analysis import create_matchup_stats
from preprocessing import load_data
from feature_engineering import (
    create_phase_feature,
    create_wicket_feature
)


def classify_matchup(row):

    if row["strike_rate"] < 100 and row["dismissals"] >= 1:
        return "Dangerous"

    elif row["strike_rate"] > 140 and row["dismissals"] == 0:
        return "Favorable"

    else:
        return "Balanced"


def create_matchup_score(df):

    df["matchup_type"] = df.apply(
        classify_matchup,
        axis=1
    )

    return df


if __name__ == "__main__":

    data = load_data(
        "data/raw/deliveries (2).csv"
    )

    data = create_phase_feature(data)

    data = create_wicket_feature(data)

    matchup_data = create_matchup_stats(data)

    matchup_data = create_matchup_score(
        matchup_data
    )

    print(
        matchup_data[
            [
                "batsman",
                "bowler",
                "strike_rate",
                "dismissals",
                "matchup_type"
            ]
        ].head(20)
    )
