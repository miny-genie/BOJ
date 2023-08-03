# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())

if not N:
    print(0); exit()

lst_ = sorted([int(input()) for _ in range(N)], key = lambda x: x)

cut = round(N * 0.15 + 0.000001)

UP = sum(lst_[cut:N-cut])
DN = N - (cut * 2)

print(round(UP/DN + 0.000001))