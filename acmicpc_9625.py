from sys import stdin
input = stdin.readline

count_a, count_b = [1], [0]
for _ in range(change_count := int(input())):
    count_a.append(count_b[-1])
    count_b.append(count_a[-2] + count_b[-1])

print(count_a[-1], count_b[-1])