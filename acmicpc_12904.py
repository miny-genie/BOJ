from sys import stdin
input = stdin.readline


def is_possible(start: str, end: str) -> bool:
    start_length = len(start)
    while start_length != len(end):
        if end[-1] == "A":
            end.pop()
        elif end[-1] == "B":
            end.pop()
            end = end[::-1]
    return start == end


start = list(input().rstrip())
end = list(input().rstrip())
print(1 if is_possible(start, end) else 0)