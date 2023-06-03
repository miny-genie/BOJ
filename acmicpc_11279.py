# ---------- Import ----------
import heapq
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())
heap = []

for _ in range(caseT):
    x = int(input())
    
    if x > 0:
        heapq.heappush(heap, -x)
        
    if x == 0:
        if heap:
            maxHeap = -heapq.heappop(heap)
            print(maxHeap)
        else:
            print(0)
        