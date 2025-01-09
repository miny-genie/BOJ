from sys import stdin
input = stdin.readline


class SegmentTree:
    def __init__(self, size: int, n: int):
        self.size = size
        self.tree = [0] * (2 * size)
        self.current_position = {}
        self.build(n)
    
    def build(self, n: int):
        for i in range(1, n + 1):
            self.current_position[i] = n - i
            self.update(n - i, 1)
    
    def get_position(self, movie_number: int) -> int:
        return self.current_position[movie_number]
    
    def raise_position(self, movie: int, top: int):
        self.current_position[movie] = top
    
    def update(self, index: int, value: int):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index >>= 1
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]
    
    def query(self, left: int, right: int) -> int:
        left += self.size
        right += self.size
        result = 0
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left >>= 1
            right >>= 1
        return result


for _ in range(int(input())):
    movie_count, query_count = map(int, input().split())
    movies = list(map(int, input().split()))
    
    max_position = movie_count + query_count
    seg_tree = SegmentTree(max_position, movie_count)
    
    current_top = movie_count
    result = []
    
    for movie in movies:
        position = seg_tree.get_position(movie)
        above_movie = seg_tree.query(position + 1, current_top)
        result.append(above_movie)
        
        seg_tree.raise_position(movie, current_top)
        seg_tree.update(position, 0)
        seg_tree.update(current_top, 1)
        current_top += 1
    
    print(*result)

# 25.01.09
# Platinum 1: 2171 > 2174 (+3pts)
# 승급까지 -29 > -26