import os
import time
import threading
import sys

# Stałe konfiguracyjne
LICZBA_KROKOW = 80_000_000
LICZBA_WATKOW = sorted({1, 2, 4, os.cpu_count() or 4})


def policz_fragment_pi(pocz: int, kon: int, krok: float, wyniki: list[float], indeks: int) -> None:
    suma = 0.0
    for i in range(pocz, kon):
        x = (i + 0.5) * krok
        suma += 4.0 / (1.0 + x * x)
    wyniki[indeks] = suma
    # Funkcja oblicza częściową sumę przybliżenia liczby pi metodą prostokątów.
    # Argumenty:
    #     pocz, kon - zakres iteracji (indeksy kroków całkowania),
    #     krok      - szerokość pojedynczego prostokąta (1.0 / LICZBA_KROKOW),
    #     wyniki    - lista, do której należy wpisać wynik dla danego wątku na pozycji indeks,
    #     indeks    - numer pozycji w liście 'wyniki' do zapisania rezultatu.

    # Każdy wątek powinien:
    #   - obliczyć lokalną sumę dla przydzielonego przedziału,
    #   - wpisać wynik do wyniki[indeks].

    # zaimplementuj obliczanie fragmentu całki dla danego wątku


def main():
    print(f"Python: {sys.version.split()[0]}  (tryb bez GIL? {getattr(sys, '_is_gil_enabled', lambda: None)() is False})")
    print(f"Liczba rdzeni logicznych CPU: {os.cpu_count()}")
    print(f"LICZBA_KROKOW: {LICZBA_KROKOW:,}\n")

    # Wstępne uruchomienie w celu stabilizacji środowiska wykonawczego
    krok = 1.0 / LICZBA_KROKOW
    wyniki = [0.0]
    w = threading.Thread(target=policz_fragment_pi, args=(0, LICZBA_KROKOW, krok, wyniki, 0))
    w.start()
    w.join()

    # ---------------------------------------------------------------
    # Tu zaimplementować:
    #   - utworzenie wielu wątków (zgodnie z LICZBY_WATKOW),
    #   - podział pracy na zakresy [pocz, kon) dla każdego wątku,
    #   - uruchomienie i dołączenie wątków (start/join),
    #   - obliczenie przybliżenia π jako sumy wyników z poszczególnych wątków,
    #   - pomiar czasu i wypisanie przyspieszenia.
    # ---------------------------------------------------------------

    czasy = {}
    for ilosc_watkow in LICZBA_WATKOW:
        wyniki = [0.0] * ilosc_watkow
        zakres = LICZBA_KROKOW // ilosc_watkow

        watki = []
        start_time = time.perf_counter()

        for i in range(ilosc_watkow):
            pocz = i * zakres
            kon = (i + 1) * zakres if i < ilosc_watkow - 1 else LICZBA_KROKOW
            w = threading.Thread(target=policz_fragment_pi, args=(pocz, kon, krok, wyniki, i))
            watki.append(w)
            w.start()

        for w in watki:
            w.join()

        pi = sum(wyniki)*krok
        czas = time.perf_counter() - start_time
        czasy[ilosc_watkow] = czas

        print(f"Wątki: {ilosc_watkow:2d} | π ≈ {pi:.15f} | czas: {czas:.4f} s")

    czas_wykonania_1_watku = czasy[1]
    print("\nPrzyspieszenie względem 1 wątku:")
    for ilosc_watkow in LICZBA_WATKOW:
        przyspieszenie = czas_wykonania_1_watku / czasy[ilosc_watkow]
        print(f"{ilosc_watkow} wątki -> {przyspieszenie:.2f}x")

if __name__ == "__main__":
    main()
