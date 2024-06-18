from sys import stdin
input = stdin.readline


def find_biggest_perfect_square(board: list, row: int, col: int) -> int:
    def is_square(num: str) -> bool:
        return int(int(num) ** 0.5) ** 2 == int(num)
    
    answer = -1
    
    for x in range(row):
        for y in range(col):
            for row_diff in range(-row, row):
                for col_diff in range(-col, col):
                    if row_diff == 0 and col_diff == 0:
                        continue
                    
                    string = ""
                    temp_x, temp_y = x, y
                    
                    while 0 <= temp_x < row and 0 <= temp_y < col:
                        string += board[temp_x][temp_y]
                        if is_square(string):
                            answer = max(answer, int(string))
                        temp_x += row_diff
                        temp_y += col_diff
    
    return answer


row, col = map(int,input().split())
board = [list(input().rstrip()) for _ in range(row)]
answer = find_biggest_perfect_square(board, row, col)
print(answer)