# ---------- Import ----------
import re
import sys
input = sys.stdin.readline

# ---------- Function ----------
def removeZero(string):
    if not (string[0] == "0"): return string
    elif set(string) == {"0"}: return "0"
    else: return string[re.match('0+', string).span()[1]:]
    
# ---------- Main ----------
nums = []

for _ in range(int(input())):
    nums += re.split('[^\d]', input().rstrip())

# Ver: print by 'int'
for num in sorted(map(int, (filter(None, nums)))):
    print(num)

# Ver: print by 'str'
for num in sorted(map(removeZero, filter(None, nums)), key = lambda x: (len(x), x)):
    print(num)