from sys import stdin
input = stdin.readline


def ladder_game(lines):
    number = [str(i) for i in range(vertical+1)]
    
    for _, i in sorted(lines, key=lambda x: (x[0], x[1])):
        number[i], number[i+1] = number[i+1], number[i]
    
    print(''.join(number))
    return ''.join(number) == ''.join([str(i) for i in range(vertical+1)])


def backtracking(depth: int, cur_lines: list, visited: dict):    
    if ladder_game(cur_lines):
        global answer
        answer = min(answer, depth)
        print(cur_lines)
    
    if depth == 3:
        return
    
    for key, value in visited.items():
        if not value:
            visited[key] = 1
            cur_lines.append(key)
            backtracking(depth+1, cur_lines, visited)
            visited[key] = 0
            cur_lines.pop()


vertical, line_count, horizontal = map(int, input().split())

# for backtracking
all_line = dict()
for ver in range(1, vertical):
    for hor in range(1, horizontal+1):
        key = (hor, ver)
        all_line[key] = 0

# early stopping
if line_count == 0:
    print(0)
    exit()

# line info and update 'all_line' info
lines = list()
how_many_line = dict()
for _ in range(line_count):
    key = tuple(map(int, input().split()))
    all_line[key] = 1
    lines.append(key)
        
# preprocessing, can not connect continuous
for height, start in lines:
    if start > 1: all_line[(height, start-1)] = 1
    if start < vertical: all_line[(height, start+1)] = 1
    
answer = 4
backtracking(0, lines, all_line)
print(-1) if answer == 4 else print(answer)