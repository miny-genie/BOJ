from sys import stdin
input = stdin.readline


def compute_six_digit_numbers(graph: list[list[str]]) -> int:
    def dfs(x: int, y: int, nums: list, depth: int) -> None:
        if depth == 6:
            six_digit_numbers.add(''.join(nums))
            return
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = dx + x
            ny = dy + y
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            
            nums.append(graph[nx][ny])
            dfs(nx, ny, nums, depth + 1)
            nums.pop()
        
    six_digit_numbers = set()
    
    for row in range(5):
        for col in range(5):
            cur = [graph[row][col]]
            dfs(row, col, cur, 1)
    
    return len(six_digit_numbers)


graph = [list(map(str, input().split())) for _ in range(5)]
six_digit_numbers = compute_six_digit_numbers(graph)
print(six_digit_numbers)
