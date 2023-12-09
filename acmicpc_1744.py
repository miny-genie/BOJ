# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def SUM(iterable):
    def EVEN_LENGTH_SUM(list_):
        sorted_list = sorted(list_)[::-1]
        answer = 0
        for i, num in enumerate(sorted_list):
            if not (i % 2):
                answer += num * sorted_list[i+1]
        return answer


    def ODD_LENGTH_SUM(list_):
        min_value = min(list_)
        list_.remove(min_value)
        return min_value + EVEN_LENGTH_SUM(list_)


    if len(iterable) % 2: return ODD_LENGTH_SUM(iterable)
    else: return EVEN_LENGTH_SUM(iterable)

# ---------- Main ----------
zero_count, one_count = 0, 0
pos_nums, neg_nums = [], []

for _ in range(int(input())):
    num = int(input())
    
    if not num: zero_count += 1
    elif num == 1: one_count += 1
    elif num > 0: pos_nums.append(num)
    else: neg_nums.append(num)

if not neg_nums:
    print(one_count + SUM(pos_nums))
    
elif len(neg_nums) % 2:
    max_value = max(neg_nums)
    neg_nums.remove(max(neg_nums))
    if zero_count: print(SUM(neg_nums) + one_count + SUM(pos_nums))
    else: print(max_value + SUM(neg_nums) + one_count + SUM(pos_nums))
    
else:
    print(SUM(neg_nums) + one_count + SUM(pos_nums))