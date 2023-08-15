# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BinarySearch(lst, budget):
    # Budget is enough
    if sum(lst) <= budget:
        return max(lst)
    
    # Init
    result = 0
    left, right = 0, max(lst)
    
    # do binary search
    while left <= right:
        total = 0
        mid = (left + right) // 2
        
        # calcuating sub budget
        for city in lst:
            total += min(city, mid)
            
        # End condition) sub budget is same the budget
        if total == budget: return mid
        
        elif total > budget:
            right = mid - 1
            result = right      # need min value
            
        else: left = mid + 1
            
    return result

# ---------- Main ----------
_ = int(input())
quest = list(map(int, input().split()))
budget = int(input())

result = BinarySearch(quest, budget)
print(result)