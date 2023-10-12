# ---------- Import ----------
import heapq
import sys
input = sys.stdin.readline

# ---------- Main ----------
length = int(input())
heap = []

for _ in range(length):
    line = list(map(int, input().split()))
    
    for number in line:
        if len(heap) < length:
            heapq.heappush(heap, number)
            
        else:
            if number > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
            
print(heap[0])