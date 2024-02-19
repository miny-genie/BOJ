# ---------- Import ----------
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def solution(text: str) -> int:
    stack, answer = [], 0
    
    tmp = 1
    for idx, char in enumerate(text):        
        if char == "(":
            stack.append(char)
            tmp *= 2
            
        elif char == "[":
            stack.append(char)
            tmp *= 3
            
        elif char == ")":
            if not stack or stack[-1] != "(":
                return 0
            
            if text[idx-1] == "(":
                answer += tmp
                
            tmp //= 2
            stack.pop()
                
        else:
            if not stack or stack[-1] != "[":
                return 0
            
            if text[idx-1] == "[":
                answer += tmp
                
            tmp //= 3
            stack.pop()
                
    if stack: return 0
    else: return answer

# ---------- Main ----------
text = input().rstrip()
answer = solution(text)
print(answer)