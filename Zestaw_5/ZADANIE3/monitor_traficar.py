import requests
import sqlite3
from datetime import datetime
from pathlib import Path

BASE_URL = "https://fioletowe.live/api/v1"
DB_FILE = "data/traficar.db"

def init_database():
    """Inicjalizacja bazy SQLite – tworzenie tabel, jeśli nie istnieją."""
    Path("data").mkdir(exist_ok=True)  # Utwórz folder na bazę, jeśli brak
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Tabela odczytów pojazdów (każdy odczyt wszystkich aut w danej chwili)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS car_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            car_id INTEGER NOT NULL,
            lat TEXT,
            lng TEXT,
            location TEXT,
            zone_id INTEGER,
            model_id INTEGER,
            reg_plate TEXT,
            side_number INTEGER,
            fuel REAL,
            range INTEGER,
            available INTEGER,
            last_update TEXT
        )
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_car_timestamp
        ON car_readings(car_id, timestamp)
    """)

    # Tabela modeli pojazdów
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS car_models (
            model_id INTEGER PRIMARY KEY,
            name TEXT,
            fuel_capacity REAL
        )
    """)

    conn.commit()
    conn.close()

def get_car_models():
    """Pobierz listę modeli samochodów przez API."""
    try:
        response = requests.get(f"{BASE_URL}/car-models", timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("carModels", [])
    except Exception as e:
        print(f"Błąd podczas pobierania modeli: {e}")
        return []

def get_cars():
    """Pobierz aktualną listę samochodów w strefie 1 (Kraków) przez API."""
    try:
        response = requests.get(f"{BASE_URL}/cars", params={"zoneId": 1}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("cars", [])
    except Exception as e:
        print(f"Błąd podczas pobierania aut: {e}")
        return []

def store_car_data(cars):
    """Zapisz dane o wszystkich samochodach do bazy SQLite."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()

    for car in cars:
        cursor.execute("""
            INSERT INTO car_readings (
                timestamp, car_id, lat, lng, location, zone_id, model_id,
                reg_plate, side_number, fuel, range, available, last_update
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            timestamp,
            car["id"],
            car.get("lat"),
            car.get("lng"),
            car.get("location"),
            car.get("zoneId"),
            car.get("modelId"),
            car.get("regPlate"),
            car.get("sideNumber"),
            car.get("fuel"),
            car.get("range"),
            1 if car.get("available") else 0,
            car.get("lastUpdate"),
        ))

    conn.commit()
    conn.close()

def store_car_models(car_models):
    """Zapisz dane modeli samochodów do bazy SQLite."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for m in car_models:
        cursor.execute("""
            INSERT OR REPLACE INTO car_models (model_id, name, fuel_capacity)
            VALUES (?, ?, ?)
        """, (
            m["id"],
            m.get("name"),
            m.get("fuelCapacity"),
        ))

    conn.commit()
    conn.close()

def main():
    print(f"[{datetime.now()}] Rozpoczynam pobieranie danych z API...")
    init_database()

    # Pobierz dane o modelach oraz aktualne dane o samochodach
    car_models = get_car_models()
    cars = get_cars()
    print(f"Pobrano {len(car_models) if car_models else 0} modeli aut "
          f"oraz {len(cars) if cars else 0} aut.")

    # Zapisz pobrane dane do bazy
    if car_models:
        store_car_models(car_models)
    if cars:
        store_car_data(cars)
        print(f"Zapisano odczyt {len(cars)} samochodów do bazy ({DB_FILE}).")
    else:
        print("Brak danych o samochodach – nie zapisano do bazy.")

if __name__ == "__main__":
    main()

