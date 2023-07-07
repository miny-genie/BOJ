# ---------- Import ----------
from collections import defaultdict
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, M = map(int, input().split())
ID_PW = defaultdict()

for _ in range(N):
    ID, PW = map(str, input().rstrip().split())
    ID_PW[ID] = PW
    
for _ in range(M):
    print(ID_PW[input().rstrip()])