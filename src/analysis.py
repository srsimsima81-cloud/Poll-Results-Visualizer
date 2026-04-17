import pandas as pd

import os

os.makedirs("outputs", exist_ok=True)

def analyze_data(df):

    vote_counts = df["Choice"].value_counts()
    vote_percent = (vote_counts / len(df)) * 100

    region_analysis = pd.crosstab(df["Region"], df["Choice"])
    age_analysis = pd.crosstab(df["Age_Group"], df["Choice"])

    # ---------------- SUMMARY TEXT ----------------
    summary = f"""
POLL RESULTS SUMMARY
----------------------------

Total Responses: {len(df)}

Vote Counts:
{vote_counts.to_string()}

Vote Percentage:
{vote_percent.round(2).to_string()}

Most Popular Option: {vote_counts.idxmax()}
Least Popular Option: {vote_counts.idxmin()}

Insights:
- Majority voted for {vote_counts.idxmax()}
- Distribution is {'balanced' if vote_counts.std() < 10 else 'uneven'}
"""

    with open("outputs/summary.txt", "w") as f:
        f.write(summary)

    return vote_counts, vote_percent, region_analysis, age_analysis
