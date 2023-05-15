# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())

for _ in range(caseT):
    cmds = list(input().rstrip())
    length = int(input())
    queue = deque(input().rstrip()[1:-1].split(','))

    FLAG = True
    cntR = 0

    # []를 입력받아도 deque의 길이는 1, deque() 초기화 필요
    if length == 0: queue = deque()

    for cmd in cmds:
        # R일 때마다 뒤집지말고 개수를 세기
        if cmd == "R":
            cntR += 1

        if cmd == "D":
            if queue:
                # R이 홀수번 나왔다면
                if cntR % 2 == 1:
                    queue.pop()

                # R이 짝수번 나왔다면
                else:
                    queue.popleft()
            else:
                FLAG = False
                print("error")
                break

    if FLAG is True:
        # R이 홀수번 나왔다면
        if cntR % 2 == 1:
            queue.reverse()
            print("[" + ','.join(queue) + "]")

        # R이 짝수번 나왔다면
        else:
            print("[" + ','.join(queue) + "]")