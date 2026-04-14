import time
try:
    from ZADANIE1.histogram import plot_histogram
    from ZADANIE1.tablica import MonitorowanaTablica
    from ZADANIE1.algorytmy import algorytmy
except ModuleNotFoundError:
    from histogram import plot_histogram
    from tablica import MonitorowanaTablica
    from algorytmy import algorytmy



N = 50
FPS = 60
TRYBY = ["R", "S", "A", "T"]

def wykonaj_pomiar():
    wszystkie_pomiary = []

    for algorytm, algo_nazwa in algorytmy:
        algo_pomiar = {
            "nazwa": algo_nazwa,
            "pomiary": [],
        }

        for tryb in TRYBY:
            tablica = MonitorowanaTablica(0, 1000, N, tryb)

            t0 = time.perf_counter()
            algorytm(tablica)
            delta_t = time.perf_counter() - t0

            algo_pomiar["pomiary"].append(
                {
                    "tryb": tryb,
                    "czas": delta_t * 1000,
                    "operacje": len(tablica.pelne_kopie),
                }
            )

            plot_histogram(tablica, algo_pomiar["nazwa"], FPS)

        wszystkie_pomiary.append(algo_pomiar)

    return wszystkie_pomiary


def zapisz(pomiary, filename="pomiary.txt"):
    with open(filename, "w") as file:
        for pomiar in pomiary:
            file.write(f'{pomiar["nazwa"]}\n')
            for tryb in pomiar["pomiary"]:
                file.write(
                    f'{tryb["tryb"]}: Tablica posortowana w czasie {tryb["czas"]:.1f} ms. Liczba operacji: {tryb["operacje"]}.\n'
                )
            file.write("\n")


################################################################
def main():
    pomiary = wykonaj_pomiar()
    zapisz(pomiary)
################################################################


if __name__ == '__main__':
    main()
