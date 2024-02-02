from sys import stdin
input = stdin.readline

length, target_number = map(int, input().split())
nums = list(map(int, input().split()))

end, cur_num = 0, 0
answer = 0

for start in range(length):
    while end < length and cur_num < target_number:
        cur_num += nums[end]
        end += 1
        
    if cur_num == target_number:
        answer += 1
        
    cur_num -= nums[start]
        
print(answer)