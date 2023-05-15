import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    lst = list(input().split())

    if lst[0] == "push":
        queue.append(int(lst[1]))
    
    if lst[0] == "pop":
        print(queue.popleft()) if queue else print(-1)
    
    if lst[0] == "size":
        print(len(queue))
    
    if lst[0] == "empty":
        print(0) if queue else print(1)
    
    if lst[0] == "front":
        print(queue[0]) if queue else print(-1)

    if lst[0] == "back":
        print(queue[-1]) if queue else print(-1)

'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''