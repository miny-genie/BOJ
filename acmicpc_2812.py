from sys import stdin
input = stdin.readline


def compute_smallest_number(number: str, remove_count: int) -> str:
    END = chr(ord("9") + 1)
    stack = []
    
    for digit, num in enumerate(number + END):
        if not stack:
            stack.append(num)
        else:
            while stack and stack[-1] < num:
                stack.pop()
                remove_count -= 1
                if remove_count == 0:
                    return ''.join(stack) + ''.join(number[digit:])
                    
            stack.append(num)


digits, remove_count = map(int, input().split())
number = input().rstrip()
smallest_number = compute_smallest_number(number, remove_count)
print(smallest_number)