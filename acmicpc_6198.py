# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
buildings = [int(input()) for _ in range(N)]
stack = []

result = 0
for b in buildings:
    while stack and stack[-1] <= b:
        stack.pop()
    
    stack.append(b)
    result += len(stack) - 1
    
print(result)

# ---------- Comment ----------
# 예제 입력으로 stack의 변화를 보면 다음과 같다
# [10], [10, 3], [10, 7], [10, 7, 4], [12], [12, 2]
# 즉 입력을 돌면서 내림차순으로 stack을 초기화한다

# 이때 가장 왼쪽의 옥상은 볼 수 있는 곳이 없으니 (길이 - 1) 값을 결과에 더한다.
# [10, 3] : 10에서 3을 바라본다
# [10, 7] : 10에서 7을 바라본다
# [10, 7, 4] : 10에서 4를 바라본다, 7에서 4를 바라본다
# [12, 2] : 12에서 2를 바라본다