from sys import stdin
input = stdin.readline

MOD = 1_000
COMMON_RATIO = [[6, -4], [1, 0]]
FIRST_TERM = [[28], [6]]


def multiply_matirx(A: list, B: list) -> list:
    rows_A, cols_A_or_rows_B, cols_B = len(A), len(B), len(B[0])
    ret = [[0] * cols_B for _ in range(rows_A)]
    for m in range(rows_A):
        for n in range(cols_B):
            for k in range(cols_A_or_rows_B):
                ret[m][n] += A[m][k] * B[k][n]
            ret[m][n] %= MOD
    return ret


def power_matrix(base: list, exp: int) -> list:
    if exp == 1:
        return base
    
    half = power_matrix(base, exp // 2)
    total = multiply_matirx(half, half)
    
    if exp % 2 == 0:
        return total
    else:
        return multiply_matirx(total, base)


for case in range(test_case := int(input())):
    exponent = int(input())
    power_ratio = power_matrix(COMMON_RATIO, exponent-1)
    last_three_digits = multiply_matirx(power_ratio, FIRST_TERM)[1][0]
    answer = str(last_three_digits - 1).zfill(3)
    print(f"Case #{case+1}: {answer}")