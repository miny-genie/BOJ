# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def isVPS(isvps: list) -> bool:
    stack = []
    
    # Check isempty
    if not isvps:
        return False

    if isvps[0] == ")" or isvps[0] == "]":
        return True
    
    for i in isvps:
        # Case open bracket
        if i == "(" or i == "[":
            stack.append(i)

        # Case close bracket: )
        elif i == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return True
            else:
                return True
            
        # Case Close bracket: ]
        else:
            if stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return True
            else:
                return True

    return stack


# ---------- Main ----------
while (s := input().rstrip()) != ".":
    bracket = []

    for i in s:
        if i == "(" or i == ")" or i == "[" or i == "]":
            bracket.append(i)

    remainder = isVPS(bracket)

    if remainder:
        print("NO")
    else:
        print("YES")