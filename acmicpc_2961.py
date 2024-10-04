from sys import stdin
input = stdin.readline


def compute_min_diff(sour_grades: list, bitter_grades: list) -> int:
    ingredient_count = len(sour_grades)
    max_num = 2 ** ingredient_count - 1
    bit_length = len(bin(max_num)[2:])
    min_diff = float('inf')
    
    for i in range(1, max_num+1):
        sour_diff = 1
        bitt_diff = 0
        for idx, digit in enumerate(map(int, bin(i)[2:].zfill(bit_length))):
            if digit:
                sour_diff *= sour_grades[idx]
                bitt_diff += bitter_grades[idx]
        min_diff = min(min_diff, abs(sour_diff - bitt_diff))
        
    return min_diff


sour_grades, bitter_grades = [], []
for _ in range(int(input())):
    sour, bitter = map(int, input().split())
    sour_grades.append(sour)
    bitter_grades.append(bitter)

min_diff = compute_min_diff(sour_grades, bitter_grades)
print(min_diff)