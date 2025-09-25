import streamlit as st
import pandas as pd
import json

st.title("📊 Classroom Usage Stats")

if st.session_state.get("role") != "Coordinator":
    st.warning("Access denied. Coordinators only.")
    st.stop()

try:
    with open("usage/usage_log.json") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    st.dataframe(df)

    st.markdown("### 🔝 Most Queried Locations")
    st.bar_chart(df["location"].value_counts())

    st.markdown("### ⏰ Usage Over Time")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    st.line_chart(df["hour"].value_counts().sort_index())

except FileNotFoundError:
    st.info("No usage data yet.")
