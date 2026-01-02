from heapq import heappop, heappush
from sys import stdin
input = stdin.readline


def print10(nums: list[int]) -> None:
    print(
        '\n'.join(
            ' '.join(map(str, nums[i : i+10]))
            for i in range(0, len(nums), 10)
        )
    )


for _ in range(int(input())):
    n = int(input())
    f = lambda n: -(-n // 10)   # lambda n: n // 10 + bool(n % 10)
    nums = sum((list(map(int, input().split())) for _ in range(f(n))), [])

    max_queue = []  # 중앙값보다 작은 원소들
    min_queue = []  # 중앙값보다 크거나 같은 원소들
    answer = []     # 정답 모아놓는 리스트
    
    for idx, num in enumerate(nums, 1):
        # 최소힙 기준으로 동작
        if idx % 2 == 0:
            heappush(max_queue, num * -1)
        else:
            heappush(min_queue, num)
        
        # 균형잡기
        if max_queue and min_queue[0] < max_queue[0] * -1:
            max_top = heappop(max_queue) * -1
            min_top = heappop(min_queue)
            heappush(max_queue, min_top * -1)
            heappush(min_queue, max_top)
        
        # 홀수번째만 중앙값 확인
        if idx % 2:
            answer.append(min_queue[0])
    
    print(len(answer))
    print10(answer)

# 2026.01.02 해결
# Diamond Ⅴ 2213 > 2213
# 승급까지 87 > 87