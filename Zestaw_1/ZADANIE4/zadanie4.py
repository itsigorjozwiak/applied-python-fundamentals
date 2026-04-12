import requests

MIASTA = [
    ("Warszawa","Warszawa"),("Kraków","Krakow"),("Łódź","Lodz"),("Wrocław","Wroclaw"),
    ("Poznań","Poznan"),("Gdańsk","Gdansk"),("Szczecin","Szczecin"),("Bydgoszcz","Bydgoszcz"),
    ("Lublin","Lublin"),("Białystok","Bialystok"),("Katowice","Katowice"),("Gdynia","Gdynia"),
    ("Częstochowa","Czestochowa"),("Radom","Radom"),("Toruń","Torun"),
]

def skaner_temperatur():
    temperature_in_cities = []
    for miasto, city in MIASTA:
        url = f"https://wttr.in/{city}?format=j1"
        website = requests.get(url)
        data = website.json()

        if "current_condition" not in data or len(data["current_condition"]) == 0:
            temp = 5
        else:
            temp = int(data["current_condition"][0]["temp_C"])

        temperature_in_cities.append((miasto, temp))
    return temperature_in_cities


# Należy zdefiniować funkcję skaner_temperatur(), która zwraca listę krotek (miasto, temperatura_int)
# w tej samej kolejności co MIASTA. Źródłem danych jest serwis wttr.in (adres: https://wttr.in/NazwaMiasta?format=j1).
# Funkcja ma pobrać bieżącą temperaturę w °C (klucz "temp_C"), zamienić ją na int i zbudować listę wyników.
#
# Oczekiwane użycie w programie:
# - wywołanie skaner_temperatur(), wypisanie zestawienia "Miasto : temperatura °C" w oddzielnych liniach,
# - wyznaczenie miasta z najniższą i najwyższą temperaturą (nazwy i wartości) na podstawie zwróconej listy,
# - przypisanie wyników do zmiennych: min_miasto, min_temp, max_miasto, max_temp.

if __name__ == "__main__":
    temperature_in_cities = skaner_temperatur()

    for city, temperature in temperature_in_cities:
        print(f"{city} : {temperature} °C")
    
    min_miasto, min_temp = min(temperature_in_cities, key=lambda p: p[1])
    max_miasto, max_temp = max(temperature_in_cities, key=lambda p: p[1])

    print("\n=== Podsumowanie ===")
    print("Najchłodniej:", min_miasto, ": ", min_temp, "°C")
    print("Najcieplej: ", max_miasto, ": ", max_temp, "°C")
