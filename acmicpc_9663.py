# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DFS(queen_cnt):
    if queen_cnt == N:
        global cnt; cnt += 1
        return
    
    for i in range(N):
        if (
            not rowNcol[i]
            and not slash[queen_cnt + i]    # x + y
            and not back_slash[queen_cnt - i + N - 1]   # x - y + N - 1
        ):
            rowNcol[i] = True
            slash[queen_cnt + i] = True
            back_slash[queen_cnt - i + N - 1] = True
            
            DFS(queen_cnt + 1)
            
            rowNcol[i] = False
            slash[queen_cnt + i] = False
            back_slash[queen_cnt - i + N - 1] = False
    

# ---------- Main ----------
N = int(input())

rowNcol = [False] * N
slash = [False] * (N * 2 - 1)
back_slash = [False] * (N * 2 - 1)

cnt = 0

DFS(0)
print(cnt, end=" ")