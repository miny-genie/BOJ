# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
# Function that check only input row
def CheckRow(lst: list, rowNum: int) -> int:
    count, maxCount = 1, 1
    first = lst[rowNum][0]
    
    for i in range(1, len(lst)):
        if first == lst[rowNum][i]:
            count += 1
        else:
            first = lst[rowNum][i]
            count = 1
        maxCount = max(maxCount, count)
    
    return maxCount


# Function that check only input col
def CheckCol(lst: list, colNum: int) -> int:
    count, maxCount = 1, 1
    first = lst[0][colNum]
    
    for i in range(1, len(lst)):
        if first == lst[i][colNum]:
            count += 1
        else:
            first = lst[i][colNum]
            count = 1
        maxCount = max(maxCount, count)
    
    return maxCount


# ---------- Main ----------
length = int(input())
candy = [list(input().rstrip()) for _ in range(length)]

# UP, DN, LFT, RGT
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 1    # Initialization

# Brute force
for row in range(length):
    for col in range(length):
        
        # Not checking all element
        if (row + col) % 2 == 0:
            
            # Checking 4 directions
            for i in range(4):
                nx = dx[i] + row
                ny = dy[i] + col
                
                if 0 <= nx < length and 0 <= ny < length:
                    
                    # swap
                    candy[row][col], candy[nx][ny] = candy[nx][ny], candy[row][col]
                    
                    # Only check, changing row and col location
                    answer = max(answer, CheckRow(candy, row))
                    answer = max(answer, CheckRow(candy, nx))
                    answer = max(answer, CheckCol(candy, col))
                    answer = max(answer, CheckCol(candy, ny))
                    
                    # rollback
                    candy[row][col], candy[nx][ny] = candy[nx][ny], candy[row][col]
                    
print(answer)