# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
wordCount = int(input())
origin = input().rstrip()

result = 0

for _ in range(wordCount-1):
    compare = list(input().rstrip())
    remain = 0
    
    for chr in origin:
        if chr in compare: compare.remove(chr)
        else: remain += 1
          
    if remain < 2 and len(compare) < 2:
        result += 1
    
print(result)

# ---------- Comment ----------
# L19 remain < 2
# counter example: DOLL, L