import streamlit as st
from utils.geocode import get_lat_long

st.title("📍 Single Location Lookup")
location = st.text_input("Enter a location name:")

if location:
    result = get_lat_long(location)
    if result:
        st.success(f"Latitude: {result['lat']}, Longitude: {result['lon']}")
        st.map([{"lat": float(result["lat"]), "lon": float(result["lon"])}])
    else:
        st.error("Location not found.")
