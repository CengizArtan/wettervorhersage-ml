Wettervorhersage mit Machine Learning 🌦️

Projektbeschreibung
Dieses Projekt dient als Lernplattform zur Anwendung und Vertiefung von Data-Science- und Machine-Learning-Kenntnissen. Ziel ist es, historische Wetterdaten für Köln zu analysieren und basierend auf Faktoren wie Temperatur und Luftfeuchtigkeit Vorhersagen für die nächsten Tage zu erstellen.
________________________________________
Projektstruktur 📂
•	data/: Enthält die Daten des Projekts.
o	weather_data.csv: Historische Wetterdaten von Meteostat.
o	processed_data.csv: Aufbereitete Daten für das Machine-Learning-Modell.
•	notebooks/: Jupyter-Notebooks für explorative Datenanalyse und Visualisierung.
•	scripts/: Python-Skripte für Datenbeschaffung, Aufbereitung und Modellierung.
o	fetch_weather_data.py: Skript zur automatisierten Datenabfrage von Meteostat.
o	split_csv_columns.py: Skript zur Spaltentrennung und Datenkorrektur.
•	README.md: Projektbeschreibung und Dokumentation.
________________________________________
Projektstatus 🚧
Das Projekt ist noch in Bearbeitung und wird iterativ aufgebaut. Die Datenbeschaffung erfolgt mittlerweile erfolgreich über die Meteostat API, nachdem Probleme mit der OpenWeather API aufgetreten sind. Der aktuelle Stand umfasst echte Wetterdaten (2018-heute) für Köln.
Aktueller Stand:
•	✅ Abgeschlossen:
o	Integration der Meteostat API für historische Wetterdaten (2018-heute).
o	Automatische Speicherung der Daten in einer CSV-Datei.
o	Fehlerbehandlung und Strukturierung der Skripte.
•	🔄 In Arbeit:
o	Datenaufbereitung für das Machine-Learning-Modell.
o	Explorative Datenanalyse und Visualisierung.
•	🛠️ Geplant:
o	Optimierung und Evaluation des Machine-Learning-Modells.
o	Ergebnispräsentation und abschließende Dokumentation.
________________________________________
Umstieg von OpenWeather API zu Meteostat 🌐
Problem mit der OpenWeather API:
Die ursprünglich geplante Integration der OpenWeather API scheiterte aufgrund folgender Punkte:
•	Fehlerhafte API-Schlüssel (Error 401).
•	Begrenzte Verfügbarkeit von historischen Wetterdaten im kostenlosen Tarif.
Lösung mit der Meteostat API:
Nach der Evaluierung alternativer Anbieter fiel die Wahl auf die Meteostat API, da sie:
•	Eine kostenlose und zuverlässige Sammlung historischer Wetterdaten bietet.
•	Wetterdaten seit 2018 bis zum aktuellen Datum abdeckt.
•	Einfache Integration mit umfangreicher Dokumentation erlaubt.
________________________________________
Roadmap 🗺️
1.	Phase 1: Datenbeschaffung
o	Nutzung der Meteostat API zur Sammlung von Wetterdaten für Köln.
2.	Phase 2: Datenaufbereitung
o	Spaltentrennung und Korrektur der CSV-Dateien.
o	Transformation und Normierung der Daten.
3.	Phase 3: Explorative Analyse
o	Visualisierung von Trends, Mustern und Zusammenhängen (z. B. Temperatur vs. Niederschlag).
4.	Phase 4: Modelltraining
o	Entwicklung und Validierung eines Machine-Learning-Modells zur Vorhersage der Durchschnittstemperatur.
5.	Phase 5: Ergebnispräsentation
o	Darstellung der Vorhersagen durch ansprechende Visualisierungen.
o	Abschlussdokumentation des Projekts.
________________________________________
Anforderungen ⚙️
Installiere die benötigten Bibliotheken mit:

pip install -r requirements.txt
________________________________________
Datenaufbereitung 🔧
•	📊 Feature Engineering:
o	Hinzufügen von Wochentagen und Monatsinformationen.
o	Berechnung von Temperaturdifferenzen zwischen aufeinanderfolgenden Tagen.
•	⚙️ Transformation und Normierung:
o	Normierung der Temperaturdaten für den Einsatz in Machine-Learning-Modellen.
________________________________________
Visualisierungen 📈
•	Temperaturtrends:
o	Liniendiagramme zeigen den Verlauf der Temperatur über die Zeit.
•	Änderungen:
o	Balkendiagramme visualisieren tägliche Temperaturdifferenzen.
________________________________________
Nutzung der Skripte 🖥️
1. Datenbeschaffung:
Führe das Skript fetch_weather_data.py aus, um die Daten von der Meteostat API abzurufen:

python scripts/fetch_weather_data.py

Die Wetterdaten werden in der Datei data/weather_data.csv gespeichert.

2. Datenaufbereitung:
Führe das Skript split_csv_columns.py aus, um die Daten zu bereinigen und korrekt zu formatieren:

python scripts/split_csv_columns.py
________________________________________
Hinweis ⚠️
Dieses Repository wird regelmäßig erweitert. Der aktuelle Stand basiert auf echten Wetterdaten, die von der Meteostat API abgerufen wurden. Ziel ist es, das Projekt bis zum Abschluss zu dokumentieren und ein funktionales Machine-Learning-Modell zu präsentieren.

