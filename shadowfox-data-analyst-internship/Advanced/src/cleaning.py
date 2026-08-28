import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("netflix-python-project/data/netflix_titles.csv")

# Initial inspection
print(df.head())
print(df.info())
print(df.describe().round())

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Check missing values
print(df.isnull().sum())

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Fill missing dates using median
df["date_added"] = df["date_added"].fillna(df["date_added"].median())

print(df.info())

# Handle missing categorical values
df["director"] = df["director"].fillna("Not available")
df["cast"] = df["cast"].fillna("Not available")
df["country"] = df["country"].fillna("Not available")

# Check again after filling
print(df.isnull().sum())

# Handle duration column
df["duration"] = df["duration"].fillna("Not available")

# Split duration into value and type
df[["value", "time"]] = df["duration"].str.split(" ", expand=True)

# Convert value to numeric
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Fill missing numeric values using median
df["value"] = df["value"].fillna(df["value"].median())

# Drop original duration column
df.drop("duration", axis=1, inplace=True)

print(df.info())

# Handle missing ratings
df["rating"] = df["rating"].fillna("Not Rated")

# Final missing check
print(df.isnull().sum())

# Remove duplicate records
df.drop_duplicates(subset="show_id", keep="first", inplace=True)

print(df.info())

# Final validation
print(df.isnull().sum())
print(df.duplicated(subset="show_id").sum())

# Save clean data set
df.to_csv("netflix-python-project/output/cleaned_data.csv", index=False)