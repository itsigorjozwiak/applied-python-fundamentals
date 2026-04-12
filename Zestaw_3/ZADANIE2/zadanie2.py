import json
import folium
import os


def process_tram_data(input_file):
    """
    Args:
        input_file (str): scieżka do pliku wesciowego JSON
    Returns:
        - statystyki: {numer_linii: liczba_przystanków}
        - liczba_unikalnych_przystanków: int
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, input_file)

    # Wczytaj dane z pliku input_file

    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Stwórz slownik ze statystykami {linia: liczba_przystanków}

    stats = {}

    # Znajdź wszystkie unikalne przystanki (użyj set)
    
    unique_stops = set()

    # Przejdź przez wszystkie linie i policz przystanki

    for line in data['linie']:
        line_number = int(line['linia'])
        stops = line['przystanki']
        stats[line_number] = len(stops)

        for stop in stops:
            unique_stops.add(stop['nazwa'])
    
    # Wypisz statystyki posortowane malejaco po liczbie przystanków
    # Format: "linia X: Y"

    for line_number, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"linia {line_number}: {count}")

    # Zwr�c wyniki
    return stats, len(unique_stops)  # przyklad


def create_tram_map(input_file, output_map_file):
    """
    Tworzy interaktywna mape sieci tramwajowej.
    Args:
        input_file (str): scieżka do pliku wesciowego JSON
        output_map_file (str): scieżka do pliku wysciowego HTML
    Przyklad:
        create_tram_map('linie_tramwajowe.json', 'mapa_tramwaje.html')
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_input_path = os.path.join(base_dir, input_file)
    full_output_path = os.path.join(base_dir, output_map_file)

    # Wczytaj dane

    with open(full_input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Stwórz mae wycentrowana na Krakowie [50.06, 19.95], zoom=12
    m = folium.Map(location=[50.06, 19.95], zoom_start=12, tiles="cartodbpositron")

    # Paleta kolorów dla różnych linii
    kolory = [
        "#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00",
        "#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62",
        "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494",
        "#b3b3b3"
    ]

    # Stwórz slownik przystanek -> lista linii

    stop_to_lines = {}

    # Narysuj linie tramwajowe - dodaj PolyLine

    for i, line in enumerate(data['linie']):
        line_number = int(line['linia'])
        coordinates = [(stop['lat'], stop['lon']) for stop in line['przystanki']]
        color = kolory[i % len(kolory)]

        folium.PolyLine(
            coordinates,
            color=color,
            weight=3,
            opacity=0.9,
            tooltip=f"Linia {line_number}"
        ).add_to(m)

        for stop in line['przystanki']:
            stop_name = stop['nazwa']
            if stop_name not in stop_to_lines:
                stop_to_lines[stop_name] = []
            if line_number not in stop_to_lines[stop_name]:
                stop_to_lines[stop_name].append(line_number)

    # Dodaj markery dla przystanków
    # Dla każdego unikalnego przystanku:
    #   - Stwórz CircleMarker
    #   - Dodaj tooltip z nazwa i lista linii

    for stop_name, lines in stop_to_lines.items():
        for line in data['linie']:
            for stop in line['przystanki']:
                if stop['nazwa'] == stop_name:
                    lat, lon = stop['lat'], stop['lon']
                    break
            else:
                continue
            break

        folium.CircleMarker(
            location=(lat, lon),
            radius=2,
            color='#333333',
            fill=True,
            fill_color='#333333',
            fill_opacity=0.9,
            tooltip=f"{stop_name} – linie: {', '.join(map(str, lines))}"
        ).add_to(m)

    # Zapisz mape do pliku
    m.save(full_output_path)


def main():
    print("=" * 60)
    print("Analiza sieci tramwajowej w Krakowie")
    print("=" * 60)
    print()

    print("-" * 60)
    stats, unique_stops = process_tram_data('linie_tramwajowe.json')
    print(f"\nLiczba unikalnych przystanków: {unique_stops}")
    print()

    print("-" * 60)
    create_tram_map('linie_tramwajowe.json', 'mapa_tramwaje.html')
    print(f"Wygenerowano mape: mapa_tramwaje.html")
    print()


if __name__ == "__main__":
    main()

