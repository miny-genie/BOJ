from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

START = 0
END = 1
BIAS = 100_000_000


def compute_max_contain(positions: list, train_len: int) -> int:
    #  declare variable
    heap = []
    max_contain = 0
    
    min_end_pos = positions[-1][END]
    compare_point = max(train_len, min_end_pos)
    
    # sweeping
    while positions:
        # heappush
        while positions and positions[-1][END] <= compare_point:
            heappush(heap, positions.pop())
        
        # heappop
        while heap and compare_point - train_len > heap[0][START]:
            heappop(heap)
        
        compare_point = positions[-1][END] if positions else float('inf')
        max_contain = max(max_contain, len(heap))
    
    return max_contain


n = int(input())

positions = []
for idx in range(n):
    s, e = map(int, input().split())
    positions.append((min(s, e) + BIAS, max(s, e) + BIAS))
positions.sort(key=lambda lst: (lst[END], lst[START]), reverse=True)

train_len = int(input())

max_contain = compute_max_contain(positions, train_len)
print(max_contain)

# 25.01.03
# Platinum 1: 2165 > 2165 (+0pts)
# 승급까지 -35 > -35