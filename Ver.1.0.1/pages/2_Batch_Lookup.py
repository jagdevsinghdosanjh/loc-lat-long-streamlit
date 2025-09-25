import streamlit as st
import pandas as pd
from utils.geocode import get_lat_long
from utils.export import save_export

st.title("📄 Batch Location Lookup")
uploaded_file = st.file_uploader("Upload CSV with 'location' column", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    results = []
    for loc in df["location"]:
        result = get_lat_long(loc)
        results.append({
            "location": loc,
            "latitude": result["lat"] if result else None,
            "longitude": result["lon"] if result else None
        })
    result_df = pd.DataFrame(results)
    st.dataframe(result_df)
    st.map(result_df.dropna(subset=["latitude", "longitude"]).rename(columns={"latitude": "lat", "longitude": "lon"}))
    save_export(result_df)
    st.download_button("📥 Download CSV", result_df.to_csv(index=False), "results.csv", "text/csv")
