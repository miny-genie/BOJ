# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
triangle = list(map(int, input().split()))
triangle.sort()

if (other := triangle[0] + triangle[1]) <= triangle[-1]:
    print(other * 2 - 1)
else:
    print(sum(triangle))