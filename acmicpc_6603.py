# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BackTracking(startIndex):    
    global subSequence, count

    if len(subSequence) == 6:
        for x in subSequence:
            print(x, end=" ")
        print()
                
    for i in range(startIndex, K):
        subSequence.append(S[i])
        BackTracking(i + 1)
        subSequence.pop()

# ---------- Main ----------
while True:
    INPUT = list(map(int, input().split()))
    if sum(INPUT) == 0: break
    
    K, S = INPUT[0], INPUT[1:]
    subSequence, count = [], 0

    BackTracking(0)
    print()