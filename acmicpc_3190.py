from collections import deque
from sys import stdin
input = stdin.readline


class Snake:
    def __init__(self) -> None:
        self.bef_head = None
        self.head = (1, 1)
        self.body = deque([])    # without head and tail
        self.tail = (1, 1)
        self.total_body_length = 1
        
        self.sight = (0, 1)    # right
        self.dx = [-1, 0, 1, 0]    # UP, RGT, DN, LFT
        self.dy = [0, 1, 0, -1]    # UP, RGT, DN, LFT
        self.d_index = 1
    
    def head_move(self) -> None:
        x, y = self.bef_head = self.head
        dx, dy = self.sight
        self.head = (dx+x, dy+y)
    
    def body_move(self) -> None:
        if self.total_body_length <= 2:
            self.tail = self.bef_head
        else:
            self.body.appendleft(self.bef_head)
            self.tail = self.body.pop()
    
    def body_expand(self) -> None:
        if self.total_body_length >= 2:
            self.body.appendleft(self.bef_head)
        self.total_body_length += 1
    
    def hit_self(self) -> bool:
        return self.head in self.body or self.head == self.tail

    def sight_change(self, direct: str) -> None:
        if direct == "L":
            self.d_index = (self.d_index - 1) % 4
        else:
            self.d_index = (self.d_index + 1) % 4
        self.sight = self.dx[self.d_index], self.dy[self.d_index]


def dummy_game(board_size: int, apple_info: dict, change_info: deque) -> int:
    def out_of_bound(check_pos: list, board_size: int) -> bool:
        x, y = check_pos
        return x < 1 or x > board_size or y < 1 or y > board_size
    
    snake = Snake()
    
    current_time = 0
    change_time, change_direct = change_info.popleft()
    change_time = int(change_time)
    
    while True:
        # Step 1
        snake.head_move()
        
        # Step 2
        if out_of_bound(snake.head, board_size) or snake.hit_self():
            return current_time + 1
        
        # Step 3
        if snake.head in apple_info:
            del(apple_info[snake.head])
            snake.body_expand()
        
        # Step 4
        else:
            snake.body_move()
        
        # spent time
        current_time += 1
        
        # after 1 second, one movement cycle end    
        if current_time == change_time:
            snake.sight_change(change_direct)
            if change_info:    # remain info
                change_time, change_direct = change_info.popleft()
                change_time = int(change_time)


board_size = int(input())
apple_count = int(input())
apple_info = {tuple(map(int, input().split())):True for _ in range(apple_count)}

change_count = int(input())
change_info = deque([list(input().rstrip().split()) for _ in range(change_count)])

play_time = dummy_game(board_size, apple_info, change_info)
print(play_time)