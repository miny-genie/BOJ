from sys import stdin
input = stdin.readline


def find_zero_location(board: list) -> list:
    return [
        (row, col)
        for row, line in enumerate(board)
        for col, value in enumerate(line)
        if value == 0
    ]


def is_valid(board: list, x: int, y: int, num: int) -> bool:
    for i in range(9):
        if num == board[x][i] or num == board[i][y]:
            return False
        
    x_start = x // 3 * 3
    y_start = y // 3 * 3
    for row in range(3):
        for col in range(3):
            if num == board[x_start+row][y_start+col]:
                return False        
    return True


def sudoku_dfs(depth: int, board: list, zero_location: dict) -> None:
    if len(zero_location) <= depth:
        for line in board:
            print(*line, sep="")
        exit()
        
    x, y = zero_location[depth]
    for num in range(1, 10):
        if is_valid(board, x, y, num):
            board[x][y] = num
            sudoku_dfs(depth+1, board, zero_location)
            board[x][y] = 0
    

board = [list(map(int, input().rstrip())) for _ in range(9)]
zero_location = find_zero_location(board)

sudoku_dfs(0, board, zero_location)