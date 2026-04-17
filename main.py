from src.data_generator import generate_poll_data
from src.analysis import analyze_data
from src.visualization import create_visuals
import os

os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
os.makedirs("images", exist_ok=True)

# Step 1: Generate data
df = generate_poll_data()

# Step 2: Analysis + summary file
vote_counts, vote_percent, region_analysis, age_analysis = analyze_data(df)

print("\nVote Counts:\n", vote_counts)
print("\nVote %:\n", vote_percent)

# Step 3: Create images
create_visuals(vote_counts, region_analysis, age_analysis)

print("\n✅ Images saved in 'images/'")
print("📄 Summary saved in 'outputs/summary.txt'")