# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
# https://yiyj1030.tistory.com/230
def nearestNum(array: list, target: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return array[mid]
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if left > len(array)-1: left = len(array)-1 # Depend overflow left index
    if right < 0: right = 0                     # Depend underflow right index
    difLeft = abs(array[left] - target)
    difRight = abs(array[right] - target)

    if difLeft < difRight:
        return array[left]
    else:
        return array[right]


def minMinusPoint(A: list, B: list, C: list) -> int:
    MIN = 1e9

    for a in A:
        diffB = nearestNum(B, a, 0, len(B)-1)
        diffC1 = nearestNum(C, a, 0, len(C)-1)
        diffC2 = nearestNum(C, diffB, 0, len(C)-1)

        max1 = max(a, diffB, diffC1)
        min1 = min(a, diffB, diffC1)
        score1 = max1 - min1

        max2 = max(a, diffB, diffC2)
        min2 = min(a, diffB, diffC2)
        score2 = max2 - min2

        mScore = min(score1, score2)
        if MIN > mScore:
            MIN = mScore

    return MIN

# ---------- Main ----------
# https://velog.io/@qwerty1434/%EB%B0%B1%EC%A4%80-16498%EB%B2%88-%EC%9E%91%EC%9D%80-%EB%B2%8C%EC%A0%90
a, b, c = map(int, input().split())
cardA = list(map(int, input().split())); cardA.sort()
cardB = list(map(int, input().split())); cardB.sort()
cardC = list(map(int, input().split())); cardC.sort()

point = minMinusPoint(cardA, cardB, cardC)
print(point)