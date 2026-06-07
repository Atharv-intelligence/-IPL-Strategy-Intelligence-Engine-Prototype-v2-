
import pandas as pd

from preprocessing import load_data


def get_top_run_scorers(df):

    top_runs = (
        df.groupby("batsman")
        .agg(total_runs=("batsman_runs", "sum"))
        .sort_values("total_runs", ascending=False)
        .reset_index()
    )

    return top_runs


def get_top_wicket_takers(df):

    wickets = (
        df[df["player_dismissed"].notna()]
        .groupby("bowler")
        .agg(total_wickets=("player_dismissed", "count"))
        .sort_values("total_wickets", ascending=False)
        .reset_index()
    )

    return wickets


def get_best_strike_rates(df):

    strike_rates = (
        df.groupby("batsman")
        .agg(
            runs=("batsman_runs", "sum"),
            balls=("ball", "count")
        )
    )

    strike_rates["strike_rate"] = (
        strike_rates["runs"]
        / strike_rates["balls"]
    ) * 100

    strike_rates = (
        strike_rates.sort_values(
            "strike_rate",
            ascending=False
        )
        .reset_index()
    )

    return strike_rates


def get_best_economy(df):

    economy = (
        df.groupby("bowler")
        .agg(
            runs_conceded=("total_runs", "sum"),
            balls_bowled=("ball", "count")
        )
    )

    economy["overs"] = (
        economy["balls_bowled"] / 6
    )

    economy["economy"] = (
        economy["runs_conceded"]
        / economy["overs"]
    )

    economy = (
        economy.sort_values(
            "economy",
            ascending=True
        )
        .reset_index()
    )

    return economy


if __name__ == "__main__":

    data = load_data(
        "data/raw/deliveries (2).csv"
    )

    print("\nTOP RUN SCORERS")
    print(
        get_top_run_scorers(data)
        .head(10)
    )

    print("\nTOP WICKET TAKERS")
    print(
        get_top_wicket_takers(data)
        .head(10)
    )

    print("\nBEST STRIKE RATES")
    print(
        get_best_strike_rates(data)
        .head(10)
    )

    print("\nBEST ECONOMY BOWLERS")
    print(
        get_best_economy(data)
        .head(10)
    )
