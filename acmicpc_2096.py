from sys import stdin
input = stdin.readline

line_count = int(input())
first_line = list(map(int, input().split()))
max_fir, max_sec, max_thi = first_line
min_fir, min_sec, min_thi = first_line

for _ in range(line_count - 1):
    fir, sec, thi = list(map(int, input().split()))
    max_fir, max_sec, max_thi, min_fir, min_sec, min_thi = (
        fir + max(max_fir, max_sec),
        sec + max(max_fir, max_sec, max_thi),
        thi + max(max_sec, max_thi),
        fir + min(min_fir, min_sec),
        sec + min(min_fir, min_sec, min_thi),
        thi + min(min_sec, min_thi)
    )    

max_ans = max(max_fir, max_sec, max_thi)
min_ans = min(min_fir, min_sec, min_thi)
print(max_ans, min_ans)