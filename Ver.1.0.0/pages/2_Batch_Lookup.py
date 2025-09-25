import streamlit as st
import pandas as pd
from utils.geocode import get_lat_long
from io import StringIO

st.title("📄 Batch Location Lookup")

uploaded_file = st.file_uploader("Upload CSV with 'location' column", type=["csv"])
show_map = st.sidebar.checkbox("Show Map Overlay", value=True)
enable_export = st.sidebar.checkbox("Enable CSV Export", value=True)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "location" not in df.columns:
        st.error("CSV must contain a 'location' column.")
    else:
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

        if show_map:
            map_data = result_df.dropna(subset=["latitude", "longitude"])
            st.map(map_data.rename(columns={"latitude": "lat", "longitude": "lon"}))

        if enable_export:
            csv = result_df.to_csv(index=False)
            st.download_button("📥 Download Results as CSV", csv, "results.csv", "text/csv")

# import streamlit as st
# import pandas as pd
# from utils.geocode import get_lat_long

# st.title("📄 Batch Location Lookup")

# uploaded_file = st.file_uploader("Upload CSV with 'location' column", type=["csv"])
# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     if "location" not in df.columns:
#         st.error("CSV must contain a 'location' column.")
#     else:
#         results = []
#         for loc in df["location"]:
#             result = get_lat_long(loc)
#             results.append({
#                 "location": loc,
#                 "latitude": result["lat"] if result else None,
#                 "longitude": result["lon"] if result else None
#             })
#         st.dataframe(pd.DataFrame(results))
