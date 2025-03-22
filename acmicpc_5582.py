from sys import stdin
input = stdin.readline


def longest_common_substring(word1: str, word2: str) -> int:
    len1, len2 = len(word1), len(word2)
    dp = [0] * (len2 + 1)
    max_len = 0
    
    for i in range(1, len1 + 1):
        for j in range(len2, 0, -1):
            if word1[i - 1] == word2[j - 1]:
                dp[j] = dp[j - 1] + 1
                max_len = max(max_len, dp[j])
            else:
                dp[j] = 0
        
    return max_len


word1 = input().rstrip()
word2 = input().rstrip()
lcs = longest_common_substring(word1, word2)
print(lcs)
