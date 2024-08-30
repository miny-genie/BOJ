from sys import stdin
input = stdin.readline


def rotate_90(list2d: list) -> list:
    N = len(list2d)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = list2d[r][c]
    return [''.join(line) for line in ret]


def get_space(room: list) -> int:
    return sum(
        sum(map(lambda x: len(x) >= 2, line.split('X')))
        for line in room
    )


size = int(input())
room = [input().rstrip() for _ in range(size)]
horizontal = get_space(room)
vertical = get_space(rotate_90(room))
print(horizontal, vertical)