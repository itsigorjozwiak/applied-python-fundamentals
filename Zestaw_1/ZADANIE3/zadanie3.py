"""
Zegar — HH : MM : SS (24h) 

Matryce cyfr i dwukropka zbudowane są z '█' i spacji (8×8 dla cyfr, 8×4 dla ':').
"""
import os
import time
from datetime import datetime

# Ustawienia
FPS = 4               # klatki/sekundę
DIGIT_H = 8           # wysokość (wiersze)
PRZERWA = 2           # odstęp (kolumny)

# Wzorce cyfr (każdy wiersz ma szerokość 8 znaków)
DIGITS = {
    '0': [
        "████████",
        "██    ██",
        "██    ██",
        "██    ██",
        "██    ██",
        "██    ██",
        "██    ██",
        "████████",
    ],
    '1': [
        "    ███ ",
        "   ████ ",
        "    ███ ",
        "    ███ ",
        "    ███ ",
        "    ███ ",
        "    ███ ",
        "  ██████",
    ],
    '2': [
        "████████",
        "      ██",
        "      ██",
        "████████",
        "██      ",
        "██      ",
        "██      ",
        "████████",
    ],
    '3': [
        "████████",
        "      ██",
        "      ██",
        "████████",
        "      ██",
        "      ██",
        "      ██",
        "████████",
    ],
    '4': [
        "██    ██",
        "██    ██",
        "██    ██",
        "████████",
        "      ██",
        "      ██",
        "      ██",
        "      ██",
    ],
    '5': [
        "████████",
        "██      ",
        "██      ",
        "████████",
        "      ██",
        "      ██",
        "      ██",
        "████████",
    ],
    '6': [
        "████████",
        "██      ",
        "██      ",
        "████████",
        "██    ██",
        "██    ██",
        "██    ██",
        "████████",
    ],
    '7': [
        "████████",
        "      ██",
        "     ██ ",
        "    ██  ",
        "   ██   ",
        "  ██    ",
        "  ██    ",
        "  ██    ",
    ],
    '8': [
        "████████",
        "██    ██",
        "██    ██",
        "████████",
        "██    ██",
        "██    ██",
        "██    ██",
        "████████",
    ],
    '9': [
        "████████",
        "██    ██",
        "██    ██",
        "████████",
        "      ██",
        "      ██",
        "      ██",
        "████████",
    ],
}

COLON = [
    "    ",
    " ██ ",
    " ██ ",
    "    ",
    "    ",
    " ██ ",
    " ██ ",
    "    ",
]



def czyszczenie():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def klatka(dt: datetime) -> str:
    time = dt.strftime("%H : %M : %S")
    result = [""] * DIGIT_H
    space = " " * PRZERWA

    for row in range(DIGIT_H):
        for elem in time:
            if elem == " ":
                result[row] += space
            elif elem == ":":
                result[row] += COLON[row] + space
            else:
                result[row] += DIGITS[elem][row] + space
    return "\n".join(result)


def rysuj():
    delay = 1.0 / max(1, FPS)
    while True:
        now = datetime.now()
        czyszczenie()
        print(klatka(now), flush=True)
        time.sleep(delay)


if __name__ == "__main__":
    rysuj()
