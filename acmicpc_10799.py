# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
INPUT = list(input().rstrip())
stack = []

result = 0
for idx, chr in enumerate(INPUT):
    if chr == "(":
        stack.append(chr)
    
    else:   # chr == ")"
        if INPUT[idx-1] == "(": # Case 1: latest chr is (
            stack.pop()
            result += len(stack)
        else:                   # Case 2: latest chr is )
            stack.pop()
            result += 1
            
print(result)