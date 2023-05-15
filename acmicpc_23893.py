# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, P, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(N-1):
    for j in range(i+1, N):
            if i == j: continue
            val1 = i * i % P
            val2 = i * j % P
            val3 = j * j % P
            val = (val1 + val2 + val3) % P
            if val == K:
                cnt += 1
            
print(cnt)