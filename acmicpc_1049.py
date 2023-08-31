# ----------Import ----------
import math
import sys
input = sys.stdin.readline

# ---------- Main ----------
guitar_line, brand = map(int, input().split())

# 가장 싼 묶음 가격, 가장 싼 개당 가격 초기화
cheapest_bundle = 1e9
cheapest_per = 1e9

# 어차피 가장 싼 묶음과 개당 가격만 필요함
for _ in range(brand):
    bundle, per = map(int, input().split())
    cheapest_bundle = min(cheapest_bundle, bundle)
    cheapest_per = min(cheapest_per, per)

# 낱개로 6개 사는 게 묶음으로 사는 것보다 싸면, 낱개로만 구매
if cheapest_bundle >= (cheapest_per * 6):
    print(cheapest_per * guitar_line)

else:
    # 번들과 낱개를 기타줄에 딱 맞게 사는 경우
    div, mod = divmod(guitar_line, 6)
    compare1 = (div * cheapest_bundle) + (mod * cheapest_per)
    
    # 번들로만 다 사는 경우(기타줄이 남을 수 있음)
    compare2 = (cheapest_bundle * math.ceil(guitar_line / 6))
    
    # 둘 중 더 작은 가격 출력
    print(min(compare1, compare2))