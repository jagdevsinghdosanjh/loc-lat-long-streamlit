import streamlit as st
import pandas as pd
from utils.geocode import get_lat_long
from utils.export import save_export, export_to_excel

enable_export = False  # Default value; will be updated later based on user role

st.title("📄 Batch Location Lookup")
uploaded_file = st.file_uploader("Upload CSV with 'location' and 'state' columns", type=["csv"])

# Role-based toggles
if st.session_state.get("role") == "Coordinator":
    show_map = st.sidebar.checkbox("Show Map Overlay", value=True)
    enable_export = st.sidebar.checkbox("Enable Excel Export", value=True)
else:
    show_map = True
    enable_export = False

# Process uploaded file
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip().str.lower()

    # Validate required columns
    if "location" not in df.columns or "state" not in df.columns:
        st.error("CSV must contain both 'location' and 'state' columns.")
        st.stop()

    # Flag missing or duplicate entries
    invalid_rows = df[df["location"].isna() | df["state"].isna()]
    duplicate_rows = df[df.duplicated(subset=["location", "state"], keep=False)]

    if not invalid_rows.empty:
        st.warning(f"⚠️ {len(invalid_rows)} row(s) have missing location or state.")
        st.dataframe(invalid_rows)

    if not duplicate_rows.empty:
        st.info(f"ℹ️ {len(duplicate_rows)} duplicate row(s) found.")
        st.dataframe(duplicate_rows)

    # Clean data before lookup
    df = df.dropna(subset=["location", "state"])
    df = df.drop_duplicates(subset=["location", "state"])

    # Geocode each location
    results = []
    for loc, state in zip(df["location"], df["state"]):
        query = f"{loc}, {state}"
        result = get_lat_long(query)
        results.append({
            "location": loc,
            "state": state,
            "latitude": result["lat"] if result else None,
            "longitude": result["lon"] if result else None
        })

    result_df = pd.DataFrame(results)
    st.dataframe(result_df)

    # Map overlay
    if show_map:
        map_df = result_df.dropna(subset=["latitude", "longitude"]).copy()
        map_df["lat"] = pd.to_numeric(map_df["latitude"], errors="coerce")
        map_df["lon"] = pd.to_numeric(map_df["longitude"], errors="coerce")
        map_df = map_df.dropna(subset=["lat", "lon"])

        if not map_df.empty:
            st.map(map_df[["lat", "lon"]])
        else:
            st.warning("No valid coordinates found for map display.")

    # Save and export
    save_export(result_df)
    st.download_button("📥 Download CSV", result_df.to_csv(index=False), "results.csv", "text/csv")

    if enable_export:
        export_to_excel(result_df)
        with open("results.xlsx", "rb") as f:
            st.download_button("📥 Download Excel", f, "results.xlsx")
else:
    st.info("Please upload a CSV file with 'location' and 'state' columns.")
