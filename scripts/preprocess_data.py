import pandas as pd

# Daten laden
df = pd.read_csv("../data/wetterdaten.csv")

# Feature 1: Temperaturänderung
df["temp_diff"] = df["temp"].diff()

# Feature 2: Wochentag hinzufügen
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

# Feature 3: Monatsinformation hinzufügen
df["month"] = pd.to_datetime(df["date"]).dt.month

# Feature 4: Normierung der Temperatur
df["temp_normalized"] = (df["temp"] - df["temp"].mean()) / df["temp"].std()

# Aufbereitete Daten speichern
df.to_csv("../data/processed_data.csv", index=False)
print("Daten aufbereitet und gespeichert!")
