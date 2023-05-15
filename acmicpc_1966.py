# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())

for _ in range(caseT):
    N, INDEX = map(int, input().split())
    queue = deque(map(int, input().split()))
    cnt = 0

    while True:
        HIGH = max(queue)

        if queue[0] == HIGH:
            queue.popleft()
            INDEX -= 1      # popleft하니 INDEX도 -1
            cnt += 1

            if INDEX < 0:
                print(cnt)
                break

        else:
            queue.rotate(-1)
            INDEX -= 1
            if INDEX < 0: INDEX = len(queue) - 1

# ---------- Comment ----------
# HIGH = max(queue)는 While 안에 있어야 한다 > 최댓값을 popleft하면 바뀌기 때문
# INDEX = len(queue) - 1에서 N - 1로 작성하면 안 된다 > 길이 역시 바뀌기 때문