# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
answer = 0

for _ in range(int(input())):
    isGoodWord = input().rstrip()
    
    stack = []
    for t in isGoodWord:
        if not stack or stack[-1] != t:
            stack.append(t)
            
        elif stack[-1] == t:
            stack.pop()
        
    if not stack:
        answer += 1
            
print(answer)