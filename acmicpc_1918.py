from sys import stdin
input = stdin.readline

OPEN_BRACKET = "("
CLOSE_BRACKET = ")"


def generate_postfix(infix: str) -> str:
    postfix = []
    stack = []
    priority = {"(":0, ")":0, "+":1, "-":1, "*":2, "/":2}
    
    for char in infix:
        if char.isalpha():
            postfix.append(char)
            
        elif char is OPEN_BRACKET:
            stack.append(char)
        
        elif char is CLOSE_BRACKET:
            while stack[-1] is not OPEN_BRACKET:
                postfix.append(stack.pop())
            stack.pop()
        
        else:   # operators
            while stack and priority[char] <= priority[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char)            
    
    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


infix_expression = input().rstrip()
postfix = generate_postfix(infix_expression)
print(postfix)