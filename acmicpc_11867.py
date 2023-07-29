# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, M = map(int, input().split())
print("B") if N * M % 2 == 1 else print("A")

# # ---------- Comment ----------
# # print('AB'[eval(input().replace(' ','&1&'))])
# # join, enumerate, map, zip, replace, zfill, eval