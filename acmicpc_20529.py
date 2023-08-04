# ---------- Import ----------
from itertools import combinations
import sys
input = sys.stdin.readline

# ---------- Function ----------
def distance(A: str, B: str) -> int:
    cnt = 0
    
    for v1, v2 in zip(A, B):
        if v1 != v2: cnt += 1
            
    return cnt

# ---------- Main ----------
caseT = int(input())

for _ in range(caseT):
    people = int(input())
    MBTI = list(input().rstrip().split())
    
    # Pigeonhole principle
    if people > 32: print(0)
        
    # Combinations all element, and sum min 3 side
    else:
        gap = []
        for v1, v2, v3 in combinations(MBTI, 3):
            g1 = distance(v1, v2)
            g2 = distance(v1, v3)
            g3 = distance(v2, v3)
            gap.append(g1 + g2 + g3)
        
        print(min(gap))

# ---------- Comment ---------- 
# 3
# 3
# ENTJ INTP ESFJ
# 4
# ESFP ESFP ESFP ESFP
# 5
# INFP INFP ESTP ESTJ ISTJ