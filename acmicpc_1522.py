# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
text = deque(list(input().rstrip()))
how_many_a = text.count('a')

answer = 1e9

for _ in range(len(text)):
    how_many_b = list(text)[:how_many_a].count('b')
    answer = min(answer, how_many_b)
    text.rotate(1)
    
print(answer)