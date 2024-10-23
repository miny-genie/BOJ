from heapq import heappop, heappush
from sys import stdin
input = stdin.readline


def compute_min_stock(my_vote: int, votes: list[int]) -> int:
    if not votes:
        return 0
    
    stock = 0
    while True:
        max_vote = -heappop(votes)
        if max_vote < my_vote:
            break
        
        else:
            stock += 1
            my_vote += 1
            max_vote -= 1
            heappush(votes, -max_vote)
        
    return stock


part_people = int(input())
my_vote = int(input())

votes = []
for _ in range(part_people - 1):
    heappush(votes, -int(input()))

min_stock = compute_min_stock(my_vote, votes)
print(min_stock)