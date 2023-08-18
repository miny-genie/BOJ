# ---------- Import ----------
import heapq
import sys
input = sys.stdin.readline

# ---------- Main ----------
print(locals())

giant, CENTI, using_hammer = map(int, input().split())
count = 0

# Init
heap = [-int(input()) for _ in range(giant)]
heapq.heapify(heap)
    
# Use toy hammer
for i in range(using_hammer):    
    if -heap[0] == 1 or -heap[0] < CENTI:
        break
    
    else:
        pop = heapq.heappop(heap)
        heapq.heappush(heap, pop // 2)
        count += 1
    
if -heap[0] < CENTI:
    print("YES", count, sep="\n")
else:
    print("NO", -heap[0], sep="\n")
    
