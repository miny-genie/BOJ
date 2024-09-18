from sys import stdin
input = stdin.readline


def mapping(board: list) -> dict:
    return {
        board[row][col]:(row, col)
        for row in range(5)
        for col in range(5)
    }


def is_bingo(board: list) -> bool:
    horizontal = sum(all(line) for line in board)
    vertical = sum(
        all([board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]])
        for i in range(5)
    )
    diagonal = sum([
        all([board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]]),
        all([board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]])
    ])
    return horizontal + vertical + diagonal >= 3


def bingo_game(board: dict, call_nums: list) -> int:
    bingo_check = [[False] * 5 for _ in range(5)]
    for nth, call_num in enumerate(call_nums, 1):
        row, col = board[call_num]
        bingo_check[row][col] = True
        if is_bingo(bingo_check):
            return nth


board = [list(map(int, input().split())) for _ in range(5)]
call_nums = sum([list(map(int, input().split())) for _ in range(5)], [])

bingo = bingo_game(mapping(board), call_nums)
print(bingo)