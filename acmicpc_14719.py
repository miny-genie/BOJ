from sys import stdin
input = stdin.readline


def fill_horizontal(block_width: int, heights: list[int]) -> int:
    stack = []
    water = 0
    curr_idx = 0
    
    while curr_idx < block_width:
        while stack and heights[stack[-1]] < heights[curr_idx]:
            top = stack.pop()
            if not stack:
                break
            
            distance = curr_idx - stack[-1] - 1
            height = min(heights[stack[-1]], heights[curr_idx]) - heights[top]
            water += distance * height
        
        stack.append(curr_idx)
        curr_idx += 1
    
    return water


def fill_vertical(block_width: int, heights: list[int]) -> int:
    left_max = [0] * block_width
    left_max[0] = heights[0]
    for i in range(1, block_width):
        left_max[i] = max(left_max[i - 1], heights[i])
    
    right_max = [0] * block_width
    right_max[-1] = heights[-1]
    for i in range(block_width - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])
    
    return sum(
        max(0, min(left_max[i], right_max[i]) - heights[i])
        for i in range(block_width)
    )


_, block_width = map(int, input().split())
heights = list(map(int, input().split()))

water = fill_vertical(block_width, heights)
print(water)