# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def binary_search(start: int, end: int, target: int, size: int) -> int:
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, size+1):
            # 각 행마다 mid보다 작거나 같은 수를 셈
            cnt += min(mid // i, size)

        # K(target)보다 작은 수가 적을 때, 최솟값(start)를 늘림
        if target > cnt:
            start = mid + 1

        # K(target)보다 작은 수가 많거나 같을 때, 최닷값(end)를 줄임
        else:
            end = mid - 1

    # 연산 후 최솟값을 반환
    return start


# ---------- Main ----------
N = int(input())
K = int(input())

result = binary_search(1, N*N, K, N)
print(result)

# ---------- Comment ----------
# L13, min(mid // i, size)인 이유
# mid // i는 각 행마다 mid보다 작은 수의 개수이다.

# 하지만, 예를 들어 mid가 27이고 size가 3인 경우
# mid // i는 9지만, size가 3이기 때문에 최대 3개의 값만 가질 수 있다.
# 즉 주어진 길이(size)와 비교해서 더 작은 값을 세줘야 한다.