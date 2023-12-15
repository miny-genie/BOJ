# ---------- Import ----------
import sys
input = sys.stdin.readline


# ---------- Function ----------
def P2P_coef(point1: tuple, point2: tuple) -> float:
    return (point2[1] - point1[1]) / (point2[0] - point1[0])


def checking_building(side: list) -> int:
    bef, count = -1e9, 0
    for x, comp in enumerate(side, 1):
        coef = P2P_coef((0, point), (x, comp))
        if coef > bef:
            count += 1
            bef = coef
    return count


# ---------- Main ----------
length = int(input())
points = list(map(int, input().split()))

max_see = 0
for idx, point in enumerate(points):
    count = 0
    LFT = points[:idx][::-1] 
    RHT = points[idx+1:]
    
    count += checking_building(LFT)
    count += checking_building(RHT)
    max_see = max(max_see, count)
    
print(max_see)