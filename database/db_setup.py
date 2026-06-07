import sqlite3
import pandas as pd

# Load IPL dataset
df = pd.read_csv("data/raw/deliveries (2).csv")

# Create database connection
conn = sqlite3.connect("database/database.db")

# Store data in SQLite
df.to_sql(
    "deliveries",
    conn,
    if_exists="replace",
    index=False
)

print("✅ Database created successfully!")
print("✅ deliveries table loaded.")

conn.close()
