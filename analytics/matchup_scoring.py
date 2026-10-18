from analytics.feature_engineering import (
    create_phase_feature,
    create_wicket_feature,
)
from analytics.matchup_analysis import create_matchup_stats
from analytics.preprocessing import load_data


def classify_matchup(row):
    if row["strike_rate"] < 100 and row["dismissals"] >= 1:
        return "Dangerous"
    if row["strike_rate"] > 140 and row["dismissals"] == 0:
        return "Favorable"
    return "Balanced"


def create_matchup_score(df):
    result = df.copy()
    result["matchup_type"] = result.apply(classify_matchup, axis=1)
    return result


if __name__ == "__main__":
    data = load_data("data/raw/deliveries (2).csv")
    data = create_phase_feature(data)
    data = create_wicket_feature(data)
    matchup_data = create_matchup_score(create_matchup_stats(data))
    print(
        matchup_data[
            ["batsman", "bowler", "strike_rate", "dismissals", "matchup_type"]
        ].head(20)
    )
