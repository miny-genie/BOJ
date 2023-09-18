# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
original = list(input().rstrip())
length = len(original)

to_one = 0
to_zero = 0

for i, v in enumerate(original):    
    if v == "0":
        to_one += 1
        while i < length and original[i] == "0":
            original[i] = "7"
            i += 1
        
    elif v == "1":
        to_zero += 1
        while i < length and original[i] == "1":
            original[i] = "7"
            i += 1
            
print(min(to_one, to_zero))