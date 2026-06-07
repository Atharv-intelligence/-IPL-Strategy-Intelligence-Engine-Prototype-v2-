import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from analytics.preprocessing import load_data
from analytics.feature_engineering import (
    create_phase_feature,
    create_wicket_feature
)


# Load data
data = load_data("data/raw/deliveries (2).csv")

# Feature engineering
data = create_phase_feature(data)
data = create_wicket_feature(data)

# Select features
features = [
    "over",
    "phase",
    "batsman",
    "bowler"
]

df = data[features + ["is_wicket"]].copy()

# Encode categorical variables
encoders = {}

for col in ["phase", "batsman", "bowler"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# X and y
X = df[features]
y = df["is_wicket"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\n🏏 WICKET PREDICTION MODEL")
print(f"Accuracy: {accuracy:.4f}")
