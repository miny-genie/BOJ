# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Bottom_Up(N: int, lst: list) -> int:
    dp = [0 for _ in range(N+1)]

    for i in range(N):
        for j in range(i+lst[i][0], N+1):
            if dp[j] < dp[i] + lst[i][1]:
                dp[j] = dp[i] + lst[i][1]

    return dp[-1]


def Top_Down(N: int, lst: list) -> int:
    dp = [0 for _ in range(N+1)]

    for i in range(N-1, -1, -1):
        if i + lst[i][0] > N:
            dp[i] = dp[i+1]

        else:
            dp[i] = max(dp[i+1], lst[i][1]+dp[i+lst[i][0]])

    return dp[0]

# ---------- Main ----------
day = int(input())

clinic = []
for _ in range(day):
    T, P = map(int, input().split())
    clinic.append([T, P])

result = Bottom_Up(day, clinic)
# result = Top_Down(day, clinic)

print(result)