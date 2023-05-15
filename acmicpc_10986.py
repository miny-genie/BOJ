# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, M = map(int, input().split())
lst = list(map(int, input().split()))
remainder = [0] * M

sum = 0
for i in lst:
    sum += i
    remainder[sum % M] += 1

result = remainder[0]
for i in remainder:
    result += i * (i-1) // 2

print(result)

# ---------- Comment ----------
# L8 M의 나머지는 M보다 작기 때문에 *M 초기화
# L12 누적합 계산
# L13 누적합 M으로 나눈 나머지 개수 세기
# L15 0인 값들은 어떻게 더하든 나머지가 0, 따라서 remainder[0]로 초기화
# L17 같은 나머지를 갖는 누적합(A-B) 구간이라면 0인 값을 가짐