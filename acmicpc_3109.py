from sys import stdin
input = stdin.readline


def dfs(row: int, depth: int, end_pos: int, pipeline: list, visited: list) -> bool:
    if depth == end_pos:
        return True
    
    for dx, dy in [(-1, 1), (0, 1), (1, 1)]:
        nx = dx + row
        ny = dy + depth
        if 0 <= nx < len(pipeline) and 0 <= ny < len(pipeline[0])\
        and pipeline[nx][ny] == "." and not visited[nx][ny]:
            visited[nx][ny] = True
            if dfs(nx, ny, end_pos, pipeline, visited):
                return True
    return False


row, col = map(int, input().split())
pipeline = [list(input().rstrip()) for _ in range(row)]
visited = [[False] * col for _ in range(row)]

connect = 0
for start in range(row):
    visited[start][0] = True
    if dfs(start, 0, col-1, pipeline, visited):
        connect += 1

print(connect)