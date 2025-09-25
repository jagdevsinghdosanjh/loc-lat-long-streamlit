import requests

def get_lat_long(location: str) -> dict | None:
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location,
        "format": "json",
        "limit": 1
    }
    headers = {"User-Agent": "streamlit-app"}
    response = requests.get(url, params=params, headers=headers)
    if response.ok and response.json():
        return response.json()[0]
    return None
