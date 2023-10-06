import sys
input = sys.stdin.readline

loc_king, loc_stone, move = map(str, input().split())

dr_list = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx_list = [0, 0, 1, -1, -1, -1, 1, 1]
dy_list = [1, -1, 0, 0, 1, -1, 1, -1]

x_king = 8-int(loc_king[1])
y_king = ord(loc_king[0])-65

x_stone = 8-int(loc_stone[1])
y_stone = ord(loc_stone[0])-65

for _ in range(int(move)):
    direct = input().rstrip()
    dx = dx_list[dr_list.index(direct)]
    dy = dy_list[dr_list.index(direct)]
    
    nx_king = x_king + dx
    ny_king = y_king + dy
    
    if (0 <= nx_king < 8) and (0 <= ny_king < 8):
        if (nx_king == x_stone) and (ny_king == y_stone):
            nx_stone = x_stone + dx
            ny_stone = y_stone + dy
            
            if (0 <= nx_stone < 8) and (0 <= ny_stone < 8):
                x_king = nx_king
                y_king = ny_king
                x_stone = nx_stone
                y_stone = ny_stone
                
        else:
            x_king = nx_king
            y_king = ny_king

print(chr(y_king+65) + str(8-x_king))
print(chr(y_stone+65) + str(8-x_stone))