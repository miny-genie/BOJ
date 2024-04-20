from copy import deepcopy
from collections import deque
from itertools import combinations
from sys import stdin
input = stdin.readline


def simulator(board: list, archer_loc: list, dist: int) -> int:
    def find_enemy(board: deque, archers: list, dist: int) -> list:
        enemy = set()
        
        for archer in archers:
            # init
            Q = deque([(row-1, archer, 1)])
            visited = [[0] * col for _ in range(row)]
            visited[row-1][archer] = 1
            
            # bfs
            while Q:
                cur_x, cur_y, move = Q.popleft()
                
                if board[cur_x][cur_y]:
                    enemy.add((cur_x, cur_y))
                    break
                
                for dx, dy in [(0, -1), (-1, 0), (0, 1)]:
                    nx, ny = dx + cur_x, dy + cur_y
                    
                    # out of bound
                    if nx < 0 or nx >= row or ny < 0 or ny >= col:
                        continue
                    
                    # move limit or already visited
                    if (move == dist) or visited[nx][ny]:
                        continue
                    
                    Q.append((nx, ny, move+1))
                    visited[nx][ny] = 1
        
        return list(enemy)
    
    
    def kill_enemy(board: deque, enemy_list: list) -> deque:
        for enemy in enemy_list:
            x, y = enemy
            board[x][y] = 0
        return board
    
    
    def move_enemy(board: deque)-> deque:
        board.rotate(1)
        board[0] = list(map(lambda x: x*0, board[0]))
        return board
    
    
    game_board = deepcopy(board)
    kill_count = 0
    
    while sum(map(sum, game_board)):
        enemy_list = find_enemy(game_board, archer_loc, dist)
        kill_count += len(enemy_list)
        game_board = kill_enemy(game_board, enemy_list)
        game_board = move_enemy(game_board)
    
    return kill_count


row, col, dist = map(int, input().split())
graph = deque([list(map(int, input().split())) for _ in range(row)])

combination = combinations([i for i in range(col)], 3)
kill_count = max(simulator(graph, comb, dist) for comb in combination)
print(kill_count)