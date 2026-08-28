import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\Keshav\vs code folder\data-analytic-projects\netflix-python-project\output\cleaned_data.csv")

# How many Movies vs TV Shows are there?
print(df.groupby("type")["type"].count())

# What is the top 10 countries producing content?
df["country"] = df["country"].str.split(",")
df = df.explode("country")
df["country"] = df["country"].str.strip()
print(df.groupby("country")["show_id"].count().sort_values(ascending=False).head(10))

# Which rating category is most common?
print(df["rating"].value_counts())

df["rating"] = df["rating"].replace(["66 min", "74 min", "84 min"], "Not Rated")
print(df["rating"].value_counts())

# What are the top 10 genres?
df["listed_in"] = df["listed_in"].str.split(",")
df = df.explode("listed_in")
df["listed_in"] = df["listed_in"].str.strip()
print(df.groupby("listed_in")["show_id"].count().sort_values(ascending=False).head(10))

# 🟡 STEP 2 — FEATURE ENGINEERING
# Q5:

# 👉 Extract:

# Year added
# Month added
# Day name
df["date_added"] = pd.to_datetime(df["date_added"])
df["year"] = df["date_added"].dt.year
df["month"] = df["date_added"].dt.month_name()
df["day"] = df["date_added"].dt.day_name()

print(df.info())
print(df[["date_added", "year", "month", "day"]].head(10))
# Q6:

# 👉 Which month has highest content addition?

print(df.groupby("month")["show_id"].count().sort_values(ascending=False).head(1))

# Q7:

# 👉 Which year had highest growth?

yearly = df.groupby("year")["show_id"].count().sort_index()
growth = yearly.diff()
print("Highest growth year:")
print(growth.sort_values(ascending=False).head(1))

# 🔵 STEP 3 — TIME ANALYSIS
# Q8:

# 👉 Weekday vs Weekend

# Which has more releases?

df["day_type"] = df["day"].apply(
lambda x: "Weekend" if x in ["Saturday", "Sunday"] else "Weekday")

print(df.groupby("day_type")["show_id"].count())
# Q9:

# 👉 Which day of week is most active?
print(df["day"].value_counts().sort_values(ascending=False).head(1))

# Q10:

# 👉 Create running total of content added over years

yearly = df.groupby("year")["show_id"].count().sort_index()
running_total = yearly.cumsum()
print("Running Total of Content:")
print(running_total)

# 🔥 STEP 4 — CONTENT ANALYSIS
# Q11:

# 👉 Which country produces most movies vs TV shows?

df["country"] = df["country"].str.split(",")
df = df.explode("country")
df["country"] = df["country"].str.strip()
result = df.groupby(["country", "type"])["show_id"].count().unstack()
print(result.sort_values(by = "Movie",ascending=False).head(1))

# 👉 Which genre is most popular in movies vs TV shows?

df["listed_in"] = df["listed_in"].str.split(",")
df = df.explode("listed_in")
df["listed_in"] = df["listed_in"].str.strip()
result = df.groupby(["listed_in", "type"])["show_id"].count().unstack()
print(result.sort_values(by = "TV Show",ascending=False).head(1))

# Q13:

# 👉 Average duration of movies
avg = df.groupby("type")["value"].mean()
print(f"{avg.head(1).round(2)}")


