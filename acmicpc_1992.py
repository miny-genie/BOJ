# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Quadtree(lst: list, x: int, y: int, n: int):
    firstNum = lst[x][y]
    
    for row in range(x, x+n):
        for col in range(y, y+n):
            if firstNum != lst[row][col]:
                
                print("(", end="")
                Quadtree(lst, x, y, n//2)
                Quadtree(lst, x, y+n//2, n//2)
                Quadtree(lst, x+n//2, y, n//2)
                Quadtree(lst, x+n//2, y+n//2, n//2)
                print(")", end="")
                
                return
    
    if firstNum == 0:
        print(0, end ="")
        
    if firstNum == 1:
        print(1, end="")

# ---------- Main ----------
N = int(input())
video = [list(map(int, input().rstrip())) for _ in range(N) ]

Quadtree(video, 0, 0, N)