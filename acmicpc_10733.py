# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
T = int(input())
stack = []

for _ in range(T):
    IN = int(input())

    if IN == 0:
        stack.pop()
    else:
        stack.append(IN)

print(sum(stack))