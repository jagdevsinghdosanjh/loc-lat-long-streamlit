import streamlit as st
import pandas as pd
import os

file_path = "exports/results.csv"

st.title("📊 Export History")

# Check if file exists and is not empty
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    try:
        df = pd.read_csv(file_path)
        if df.empty or df.columns.size == 0:
            st.warning("The export file exists but contains no data.")
        else:
            st.dataframe(df)
            st.success("Export history loaded successfully.")
    except pd.errors.EmptyDataError:
        st.error("The export file is empty or unreadable.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
else:
    st.info("No export history found yet. Run a batch lookup to generate results.")
