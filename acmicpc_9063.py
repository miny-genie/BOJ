# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
coordinateX = []
coordinateY = []

for _ in range(N):
    X, Y = map(int, input().split())
    coordinateX.append(X)
    coordinateY.append(Y)
    
print((max(coordinateX) - min(coordinateX)) * (max(coordinateY) - min(coordinateY)))