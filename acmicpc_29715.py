# ---------- Import ----------
import sys
input = sys.stdin.readline


# ---------- Function ----------
def nPm(n, m):
    answer = 1
    for _ in range(m):
        answer *= n
        n -= 1
        
    return answer


def cal_time(p, it, wt):
    if p % 3:
        return (p * it) + (p // 3 * wt)
    else:
        return (p * it) + ((p // 3 - 1) * wt)


# ---------- Main ----------
pw_length, remember = map(int, input().split())
pw_input_time, wrong_time = map(int, input().split())
cards = [i for i in range(1, 10)]

if not remember:
    possible = nPm(len(cards), pw_length)
    print(cal_time(possible, pw_input_time, wrong_time))
    
else:
    need_num = []
    
    for _ in range(remember):
        isNotZero, num = map(int, input().split())
        
        if isNotZero:
            cards.remove(num)
            pw_length -= 1
            
        else:
            cards.remove(num)
            need_num.append(num)
            
    if not need_num:
        possible = nPm(len(cards), pw_length)
        print(cal_time(possible, pw_input_time, wrong_time))
        
    else:
        condition_1 = nPm(pw_length, len(need_num))
        condition_2 = nPm(len(cards), pw_length-len(need_num))
        possible = condition_1 * condition_2
        
        print(cal_time(possible, pw_input_time, wrong_time))