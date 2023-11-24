# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
goals = [list(input().rstrip()) for _ in range(int(input()))]
goal_dict = dict()

for goal in goals:
    team = goal[0]
    time = int(''.join(goal[2:4])) * 60 + int(''.join(goal[5:]))
    goal_dict[time] = team

win_team, score = "", 0
situation = [0, 0]

for i in range(48 * 60):
    if i in goal_dict:
        win_team = goal_dict[i]
        
        if win_team == "1": score += 1
        elif win_team == "2": score -= 1
        
    if score > 0: situation[0] += 1
    elif score < 0: situation[1] += 1
        
print(str(situation[0]//60).zfill(2) + ":" + str(situation[0]%60).zfill(2))
print(str(situation[1]//60).zfill(2) + ":" + str(situation[1]%60).zfill(2))