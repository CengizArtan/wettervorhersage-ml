import pandas as pd

# Eingabedatei und Ausgabedatei definieren
input_file = "../data/weather_data.csv"
output_file = "../data/weather_data_split.csv"

try:
    # Datei mit dem richtigen Trennzeichen (Komma) einlesen
    df = pd.read_csv(input_file, sep=",", header=0)

    # Spaltennamen überprüfen und ggf. aktualisieren
    if len(df.columns) == 1:  # Falls die Daten in einer Spalte zusammenhängen
        df = df.iloc[:, 0].str.split(',', expand=True)
        df.columns = [
            "Date", "Average Temperature (°C)", "Min Temperature (°C)", 
            "Max Temperature (°C)", "Precipitation (mm)", "Wind Speed (km/h)", 
            "Pressure (hPa)", "Sunshine Duration (h)"
        ]

    # Datei speichern
    df.to_csv(output_file, index=False)
    print(f"Datei erfolgreich verarbeitet und gespeichert unter: {output_file}")

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
