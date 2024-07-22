from sys import stdin
input = stdin.readline

part_people = int(input())
t_shirts = list(map(int, input().split()))
shirt_potion, pen_potion = map(int, input().split())

count = 0
for t_shirt in t_shirts:
    div, mod = divmod(t_shirt, shirt_potion)
    count += div
    if mod:
        count += 1
print(count)

print(*divmod(part_people, pen_potion))