from sys import stdin
input = stdin.readline


def generate_down_numbers(down_numbers: list, curr: list) -> list:
    for num in range(10):
        if not curr or curr[-1] > str(num):
            curr.append(str(num))
            generate_down_numbers(down_numbers, curr)
            curr.pop()
        else:
            down_numbers.append(''.join(curr))
            return
    return sorted(map(int, down_numbers))


idx = int(input())
down_numbers = generate_down_numbers([], [])
print(down_numbers[idx] if idx < len(down_numbers) else -1)