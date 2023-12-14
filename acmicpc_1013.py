# ---------- Import ----------
import re

# ---------- Main ----------
for _ in range(int(input())):
    string = input()
    result = re.fullmatch("(100+1+|01)+", string)
    
    print("NO") if result is None else print("YES")