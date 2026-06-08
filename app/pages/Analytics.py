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

# Top Run Scorers

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

# Top Wicket Takers

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

# Strike Rates

st.header("⚡ Best Strike Rates")

sr_df = get_best_strike_rates(data).head(10)

st.dataframe(sr_df)

# Economy

st.header("🧤 Best Economy Bowlers")

eco_df = get_best_economy(data).head(10)

st.dataframe(eco_df)
