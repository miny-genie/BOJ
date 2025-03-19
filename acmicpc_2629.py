from sys import stdin
input = stdin.readline

MAX_WEIGHT = 40_000


def knapsack_2d() -> str:
    # dp[i][w]: i번째 추까지 고려했을 때, 무게 w를 만들 수 있는지 여부
    dp = [[False] * (MAX_WEIGHT + 1) for _ in range(weight_count + 1)]
    dp[0][0] = True
    
    for i in range(1, weight_count + 1):
        weight = weights[i - 1]
        
        for w in range(MAX_WEIGHT + 1):
            if dp[i-1][w]:
                if weight + w <= MAX_WEIGHT:
                    dp[i][weight + w] = True
                dp[i][abs(weight - w)] = True
                dp[i][w] = True
    
    return ' '.join("Y" if dp[-1][bead] else "N" for bead in beads)


weight_count = int(input())
weights = list(map(int, input().split()))
bead_count = int(input())
beads = list(map(int, input().split()))

result = knapsack_2d()
print(result)
