from sys import stdin
input = stdin.readline


class Manacher:
    def __init__(self, string: str):
        self.original = string
        self.string = self.preprocessing(string)
        self.longest_palindrome = 0
        self.find_longest_palindrome()
    
    def preprocessing(self, string: str) -> str:
        return "^_" + '_'.join(string) + "_$"
    
    def find_longest_palindrome(self):
        length = len(self.string)
        radius = [0] * length
        center = right_boundary = 0
        
        for idx in range(1, length-1):
            mirror_idx = 2 * center - idx
            
            # minimize redundant calculation
            if idx < right_boundary:
                radius[idx] = min(right_boundary - idx, radius[mirror_idx])
            
            # compare left side and right side based on idx
            while self.string[idx-radius[idx]-1] == self.string[idx+radius[idx]+1]:
                radius[idx] += 1
            
            # current idx's palindrome over right boundary 
            if idx + radius[idx] > right_boundary:
                center = idx
                right_boundary = idx + radius[idx]
        
        max_length, _ = max((n, i) for i, n in enumerate(radius))
        self.longest_palindrome = max_length 


manacher = Manacher(input().rstrip())
print(manacher.longest_palindrome)