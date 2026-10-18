import sys
from pathlib import Path

import streamlit as st

# Add project root to Python path when Streamlit runs this page directly.
ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from analytics.feature_engineering import create_phase_feature, create_wicket_feature
from analytics.matchup_analysis import create_matchup_stats
from analytics.matchup_scoring import create_matchup_score
from analytics.preprocessing import load_data
from recommendation_engine.recommendations import (
    get_favorable_matchups,
    get_top_recommendations,
)


st.title("🧠 Recommendations")

data = load_data("data/raw/deliveries (2).csv")
data = create_phase_feature(data)
data = create_wicket_feature(data)

matchups = create_matchup_score(create_matchup_stats(data))

st.subheader("⚠ Dangerous Matchups")
st.dataframe(get_top_recommendations(matchups))

st.subheader("✅ Favorable Matchups")
st.dataframe(get_favorable_matchups(matchups).head(20))
