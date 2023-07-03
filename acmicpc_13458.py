# ---------- Import ----------
import math
import sys
input = sys.stdin.readline

# ---------- Main ----------
rooms = int(input())
people = list(map(int, input().split()))
main, sub = map(int, input().split())

result = 0
for person in people:
	if person < main:
		result += 1
		continue
	else:
		person -= main
		result += math.ceil(person/sub) + 1
		
print(result)