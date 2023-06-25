# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BackTracking(start):
    global subSequence, count

    if sum(subSequence) == S and len(subSequence) > 0:
        count += 1
        
    for i in range(start, N):
        subSequence.append(sequence[i])
        BackTracking(i + 1)
        subSequence.pop()
        
    return count 

# ---------- Main ----------
N, S = map(int, input().split())
sequence = list(map(int, input().split()))
subSequence, count = [], 0

result = BackTracking(0)
print(result)