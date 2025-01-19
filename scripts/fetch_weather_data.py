import requests
import pandas as pd
from datetime import datetime

# API-Details
API_KEY = "5d5c062bc3fba2e60744082d3b114e81"  # Dein API-Schlüssel
BASE_URL = "http://api.openweathermap.org/data/2.5/onecall"

# Standort festlegen (Köln)
latitude = 50.9375  # Breitengrad von Köln
longitude = 6.9603  # Längengrad von Köln
params = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "minutely,hourly,alerts",
    "units": "metric",
    "appid": API_KEY
}

# API-Anfrage
response = requests.get(BASE_URL, params=params)
data = response.json()

# API-Antwort anzeigen
print(data)  # Füge dies hier ein, um die gesamte API-Antwort anzuzeigen

# Prüfe, ob 'daily' in der Antwort enthalten ist
if "daily" not in data:
    print("Fehler in der API-Antwort:", data)
    exit()

# Daten verarbeiten
daily_data = data["daily"]
weather_list = []
for day in daily_data:
    date = datetime.fromtimestamp(day["dt"]).strftime('%Y-%m-%d')
    temp = day["temp"]["day"]
    humidity = day["humidity"]
    weather_list.append({"date": date, "temp": temp, "humidity": humidity})

# Daten speichern
df = pd.DataFrame(weather_list)
df.to_csv("../data/wetterdaten.csv", index=False)
print("Wetterdaten gespeichert!")
