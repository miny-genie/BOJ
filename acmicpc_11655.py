# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
text = input().rstrip()

for t in text:
    ascii_num = ord(t)
    
    if 65 <= ascii_num <= 90:
        ascii_num -= 13
        if ascii_num < 65: ascii_num += 26
        print(chr(ascii_num), end="")
        
    elif 97 <= ascii_num <= 122:
        ascii_num += 13
        if ascii_num > 122: ascii_num -= 26
        print(chr(ascii_num), end="")            
        
    else:
        print(t, end="")