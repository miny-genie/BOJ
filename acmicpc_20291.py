import sys
input = sys.stdin.readline

extension = dict()
for _ in range(int(input())):
    fn, ex = input().rstrip().split('.')
    extension[ex] = extension.get(ex, 0) + 1
    
for ex, cnt in sorted(extension.items()):
    print(ex, cnt)