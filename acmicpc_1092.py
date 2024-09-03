from sys import stdin
input = stdin.readline


def compute_minimum_time(cranes: list, boxes: list) -> int:
    if cranes[0] < boxes[0]:
        return -1
    
    time = 0
    while boxes:
        time += 1
        for crane in cranes:
            if boxes and crane < boxes[-1]:
                continue
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
    return time


_ = int(input())
cranes = sorted(map(int, input().split()), reverse=True)
_ = int(input())
boxes = sorted(map(int, input().split()), reverse=True)
time = compute_minimum_time(cranes, boxes)
print(time)