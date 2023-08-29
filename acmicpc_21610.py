# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def first_make_cloud(N: int):
    global cloud
    cloud[N-1][0] = 7; cloud[N-1][1] = 7
    cloud[N-2][0] = 7; cloud[N-2][1] = 7
    return


def move_cloud(dir, dist):
    global cloud
    cloud.rotate(dx[dir] * dist)
    for each in cloud:
        each.rotate(dy[dir] * dist)
    return


def rain_cloud():
    global bucket
    for r in range(length):
        for c in range(length):
            if cloud[r][c]:
                bucket[r][c] += 1
    return


def diagonal_check():
    idx = [1, 3, 5, 7]
    for x in range(length):
        for y in range(length):
            if cloud[x][y]:
                for i in idx:
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < length and 0 <= ny < length and bucket[nx][ny]:
                        bucket[x][y] += 1
    return        


def make_cloud():
    global bucket, cloud
    for x in range(length):
        for y in range(length):
            if cloud[x][y] == 7:
                cloud[x][y] = 0
                continue
            else:
                if bucket[x][y] >= 2:
                    bucket[x][y] -= 2
                    cloud[x][y] = 7
    return

# ---------- Main ----------
length, time = map(int, input().split())
bucket = [list(map(int, input().split())) for _ in range(length)]
cloud = deque([deque([0]) * length for _ in range(length)])

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# Init
answer = 0

# Fisrt cloud is 2*2 size, the most left bottom
first_make_cloud(length)

for _ in range(time):
    dir, dist = map(int, input().split())
    
    # Cloud move to use deque
    move_cloud(dir-1, dist)

    # Plus 1, under the cloud
    rain_cloud()

    # Check the diagonal bucket within bound
    diagonal_check()
    
    # Create cloud only where height is greater than 2, except already exist
    make_cloud()

print(sum(map(sum, bucket)))