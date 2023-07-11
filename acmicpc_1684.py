# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        
    return a

# ---------- Main ----------
length = int(input())
N = list(map(int, input().split()))
N.sort()

# Gap each index N
dif_list = [N[i+1]-N[i] for i in range(length-1)]

# Init num
num = dif_list[0]

# Calculate GCD
for i in range(1, len(dif_list)):
    num = gcd(num, dif_list[i])
    
print(num)

# ---------- Comment ----------
# R = N - Q * D
# >>> Q, R = divmod(N, D)
# >>> gcd(N, D) = gcd(D, R)

# R = n1 - (q1 * D)
# R = n2 - (q2 * D)
# >>> n1 - (q1 * D) = n2 - (q2 * D)
# >>> n1 - n2 = (q1 * D) - (q2 * D)
# >>> n1 - n2 = D * (q1 - q2)

# >>> tmp = q1 - q2
# >>> n1 - n2 = D * tmp
# >>> D is factor of (n1 - n2)
# >>> also D is factor of (n2 - n3) ... and so on
# >>> we need MAX D
# >>> so calculate GCD, (n1-n2) & (n2-n3) & ... & (nx-1-nx)