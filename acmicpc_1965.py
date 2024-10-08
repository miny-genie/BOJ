from sys import stdin
input = stdin.readline


def compute_max_stack_box(box_count: int, box_sizes: list[int]) -> int:
    dp = [1] * box_count
    for cur in range(1, box_count):
        for bef in range(cur):
            if box_sizes[cur] > box_sizes[bef]:
                dp[cur] = max(dp[cur], dp[bef] + 1)
    return max(dp)


box_count = int(input())
box_sizes = list(map(int, input().split()))
max_stack = compute_max_stack_box(box_count, box_sizes)
print(max_stack)