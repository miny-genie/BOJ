from itertools import product
from sys import stdin
input = stdin.readline

_, k = map(int, input().split())
nums = sorted(map(int, input().split()))

for perm in product(nums, repeat=k):
    print(*perm)