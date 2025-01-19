Wettervorhersage mit Machine Learning 🌦️

Projektbeschreibung

Dieses Projekt dient als Lernplattform zur Anwendung und Vertiefung von Data-Science- und Machine-Learning-Kenntnissen. Ziel ist es, historische Wetterdaten für Köln zu analysieren und basierend auf Faktoren wie Temperatur und Luftfeuchtigkeit Vorhersagen für die nächsten Tage zu erstellen.

________________________________________

Projektstruktur 📂

•	data/: Enthält die Daten des Projekts.
    o	dummy_data.csv: Dummy-Daten zur Simulation des Workflows.
    o	processed_data.csv: Aufbereitete Daten.
•	notebooks/: Jupyter-Notebooks für explorative Datenanalyse und Visualisierung.
•	scripts/: Python-Skripte für Datenbeschaffung, Aufbereitung und Modellierung.
•	README.md: Projektbeschreibung und Dokumentation.
________________________________________

Projektstatus 🚧

Das Projekt ist noch in Bearbeitung und wird iterativ aufgebaut. Der aktuelle Stand basiert auf Dummy-Daten, bis die OpenWeather-API aktiviert ist.

Aktueller Stand:

•	✅ Abgeschlossen:
    o	Projektstruktur angelegt.
    o	Explorations-Notebook für Visualisierungen vorbereitet.
    o	Dummy-Daten hinzugefügt.
•	🔄 In Arbeit:
    o	API-Integration zur Beschaffung realer Wetterdaten.
    o	Datenaufbereitung und -speicherung.
    o	Modelltraining und -evaluation.
•	🛠️ Geplant:
    o	Optimierung und Evaluation des Machine-Learning-Modells.
    o	Visualisierung und Dokumentation der Ergebnisse.
________________________________________

Roadmap 🗺️

1.	Phase 1: Datenbeschaffung
    o	Nutzung der OpenWeather-API zur Sammlung von Wetterdaten für Köln.
2.	Phase 2: Datenaufbereitung
    o	Berechnung von Temperaturdifferenzen.
    o	Hinzufügen von zeitlichen Features (z. B. Wochentag, Monat).
    o	Transformation und Normierung der Daten.
3.	Phase 3: Explorative Analyse
    o	Visualisierung von Trends, Mustern und Zusammenhängen (z. B. Luftfeuchtigkeit vs. Temperatur).
4.	Phase 4: Modelltraining
    o	Entwicklung und Validierung eines Machine-Learning-Modells zur Temperaturvorhersage.
5.	Phase 5: Ergebnispräsentation
    o	Darstellung der Vorhersagen durch ansprechende Visualisierungen.
    o	Abschlussdokumentation des Projekts.
________________________________________
Anforderungen ⚙️
Installiere die benötigten Bibliotheken mit:

    -   pip install -r requirements.txt

________________________________________

Datenaufbereitung 🔧

•	📊 Feature Engineering:
    o	Berechnung von Temperaturdifferenzen zwischen aufeinanderfolgenden Tagen.
    o	Hinzufügen von Wochentagen und Monatsinformationen.
•	⚙️ Transformation und Normierung:
    o	Normierung der Temperaturdaten für den Einsatz in Machine-Learning-Modellen.
________________________________________

Visualisierungen 📈

•	Temperaturtrends:
    o	Liniendiagramme zeigen den Verlauf der Temperatur über die Zeit.
•	Änderungen:
    o	Balkendiagramme visualisieren tägliche Temperaturdifferenzen.
________________________________________

Hinweis ⚠️

Dieses Repository wird regelmäßig erweitert. Der aktuelle Stand basiert auf Dummy-Daten, um den Workflow zu simulieren. Ziel ist es, das Projekt bis zum Jahresende abzuschließen und die Ergebnisse in einer finalen Version zu präsentieren.
