from sys import stdin
input = stdin.readline


def solution(fruits: list) -> int:
    from collections import defaultdict
    
    fruit_count = defaultdict(int)
    left = 0
    max_length = 0
    
    for right, fruit in enumerate(fruits):
        fruit_count[fruit] += 1
        
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
            
        max_length = max(max_length, right - left + 1)
    
    return max_length


_ = int(input())
fruits = list(map(int, input().split()))
print(solution(fruits))