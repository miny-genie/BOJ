# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DFS(X, Y):
    global cnt

    if X < 0 or Y < 0 or X >= N or Y >= N:
        return False

    if graph[X][Y] == 1:
        cnt += 1
        graph[X][Y] = 0
        DFS(X+1, Y)
        DFS(X-1, Y)
        DFS(X, Y+1)
        DFS(X, Y-1)

        return True
    
    return False

# ---------- Main ----------
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

ans = []
for x in range(N):
    for y in range(N):
        cnt = 0
        if DFS(x, y):
            ans.append(cnt)

ans.sort()
print(len(ans))
for i in ans:
    print(i)