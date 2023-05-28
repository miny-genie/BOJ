# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())

for i in range(1, N):
    print("*" * i, end="")
    print(" " * ((N * 2) - (i * 2)), end="")
    print("*" * i)

for i in range(N, 0, -1):
    print("*" * i, end="")
    print(" " * ((N * 2) - (i * 2)), end="")
    print("*" * i)