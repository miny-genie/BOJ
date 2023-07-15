# -------------------- Case 1: Python3 TLE, PyPy3 AC --------------------
# # ---------- Import ----------
from collections import Counter
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Minecraft(row, col, inventory, ground):
    SECOND = 1e9
    HEIGHT = -1
    
    minHeight = min(map(min, ground))
    maxHeight = max(map(max, ground))
    
    # Brute Force
    for h in range(minHeight, maxHeight + 1):
        lessThanH = 0
        moreThanH = 0
        
        # Count less and more block, each height
        for r in range(row):
            for c in range(col):
                if ground[r][c] <= h: lessThanH += h - ground[r][c]
                else: moreThanH += ground[r][c] - h
                
        # Checking inventory
        if moreThanH + inventory >= lessThanH:
            
            # Chekcing HEIGHT and SECOND
            if (lessThanH) + (moreThanH*2) <= SECOND:
                SECOND = (lessThanH) + (moreThanH * 2)
                HEIGHT = h
                
    return SECOND, HEIGHT

# ---------- Main ----------
row, col, inventory = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(row)]

second, height = Minecraft(row, col, inventory, ground)
print(second, height)

# INPUT = [
#     [3, 4, 99, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]],             # 2 0
#     [3, 4, 1, [[64, 64, 64, 64], [64, 64, 64, 64], [64, 64, 64, 63]]],  # 1 64
#     [3, 4, 0, [[64, 64, 64, 64], [64, 64, 64, 64], [64, 64, 64, 63]]]   # 22 63
# ]

# for row, col, inventory, ground in INPUT:
#     second, height = Minecraft(row, col, inventory, ground)
#     print(second, height)
    

# -------------------- Case 2: Python3 AC, PyPy3 AC --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
minTime, maxHeight = 1e9, -1
ground = dict()
row, col, inventory = map(int, input().split())

# Dictionary initalization
for _ in range(row):
    for i in map(int, input().split()):
        ground[i] = ground.get(i, 0) + 1
        
keys = ground.keys()

# Brute Force
for currentH in range(min(keys), max(keys)+1):
    difList = [(currentH - height) * count for height, count in ground.items()]
    needBlock = sum(difList)
    spendTime = sum(map(lambda x: x if x > 0 else -2 * x, difList))
    print(currentH, difList, needBlock, spendTime)
    # Checking inventory
    if needBlock <= inventory:
        minTime = min(minTime, spendTime)
        
        if minTime == spendTime:
            maxHeight = max(maxHeight, currentH)
            
print(minTime, maxHeight)