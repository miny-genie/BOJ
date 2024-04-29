from sys import stdin
input = stdin.readline


def min_palindrome_cuts(text):
    n = len(text)
    is_palindrome = [[False] * n for _ in range(n)]
    dp = [0] * n
    
    for i in range(n):
        # single character
        is_palindrome[i][i] = True
        
        # two consecutive characters are the same
        if i < n-1 and text[i] == text[i+1]:
            is_palindrome[i][i+1] = True
    
    # find all palindrome
    for length in range(3, n+1):
        for sIdx in range(n-length+1):
            eIdx = sIdx + length - 1
            if text[sIdx] == text[eIdx] and is_palindrome[sIdx+1][eIdx-1]:
                is_palindrome[sIdx][eIdx] = True
    
    for cur_idx in range(n):
        # to check text[:i] is palindrome
        if is_palindrome[0][cur_idx]:
            dp[cur_idx] = 1
            
        else:
            dp[cur_idx] = float('inf')
            for frt_idx in range(1, cur_idx+1):
                if is_palindrome[frt_idx][cur_idx]:
                    dp[cur_idx] = min(dp[cur_idx], dp[frt_idx-1] + 1)
    
    return dp[-1]


text = input().rstrip()
answer = min_palindrome_cuts(text)
print(answer)