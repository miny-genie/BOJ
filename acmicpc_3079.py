from sys import stdin
input = stdin.readline


def check(nums: list, k: int, person_count: int) -> bool:
    entry_count = 0
    for num in nums:
        entry_count += k // num
        if entry_count >= person_count:
            return True
    return False


immigration_count, person_count = map(int, input().split())
immigrations = [int(input()) for _ in range(immigration_count)]

low, high = 0, int(1e18)
while low + 1 < high:
    mid = (low + high) // 2
    if check(immigrations, mid, person_count):
        high = mid
    else:
        low = mid

print(high)

# 24.12.13
# Platinum 1: 2141 > 2141 (+0pts)
# 승급까지 -59 > -59