# ---------- Import ----------
from sys import stdin
input = stdin.readline

# ---------- Main ----------
room, playerPower = map(int, input().split())
roomInfo = [list(map(int, input().split())) for _ in range(room)]

monsters, items = [], []
for type, value in roomInfo:
    if type == 1: monsters.append(value)
    else: items.append(value)
    
monsters.sort()
items.sort(reverse=True)

clearCount = 0

for monster in monsters:
    # Player can not kill the monster
    if playerPower <= monster:
        # Training until kill the monster
        while playerPower <= monster:
            if not items:
                break
                
            playerPower *= items.pop()
            clearCount += 1
            
        else:
            playerPower += monster
            clearCount += 1
        
    # Player can kill the monster
    else:
        playerPower += monster
        clearCount += 1
        
print(clearCount + len(items))