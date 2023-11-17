# ---------- Import ----------
import sys
ipnut = sys.stdin.readline


# ---------- Function ----------
def canMove(location1, location2):
    startX = 6 - int(location1[1])
    startY = ord(location1[0]) - 65
    endX = 6 - int(location2[1])
    endY = ord(location2[0]) - 65
    
    if abs(startX - endX) > 2 or abs(startY - endY) > 2:
        return False
    
    if abs(startX - endX) + abs(startY - endY) == 3:
        return True
    else:
        return False


# ---------- Main ----------
board = [[0] * 6 for _ in range(6)]
footprint = [input().rstrip() for _ in range(36)]
FLAG = "Valid"

for idx, move in enumerate(footprint):
    row = 6 - int(move[1])
    col = ord(move[0]) - 65
    
    if not board[row][col]:
        board[row][col] = 1
        
        if not canMove(footprint[idx], footprint[idx-1]):
            FLAG = "Invalid"
            break
        
    else:
        FLAG = "Invalid"
        break
    
else:
    if not canMove(footprint[0], footprint[-1]):
        FLAG = "Invalid"

print(FLAG)