from sys import stdin
input = stdin.readline

# CENTER(0), UP(1), LFT(2), DN(3), RGT(4)
def move(start: int, end: int) -> int:
    if start == end: return 1
    elif start == 0: return 2
    elif abs(start-end) == 2: return 4
    else: return 3


def DDR(cmds: list) -> int:
    # dp[i][lft][rgt]
    # i-th번쨰에 (lft, rgt)로 발을 뒀을 때 드는 최소 힘
    dp = [
        [[float('inf') for _ in range(5)] for _ in range(5)]
        for _ in range(len(cmds))
    ]
    dp[0][0][0] = 0
    
    cmds.pop()
    for idx, cmd in enumerate(cmds):
        for lft in range(5):
            for rgt in range(5):
                cur_cost = dp[idx][lft][rgt]
                
                dp[idx+1][cmd][rgt] = min(
                    dp[idx+1][cmd][rgt],
                    cur_cost + move(lft, cmd)
                )
                
                dp[idx+1][lft][cmd] = min(
                    dp[idx+1][lft][cmd],
                    cur_cost + move(rgt, cmd)
                )
                
    return min(map(min, dp[-1]))


commands = list(map(int, input().split()))
minimum_power = DDR(commands)
print(minimum_power)