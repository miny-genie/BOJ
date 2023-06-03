# ----------Import ----------
from itertools import permutations
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, M = map(int, input().split())
numList = list(map(int, input().split()))

numList.sort()
result = list(permutations(numList, M))

for v in result:
    for i in v:
        print(i, end=" ")