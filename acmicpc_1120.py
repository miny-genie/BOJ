# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def compare_str(one: str, two: str) -> int:
    count = 0
    
    for a, b in zip(one, two):
        if a != b:
            count += 1
    
    return count

# ---------- Main ----------
strA, strB = map(str, input().split())
answer = 50

lenA = len(strA)
lenB = len(strB)

for i in range(lenB - lenA + 1):
    how_many_diff = compare_str(strA, strB[i:i+lenA])
    answer = min(answer, how_many_diff)
    
print(answer)