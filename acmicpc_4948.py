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


# ---------- Main ----------
# Find all prime number 2 to 246912(2n)
list_ = [i for i in range(2, 246913) if isPrime(i)]

while True:
    N = int(input())
    
    # End condition
    if N == 0: break
    
    # Counting prime number
    cnt = 0
    for i in list_:
        if N < i and i <= 2*N:
            cnt += 1
            
    print(cnt)