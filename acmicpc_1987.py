# # -------------------- Case 1: PyPy3(AC: 7324ms, 155756KB) --------------------
# # ---------- Import ----------
# import sys
# input = sys.stdin.readline

# # ---------- Function ----------
# def DFS(x, y, cur_move):
#     global max_move
#     max_move = max(max_move, cur_move)
    
#     for dx, dy in dxy:
#         nx = x + dx
#         ny = y + dy
        
#         if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] not in alphabet:
#             alphabet.add(graph[nx][ny])
#             DFS(nx, ny, cur_move+1)
#             alphabet.remove(graph[nx][ny])
            
# # ---------- Main ----------
# row, col = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(row)]

# alphabet = set()
# alphabet.add(graph[0][0])

# dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# max_move = 1
# DFS(0, 0, 1)

# print(max_move)


# -------------------- Case 2: Python3(AC: 1056ms, 50712KB) --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def NonRecursiveDFS(x, y):
    global max_move
    
    alphabet = set([(x, y, graph[0][0])])

    while alphabet and max_move < 26:
        x, y, footprint = alphabet.pop()
        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] not in footprint:
                alphabet.add((nx, ny, footprint + graph[nx][ny]))
                max_move = max(max_move, len(footprint)+1)

# ---------- Main ----------
row, col = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(row)]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_move = 1

NonRecursiveDFS(0, 0)

print(max_move)