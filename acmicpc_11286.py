# ---------- Import ----------
import heapq
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())
heap = []

for _ in range(caseT):
    x = int(input())
        
    if x == 0:
        if heap:
            absHeap = heapq.heappop(heap)[1]
            print(absHeap)
            
        else:
            print(0)
    
    else:
        heapq.heappush(heap, (abs(x), x))