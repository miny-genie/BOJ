# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def check_cloud(line: str) -> list:
    cloud = []
    
    for idx in range(len(line)):
        FIND = line.find('c', idx)
        if FIND >= 0: FIND -= idx
        cloud.append(FIND)
    
    return cloud[::-1]

# ---------- Main ----------
row, col = map(int, input().split())

for _ in range(row):
    line = input().rstrip()[::-1]
    print(*check_cloud(line))