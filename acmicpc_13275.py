from sys import stdin
input = stdin.readline


class Manacher:
    def __init__(self, text: str) -> None:
        self.original = text
        self.processed_text = self.preprocessing(text)
        self.longest_palindrome = self.find_longest_palindrome()
    
    def preprocessing(self, text: str) -> str:
        return "^_" + '_'.join(text) + "_$"
    
    def find_longest_palindrome(self) -> None:
        length = len(self.processed_text)
        radius = [0] * length
        center = right_boundary = 0
        
        for idx in range(1, length-1):
            # minimize redundant calculation
            if idx < right_boundary:
                mirror_idx = 2 * center - idx
                radius[idx] = min(right_boundary-idx, radius[mirror_idx])
            
            # compare left and right, based on idx
            while self.processed_text[idx-radius[idx]-1] == self.processed_text[idx+radius[idx]+1]:
                radius[idx] += 1
            
            # current idx's palindrome over right boundary
            if idx + radius[idx] > right_boundary:
                center = idx
                right_boundary = idx + radius[idx]
        
        max_length, center_idx = max((n, i) for i, n in enumerate(radius))
        start = (center_idx - max_length) // 2
        return self.original[start : start+max_length]


manacher = Manacher(input().rstrip())
print(len(manacher.longest_palindrome))