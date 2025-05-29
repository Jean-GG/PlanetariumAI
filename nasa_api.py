# nasa_api.py

import requests

API_KEY = "JzMmWe6NWqVdDGfzABvJDCgUGoQvTkvADFw4r9I7"

def obtener_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "titulo": data.get("title"),
            "descripcion": data.get("explanation"),
            "imagen": data.get("url")
        }
    return None
