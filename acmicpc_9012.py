# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def isVPS(isvps: list):
    stack = []

    if isvps[0] == ")":
        return True

    for i in isvps:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return True    # '(' 없이 ')' 만 추가하는 것은 결국 NO

    return stack

# ---------- Main ----------
T = int(input())

for _ in range(T):
    str = list(input().rstrip())
    
    remainder = isVPS(str)
            
    if remainder:
        print("NO")
    else:
        print("YES")
        
# ---------- Comment ----------
# 만약 ) 로 시작한다면 무조건 NO
# 왜냐하면 예제에서 ())(()를 NO로 출력했고, 그말은 )(를 VPS로 보지 않는다는 것