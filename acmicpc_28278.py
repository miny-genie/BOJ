# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())
stack = []

for _ in range(caseT):
    cmd = list(input().rstrip().split())
    
    if cmd[0] == "1":
        stack.append(int(cmd[1]))
    
    elif cmd[0] == "2":
        print(stack.pop()) if stack else print(-1)
        
    elif cmd[0] == "3":
        print(len(stack))
        
    elif cmd[0] == "4":
        print(0) if stack else print(1)
        
    else:
        print(stack[-1]) if stack else print(-1)