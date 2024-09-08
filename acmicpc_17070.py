from sys import stdin
input = stdin.readline

# Direction: Right, Diagonal, Down
RGT, DIG, DN = 0, 1, 2
WALL = 0

def compute_case_of_way(length: int, board: list) -> int:
    dp = [[[0 for _ in range(length)] for _ in range(length)] for _ in range(3)]
    dp[RGT][0][1] = 1
    
    for i in range(2, length):
        if board[0][i] == WALL:
            dp[RGT][0][i] = dp[RGT][0][i-1]
	
    for r in range(1, length):
        for c in range(1, length):
            if (board[r][c] + board[r][c-1] + board[r-1][c]) == WALL:
                dp[DIG][r][c] = sum([
                    dp[RGT][r-1][c-1],
                    dp[DIG][r-1][c-1],
                    dp[DN][r-1][c-1]
                ])
                
            if board[r][c] == WALL:
                dp[RGT][r][c] = dp[RGT][r][c-1] + dp[DIG][r][c-1]
                dp[DN][r][c] = dp[DN][r-1][c] + dp[DIG][r-1][c]
    
    return sum(dp[i][-1][-1] for i in range(3))


length = int(input())
board = [list(map(int, input().split())) for _ in range(length)]
case_of_way = compute_case_of_way(length, board)
print(case_of_way)