from collections import defaultdict
from sys import stdin
input = stdin.readline

INFO = 0
ALGR_CNT, ABLTY = 0, 1
ALGR_KNW = 1


def get_ability(left: tuple, right: tuple) -> int:
    return students[right][INFO][ABLTY] - students[left][INFO][ABLTY]


student_count, algorithm_count, max_diff = map(int, input().split())
students = [
    (list(map(int, input().split())), list(map(int, input().split())))
    for _ in range(student_count)
]
students.sort(key=lambda stu: (stu[INFO][ABLTY]))

answer = left = right = 0
algr_dict = defaultdict(int)

while right < student_count:
    for algr in students[right][ALGR_KNW]:
        algr_dict[algr] += 1
    
    right += 1
    while left < right and get_ability(left, right-1) > max_diff:
        for algr in students[left][ALGR_KNW]:
            algr_dict[algr] -= 1
            if not algr_dict[algr]:
                del algr_dict[algr]
        left += 1
    
    member = right - left
    all_knw_algr = list(algr_dict.values()).count(member)
    efficiency = (len(algr_dict) - all_knw_algr) * member
    answer = max(answer, efficiency)

print(answer)

# 25.01.27
# Platinum 1: 2189 > 2189 (+0pts)
# 승급까지 -11 > -11 