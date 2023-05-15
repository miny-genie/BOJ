# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
INPUT = input().rstrip().split("-")

# Seperate by -, and sum each index
for i, v in enumerate(INPUT):
    popleft = v.split("+")
    
    tmp = 0
    for idx in popleft:
        tmp += int(idx)
        
    INPUT[i] = tmp
  
# Sum all minus index  
sum = INPUT[0] * 2
for i in INPUT:
    sum -= i
    
print(sum)