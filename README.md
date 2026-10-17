# IPL Strategy Intelligence Engine — Prototype V2

A Python and Streamlit prototype for exploring IPL ball-by-ball data through analytics, historical batter–bowler matchups, and offline model experiments.

> **Project status:** work in progress. This repository is a learning/prototype project; its recommendation rules and model scripts should not be treated as live-match decision systems.

## What is included

- Streamlit pages for top run scorers, wicket takers, strike rates, economy figures, and matchup tables
- Feature engineering for match phase and wicket flags
- Historical batter–bowler matchup summaries, classified with rule-based labels
- Offline Random Forest scripts for per-delivery run and wicket experiments
- SQLite setup script for loading the delivery data into a local database

## Repository structure

```text
analytics/               Data loading, features, analytics, and matchup logic
app/                     Streamlit home page and application pages
data/raw/                IPL delivery-level source data
database/                SQLite setup and query helpers
models/                  Offline training/evaluation scripts
recommendation_engine/   Recommendation module
visualizations/          Chart helper module
```

## Run locally

1. Create and activate a virtual environment.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the app from the repository root:

   ```bash
   streamlit run app/Home.py
   ```

The application reads `data/raw/deliveries (2).csv`; keep that file in place.

## Notes on the modelling scripts

The scripts in `models/` train and evaluate models when they are run. They are not wired to an interactive prediction form in the Streamlit interface, and this repository does not currently publish validated production metrics.

## Technologies

Python, pandas, NumPy, scikit-learn, Streamlit, Plotly, Matplotlib, SQLite, and joblib.

## Next improvements

- Remove generated local environment files from version control
- Add tests and documented, reproducible model evaluation
- Resolve module import paths and connect model outputs to the interface
- Document the dataset version, assumptions, and limitations
