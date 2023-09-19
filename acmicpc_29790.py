# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
solved_count, union_level, high_level = map(int, input().split())

if solved_count >= 1000:
    if union_level >= 8000 or high_level >= 260:
        print("Very Good")
    
    else:
        print("Good")
    
else:
    print("Bad")

# condition_1 = True if solved_count >= 1000 else False
# condition_2 = True if (union_level >= 8000 or high_level >= 260) else False

# if condition_1 + condition_2 == 2:
#     print("Very Good")
    
# elif condition_1 + condition_2 == 1:
#     print("Good")
    
# else:
#     print("Bad")