from collections import deque
from sys import stdin
input = stdin.readline


def rotate_saw(diff_state: list, bias: int, weight: int = 1) -> None:
    if bias >= 3:
        weight = -1
        bias -= 2
         
    for dir, diff in enumerate(diff_state):
        if not diff: break
        if dir % 2: sawtooth[weight*dir+bias].rotate(spin)
        else: sawtooth[weight*dir+bias].rotate(-spin)
        

sawtooth = [deque(map(int, input().rstrip())) for _ in range(4)]

for _ in range(int(input())):
    # index 2 - 3'clock, # index 6 - 9'clock
    fir_sec = sawtooth[0][2] ^ sawtooth[1][6]
    sec_thi = sawtooth[1][2] ^ sawtooth[2][6]
    thi_for = sawtooth[2][2] ^ sawtooth[3][6]
    diff_state = [fir_sec, sec_thi, thi_for]
    
    # input and rotate own saw
    saw, spin = map(int, input().split())
    sawtooth[saw-1].rotate(spin)

    if saw == 2:
        if fir_sec: sawtooth[0].rotate(-spin)
        diff_state = [sec_thi, thi_for]
 
    elif saw == 3:
        if thi_for: sawtooth[3].rotate(-spin)
        diff_state = [sec_thi, fir_sec]

    elif saw == 4:
        diff_state = diff_state[::-1]
        
    rotate_saw(diff_state, saw)
           
# Calculate score 
ans, scores = 0, [1, 2, 4, 8]
for score, saw in zip(scores, sawtooth):
    ans += score * saw[0]
    
print(ans)