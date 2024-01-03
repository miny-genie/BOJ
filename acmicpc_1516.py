# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
building_count = int(input())

graph = [[] for _ in range(building_count+1)]
inDegree = [0] * (building_count+1)
build_time = [0] * (building_count+1)

# Topology sort initialization
for idx in range(building_count):
    tmp = list(map(int, input().split()))
    
    # time store
    build_time[idx+1] = tmp[0]
    
    # pre-build store
    for p in tmp[1:-1]:
        graph[p].append(idx+1)
        inDegree[idx+1] += 1
        
# Starting queue initialization
Q = deque([i for i in range(1, building_count+1) if not inDegree[i]])

# Doing topology sort
dp = [0] * (building_count+1)

while Q:
    num = Q.popleft()
    dp[num] += build_time[num]    # cur-build spend time

    for next in graph[num]:
        inDegree[next] -= 1     # pre-build complete
        dp[next] = max(dp[num], dp[next])   # pre-build spend time
        
        if not inDegree[next]:
            Q.append(next)
    
    

print(*dp[1:], sep="\n")