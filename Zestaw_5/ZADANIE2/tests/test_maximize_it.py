from itertools import product
from ZADANIE2.maximize_it import maximize_expression 

def test_simple_case():
    K = 3
    M = 1000
    lists = [
        [2, 5, 4],
        [3, 7, 8, 9],
        [5, 5, 7, 8, 9, 10],
    ]
    result = maximize_expression(K, M, lists)
    assert result == 206, f"Expected 206, got {result}"

def test_single_list_case():
    K = 1
    M = 10
    lists = [
        [1, 2, 3],
    ]
    result = maximize_expression(K, M, lists)
    assert result == 9, f"Expected 9, got {result}"

def test_all_equal_elements():
    K = 2
    M = 100
    lists = [
        [5, 5, 5],
        [5, 5, 5],
    ]
    result = maximize_expression(K, M, lists)
    assert result == 50, f"Expected 50, got {result}"

def test_large_values():
    K = 3
    M = 1000
    lists = [
        [10**9, 10**9 - 1],
        [10**9 - 2, 10**9 - 3],
        [10**9 - 4, 10**9 - 5],
    ]
    result = maximize_expression(K, M, lists)
    expected_result = max(
        sum(x**2 for x in comb) % M for comb in product(*lists)
    )
    assert result == expected_result, f"Expected {expected_result}, got {result}"

def test_small_values():
    K = 3
    M = 5
    lists = [
        [1, 2],
        [1, 2],
        [1, 2],
    ]
    result = maximize_expression(K, M, lists)
    assert result == 4, f"Expected 4, got {result}"

def test_max_k_and_m():
    K = 7
    M = 1000
    lists = [
        [i for i in range(1, 8)] for _ in range(7)
    ]
    result = maximize_expression(K, M, lists)
    expected_result = max(
        sum(x**2 for x in comb) % M for comb in product(*lists)
    )
    assert result == expected_result, f"Expected {expected_result}, got {result}"

def test_modulo_effect():
    K = 2
    M = 6
    lists = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    result = maximize_expression(K, M, lists)
    assert result == 5, f"Expected 5, got {result}"
