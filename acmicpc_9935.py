# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def isBOOM(text: str, BOOM: str):
    stack = []
    length = len(BOOM)
    
    for c in text:
        stack.append(c)
        
        if c == BOOM[-1] and BOOM == ''.join(stack[-length:]):
            for _ in range(length):
                stack.pop()

    return stack

# ---------- Main ----------
text = input().rstrip()
BOOM = input().rstrip()

remainder = isBOOM(text, BOOM)
print(''.join(remainder)) if remainder else print("FRULA")

# ---------- Comment ----------
# Refactoring: L13 ~ L15

# if c == BOOM[-1]:
#     check = ''.join(stack[-length:])
    
#     if check == BOOM:
#         for _ in range(length):
#             stack.pop()