# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Find_Case(start, GOAL, K):
    already = dict()
    already[start] = 0

    Q = deque([(start, 0)])
    
    while Q:
        nums, depth = Q.popleft()
        
        if nums == GOAL:
            return depth
        
        for i in range(length - K + 1):            
            new = nums[:i] + nums[i:i+K][::-1] + nums[i+K:]
            
            if new not in already:
                Q.append((new, depth+1))
                already[new] = depth+1
                
    return -1

# ---------- Main ----------
length, K = map(int, input().split())
GOAL = tuple(map(int, input().split()))
start = tuple(i for i in range(1, length+1))

answer = Find_Case(start, GOAL, K)
print(answer)

# ---------- Comment ----------
# 11112번 문제랑 같은 개념