import heapq
from heapq import heapify, heappop, heappush
from sys import stdin
input = stdin.readline

FIRST, WEIGHT, VALUE = 0, 0, 1


def find_max_price(jewels: heapq, bags: list) -> int:
    heapify(jewels)
    max_price, temp = 0, []    
    for bag in bags:
        while jewels and bag >= jewels[FIRST][WEIGHT]:
            heappush(temp, -heappop(jewels)[VALUE])
        if temp:
            max_price -= heappop(temp)
    return max_price


jewel_count, bag_count = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(jewel_count)]
bags = sorted(int(input()) for _ in range(bag_count))

max_price = find_max_price(jewels, bags)
print(max_price)