# ---------- Import ----------
from itertools import permutations
import sys
input = sys.stdin.readline

# ---------- Function ----------
def how_many_half(lst):
    if max(lst) > 50:
        return 0
    
    MAX = 0
    
    for case in permutations(lst, len(lst)):
        tmp, count, prefixsum = 0, 0, []
        
        for i in case:
            tmp += i
            prefixsum.append(tmp)
            
        for i in prefixsum:
            if (i + 50) in prefixsum:
                count += 1
                
        MAX = max(MAX, count)
        
    return MAX

# ---------- Main ----------
pi = int(input())
percent = list(map(int, input().split()))

answer = how_many_half(sorted(percent))
print(answer)