# ---------- Import ----------
from math import ceil, floor
import sys
input = sys.stdin.readline


# ---------- Function ----------
def magic_sqaure_base(num):
    lst = [[0] * num for _ in range(num)]
    half = num // 2
    
    for r in range(0, num, half):
        for c in range(0, num, half):
            if c == 0:
                for i in range(half):
                    for j in range(half):
                        # 제 2사분면
                        if r == 0:
                            if c + j < floor(num / 4):
                                lst[r+i][c+j] = 3
                            else:
                                lst[r+i][c+j] = 0
                                
                        # 제 3사분면
                        else:
                            if c + j < floor(num / 4):
                                lst[r+i][c+j] = 0
                            else:
                                lst[r+i][c+j] = 3
                                
            else:
                for i in range(half):
                    for j in range(half):
                        # 제 1사분면
                        if r == 0:
                            if j < ceil(num / 4) + 1:
                                lst[r+i][c+j] = 2
                            else:
                                lst[r+i][c+j] = 1
                                
                        # 제 4사분면
                        else:
                            if j < ceil(num / 4) + 1:
                                lst[r+i][c+j] = 1
                            else:
                                lst[r+i][c+j] = 2
    
    mid = floor(num/4)
    lst[mid][0], lst[mid][mid] = lst[mid][mid], lst[mid][0]
    lst[half + mid][0], lst[half + mid][mid] = lst[half + mid][mid], lst[half + mid][0]
    
    return lst


def check_UPDN(lst, y, N):
    if 0 <= y < N:
        for i in range(N):
            if lst[i][y] == 0:
                return i, y
    else:
        return False


def check_LFTRGT(lst, x, N):
    if 0 <= x < N:
        for i in range(N):
            if lst[x][i] == 0:
                return x, i
    else:
        return False


def odd_magic_square(num: int) -> list:
    sqaure = [[0] * num for _ in range(num)]
    
    mid = num // 2
    current = 1
    
    x = num - 1
    y = mid
    
    sqaure[x][y] = current
    current += 1
    
    for _ in range(num**2 - 1):
        x += 1
        y += 1
        
        if x < 0 or x >= num or y < 0 or y >= num:
            if value := check_UPDN(sqaure, y, num):
                x, y = value[0], value[1]
                sqaure[x][y] = current
                current += 1
                continue
            elif value := check_LFTRGT(sqaure, x, num):
                x, y = value[0], value[1]
                sqaure[x][y] = current
                current += 1
                continue
            else:
                x -= 2
                y -= 1
                sqaure[x][y] = current
                current += 1
                continue
        
        elif 0 <= x < num and 0 <= y < num and sqaure[x][y] == 0:
            sqaure[x][y] = current
            current += 1
            continue
        
        elif 0 <= x < num and 0 <= y < num and sqaure[x][y]:
            x -= 2
            y -= 1
            sqaure[x][y] = current
            current += 1
            continue
            
    return sqaure


def even_magic_square(num: int) -> list:
    def mul_4(num: int) -> list:
        sqaure = [[0] * num for _ in range(num)]
        isExist = set()
        KEY = num // 4
        
        isOK = [[0] * num for _ in range(num)]
        for r in range(0, num, KEY):
            for c in range(0, num, KEY):
                if r == c or r + c == num - KEY:
                    for i in range(KEY):
                        for j in range(KEY):
                            isOK[r+i][c+j] = 1

        current = 0
        for r in range(num):
            for c in range(num):
                current += 1
                if isOK[r][c]:
                    sqaure[r][c] = current
                    isExist.add(current)
        
        all = set([i for i in range(1, num**2+1)])
        all -= isExist

        for r in range(num-1, -1, -1):
            for c in range(num-1, -1, -1):
                if sqaure[r][c] == 0:
                    sqaure[r][c] = all.pop()
        
        return sqaure
    
    
    def not_mul_4(num: int) -> list:
        using_value = odd_magic_square(num // 2)
        base = magic_sqaure_base(num)
        
        half = num // 2
        for x in range(0, num, half):
            for y in range(0, num, half):
                for i in range(half):
                    for j in range(half):
                        base[x+i][y+j] = base[x+i][y+j] * (num * num // 4) + using_value[i][j]
        
        return base
    
    
    if num % 4 == 0:
        return mul_4(num)
    else:
        return not_mul_4(num)


# ---------- Main ----------
N = int(input())

if N % 2 == 0:
    answer = even_magic_square(N)
else:
    answer = odd_magic_square(N)
    
for line in answer:
    print(*line)