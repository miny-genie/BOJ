# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
print((2 ** int(input()) + 1) ** 2)

# ---------- Comment ----------
# 또 다른 풀이(Other Solution)

# N = int(input())
# dot = 2
# for i in range(N):
#     dot += dot - 1

# print(pow(dot, 2))

# 증명(Proof)
# n = 2
# 0 = 4 = 2^2 = n^2

# n = n + (n-1) = 2 + 1 = 3
# 1 = 9 = 3^2 = n^2

# n = n + (n-1) = 3 + 2 = 5
# 2 = 25 = 5^2 = n^2

# n = n + (n-1) = 5 + 4 = 9
# 3 = 81 = 9^2 = n^2

# n = n + (n-1) = 9 + 8 = 17
# 4 = 289 = 17^2

# n = n + (n-1) = 17 + 16 = 33
# 5 = 1089 = 33^2