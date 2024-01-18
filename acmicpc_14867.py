# ---------- Import ----------
from collections import deque
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def BFS(A, B, goalA, goalB):
    actions = ["fillA", "fillB", "clearA", "clearB", "AtoB", "BtoA"]
    possible = dict()
    
    # cur_A, cur_B, count
    Q = deque([(0, 0, 0)])
    possible[(0, 0)] = 0
    
    while Q:
        a, b, cnt = Q.popleft()
        
        if a == goalA and b == goalB:
            return cnt
        
        for action in actions:
            if action == "fillA" and (A, b) not in possible:
                Q.append((A, b, cnt+1))
                possible[(A, b)] = cnt+1
                
            elif action == "fillB" and (a, B) not in possible:
                Q.append((a, B, cnt+1))
                possible[(a, B)] = cnt+1
                
            elif action == "clearA" and (0, b) not in possible:
                Q.append((0, b, cnt+1))
                possible[(0, b)] = cnt+1
                
            elif action == "clearB" and (a, 0) not in possible:
                Q.append((a, 0, cnt+1))
                possible[(a, 0)] = cnt+1
                
            elif action == "AtoB":
                b += a
                a = 0
                if b > B:
                    a = b - B
                    b = B
                if (a, b) not in possible:
                    Q.append((a, b, cnt+1))
                    possible[(a, b)] = cnt+1
            
            elif action == "BtoA":
                a += b
                b = 0
                if a > A:
                    b = a - A
                    a = A
                if (a, b) not in possible:
                    Q.append((a, b, cnt+1))
                    possible[(a, b)] = cnt+1
                
    return -1
                

# ---------- Main ----------
A, B, goalA, goalB = map(int, input().split())
answer = BFS(A, B, goalA, goalB)
print(answer)