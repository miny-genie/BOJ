from sys import stdin
input = stdin.readline


def generate_triangle_nums() -> list:
    ret = []
    n = 1
    while True:
        triangle_num = (n * (n+1)) // 2
        if triangle_num > 1000:
            break
        ret.append(triangle_num)
        n += 1        
    return ret


def is_triangle_sum(num: int) -> int:
    triangle_nums = generate_triangle_nums()
    for fir in triangle_nums:
        for sec in triangle_nums:
            for thi in triangle_nums:
                if fir + sec + thi == num:
                    return 1
    return 0


for _ in range(int(input())):
    num = int(input())
    print(is_triangle_sum(num))