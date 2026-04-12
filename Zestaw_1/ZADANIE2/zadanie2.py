"""
Generator strumienia znaków + liczony "w locie" współczynnik
kompresji RLE. Założenia:
- Alfabet: A-Z, a-z.
- Każdy ciąg jednakowych znaków ma długość losowaną z zakresu 1–10.
- Wydruk: jedna linia (ostatnie WIDTH znaków) + procent kompresji.
- Brak wyjątków; generacja zatrzymuje się po MAXLEN znakach.

Uwaga: animacja w jednej linii powinna być zrealizowana przez print(..., end="\r", flush=True),
a do czyszczenia „resztek” w obrębie okna – przez ljust(WIDTH). Na końcu stały sufiks "  {:3d}%".
"""

import random
import string
import time
from collections import deque

WIDTH = 80            # szerokość okna podglądu
MAXLEN = 1000         # maksymalna liczba generowanych znaków
DELAY_SEC = 0.02      # opóźnienie między kolejnymi znakami (płynność animacji)

ALPHABET = string.ascii_letters  # A-Z, a-z


def znaki():
    while True:
        sign = random.choice(ALPHABET)
        for i in range(random.randint(1, 10)):
          yield sign


def dlugosc(count: int) -> int:
    if count == 1:
        return 1
    else:
        return 1 + len(str(count))


def main():
    buf = deque(maxlen=WIDTH)
    total_raw = 0
    total_rle = 0
    current_char = ""
    current_run_length = 0

    for ch in znaki():
      buf.append(ch)
      total_raw += 1

      if ch == current_char:
        current_run_length += 1
      else:
        if current_run_length > 0 :
          total_rle += dlugosc(current_run_length)
        current_char = ch
        current_run_length = 1

      total_rle_current = total_rle + dlugosc(current_run_length)
      display = "".join(buf)
      percent = round(100 * total_rle_current / total_raw)

      print (f"{display.ljust(WIDTH)} {percent:3d}%", end="\r", flush=True)

      time.sleep(DELAY_SEC)

      if total_raw >= MAXLEN:
        break

    print()


if __name__ == "__main__":
    main()
