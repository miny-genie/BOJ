# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BinarySearch(lectures, disk, min_time, max_time):
    answer = 0
    
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        
        total, count = 0, 1
        for lecture in lectures:
            if mid < lecture:
                count = disk + 1
                break
            
            if total + lecture <= mid:
                total += lecture
            else:
                total = lecture
                count += 1
                
        if count > disk:
            min_time = mid + 1
        else:
            max_time = mid - 1
            answer = mid
        
    return answer

# ---------- Main ----------
_, disk = map(int, input().split())
lectures = list(map(int, input().split()))

answer = BinarySearch(lectures, disk, 1, sum(lectures))
print(answer)