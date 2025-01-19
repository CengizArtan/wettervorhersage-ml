import requests
import pandas as pd
from datetime import date

# API-Details
API_KEY = "d0d5234f99msh68b1f0b74d956cbp191c67jsn2fb974298714"  # RapidAPI-Key
BASE_URL = "https://meteostat.p.rapidapi.com/point/monthly"

# Standort festlegen (Köln)
latitude = 50.9375  # Breitengrad von Köln
longitude = 6.9603  # Längengrad von Köln
altitude = 48  # Höhe (optional, ca. 48 Meter für Köln)

# Zeitraum festlegen
start_date = "2018-01-01"  # Startdatum
end_date = date.today().strftime("%Y-%m-%d")  # Automatisches heutiges Datum

# Anfrage-Header und Parameter
headers = {
    "x-rapidapi-host": "meteostat.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}
params = {
    "lat": latitude,
    "lon": longitude,
    "alt": altitude,
    "start": start_date,
    "end": end_date
}

try:
    # API-Anfrage
    response = requests.get(BASE_URL, headers=headers, params=params)
    print("API-URL:", response.url)
    print("Status Code:", response.status_code)

    # Überprüfen, ob die Anfrage erfolgreich war
    if response.status_code != 200:
        print("Fehler bei der API-Anfrage:", response.text)
        exit()

    # JSON-Daten extrahieren
    data = response.json()

    # Überprüfen, ob die Daten vorhanden sind
    if "data" not in data:
        print("Fehler: Keine Daten im API-Response gefunden.")
        exit()

    # Daten in ein DataFrame umwandeln
    weather_data = pd.DataFrame(data["data"])

    # Spaltenüberschriften setzen
    weather_data.columns = [
        "Date", "Average Temperature (°C)", "Min Temperature (°C)", 
        "Max Temperature (°C)", "Precipitation (mm)", "Wind Speed (km/h)", 
        "Pressure (hPa)", "Sunshine Duration (h)"
    ]

    # Datumsformat korrigieren
    weather_data["Date"] = pd.to_datetime(weather_data["Date"]).dt.strftime("%d.%m.%Y")

    # CSV-Datei speichern
    file_path = "../data/weather_data.csv"
    weather_data.to_csv(file_path, index=False, sep=";", encoding="utf-8-sig")
    print("Wetterdaten gespeichert unter:", file_path)

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
