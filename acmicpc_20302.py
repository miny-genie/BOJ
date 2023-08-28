# -------------------- Python3 TLE, PyPy3 AC --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

UP = 0
DN = 1

# ---------- Function ----------
def prime_factorization(num: int, state: int):
    div, sqrt = 2, int(num ** 0.5) + 1

    while div <= sqrt:
        if num % div: div += 1
        else:
            if state == UP: calculation[UP][div] += 1
            else: calculation[DN][div] += 1
            num //= div
        
    if num > 1:
        if state == UP: calculation[UP][num] += 1
        else: calculation[DN][num] += 1

    return

# ---------- Main ----------
num = int(input())
text = list(input().rstrip().split())

FLAG = UP
calculation = [[0] * 100001 for _ in range(2)]

for op in text:
    if op == "0": print("mint chocolate"); exit()
    elif op == "1": continue
    elif op == "*": FLAG = UP
    elif op == "/": FLAG = DN
    else: prime_factorization(abs(int(op)), FLAG)
        
for i in range(2, 100001):
    if calculation[UP][i] < calculation[DN][i]:
        print("toothpaste")
        break
else:
    print("mint chocolate")
    
# ---------- Comment ----------
# eval(): RecursionError
# sys.setrecursionlimit(35000): OverflowError
# L36: int(op) > abs(int(op)) | WA
# L33 add | TLE
# L40 calculation[DN][i] add | TLE
# 2d list > 1d list | TLE
# Refatoring:   1. using defaultdict
#               2. all prime calculate first
#               3. In prime_factorization() not one by one, jumping next prime