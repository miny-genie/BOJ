from sys import stdin
input = stdin.readline


# LPS(Longest Prefix Suffix): 부분 일치 테이블
def compute_lps(word: str) -> list:
    word_length = len(word)
    lps = [0] * word_length
    length = 0
    i = 1
    
    while i < word_length:
        if word[i] == word[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text: str, pattern: str) -> list:
    text_length = len(text)
    pattern_length = len(pattern)
    lps = compute_lps(pattern)
    
    search_list = []
    text_idx, pattern_idx = 0, 0
    
    while text_idx < text_length:
        if pattern[pattern_idx] == text[text_idx]:
            text_idx += 1
            pattern_idx += 1
            
        if pattern_idx == pattern_length:
            search_list.append(text_idx - pattern_idx + 1)    # 1-based index
            pattern_idx = lps[pattern_idx - 1]
        elif text_idx < text_length and pattern[pattern_idx] != text[text_idx]:
            if pattern_idx:
                pattern_idx = lps[pattern_idx - 1]
            else:
                text_idx += 1
        
    return search_list


text = input().rstrip()
pattern = input().rstrip()
locations = kmp_search(text, pattern)
print(len(locations))
print(*locations)