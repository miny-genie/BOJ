# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


def isPalindrome(text):
    if text == text[::-1]: return True
    else: False

# ---------- Main ----------
N = int(input())

while True:
    if isPrime(N) and isPalindrome(str(N)):
        print(N)
        break
        
    N += 1