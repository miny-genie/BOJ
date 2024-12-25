from sys import stdin
input = stdin.readline

MOD = 1_000_000_007
LEN = 8


def multiply_matrix(matX: list, matY: list) -> list:
    result = [[0] * LEN for _ in range(LEN)]
    for m in range(LEN):
        for n in range(LEN):
            for k in range(LEN):
                result[m][n] += matX[m][k] * matY[k][n]
            result[m][n] %= MOD
    return result


def power_matrix(base: list, exp: int) -> list:
    if exp == 1:
        return base
    half = power_matrix(base, exp // 2)
    if exp % 2:
        return multiply_matrix(base, multiply_matrix(half, half))
    else:
        return multiply_matrix(half, half)


adj_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],   # 학생회관
    [1, 0, 0, 1, 0, 0, 0, 0],   # 형남공학관
    [1, 0, 0, 1, 1, 0, 0, 0],   # 진리관
    [0, 1, 1, 0, 1, 1, 0, 0],   # 한경직기념관
    [0, 0, 1, 1, 0, 1, 1, 0],   # 신양관
    [0, 0, 0, 1, 1, 0, 1, 1],   # 미래관
    [0, 0, 0, 0, 1, 1, 0, 1],   # 전산관
    [0, 0, 0, 0, 0, 1, 1, 0]    # 정보과학관
]

time = int(input())
result_matrix = power_matrix(adj_matrix, time)
print(result_matrix[-1][-1])

# 24.12.26
# Platinum 1: 2151 > 2151 (+0pts)
# 승급까지 -49 > -49