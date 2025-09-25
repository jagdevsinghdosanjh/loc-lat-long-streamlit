import streamlit as st
from utils.geocode import get_lat_long

st.set_page_config(page_title="Location to Lat-Long", layout="centered")
st.title("📍 Location to Latitude & Longitude")

location = st.text_input("Enter a location name:")

if location:
    with st.spinner("Fetching coordinates..."):
        result = get_lat_long(location)
    if result:
        st.success(f"Latitude: {result['lat']}, Longitude: {result['lon']}")
        st.map([{"lat": float(result["lat"]), "lon": float(result["lon"])}])
    else:
        st.error("Location not found. Try a more specific name.")
