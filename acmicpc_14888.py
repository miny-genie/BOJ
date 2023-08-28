# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DFS(depth, plus, minus, multiply, divide, result):
    global maxNum, minNum
    
    if depth == N:
        maxNum = max(result, maxNum)
        minNum = min(result, minNum)
        return
    
    if plus:
        DFS(depth + 1, plus - 1, minus, multiply, divide, result + num[depth])
        
    if minus:
        DFS(depth + 1, plus, minus - 1, multiply, divide, result - num[depth])
        
    if multiply:
        DFS(depth + 1, plus, minus, multiply - 1, divide, result * num[depth])
        
    if divide:
        DFS(depth + 1, plus, minus, multiply, divide - 1, int(result / num[depth]))

# ---------- Main ----------
N = int(input())
num = list(map(int, input().split()))
opCnt = list(map(int, input().split()))

maxNum = -1e9
minNum = 1e9

DFS(1, opCnt[0], opCnt[1], opCnt[2], opCnt[3], num[0])

print(maxNum, minNum, sep="\n")

# ---------- Comment ----------
# L24 int(/) AC, // WA