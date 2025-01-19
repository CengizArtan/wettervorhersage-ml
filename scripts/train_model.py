import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Daten laden
df = pd.read_csv("../data/processed_data.csv")

# Features und Zielvariable
X = df[["humidity", "temp_normalized"]]  # Eingabefeatures
y = df["temp"]  # Zielvariable

# Trainings- und Testdaten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell trainieren
model = LinearRegression()
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Fehlerbewertung
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")
