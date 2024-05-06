from sys import stdin
input = stdin.readline


def digit_one_count(num):  
    cnt = 0  
    bin_num = bin(num)[2:]  
    length = len(bin_num)  
    
    for i in range(length):  
        if bin_num[i] == '1':  
            val = length-i-1  
            cnt += dp[val] + (num - 2**val + 1)
            num = num - 2 ** val 
             
    return cnt  


x, y = map(int, input().split())  
dp = [0 for _ in range(60)]

for i in range(1, 60):  
    dp[i] = 2**(i-1) + 2 * dp[i-1]  

print(digit_one_count(y) - digit_one_count(x-1))