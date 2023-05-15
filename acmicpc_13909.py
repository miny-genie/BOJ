# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())

cnt, index = 0, 1
while True:
    if pow(index, 2) <= N:
        cnt += 1
        index += 1
    else:
        break
    
print(cnt)

# ---------- Comment ----------
# N까지의 제곱수의 개수를 세면 된다
# 제곱수는 약수의 개수가 홀수, 나머지는 약수의 개수가 짝수이다
# 짝수일 시 여닫여닫, 고로 제곱수를 헤아리는 문제