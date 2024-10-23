n = int(input())
house = sorted(map(int, input().split()))
print(house[(n - 1) // 2])
