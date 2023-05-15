# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
K, N = map(int, input().split())
wire = [int(input()) for _ in range(K)]

start, end = 1, max(wire)
while start <= end:
    mid = (start + end) // 2    # start, mid, end는 길이
    wires = 0
    
    for i in wire:
        wires += i // mid
        
    # 개수가 충분한 상황, 길이를 늘려도 된다
    if wires >= N:
        start = mid + 1
    
    # 개수가 부족한 상황, 길이를 줄여야 한다
    else:
        end = mid -1
        
print(end)