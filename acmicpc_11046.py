from sys import stdin
input = stdin.readline


class Manacher:
    def __init__(self, _input: list):
        self.processed = self.preprocessing(_input)
        self.radius = self.compute_palindrome_radius()
    
    def preprocessing(self, _input: list):
        tmp = ["_"] * (len(_input) * 2 + 1)
        tmp[1::2] = _input
        return tmp
    
    def compute_palindrome_radius(self):
        length = len(self.processed)
        radius = [0] * length
        center = right_boundary = -1
        
        for idx in range(length-1):
            if idx <= right_boundary:
                mirror_idx = 2 * center - idx
                radius[idx] = min(right_boundary - idx, radius[mirror_idx])
            
            while idx + radius[idx] + 1 < length and\
            self.processed[idx-radius[idx]-1] == self.processed[idx+radius[idx]+1]:
                radius[idx] += 1
            
            if idx + radius[idx] > right_boundary:
                center = idx
                right_boundary = idx + radius[idx]
                
        return radius


_ = int(input())
nums = input().rstrip().split()
manacher = Manacher(nums)

for _ in range(int(input())):
    left, right = map(int, input().split())
    print(0 + (right - left <= manacher.radius[left + right - 1]))