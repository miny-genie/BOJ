from collections import deque
from sys import stdin
input = stdin.readline


def solution() -> int:
    # data structure init
    graph = [[] for _ in range(building_count+1)]
    indegree = [0 for _ in range(building_count+1)]

    # topology sort init
    for forward, backward in build_priority:
        graph[forward].append(backward)
        indegree[backward] += 1
        
    # start queue init
    queue = deque()
    dp = [0 for _ in range(building_count+1)]
    
    for i in range(1, building_count+1):
        if not indegree[i]:
            queue.append(i)
            dp[i] = build_time[i]
            
            if i == victory_building:
                return build_time[i]
            
    # do topology sort
    while queue:
        value = queue.popleft()
        
        if value == victory_building:
            return dp[value]
        
        for i in graph[value]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[value]+build_time[i])
            
            if indegree[i] == 0:
                queue.append(i)
            
            
for _ in range(caseT := int(input())):
    building_count, rule_count = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
    build_priority = [list(map(int, input().split())) for _ in range(rule_count)]
    victory_building = int(input())

    answer = solution()                
    print(answer)