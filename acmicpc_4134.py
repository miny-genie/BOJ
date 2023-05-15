# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def isPrime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
# ---------- Main ----------
T = int(input())

for _ in range(T):
    N = int(input())
    
    while True:
        if isPrime(N):
            print(N)
            break
        else:
            N += 1