# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Nonatree(x: int, y: int, n: int):
    global minusCnt, zeroCnt, plusCnt
    
    firstNum = paper[x][y]
    
    for row in range(x, x+n):
        for col in range(y, y+n):
            if firstNum != paper[row][col]:
                N = n // 3
            
                Nonatree(x, y, N)
                Nonatree(x, y+N, N)
                Nonatree(x, y+N+N, N)
                
                Nonatree(x+N, y, N)
                Nonatree(x+N, y+N, N)
                Nonatree(x+N, y+N+N, N)
                
                Nonatree(x+N+N, y, N)
                Nonatree(x+N+N, y+N, N)
                Nonatree(x+N+N, y+N+N, N)
                
                return
    
    count[firstNum] += 1
        
# ---------- Main ----------
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

count = {-1:0, 0:0, 1:0}

Nonatree(0, 0, N)
for v in count.values():
    print(v)

# ---------- Comment ----------
# Single(1), Dual(2), Triple(3), Quad(4), Penta(5)
# Hexa(6), Hepta(7), Octa(8), Nona(9), Deca(10)
# Undeca(11), Dodeca(12)