# Wettervorhersage mit Machine Learning 🌦️

## Projektbeschreibung
Dieses Projekt analysiert historische Wetterdaten für **Köln** und sagt die tägliche Temperatur basierend auf Luftfeuchtigkeit und anderen Faktoren vorher.


## Ordnerstruktur
- `data/`: Enthält die Rohdaten (`wetterdaten.csv`) und die aufbereiteten Daten (`processed_data.csv`).
- `notebooks/`: Jupyter-Notebooks für Datenanalyse und Visualisierung.
- `scripts/`: Python-Skripte für die Datenverarbeitung und Modelltraining.

## Anforderungen
Installiere die benötigten Bibliotheken mit:
```bash
pip install -r requirements.txt

## Geplante Analysen
1. **Temperaturtrends**:
   - Tages- und Wochenschwankungen der Temperatur analysieren.
2. **Zusammenhänge**:
   - Beziehung zwischen Luftfeuchtigkeit und Temperatur untersuchen.
3. **Vorhersage**:
   - Ein Machine-Learning-Modell entwickeln, das die Temperatur der nächsten Tage vorhersagt.

## Datenaufbereitung
- Berechnung von Temperaturdifferenzen zwischen aufeinanderfolgenden Tagen.
- Hinzufügen von Wochentagen und Monatsinformationen.
- Normierung der Temperatur für Machine-Learning-Modelle.

## Visualisierungen
- **Temperaturtrends:** Liniendiagramme zeigen den Verlauf der Temperatur über Zeit.
- **Änderungen:** Balkendiagramme visualisieren tägliche Schwankungen.

## Nächste Schritte
1. Aktivierung des API-Schlüssels abwarten.
2. Daten abrufen und speichern.
3. Machine-Learning-Modell trainieren und evaluieren.
4. Ergebnisse visualisieren und dokumentieren.
