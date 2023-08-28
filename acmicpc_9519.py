# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def oneCycle(input_text: list) -> list:
    L = len(input_text)
    
    front = input_text[:L // 2 + 1]
    back = input_text[L // 2 + 1:]
    
    text = []
    for _ in range(len(back)):
        text.append(front.pop(0))
        text.append(back.pop())
    text += front
    
    return text

# ---------- Main ----------
INPUT_NUM = int(input())
text = list(input().rstrip())
pattern = []

# Calculate cycle
while True:
    pattern.append(text)
    text = oneCycle(text)
    
    if text == pattern[0]:
        break

# Relocation
pattern = [pattern[0]] + pattern[1:][::-1]

# Print answer with 'join'
print(''.join(pattern[INPUT_NUM % len(pattern)]))

# ---------- Comment ----------
# 'INPUT_NUM % CYCLE'th is answer location