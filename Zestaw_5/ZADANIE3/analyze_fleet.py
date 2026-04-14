import sqlite3
from datetime import datetime

DB_FILE = "data/traficar.db"

def show_database_stats():
    """Wyświetl podstawowe statystyki zgromadzonych danych."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM car_readings")
    total = cursor.fetchone()[0]
    print(f"Liczba wszystkich zapisanych odczytów: {total}")

    cursor.execute("SELECT MIN(timestamp), MAX(timestamp) FROM car_readings")
    min_date, max_date = cursor.fetchone()
    print(f"Pierwszy odczyt: {min_date}")
    print(f"Ostatni odczyt: {max_date}")

    cursor.execute("SELECT COUNT(DISTINCT car_id) FROM car_readings")
    unique_cars = cursor.fetchone()[0]
    print(f"Liczba unikalnych samochodów: {unique_cars}")

    conn.close()

    return min_date, max_date, unique_cars

def analyze_fuel_consumption(min_date, max_date, total_unique_cars):
    """Analiza zużycia paliwa na podstawie zebranych odczytów."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT model_id, fuel_capacity FROM car_models")
    capacities = {row[0]: row[1] for row in cursor.fetchall()}

    cursor.execute("""
        SELECT car_id, COUNT(*) as cnt
        FROM car_readings
        GROUP BY car_id
        HAVING cnt > 1
    """)
    cars_with_data = cursor.fetchall()
    print(f"\nSamochody z wieloma odczytami: {len(cars_with_data)}")

    consumption_events = []  # lista zdarzeń zużycia paliwa

    for car_id, _ in cars_with_data:
        cursor.execute("""
            SELECT timestamp, fuel, available, model_id
            FROM car_readings
            WHERE car_id = ?
            ORDER BY timestamp
        """, (car_id,))
        readings = cursor.fetchall()

        for i in range(len(readings) - 1):
            prev_ts, prev_fuel, prev_available, model_id = readings[i]
            curr_ts, curr_fuel, curr_available, _ = readings[i + 1]

            # 1. Sprawdź, czy poprzedni odczyt dotyczył auta dostępnego (prev_available == 1).
            # 2. Oblicz różnicę paliwa: delta = prev_fuel - curr_fuel.
            # 3. Jeśli delta > 0.1 (paliwo spadło o więcej niż 0.1%), uznaj to za zdarzenie zużycia paliwa.
            # 4. Dodaj słownik do consumption_events, np.:
            #    {
            #        "car_id": car_id,
            #        "delta": delta,
            #        "from": prev_ts,
            #        "to": curr_ts,
            #    }
            if prev_available == 1:
                delta = prev_fuel - curr_fuel
                if delta > 0.1:
                    capacity = capacities.get(model_id)
                    if not capacity:
                        continue

                    liters = (delta / 100.0) * capacity

                    consumption_events.append({
                        "car_id": car_id,
                        "delta": delta,
                        "liters_burned": liters,
                        "from": prev_ts,
                        "to": curr_ts,
                    })


    conn.close()

    # 1. Wyznacz liczbę wszystkich zdarzeń zużycia paliwa (len(consumption_events)).
    # 2. Wyznacz liczbę unikalnych samochodów, które miały co najmniej jedno zdarzenie
    #    (np. zbiór car_id z consumption_events).
    # 3. Wypisz podsumowanie na konsoli:
    #    - liczba zdarzeń,
    #    - liczba samochodów, które były w ruchu,
    #    - np. kilka pierwszych zdarzeń jako przykłady.

    start = datetime.fromisoformat(min_date.replace('Z', '+00:00'))
    end = datetime.fromisoformat(max_date.replace('Z', '+00:00'))
    hours = (end - start).total_seconds() / 3600
    days = hours / 24 if hours > 0 else 1

    total_liters = sum(e["liters_burned"] for e in consumption_events)
    liters_per_day = total_liters / days

    cars_in_motion = {e["car_id"] for e in consumption_events}

    print("\n=== RAPORT ANALIZY FLOTY ===")
    print(f"Liczba wszystkich unikalnych aut: {total_unique_cars}")
    print(f"Liczba aut, które były w ruchu: {len(cars_in_motion)}")
    print(f"Liczba zdarzeń zużycia paliwa: {len(consumption_events)}")
    print(f"Całkowite zużycie paliwa: {total_liters:.2f} L")
    print(f"Średnie zużycie paliwa (na dobę): {liters_per_day:.2f} L / 24h")

    print("\nPrzykładowe zdarzenia:")
    for e in consumption_events[:5]:
        print(e)


if __name__ == "__main__":
    try:
        min_date, max_date, total_unique_cars = show_database_stats()
        analyze_fuel_consumption(min_date, max_date, total_unique_cars)
    except sqlite3.OperationalError as e:
        print(f"Błąd: {e}")
        print("Upewnij się, że najpierw zebrałeś dane "
              "uruchamiając monitor_traficar.py (np. przez GitHub Actions) "
              "wielokrotnie w czasie.")

