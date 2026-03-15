import streamlit as st
import pandas as pd

st.title("📧 Email Group Conversation Dashboard")

st.write("Summary of email threads")

# Load summarized data
df = pd.read_csv("thread_summary.csv")

# Show table
st.dataframe(df)

# Filter by owner
owners = df["Owner"].unique()
selected_owner = st.selectbox("Filter by Owner", owners)

filtered_df = df[df["Owner"] == selected_owner]

st.subheader("Filtered Threads")
st.dataframe(filtered_df)

# Show statistics
st.subheader("Thread Statistics")

st.write("Total Threads:", len(df))

topic_counts = df["Key Topic"].value_counts()

st.bar_chart(topic_counts)