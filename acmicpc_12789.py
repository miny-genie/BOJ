# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
_ = int(input())
waiting = list(map(int, input().split()))
number = 1

stack = []
for wait in waiting:
    stack.append(wait)
    
    while stack:
        if stack[-1] == number:
            stack.pop()
            number += 1
        else:
            break
        
print("Sad") if stack else print("Nice")