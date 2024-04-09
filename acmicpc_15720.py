def total():
    return sum(burgers) + sum(sides) + sum(beverages)


min_count = min(map(int, input().split()))
burgers = sorted(map(int, input().split()))
sides = sorted(map(int, input().split()))
beverages = sorted(map(int, input().split()))

print(total())

ans = sum(
    (burgers.pop() + sides.pop() + beverages.pop()) * 0.9
    for _ in range(min_count)
)
print(int(ans) + total())