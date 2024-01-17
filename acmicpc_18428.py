# ---------- Import ----------
from itertools import combinations
from copy import deepcopy
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def big_brother_is_watching_you(graph, teacher) -> str:
    x, y = teacher
    
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = dx + x
        ny = dy + y
        
        while 0 <= nx < size and 0 <= ny < size:
            if graph[nx][ny] == "S": return "GOTCHA"
            elif graph[nx][ny] == "T": break
            elif graph[nx][ny] == "O": break
            
            nx += dx
            ny += dy
    
    return "NON"


def canEscape(graph, all_case, teacher) -> str:
    for i, ((x1, y1), (x2, y2), (x3, y3)) in enumerate(all_case):
        room = deepcopy(graph)
        room[x1][y1] = room[x2][y2] = room[x3][y3] = "O"
        
        for T in teacher:
            result = big_brother_is_watching_you(room, T)
            if result == "GOTCHA":
                break
            
        else:
            return "YES"
        
    return "NO"

# ---------- Main ----------
size = int(input())
graph = [list(input().rstrip().split()) for _ in range(size)]

empty, teacher = [], []
for x in range(size):
    for y in range(size):
        if graph[x][y] == "X": empty.append((x, y))
        elif graph[x][y] == "T": teacher.append((x, y))
        
answer = canEscape(graph, combinations(empty, 3), teacher)
print(answer)