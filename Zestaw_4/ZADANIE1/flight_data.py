import pandas as pd
import matplotlib.pyplot as plt
import requests

try:
    from ZADANIE1.database import save_to_db, load_flight_data
except ImportError:
    from database import save_to_db, load_flight_data

# Funkcja do pozyskania danych z OpenSky Network API
def fetch_flight_data(databasefile="flights.db"):
    # wspolrzedne ATL (Atlanta) w stopniach
    lon_min, lat_min = -88.4277, 30.6407
    lon_max, lat_max = -82.4277, 36.6407

    # napisz kod do pozyskania danych z OpenSky Network API, pamietaj o zalozeniu konta
    user_name = "odloootowo-api-client"
    password = "jBNPgZkXV28dTZGfO05jKfH3onn7eUVW"

    url_data = (
        "https://opensky-network.org/api/states/all?" +
        f"lamin={lat_min}&lomin={lon_min}&lamax={lat_max}&lomax={lon_max}"
    )

    response = requests.get(url_data).json()

    col_name = [
        'icao24', 'callsign', 'origin_country', 'time_position', 'last_contact',
        'long', 'lat', 'baro_altitude', 'on_ground', 'velocity',
        'true_track', 'vertical_rate', 'sensors', 'geo_altitude',
        'squawk', 'spi', 'position_source'
    ]

    states = response.get("states")

    if states is None:
        print("No aircraft in this area. The database will not be updated.")
        return

    flight_df = pd.DataFrame(states, columns=col_name)
    # flight_df = flight_df.replace({None: float("nan")})
    
    # Zapisz dane do bazy danych SQLite
    save_to_db(flight_df, databasefile)
    print("Data saved to database successfully!")


# Odczyt danych i wygenerowanie wykresu z danych lotniczych
def plot_flight_data(databasefile="flights.db", show_plot=True):
    # Wczytaj dane lotnicze z bazy danych
    flight_df =  load_flight_data(databasefile)# to bedzie obiekt typu DataFrame

    # caly kod tutaj (filtracja, konwersja jednostek, sortowanie i wybieranie jednego, rysowanie wykresu)
    flight_df["velocity"] = pd.to_numeric(flight_df["velocity"], errors="coerce").fillna(0)
    flight_df["geo_altitude"] = pd.to_numeric(flight_df["geo_altitude"], errors="coerce").fillna(0)

    flight_df["velocity"] = flight_df["velocity"] * 3.6
    flight_df["geo_altitude"] = flight_df["geo_altitude"] / 1000

    flight_df = flight_df.sort_values(by="velocity", ascending=False).drop_duplicates(subset="icao24", keep="first")

    plt.figure(figsize=(10, 6))
    plt.scatter(
        flight_df["velocity"],
        flight_df["geo_altitude"],
        alpha=0.6
    )

    plt.xlabel("Velocity (km/h)")
    plt.ylabel("Geometric altitude (km)")
    plt.title("Aircraft Velocity vs. Geometric Altitude")

    plt.grid(True)
    plt.tight_layout()
    # Wyświetlanie wykresu tylko, jeśli show_plot=True
    if show_plot:
        plt.show()
