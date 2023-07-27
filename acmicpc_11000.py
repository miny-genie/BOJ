# ---------- Import ----------
import heapq
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
time_list = sorted([list(map(int, input().split())) for _ in range(N)])
time_heap = [time_list[0][1]]

for i in range(1, N):
    current_start_time = time_list[i][0]
    min_end_time = time_heap[0]
    
    if min_end_time > current_start_time:
        heapq.heappush(time_heap, time_list[i][1])
        
    else:
        heapq.heappop(time_heap)
        heapq.heappush(time_heap, time_list[i][1])
        
print(len(time_heap))