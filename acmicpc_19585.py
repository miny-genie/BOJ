from sys import stdin
input = stdin.readline


class Trie:
    def __init__(self):
        self.trie_root = {}
    
    def insert(self, word: str):
        cur_trie = self.trie_root
        for char in word:
            char = self.hash(char)
            if char not in cur_trie:
                cur_trie[char] = {}
            cur_trie = cur_trie[char]
        cur_trie["leaf"] = True
        
    def search(self, word: str) -> bool:
        cur_trie = self.trie_root
        for idx, char in enumerate(word):
            char = self.hash(char)
            if char not in cur_trie:
                return False
            cur_trie = cur_trie[char]
            if "leaf" in cur_trie and word[idx+1:] in nicknames:
                return True
        return False
    
    
color_count, nickname_count = map(int, input().split())

trie = Trie()
for _ in range(color_count):
    color = input().rstrip()
    trie.insert(color)
    
nicknames = {input().rstrip() for _ in range(nickname_count)}
team_count = int(input())
for _ in range(team_count):
    team = input().rstrip()
    is_find = trie.search(team)
    print("Yes" if is_find else "No")