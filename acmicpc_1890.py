from sys import stdin
input = stdin.readline


def get_case_of_way(length: int, board: list[list[int]]) -> int:
    dp = [[0] * length for _ in range(length)]
    dp[0][0] = 1
    
    for row in range(length):
        for col in range(length):
            curr_value = dp[row][col]
            dist = board[row][col]
            
            if row == length-1 and col == length-1:
                return curr_value
            
            if row + dist < length:
                dp[row + dist][col] += curr_value
                
            if col + dist < length:
                dp[row][col + dist] += curr_value


length = int(input())
board = [list(map(int, input().split())) for _ in range(length)]
case_of_way = get_case_of_way(length, board)
print(case_of_way)
