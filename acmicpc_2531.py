from sys import stdin
input = stdin.readline


def sushi_belt(n: int, d: int, k: int, c: int, sushi: list) -> int:
    # Sliding window에서 초밥 종류를 카운트할 list
    sushi_count = [0] * (d + 1)
    
    # 처음 k개의 초밥을 윈도우에 포함
    current_variety = 0
    for i in range(k):
        if sushi_count[sushi[i]] == 0:
            current_variety += 1
        sushi_count[sushi[i]] += 1
    
    # 쿠폰으로 제공하는 초밥을 포함하여 최대 종류 초기화
    max_variety = current_variety
    if sushi_count[c] == 0:
        max_variety += 1
    
    # Sliding window를 통해 최대 초밥 가짓수 탐색
    for i in range(1, n):
        # 이전 접시 제거
        prev_sushi = sushi[i - 1]
        sushi_count[prev_sushi] -= 1
        if sushi_count[prev_sushi] == 0:
            current_variety -= 1
        
        # 다음 접시 추가
        next_sushi = sushi[(i + k - 1) % n]
        if sushi_count[next_sushi] == 0:
            current_variety += 1
        sushi_count[next_sushi] += 1
        
        # 쿠폰 초밥이 없다면 추가 가능
        current_max_variety = current_variety
        if sushi_count[c] == 0:
            current_max_variety += 1
        
        # 최대 가짓수 갱신
        max_variety = max(max_variety, current_max_variety)        
    
    return max_variety


n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

print(sushi_belt(n, d, k, c, sushi))
