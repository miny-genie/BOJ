# ------------------------------ Import ------------------------------
from collections import defaultdict as ddict
import sys
input = sys.stdin.readline

X, Y = 0, 1

# ------------------------------ Function ------------------------------
def condition_0(board: list) -> list:
    # Init
    cnt = 0
    empty = []
    
    # Which space is empty; brute force
    for x in range(length):
        for y in range(length):
            
            # isEmpty
            if not board[x][y]:
                cnt += 1
                empty.append((x, y))
    
    # All empty space
    return empty


def condition_1(board: list, seat: list, now: list) -> list:
    # Init
    empty = ddict(list)
    
    # Which space is the most high favorite around
    for (x, y) in seat:
        like_count = 0
        
        # Check 4 directions
        for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < length and 0 <= ny < length and board[nx][ny] in now:
                like_count += 1
                
        # Append using default-dict
        empty[like_count].append((x, y))
        
    # Empty space list; the most high favorite around
    return empty[max(empty.keys())]
     

def condition_2(board: list, seat: list) -> list:
    # Init
    empty = ddict(list)
    
    # Which space is the most empty around
    for (x, y) in seat:
        empty_count = 0
        
        # Chekcing 4 directions
        for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                empty_count += 1

        # Append using default-dict
        empty[empty_count].append((x, y))
        
    # Empty space list; the most empty around
    return empty[max(empty.keys())]


def student_satisfaction(board: list, likes: list) -> int:
    # Init
    answer = 0
    satis = [0, 1, 10, 100, 1000]
    
    # Checking one of each index
    for x in range(length):
        for y in range(length):
            count = 0
            value = likes[board[x][y]]  # each index is key
            
            # Chekcing 4 directions
            for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                nx, ny = x + dx, y + dy
            
                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] in value:
                    count += 1
                    
            # Add satusfaction using the 'satis' list index
            answer += satis[count]
            
    return answer


# ------------------------------ Main ------------------------------
length = int(input())
classroom = [[0] * length for _ in range(length)]

# Key: Student number
# value: Favorite student number
likes = dict()

for _ in range(length ** 2):    
    num, *like = map(int, input().split())
    likes[num] = like

    # Is 'empty' seat only one?
    if len(seat := condition_0(classroom)) == 1:
        classroom[seat[0][X]][seat[0][Y]] = num
        continue
    
    # Is 'the most favorite section(UDLR)' seat only one?
    if len(seat := condition_1(classroom, seat, likes[num])) == 1:
        classroom[seat[0][X]][seat[0][Y]] = num
        continue
    
    # Is 'the most empty section(UDLR)' seat only one?
    if len(seat := condition_2(classroom, seat)) == 1:
        classroom[seat[0][X]][seat[0][Y]] = num
        continue

    # Where is first row and first col?
    classroom[seat[0][X]][seat[0][Y]] = num

# Calculating all student's satisfaction
answer = student_satisfaction(classroom, likes)
print(answer)

# ------------------------------ Comment ------------------------------
# https://docs.python.org/3/reference/expressions.html#operator-precedence
# https://brownbears.tistory.com/456


# from timeit import timeit
# dict_ = {3: [1], 4: [(0, 0), (1, 0)], 5: 5, 7: [(0, 0), (1, 0)]}
# print(next(iter(sorted(dict_.items(), key = lambda item: item[0], reverse=True))))
# print(dict_[max(dict_.keys())])

# ti1 = timeit(stmt= "sorted(dict_.items(), key = lambda item: item[0])",
#        setup = "dict_ = {3: [1], 4: [(0, 0), (1, 0)], 5: 5, 7: [(0, 0), (1, 0)]}")

# ti2 = timeit(stmt= "dict_[max(dict_.keys())]",
#              setup= "dict_ = {3: [1], 4: [(0, 0), (1, 0)], 5: 5, 7: [(0, 0), (1, 0)]}")

# print(ti1)
# print(ti2)