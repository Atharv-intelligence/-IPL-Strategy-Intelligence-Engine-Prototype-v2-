import pandas as pd

from analytics.preprocessing import load_data
from feature_engineering import (
    create_phase_feature,
    create_wicket_feature
)


def create_matchup_stats(df):

    matchup_stats = (
        df.groupby(["batsman", "bowler"])
        .agg(
            runs_scored=("batsman_runs", "sum"),
            balls_faced=("ball", "count"),
            dismissals=("is_wicket", "sum")
        )
        .reset_index()
    )

    matchup_stats["strike_rate"] = (
        matchup_stats["runs_scored"]
        / matchup_stats["balls_faced"]
    ) * 100

    return matchup_stats


if __name__ == "__main__":

    file_path = "data/raw/deliveries (2).csv"

    data = load_data(file_path)

    data = create_phase_feature(data)

    data = create_wicket_feature(data)

    matchup_data = create_matchup_stats(data)

    print(matchup_data.head(20))

