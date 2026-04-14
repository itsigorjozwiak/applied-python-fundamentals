from fractions import Fraction
from ZADANIE2.reduce_function import product  

def test_product_with_simple_fractions():
    fracs = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]
    result = product(fracs)
    assert result == (1, 4), f"Expected (1, 4), got {result}"

def test_product_with_whole_numbers():
    fracs = [Fraction(2, 1), Fraction(3, 1), Fraction(4, 1)]
    result = product(fracs)
    assert result == (24, 1), f"Expected (24, 1), got {result}"

def test_product_with_negative_fractions():
    fracs = [Fraction(-1, 2), Fraction(3, 4), Fraction(-4, 5)]
    result = product(fracs)
    assert result == (3, 10), f"Expected (3, 10), got {result}"

def test_product_with_large_fractions():
    fracs = [Fraction(10**6, 10**5), Fraction(10**5, 10**4), Fraction(10**4, 10**3)]
    result = product(fracs)
    assert result == (1000, 1), f"Expected (1000, 1), got {result}"

def test_product_with_zero():
    fracs = [Fraction(1, 2), Fraction(0, 1), Fraction(3, 4)]
    result = product(fracs)
    assert result == (0, 1), f"Expected (0, 1), got {result}"

def test_product_with_one():
    fracs = [Fraction(1, 1), Fraction(1, 1), Fraction(1, 1)]
    result = product(fracs)
    assert result == (1, 1), f"Expected (1, 1), got {result}"

def test_product_with_reducing_fractions():
    fracs = [Fraction(2, 4), Fraction(3, 9), Fraction(4, 16)]
    result = product(fracs)
    assert result == (1, 24), f"Expected (1, 24), got {result}"

def test_product_with_large_count_of_fractions():
    fracs = [Fraction(1, 2)] * 50
    result = product(fracs)
    expected_numerator = 1
    expected_denominator = 2**50
    assert result == (expected_numerator, expected_denominator), f"Expected ({expected_numerator}, {expected_denominator}), got {result}"

def test_product_with_alternating_signs():
    fracs = [Fraction(-1, 2), Fraction(1, 3), Fraction(-2, 5), Fraction(3, 7)]
    result = product(fracs)
    assert result == (1, 35), f"Expected (1, 35), got {result}"

def test_product_with_single_fraction():
    fracs = [Fraction(5, 6)]
    result = product(fracs)
    assert result == (5, 6), f"Expected (5, 6), got {result}"
