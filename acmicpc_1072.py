# ---------- Import ----------
import sys
input = sys.stdin.readline


# ---------- Function ----------
def BinarySearch(game, win):
    cur_win_rate = int(win * 100 / (game))
    
    if cur_win_rate >= 99:
        return -1
    
    LFT = 0
    RGT = int(1e9)
    answer = None
    
    while LFT <= RGT:
        mid = (LFT + RGT) // 2
        chg_win_rate = int((win + mid) * 100 / (game + mid))
        
        if cur_win_rate != chg_win_rate:
            RGT = mid - 1
            
        else:
            LFT = mid + 1
            answer = LFT
    
    return answer


# ---------- Main ----------
game, win = map(int, input().split())

answer = BinarySearch(game, win)
print(answer)