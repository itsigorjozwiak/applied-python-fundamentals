import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # Generowanie wartości x i y przy użyciu eval()
    # Rysowanie wykresu ale bez show()
    funkcja, przedzial = wejscie.split(',')
    x_min, x_max = map(float, przedzial.strip().split())

    x_val = np.linspace(x_min, x_max, 200)
    y_val = [float(eval(funkcja, {"__builtins__": None}, {"x": x})) for x in x_val]

    plt.figure()
    plt.plot(x_val, y_val, label=f"f(x) = {funkcja}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres wielomianu (eval)")
    plt.grid(True)
    plt.legend()

    # Zwracanie wartości na granicach przedziału
    return y_val[0], y_val[-1]

# Funkcja rysująca wykres na podstawie SymPy i lambdify()
def rysuj_wielomian_sympy(wejscie):
    funkcja, przedzial = wejscie.split(',')
    x_min, x_max = map(float, przedzial.strip().split())

    x = symbols('x')
    mathematical_expression = sympify(funkcja)
    funkcja_numeryczna = lambdify(x, mathematical_expression, modules=['numpy'])

    x_val_sympy = np.linspace(x_min, x_max, 200)
    y_val_sympy = funkcja_numeryczna(x_val_sympy)

    plt.figure()
    plt.plot(x_val_sympy, y_val_sympy, label='SymPy')
    plt.title("Wykres funkcji (SymPy)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    # Definicja symbolu i konwersja do funkcji numerycznej za pomocą SymPy
    # Generowanie wartości x i y przy użyciu funkcji numerycznej
    # Rysowanie wykresu ale bez show()

    # Zwracanie wartości na granicach przedziału
    return y_val_sympy[0], y_val_sympy[-1]

if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    
    # Pierwszy wykres z eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)
    
    # Drugie wejście dla funkcji SymPy - bardziej złożona funkcja 
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"  
    
    # Drugi wykres z SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)
    
    # Wyświetlanie obu wykresów
    plt.show()
