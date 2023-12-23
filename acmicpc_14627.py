# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BinarySearch(order: int, pas: list) -> int:
    start = 1
    end = 1_000_000_000
    
    while start <= end:
        mid = (start + end) // 2
        
        count = 0
        for pa in pas:
            count += pa // mid
            
        if count < order:
            end = mid - 1
            
        else:
            remain_pa = sum(pas) - order * mid
            start = mid + 1
    
    return remain_pa

# ---------- Main ----------
pa_count, chicken_order = map(int, input().split())
pas = [int(input()) for _ in range(pa_count)]

answer = BinarySearch(chicken_order, pas)
print(answer)