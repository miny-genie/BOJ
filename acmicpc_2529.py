# -------------------- Case 1: Python3 AC(34176KB, 4052ms) --------------------
# ---------- Import ----------
from collections import deque
import sys
ipnut = sys.stdin.readline

# ---------- Function ----------
def Backtracking(exp):
    global visited, count
    
    if count == length + 1:
        global max_ans, min_ans
        tmp = exp[3:].replace("<", "").replace(">", "")
        max_ans = max(max_ans, int(tmp))
        min_ans = min(min_ans, int(tmp))
        return
    
    for num, is_yet in enumerate(visited):
        if is_yet == 0 and eval(exp+str(num)):
            count += 1
            visited[num] = 1
            exp += str(num)
            exp += not_equal.popleft()
            
            Backtracking(exp)
            
            count -= 1
            visited[num] = 0
            not_equal.appendleft(exp[-1])            
            exp = exp[:-2]
    
    return

# ---------- Main ----------
length = int(input())
not_equal = deque(list(map(str, input().split())) + [">"])

visited = [0] * 10
count = 0
exp = "-1<"

max_ans = -1e10
min_ans = 1e10

Backtracking(exp)

print(str(max_ans).zfill(length+1))
print(str(min_ans).zfill(length+1))




# -------------------- Case 2: Python3 AC(32276KB, 140ms) --------------------
# ---------- Function ----------
def check(a, b, op):
    if op == "<": return a < b
    else: return a > b


def DFS(cnt, num):
    if cnt == K+1:
        answer.append(num)
        return
    
    for i in range(10):
        if visited[i]: continue
        
        if cnt == 0 or check(num[cnt-1], str(i), signs[cnt-1]):
            visited[i] = 1
            DFS(cnt+1, num+str(i))
            visited[i] = 0


# ---------- Main ----------
K = int(input())
signs = list(input().split())

visited = [0] * 10
answer = []

DFS(0, '')
answer.sort()

print(answer[-1])
print(answer[0])