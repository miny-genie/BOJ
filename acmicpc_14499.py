# ---------- Import ----------
from sys import stdin
input = stdin.readline

TOP, BTM = 2, 5

# ---------- Function ----------
def roll_dice(dice, direction):
    if direction == "R":
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
        return dice
        
    elif direction == "L":
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
        return dice
        
    elif direction == "U":
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
        return dice
    
    else:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
        return dice

# ---------- Main ----------
graph_row, graph_col, dice_x, dice_y, _ = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(graph_row)]

dice = [0, 0, 0, 0, 0, 0]
cmd_dict = {1:"R", 2:"L", 3:"U", 4:"D"}
move_dict = {1:(0, 1), 2:(0, -1), 3:(-1, 0), 4:(1, 0)}

for cmd in list(map(int, input().split())):
    dx, dy = move_dict[cmd]
    nx, ny = dx + dice_x, dy + dice_y
    
    if 0 <= nx < graph_row and 0 <= ny < graph_col:
        dice_x, dice_y = nx, ny
        dice = roll_dice(dice, cmd_dict[cmd])
        
        if graph[nx][ny]:
            dice[BTM] = graph[nx][ny]
            graph[nx][ny] = 0
        else:
            graph[nx][ny] = dice[BTM]
    
        print(dice[TOP])