from itertools import product



def maximize_expression(K, M, lists):
    return max(
        sum(x*x for x in comb) % M
        for comb in product(*lists)
    )



if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
