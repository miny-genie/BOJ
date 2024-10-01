from sys import stdin
input = stdin.readline


def compute_decrypt_case(cipher_text: str) -> int:
    if cipher_text[0] == "0":
        return 0
    
    dp = [1] * (len(cipher_text) + 1)
    bef_num = "9"
    
    for idx, cur_num in enumerate(cipher_text, 1):
        dp[idx] = dp[idx-1]
        
        if bef_num + cur_num == "00":
            return 0
        elif cur_num == "0" and bef_num >= "3":
            return 0
        elif cur_num == "0" and bef_num <= "2":
            dp[idx] = dp[idx-2]
        elif 10 <= int(bef_num + cur_num) <= 26:
            dp[idx] = (dp[idx] + dp[idx-2]) % 1_000_000
        
        bef_num = cur_num
        
    return dp[-1]


cipher_text = input().rstrip()
plain_text_case = compute_decrypt_case(cipher_text)
print(plain_text_case)
