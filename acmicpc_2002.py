from sys import stdin
input = stdin.readline

car_count = int(input())
inner = {input().rstrip():i for i in range(car_count)}
outer = [input().rstrip() for _ in range(car_count)]

violation = 0
for bef in range(car_count-1):
    for aft in range(bef+1, car_count):
        if inner[outer[bef]] > inner[outer[aft]]:
            violation += 1
            break

print(violation)