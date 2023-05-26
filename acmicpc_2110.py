# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def binarySearch(lst: list, start: int, end: int) -> int:
    result = 0
    
    while start <= end:
        mid = (start + end) // 2    # distance
        current = lst[0]
        count = 1

        for i in range(1, len(lst)):
            if lst[i] >= current + mid:
                count += 1
                current = lst[i]

        # Router is enough, reducing distance
        if count >= C:
            start = mid + 1
            result = mid

        # Router is not enough, increasing distance
        else:
            end = mid - 1

    return result

# ---------- Main ----------
N, C = map(int, input().split())

houses = [int(input().rstrip()) for _ in range(N)]
houses.sort()

end = houses[-1] - houses[0]
result = binarySearch(houses, 1, end)
print(result)

# ---------- Comment ----------
# L22에서 result = mid를 하지 않고서
# result 선언 없이 마지막에 return mid를 하면 오답이다.

# start = end(마지막에)일 때, while문을 한 번 더 돌고 else 분기문으로 빠져나가면
# mid값이 result보다 커질 수 있기 때문이다.

# L22를 지운 코드에 대한 반례 예시)
# N, C = (10, 6)
# houses = [2, 6, 22, 13, 94, 15, 465, 30, 21, 97]