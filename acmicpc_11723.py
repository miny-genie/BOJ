# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())

S = 0

for _ in range(caseT):
    cmd = list(map(str, input().split()))
    
    if cmd[0] == "add":
        S |= (1 << int(cmd[1]))
        
    elif cmd[0] == "remove":
        S &= ~(1 << int(cmd[1]))
        
    elif cmd[0] == "check":
        print(1 if S & (1 << int(cmd[1])) != 0 else 0)
        
    elif cmd[0] == "toggle":
        S ^= (1 << int(cmd[1]))
        
    elif cmd[0] == "all":
        S = (1 << 21) - 1
        
    else:   # cmd[0] == empty
        S = 0
        
# --- ------- Comment ----------
# https://velog.io/@1998yuki0331/Python-비트-마스킹-정리