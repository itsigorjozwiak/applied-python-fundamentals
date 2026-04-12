def rzymskie_na_arabskie(rzymskie):
    ROMAN_TO_ARAB_MAP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if not isinstance(rzymskie, str):
        raise TypeError("The Roman numeral must be of type string!!!")
    
    for x in rzymskie:
        if x not in ROMAN_TO_ARAB_MAP:
            raise ValueError("At least one character in the given expression doesn't belong to Roman symbols!!!")
        
    if ("VV" in rzymskie or "LL" in rzymskie or "DD" in rzymskie):
        raise ValueError("Roman numeral notation inconsistent with the rules!!!")
    
    wartosc = 0
    i = 0
    while i < len(rzymskie):
        if i + 1 < len(rzymskie) and ROMAN_TO_ARAB_MAP[rzymskie[i]] < ROMAN_TO_ARAB_MAP[rzymskie[i + 1]]:
            wartosc += ROMAN_TO_ARAB_MAP[rzymskie[i + 1]] - ROMAN_TO_ARAB_MAP[rzymskie[i]]
            i += 2
        else:
            wartosc += ROMAN_TO_ARAB_MAP[rzymskie[i]]
            i += 1

    if not (1 <= wartosc <= 3999):
        raise ValueError("The number received is outside the range of 1-3999!!!")
    
    if arabskie_na_rzymskie(wartosc) != rzymskie:
        raise ValueError("The number given in Roman numerals is probably incorrect due to the use of >3 identical symbols next to each other!!!")
    
    return wartosc

def arabskie_na_rzymskie(arabskie):
    ARAB_TO_ROMAN_MAP = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
    (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

    if not isinstance(arabskie, int):
        raise TypeError("The number in Arabic notation must be of type int!!!")
    
    if not (1 <= arabskie <= 3999):
        raise ValueError("The number given is beyond the range of 1-3999!!!")
    
    rzymskie = ""
    for x, y in ARAB_TO_ROMAN_MAP:
        while arabskie >= x:
            rzymskie += y
            arabskie -= x

    return rzymskie

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
