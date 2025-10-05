from sys import stdin
input = stdin.readline


def pooling(arr: list[int], length: int) -> tuple[list[int], int]:
    half = length // 2
    return_arr = []
    
    for trial in range(half ** 2):
        bias = trial // half
        start = (((trial + 1) * 2) - 1 + (bias * length))
        
        index1 = [start, start + 1, start + length, start + length + 1]
        index0 = list(map(lambda x: x - 1, index1))
        values = sorted(map(lambda x: arr[x], index0))
        return_arr.append(values[-2])
    
    return return_arr, half


length = int(input())

# TLE가 뜨는 이유
# arr = sum([list(map(int, input().split())) for _ in range(length)], [])
arr = []
for _ in range(length):
    arr.extend(map(int, input().split()))

while len(arr) != 1:
    arr, length = pooling(arr, length)

print(*arr)

# 2025.10.04 해결
# Diamond Ⅴ 2213 > 2213
# 승급까지 87 > 87