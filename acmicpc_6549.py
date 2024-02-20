# ---------- Import ----------
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def solution(heights: list) -> int:    
    max_area = 0
    stack = []      
    
    for cur_idx, cur_height in enumerate(heights + [0]):        
        if stack and cur_height < stack[END][HEIGHT]:
            while stack and cur_height < stack[END][HEIGHT]:
                _, bef_height = stack.pop()                 # pop in stack
                bef_idx = 0
                if stack: bef_idx = stack[END][IDX] + 1     # DESC exception
                area = (cur_idx - bef_idx) * bef_height     # calculating area
                max_area = max(max_area, area)              # which is biggest
            
        if not stack or stack[END][HEIGHT] <= cur_height:
            stack.append((cur_idx, cur_height))
            
    return max_area

# ---------- Main ----------
END, IDX, HEIGHT = -1, 0, 1    # key word init

while True:
    histogram = list(map(int, input().split()))
    if histogram == [0]: break
    
    answer = solution(histogram[1:])    # first num is length
    print(answer)