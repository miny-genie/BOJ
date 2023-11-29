# ---------- Import ----------
from copy import deepcopy
import sys
input = sys.stdin.readline


# ---------- Function ----------
def Rotate_90_Degree(board):
    ret = [[0]*length for _ in range(length)]
    for r in range(length):
        for c in range(length):
            ret[c][length-1-r] = board[r][c]
    return ret


def Rotate_270_Degree(board):
    ret = [[0]*length for _ in range(length)]
    for r in range(length):
        for c in range(length):
            ret[length-1-c][r] = board[r][c]
    return ret


def Reflect(board):
    for i in range(length):
        board[i] = board[i][::-1]
    return board


def LFT(board):
    for i in range(length):
        line = list(filter(None, board[i]))
        for idx in range(len(line)-1):
            if not (line[idx] - line[idx+1]):
                line[idx] *= 2
                line[idx+1] = 0
        line = list(filter(None, line))
        line += [0] * (length - len(line))
        board[i] = line
    return board


def UP(board):
    board = Rotate_270_Degree(board)
    board = LFT(board)   
    return Rotate_90_Degree(board)


def DN(board):
    board = Rotate_90_Degree(board)
    board = LFT(board)
    return Rotate_270_Degree(board)


def RGT(board):
    board = Reflect(board)
    board = LFT(board)
    return Reflect(board)


def BoardGame2048(board, move_count):
    if move_count == 5:
        global max_block
        max_block = max(max_block, max(map(max, board)))
        return
    
    for direct in ["U", "D", "L", "R"]:
        copy_board = deepcopy(board)
        BoardGame2048(switch[direct](copy_board), move_count+1)
    return


# ---------- Main ----------
max_block = 0
switch = {"U":UP, "D":DN, "L":LFT, "R":RGT}

length = int(input())
board = [list(map(int, input().split())) for _ in range(length)]

BoardGame2048(board, 0)
print(max_block)

# ---------- Comment ----------
# https://shoark7.github.io/programming/algorithm/rotate-2d-array.html