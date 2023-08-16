# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DivideAndConquer(num, left, right):    
    if num == 1: return 0
    if num == 2: return 1
    
    left_point = 2 ** left + 1
    right_point = 2 ** right
    
    dif = (right_point - left_point + 1) // 2
    
    if num <= (left_point + right_point) // 2:
        return DivideAndConquer(num-dif, left-1, right-1)
        
    else:
        return not DivideAndConquer(num-(dif*2), left-1, right-1)

# ---------- Main ----------
k = int(input())
left = len(bin(k-1))-3
right = left + 1

result = DivideAndConquer(k, left, right)
print(1) if result else print(0)