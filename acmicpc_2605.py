# ---------- Import ----------
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def solution(orders: list) -> list:
    answer = [1]
    for idx, order in enumerate(orders[1:], 2):
        answer.insert(order, idx)
    return answer[::-1]

# ---------- Main ----------
_ = int(input())
answer = solution(list(map(int, input().split())))
print(*answer)