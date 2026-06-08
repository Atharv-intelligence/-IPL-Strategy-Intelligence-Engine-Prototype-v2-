import streamlit as st

from analytics.preprocessing import load_data
from analytics.feature_engineering import (
    create_phase_feature,
    create_wicket_feature
)

from analytics.matchup_analysis import (
    create_matchup_stats
)

from analytics.matchup_scoring import (
    create_matchup_score
)

st.title("🧠 Recommendations")

data = load_data("data/raw/deliveries (2).csv")

data = create_phase_feature(data)
data = create_wicket_feature(data)

matchups = create_matchup_stats(data)
matchups = create_matchup_score(matchups)

st.subheader("⚠ Dangerous Matchups")

dangerous = matchups[
    matchups["matchup_type"] == "Dangerous"
]

st.dataframe(
    dangerous.head(20)
)

st.subheader("✅ Favorable Matchups")

favorable = matchups[
    matchups["matchup_type"] == "Favorable"
]

st.dataframe(
    favorable.head(20)
)
