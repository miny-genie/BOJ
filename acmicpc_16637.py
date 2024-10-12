from sys import stdin
input = stdin.readline


def calculate_expression(num1: str|int, op: str, num2: str|int) -> int:
    if op == "+":
        return int(num1) + int(num2)
    elif op == "-":
        return int(num1) - int(num2)
    else:
        return int(num1) * int(num2)


def compute_max_result(index: int, value: int, exp: str) -> None:
    # End condition: calculated all number
    if index == expression_length - 1:
        global max_result
        max_result = max(max_result, value)
        return
    
    # Next number is not in round bracket 
    if index + 2 < expression_length:
        next_value = calculate_expression(value, exp[index+1], exp[index+2])
        compute_max_result(index+2, next_value, exp)
    
    # Next number is in round bracket 
    if index + 4 < expression_length:
        bracket_value = calculate_expression(exp[index+2], exp[index+3], exp[index+4])
        next_value = calculate_expression(value, exp[index+1], bracket_value)
        compute_max_result(index+4, next_value, exp)


expression_length = int(input())
expression = input().rstrip()

max_result = -float('inf')
compute_max_result(index=0, value=int(expression[0]), exp=expression)
print(max_result)
