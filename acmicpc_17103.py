# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
T = int(input())
inputs = [ int(input()) for _ in range(T) ]
max_input = max(inputs)
Prime = [0, 0] +  [1] * (max_input - 1)

# 입력받은 수 중 가장 큰 수를 기준으로 소수 구하기
for i in range(2, max_input + 1):
    if Prime[i]:
        for multiple in range(i + i, max_input + 1, i):    # i의 배수를 false로
            Prime[multiple] = 0

# 입력 받은 수의 골드바흐 파티션 구하기
for num in inputs:
    cnt = 0
    
    for i in range(2, num // 2 + 1):    # 1은 소수가 아니기에 2부터 확인
        if Prime[i] and Prime[num - i]:
            cnt += 1
            
    print(cnt)
    
# ---------- Comment ----------
# 첫 번째, 들어온 수에 대해 그때그때 소수 여부를 판별한다(시간 초과)
# 두 번째, 2부터 N까지의 모든 소수를 구한 뒤 그 숫자들로 판단한다(시간 초과)
# 세 번째, 두 번째와 방법은 같으나 소수 배열을 자신의 index 위치로 초기화한다.