import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

def create_visuals(vote_counts, region_analysis, age_analysis):

    # ---------------- BAR CHART ----------------
    plt.figure(figsize=(6,4))
    vote_counts.plot(kind='bar')
    plt.title("Poll Results - Count")
    plt.tight_layout()
    plt.savefig("images/bar_chart.png", dpi=150)
    plt.close()

    # ---------------- PIE CHART ----------------
    plt.figure(figsize=(6,6))
    vote_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Poll Share")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("images/pie_chart.png", dpi=150)
    plt.close()

    # ---------------- REGION CHART ----------------
    plt.figure(figsize=(7,5))
    region_analysis.plot(kind='bar', stacked=True)
    plt.title("Region-wise Analysis")
    plt.tight_layout()
    plt.savefig("images/region_chart.png", dpi=150)
    plt.close()

    # ---------------- AGE CHART ----------------
    plt.figure(figsize=(7,5))
    age_analysis.plot(kind='bar', stacked=True)
    plt.title("Age-wise Analysis")
    plt.tight_layout()
    plt.savefig("images/age_chart.png", dpi=150)
    plt.close()