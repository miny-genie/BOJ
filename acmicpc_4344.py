# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Fcuntion ----------
def roundTraditional(val, digits):
    return round(val + 10**(-len(str(val)) - 1), digits)

# ---------- Main ----------
T = int(input())

for _ in range(T):
    tmp = list(map(int, input().split()))
    people = tmp[0]
    scores = tmp[1:]
    
    avg = sum(scores) / people
    
    isOver = 0
    for score in scores:
        if score > avg:
            isOver += 1
    
    result = isOver / people * 100
    print(f'{roundTraditional(result, 3):.3f}%')
    
# ---------- Comment ----------
# for k in [*open(0)][1:]:N,*l =map(int,k.split());print(f"{sum(i*N>sum(l)for i in l)/N+9**-9:.3%}")

# 일반적인 반올림 코드 문제는 IEEE 754에 따라 오사오입 반올림 방식을 사용힌디.
# 그리고 C, C++, Python의 반올림 함수들은 오사오입 방식으로 계산한다.
# 하지만 이 문제는 사사오입 방식으로 채점을 진행한다.
# 함수를 만들어 사사오입을 구현하든가, 일정 수를 더해서 구현하든가 해야한다...

# https://www.acmicpc.net/board/view/120014
# https://www.acmicpc.net/board/view/119920
# https://www.acmicpc.net/board/view/99713