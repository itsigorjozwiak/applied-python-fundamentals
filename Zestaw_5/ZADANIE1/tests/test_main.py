from ZADANIE1.main import wykonaj_pomiar

TOLERANCJA = 0.10  # 10% margines błędu

dane_referencyjne = {
    "Insertion Sort": {"R": 3730, "S": 98, "A": 7350, "T": 2254},
    "Bubble Sort": {"R": 4876, "S": 98, "A": 7350, "T": 3424},
    "Shell Sort": {"R": 884, "S": 396, "A": 803, "T": 606},
    "Merge Sort": {"R": 1008, "S": 878, "A": 838, "T": 930},
    "Quick Sort": {"R": 1030, "S": 6370, "A": 3870, "T": 2230},
    "Tim Sort": {"R": 2288, "S": 260, "A": 4030, "T": 1002},
}

def porownaj_algorytm(algorytm, dane_pomiarowe, tolerancja):
    """Porównuje wyniki dla jednego algorytmu."""
    tryby_referencyjne = dane_referencyjne[algorytm]
    tryby_pomiarowe = {m["tryb"]: m["operacje"] for m in next(
        algo["pomiary"] for algo in dane_pomiarowe if algo["nazwa"] == algorytm
    )}
    rozbieznosci = []
    for tryb, operacje_referencyjne in tryby_referencyjne.items():
        operacje_pomiarowe = tryby_pomiarowe.get(tryb, None)
        if operacje_pomiarowe is None:
            rozbieznosci.append((algorytm, tryb, "brak_pomiaru"))
        elif abs(operacje_referencyjne - operacje_pomiarowe) > tolerancja * operacje_referencyjne:
            rozbieznosci.append((algorytm, tryb, operacje_referencyjne, operacje_pomiarowe))
    return rozbieznosci

def test_insertion_sort():
    dane_pomiarowe = wykonaj_pomiar()
    rozbieznosci = porownaj_algorytm("Insertion Sort", dane_pomiarowe, TOLERANCJA)
    assert not rozbieznosci, f"Znaleziono rozbieżności dla Insertion Sort: {rozbieznosci}"

def test_bubble_sort():
    dane_pomiarowe = wykonaj_pomiar()
    rozbieznosci = porownaj_algorytm("Bubble Sort", dane_pomiarowe, TOLERANCJA)
    assert not rozbieznosci, f"Znaleziono rozbieżności dla Bubble Sort: {rozbieznosci}"

def test_shell_sort():
    dane_pomiarowe = wykonaj_pomiar()
    rozbieznosci = porownaj_algorytm("Shell Sort", dane_pomiarowe, TOLERANCJA)
    assert not rozbieznosci, f"Znaleziono rozbieżności dla Shell Sort: {rozbieznosci}"

def test_merge_sort():
    dane_pomiarowe = wykonaj_pomiar()
    rozbieznosci = porownaj_algorytm("Merge Sort", dane_pomiarowe, TOLERANCJA)
    assert not rozbieznosci, f"Znaleziono rozbieżności dla Merge Sort: {rozbieznosci}"

def test_quick_sort():
    dane_pomiarowe = wykonaj_pomiar()
    rozbieznosci = porownaj_algorytm("Quick Sort", dane_pomiarowe, TOLERANCJA)
    assert not rozbieznosci, f"Znaleziono rozbieżności dla Quick Sort: {rozbieznosci}"

def test_tim_sort():
    dane_pomiarowe = wykonaj_pomiar()
    rozbieznosci = porownaj_algorytm("Tim Sort", dane_pomiarowe, TOLERANCJA)
    assert not rozbieznosci, f"Znaleziono rozbieżności dla Tim Sort: {rozbieznosci}"
