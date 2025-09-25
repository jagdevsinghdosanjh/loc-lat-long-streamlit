import requests
from utils.export import log_diagnostic

def get_lat_long(location: str) -> dict | None:
    ...
    if not response.ok or not response.json():
        log_diagnostic(f"Ambiguous or failed lookup: {location}")


def get_lat_long(location: str) -> dict | None:
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": location, "format": "json", "limit": 1}
    headers = {"User-Agent": "streamlit-app"}
    try:
        response = requests.get(url, params=params, headers=headers)
        if response.ok and response.json():
            return response.json()[0]
        else:
            log_diagnostic(f"Failed lookup: {location}")
    except Exception as e:
        log_diagnostic(f"Error for {location}: {e}")
    return None
