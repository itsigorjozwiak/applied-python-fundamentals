import time
import sys
import gmpy2

if hasattr(sys, "set_int_max_str_digits"): 
    sys.set_int_max_str_digits(0) 


def fib_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def mat_mul(A: tuple[int, int, int, int],
            B: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    """
    Mnożenie macierzy 2×2 zapisanych jako krotki (a, b, c, d).
    Zwróć krotkę (a', b', c', d') będącą wynikiem A·B.
    """
    a, b, c, d = A
    e, f, g, h = B
    return (a*e + b*g,
            a*f + b*h,
            c*e + d*g,
            c*f + d*h)


def mat_pow(M: tuple[int, int, int, int], n: int) -> tuple[int, int, int, int]:
    """
    Szybkie potęgowanie macierzy.
    R = (1, 0, 0, 1) – macierz jednostkowa.
    Pętla: jeśli bit n to 1 → R = R·M; zawsze M = M·M; n >>= 1.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    R = (1, 0, 0, 1)
    if n == 0:
        return R

    while n > 0:
        if n & 1:
            R = mat_mul(R, M)
        M = mat_mul(M, M)
        n >>= 1
    return R


def fib_matrix(n: int) -> int:
    """
    Zwraca F_n metodą macierzową.
    • Wyznacz A^n dla A = (1, 1, 1, 0).
    • Zwróć F_n = element [0][1].
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n

    A = (1, 1, 1, 0)
    An = mat_pow(A, n)
    return An[1] 


def main() -> None:
    n = int(input("Podaj n: "))

    start = time.perf_counter()
    f1 = fib_iter(n)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    f2 = fib_matrix(n)
    t2 = time.perf_counter() - start

    start = time.perf_counter()
    f3 = gmpy2.fib(n)
    t3 = time.perf_counter() - start

    print(f"fib_iter:   {t1:.6f} s")
    print(f"fib_matrix: {t2:.6f} s")
    print(f"gmpy2.fib:  {t3:.6f} s")

    print("Długość wyników (liczba cyfr):")
    print("fib_iter:",   len(str(f1)))
    print("fib_matrix:", len(str(f2)))
    print("gmpy2.fib:",  len(str(f3)))

    # dopisać zapis wyników do plików:
    # fib_iter.txt, fib_matrix.txt, fib_gmpy2.txt
    # (po jednym wyniku w każdym pliku) i dodać je
    # do repozytorium

    with open("fib_iter.txt", "w") as f:
        f.write(str(f1))

    with open("fib_matrix.txt", "w") as f:
        f.write(str(f2))

    with open("fib_gmpy2.txt", "w") as f:
        f.write(str(f3))


if __name__ == "__main__":
    main()

