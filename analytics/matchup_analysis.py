from analytics.preprocessing import load_data
from analytics.feature_engineering import (
    create_phase_feature,
    create_wicket_feature,
)


def create_matchup_stats(df):
    matchup_stats = (
        df.groupby(["batsman", "bowler"])
        .agg(
            runs_scored=("batsman_runs", "sum"),
            balls_faced=("ball", "count"),
            dismissals=("is_wicket", "sum"),
        )
        .reset_index()
    )

    matchup_stats["strike_rate"] = (
        matchup_stats["runs_scored"] / matchup_stats["balls_faced"]
    ) * 100

    return matchup_stats


if __name__ == "__main__":
    data = load_data("data/raw/deliveries (2).csv")
    data = create_phase_feature(data)
    data = create_wicket_feature(data)
    print(create_matchup_stats(data).head(20))
