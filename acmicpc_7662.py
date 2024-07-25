from heapq import heappush, heappop
from sys import stdin
input = stdin.readline


def solution(cmd_count: int, cmds: list) -> tuple|None:
    visited = [False] * cmd_count
    max_heap = []
    min_heap = []
    
    for id, cmd in enumerate(cmds):
        op, value = cmd
        value = int(value)
        
        if op == "I":
            heappush(max_heap, (-value, id))
            heappush(min_heap, (value, id))
            visited[id] = True
        
        elif value == 1:
            # Adjusting
            while max_heap and not visited[max_heap[0][1]]:
                heappop(max_heap)
                
            if max_heap:
                _, pop_id = heappop(max_heap)
                visited[pop_id] = False
        
        else:
            # Adjusting
            while min_heap and not visited[min_heap[0][1]]:
                heappop(min_heap)
                
            if min_heap:
                _, pop_id = heappop(min_heap)
                visited[pop_id] = False
    
    # Adjusting
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)
    
    if max_heap:
        return (-max_heap[0][0], min_heap[0][0])


for _ in range(int(input())):
    cmd_count = int(input())
    cmds = [list(input().rstrip().split()) for _ in range(cmd_count)]
    answer = solution(cmd_count, cmds)
    
    if answer:
        print(*answer)
    else:
        print("EMPTY")