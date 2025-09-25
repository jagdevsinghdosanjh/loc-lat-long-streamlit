import streamlit as st
import pandas as pd
import os

st.title("📤 Export History")
file_path = "exports/results.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.dataframe(df)
else:
    st.info("No export history found.")
