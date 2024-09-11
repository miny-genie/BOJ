import re
from sys import stdin
input = stdin.readline


def fill_board(board: str) -> str:
    ret = []
    for parts in re.findall(r'X+|\.+', board):
        if parts[0] == ".":
            ret.append(parts)
        else:
            if len(parts) % 2 == 1:
                return -1
            elif len(parts) % 4 == 0:
                ret.append("A" * len(parts))
            else:
                ret.append("A" * (len(parts)-2) + "BB")
    return ''.join(ret)


board = input().rstrip()
board = fill_board(board)
print(board)