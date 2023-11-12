# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
stack_frt = list(input().rstrip())
stack_bck = []

for _ in range(int(input())):
    cmd = list(input().split())

    if cmd[0] == "L":
        if stack_frt: stack_bck.append(stack_frt.pop())
            
    elif cmd[0] == "D":
        if stack_bck: stack_frt.append(stack_bck.pop())
            
    elif cmd[0] == "B":
        if stack_frt: stack_frt.pop()
            
    else:
        stack_frt.append(cmd[1])

print(''.join(stack_frt) + ''.join(stack_bck)[::-1])