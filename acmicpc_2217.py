# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse = True)

MAX = -1e9
for i, v in enumerate(rope):
    MAX = max((i+1)*v, MAX)
    
print(MAX)