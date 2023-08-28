# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
list_ = [list(map(int,input().split())) for _ in range(N)]
list_.append(list_[0])

sum = 0

for i in range(N):
    fir = list_[i][0] * list_[i+1][1]
    sec = list_[i][1] * list_[i+1][0]
    sum += fir - sec

print(round(abs(sum / 2), 1))