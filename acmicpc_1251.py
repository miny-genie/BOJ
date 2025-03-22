from sys import stdin
input = stdin.readline

word = input().rstrip()

print(
    sorted(
        word[:sep1][::-1] + word[sep1:sep2][::-1] + word[sep2:][::-1]
        for sep1 in range(1, len(word) - 1)
        for sep2 in range(sep1 + 1, len(word))
    )[0]
)