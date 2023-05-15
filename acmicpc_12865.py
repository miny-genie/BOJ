# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, K = map(int, input().split())
dp = [ [ 0 for _ in range(K + 1)] for _ in range(N + 1) ]

weightList, valueList = [0], [0]
for _ in range(N):
    w, v = map(int, input().split())
    weightList.append(w)
    valueList.append(v)
    
for N in range(1, N + 1):
    for K in range(1, K + 1):
        weight = weightList[N]    # Current Weight
        value = valueList[N]      # Current Value
        
        if K < weight:  # 현재 물건의 무게가 최대 용량보다 무겁다면
            dp[N][K] = dp[N - 1][K]
        else:
            # 담을 물건 무게만큼 빼고 담을 물건 가치 더하기
            compare1 = dp[N - 1][K - weight] + value
            # 기존 물건 그대로 들고 가기
            compare2 = dp[N - 1][K]                     
            
            dp[N][K] = max(compare1, compare2)
            
print(dp[N][K])