# -------------------- Case 1 --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Triangle(graph, x, y, size):
    if size == 3:
        graph[x][y] = "*"                         # "  *  "
        graph[x+1][y-1] = graph[x+1][y+1] = "*"   # " * * "
        
        for i in range(-2, 3):
            graph[x+2][y+i] = "*"                 # "*****"

        return graph
    
    else:
        dif = size // 2
        Triangle(graph, x, y, dif)
        Triangle(graph, x+dif, y-dif, dif)
        Triangle(graph, x+dif, y+dif, dif)
        
        return graph

# ---------- Main ----------
N = int(input())

map_ = [[" "]*((2*N)-1) for _ in range(N)]
map_ = Triangle(map_, 0, N-1, N)

for line in map_:
    print(''.join(line))
    
# -------------------- Case 2 --------------------
def tri(n):
    if n == 3:
        return ["*", "* *", "*****"]
    
    else:
        arr = tri(n//2)
        res = []
        for a in arr:
            res.append(a)
        for idx, a in enumerate(arr):
            res.append(a + ' ' * len(arr[-idx-1]) + a)
        return res

n = int(input())
for i, t in enumerate(tri(n)):
    print(t.rjust(n + i, ' ') + ' ' * (n-i-1))