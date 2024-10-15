from sys import stdin
input = stdin.readline


def count_usable_way(map_size: int, runway_length: int, map_info: list) -> int:
    def rotate_90(list2D: list) -> list:
        n = len(list2D)
        ret = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                ret[c][n-1-r] = list2D[r][c]
        return ret
    
    def is_usable_line(map_size: int, runway_length: int, line: list) -> bool:
        runway = [False] * map_size
        for curr_idx, curr_height in enumerate(line):
            if curr_idx == map_size - 1 or line[curr_idx+1] == curr_height:
                continue
            elif runway[curr_idx] and curr_height + 1 == line[curr_idx+1]:
                return False
            elif abs(curr_height - line[curr_idx+1]) > 1:
                return False
            
            try:
                next_height = line[curr_idx+1]
                if curr_height > next_height:
                    for i in range(runway_length):
                        exist = runway[curr_idx + i + 1]
                        diff_height = line[curr_idx + i + 1] != next_height
                        if exist or diff_height:
                            return False
                        runway[curr_idx + i + 1] = True
                    
                elif curr_height < next_height:
                    for i in range(runway_length):
                        exist = runway[curr_idx - i]
                        diff_height = line[curr_idx - i] != curr_height
                        if exist or diff_height:
                            return False
                        runway[curr_idx - i] = True
                        
            except Exception:
                return False
        return True
    
    horizontal = sum(
        is_usable_line(map_size, runway_length, line)
        for line in map_info
    )
    vertical = sum(
        is_usable_line(map_size, runway_length, line)
        for line in rotate_90(map_info)
    )  
    return horizontal + vertical


map_size, runway_length = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(map_size)]
usable_way = count_usable_way(map_size, runway_length, map_info)
print(usable_way)
