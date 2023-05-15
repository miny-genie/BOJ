# -------------------- Import --------------------
import sys
input = sys.stdin.readline

# -------------------- Function --------------------
def prefixSum(borad: list, row: int, col: int) -> list:
    pfSum = [[0] * (col+1) for _ in range(row+1)]
    
    for r in range(1, row+1):
        for c in range(1, col+1):
            if (r+c) % 2 == 0:
                if borad[r-1][c-1] == "B":
                    pfSum[r][c] = pfSum[r-1][c] + pfSum[r][c-1] - pfSum[r-1][c-1]
                else:
                    pfSum[r][c] = pfSum[r-1][c] + pfSum[r][c-1] - pfSum[r-1][c-1] + 1
            
            else:
                if borad[r-1][c-1] == "W":
                    pfSum[r][c] = pfSum[r-1][c] + pfSum[r][c-1] - pfSum[r-1][c-1]
                else:
                    pfSum[r][c] = pfSum[r-1][c] + pfSum[r][c-1] - pfSum[r-1][c-1] + 1
    
    return pfSum


def countMinRecolor(board: list, row, col, K) -> int:
    MAX, MIN = -1e9, 1e9
    
    for r in range(K, row+1):
        for c in range(K, col+1):
            value = board[r][c] - board[r-K][c] - board[r][c-K] + board[r-K][c-K]
            MAX = max(value, MAX)
            MIN = min(value, MIN)            
    
    return min(MIN, MAX, K*K-MIN, K*K-MAX)

# -------------------- Main --------------------
row, col, K = map(int, input().split())
chessboard = [list(input().rstrip()) for _ in range(row)]
    
# just making prefixsum list about chessboard
prefixSumList = prefixSum(chessboard, row, col)

# calculating recolor count using prefixsum list
result = countMinRecolor(prefixSumList, row, col, K)

# print result
print(result)