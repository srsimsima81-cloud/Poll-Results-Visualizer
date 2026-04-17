import streamlit as st
from src.data_generator import generate_poll_data
from src.analysis import analyze_data
from src.visualization import create_visuals
import pandas as pd

st.set_page_config(page_title="Poll Results Visualizer", layout="wide")

st.title("📊 Poll Results Visualizer Dashboard")

# Generate / Load data
df = generate_poll_data()

st.subheader("📁 Dataset Preview")
st.dataframe(df.head())

# Analysis
vote_counts, vote_percent, region_analysis, age_analysis = analyze_data(df)

# Charts
st.subheader("📊 Vote Distribution")

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(vote_counts)

with col2:
    st.write(vote_percent)

st.subheader("🌍 Region-wise Analysis")
st.bar_chart(region_analysis)

st.subheader("👥 Age-wise Analysis")
st.bar_chart(age_analysis)

# Optional: generate saved images
create_visuals(vote_counts, region_analysis, age_analysis)

st.success("Charts generated successfully!")