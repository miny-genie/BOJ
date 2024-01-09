import sys
input = sys.stdin.readline


def Backtracking(nums, length):
    if len(answer)-1 == length:
        print(*answer[1:])
        return
    
    for num in nums:
        if not visited[num] and answer[-1] < num:
            answer.append(num)
            visited[num] = 1
            
            Backtracking(nums, length)
            
            answer.pop()
            visited[num] = 0
    
    return


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * (10000 + 1)
answer = [0]

Backtracking(nums, M)