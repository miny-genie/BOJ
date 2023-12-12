# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
_ = int(input())
brackets = input().rstrip()

stack, longest = [-1], 0
for i, bracket in enumerate(brackets):
    if bracket == "(":
        stack.append(i)
        
    else:
        stack.pop()
        if stack: longest = max(longest, i - stack[-1])
        else: stack.append(i)
        
print(longest)