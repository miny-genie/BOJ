# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
stack, answer = [], []
FLAG, initNum = 0, 1

for i in range(N):
    num = int(input())

    while initNum <= num:
        stack.append(initNum)
        answer.append("+")
        initNum += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")

    else:
        print("NO")
        FLAG = 1
        break

if FLAG == 0:
    for index in answer:
        print(index)