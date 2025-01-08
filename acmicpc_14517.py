from sys import stdin, setrecursionlimit
setrecursionlimit(2000)
input = stdin.readline


def count(l: int, r: int) -> int:
    if dp[l][r]:
        return dp[l][r]
    
    if l == r:
        return 1 
    elif l > r:
        return 0
     
    dp[l][r] = (count(l, r - 1) + count(l + 1, r) - count(l + 1, r - 1)) % mod
    if word[l] == word[r]:
        dp[l][r] = (1 + dp[l][r] + count(l + 1, r - 1)) % mod
    
    return dp[l][r]


word = input().rstrip()
length = len(word)

mod = 10007

dp = [[0] * length for _ in range(length)]
palindromes = count(0, length - 1)
print(palindromes)

# 25.01.08
# Platinum 1: 2170 > 2171 (+1pts)
# 승급까지 -30 > -29