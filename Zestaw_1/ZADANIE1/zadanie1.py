import sys

def rozklad_na_czynniki(n):
    if n==1:
        return ""
    
    prime_number = 2
    prime_counts = {}

    while prime_number*prime_number <= n:
        while n % prime_number == 0:
            prime_counts[prime_number] = prime_counts.get(prime_number, 0) + 1
            n=n//prime_number
        prime_number += 1
    
    if n>1:
        prime_counts[n] = prime_counts.get(n, 0) + 1

    result = ""
    for number, power in prime_counts.items():
        if result != "":
            result += "*"
        if power == 1:
            result += str(number)
        else:
            result += f"{number}^{power}"

    return result

if __name__ == "__main__":
    argv = sys.argv[1:]

    for arg in argv:
        liczba = int(arg)
        wynik = rozklad_na_czynniki(liczba)
        print(f"{liczba} = {wynik}")
