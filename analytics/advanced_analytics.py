import pandas as pd

def get_top_run_scorers(df):
    return (
        df.groupby("batsman")
        .agg(total_runs=("batsman_runs", "sum"))
        .sort_values("total_runs", ascending=False)
        .reset_index()
    )

def get_top_wicket_takers(df):
    wickets = df[df["player_dismissed"].notna()]

    return (
        wickets.groupby("bowler")
        .size()
        .reset_index(name="total_wickets")
        .sort_values("total_wickets", ascending=False)
    )

def get_best_strike_rates(df):
    batting = (
        df.groupby("batsman")
        .agg(
            runs=("batsman_runs", "sum"),
            balls=("ball", "count")
        )
        .reset_index()
    )

    batting["strike_rate"] = (
        batting["runs"] / batting["balls"]
    ) * 100

    return batting.sort_values(
        "strike_rate",
        ascending=False
    )

def get_best_economy(df):
    bowling = (
        df.groupby("bowler")
        .agg(
            runs_conceded=("total_runs", "sum"),
            balls_bowled=("ball", "count")
        )
        .reset_index()
    )

    bowling["economy"] = (
        bowling["runs_conceded"] /
        (bowling["balls_bowled"] / 6)
    )

    return bowling.sort_values(
        "economy"
    )
