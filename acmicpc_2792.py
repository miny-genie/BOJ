# ---------- Import ----------
from math import ceil as ROUNDUP
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BinarySearch(children, jams, start, end):
    # start, end is jam count  
    while start <= end:
        mid = (start + end) // 2
        
        how_many_child = list()
        for jam in jams:
            how_many_child.append(ROUNDUP(jam / mid))
        
        if sum(how_many_child) > children:
            start = mid + 1
            
        else:
            end = mid - 1
    
    return start

# ---------- Main ----------
children, colors = map(int, input().split())
jams = [int(input()) for _ in range(colors)]

answer = BinarySearch(children, jams, 1, max(jams))
print(answer)