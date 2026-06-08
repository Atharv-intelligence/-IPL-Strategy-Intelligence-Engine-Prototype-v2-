import streamlit as st
import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

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
