# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def isPrime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


def Backtracking(number: str):
    if len(number) == length and isPrime(int(number)):
        print(number)
        return
    
    for i in range(10):
        if isPrime(int(number) * 10 + i):
            Backtracking(number + str(i))
    

# ---------- Main ----------
length = int(input())

for i in range(1, 10):
    if isPrime(i):
        Backtracking(str(i))

# ---------- Comment ----------
# MLE: 4,000,000 Byte