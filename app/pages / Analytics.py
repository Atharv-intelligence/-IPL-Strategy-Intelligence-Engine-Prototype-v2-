import streamlit as st
import plotly.express as px

from analytics.preprocessing import load_data
from analytics.advanced_analytics import (
    get_top_run_scorers,
    get_top_wicket_takers,
    get_best_strike_rates,
    get_best_economy
)

st.title("📈 Advanced Cricket Analytics")

data = load_data("data/raw/deliveries (2).csv")

# -----------------------
# Top Run Scorers
# -----------------------

st.header("🏏 Top Run Scorers")

runs_df = get_top_run_scorers(data).head(10)

fig_runs = px.bar(
    runs_df,
    x="batsman",
    y="total_runs",
    title="Top 10 Run Scorers"
)

st.plotly_chart(fig_runs, use_container_width=True)

st.dataframe(runs_df)

# -----------------------
# Top Wicket Takers
# -----------------------

st.header("🎯 Top Wicket Takers")

wickets_df = get_top_wicket_takers(data).head(10)

fig_wickets = px.bar(
    wickets_df,
    x="bowler",
    y="total_wickets",
    title="Top 10 Wicket Takers"
)

st.plotly_chart(fig_wickets, use_container_width=True)

st.dataframe(wickets_df)

# -----------------------
# Strike Rate Analysis
# -----------------------

st.header("⚡ Strike Rate Analysis")

sr_df = get_best_strike_rates(data)

sr_df = sr_df[sr_df["balls"] >= 100]

sr_df = sr_df.head(10)

fig_sr = px.bar(
    sr_df,
    x="batsman",
    y="strike_rate",
    title="Best Strike Rates"
)

st.plotly_chart(fig_sr, use_container_width=True)

st.dataframe(sr_df)

# -----------------------
# Economy Analysis
# -----------------------

st.header("🧤 Economy Analysis")

eco_df = get_best_economy(data)

eco_df = eco_df[eco_df["balls_bowled"] >= 120]

eco_df = eco_df.head(10)

fig_eco = px.bar(
    eco_df,
    x="bowler",
    y="economy",
    title="Best Economy Bowlers"
)

st.plotly_chart(fig_eco, use_container_width=True)

st.dataframe(eco_df)

# -----------------------
# Player Search
# -----------------------

st.header("🔍 Player Search")

players = sorted(
    data["batsman"].dropna().unique()
)

selected_player = st.selectbox(
    "Select Batter",
    players
)

player_stats = (
    data[data["batsman"] == selected_player]
    .groupby("batsman")
    .agg(
        runs=("batsman_runs", "sum"),
        balls=("ball", "count")
    )
)

st.dataframe(player_stats)
