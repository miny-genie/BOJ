# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(start, end, N):
    visited = [0] * (N+1)
    visited[start] = 1
    
    Q = deque([(start, 0)])
    while Q:
        person, how_long = Q.popleft()
        
        if person == end:
            return how_long
        
        for other in family_tree[person]:
            if not visited[other]:
                Q.append((other, how_long+1))
                visited[other] = 1
                
    return -1
        
# ---------- Main ----------
people = int(input())
person1, person2 = map(int, input().split())
family_tree = [[] for _ in range(people+1)]

for _ in range(int(input())):
    parent, child = map(int, input().split())
    family_tree[parent].append(child)
    family_tree[child].append(parent)
    
how_long = BFS(person1, person2, people)
print(how_long)