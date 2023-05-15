# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Quadtree(paper: list, x: int, y: int, length: int):
    global whiteCnt, blueCnt
    firstColor = paper[x][y]
    
    for row in range(x, x+length):
        for col in range(y, y+length):
            if firstColor != paper[row][col]:
                Quadtree(paper, x, y, length//2)
                Quadtree(paper, x, y+length//2, length//2)
                Quadtree(paper, x+length//2, y, length//2)
                Quadtree(paper, x+length//2, y+length//2, length//2)
                
                return
                
    if firstColor == 0:
        whiteCnt += 1
    else:
        blueCnt += 1

# ---------- Main ----------
size = int(input())
paper = [list(map(int, input().split())) for _ in range(size)]

whiteCnt, blueCnt = 0, 0
Quadtree(paper, 0, 0, size)

print(whiteCnt, blueCnt, sep="\n")