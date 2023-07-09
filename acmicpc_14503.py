# ---------- Import ----------
import copy
import sys
input = sys.stdin.readline

# ---------- Function ----------
def simulation(rowSize, colSize, x, y, direction, area):
    # direction : North(0), East(1), South(2), West(3)
    
    cnt = 0
    iscleaning = copy.deepcopy(area)
    
    # UP, RGT, DN, LFT
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while True:
        if iscleaning[x][y] == 0:
            iscleaning[x][y] = 1
            cnt += 1
            
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<rowSize and 0<=ny<colSize and\
                area[nx][ny] != 1 and iscleaning[nx][ny] == 0:
                direction -= 1
                if direction < 0: direction = 3
                
                if area[x + dx[direction]][y + dy[direction]] == 0 and\
                    iscleaning[x + dx[direction]][y + dy[direction]] == 0:
                    x += dx[direction]
                    y += dy[direction]
                
                break
        else:
            nx = x - dx[direction]
            ny = y - dy[direction]
            
            if 0 <= nx < rowSize and 0 <= ny < colSize and area[nx][ny] != 1:
                x, y = nx, ny
            else:
                return cnt
            
# ---------- Main ----------
row, col = map(int, input().split())
# d: North(0), East(1), South(2), West(3)
firstX, firstY, direction = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(row)]

result = simulation(row, col, firstX, firstY, direction, area)
print(result)

# ---------- Comment ----------
# Cleaning condition
# 0 is not clean, 1 is clean

# 1. Cleaning current area
# 2. all direction is already clean
#     1. keep direction, go backward and STEP 1
#     2. if can not move backward, then Stop
# 3. not clean area exits any dicreation
#     1. rotate left 90
#     2. if front area is not clean, then move forward
#     3. go STEP 1