from sys import stdin
input = stdin.readline

length = int(input())
nums = list(map(int, input().split()))

stack = [(0, nums[0])]
answer = [-1] * length

for i, num in enumerate(nums[1:], 1):
    while True:
        if not stack or stack[-1][1] >= num:
            break
        
        if stack[-1][1] < num:
            idx, _ = stack.pop()
            answer[idx] = num
        
    stack.append((i, num))
        
print(*answer)