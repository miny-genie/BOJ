from math import ceil, log2
from sys import stdin
input = stdin.readline


def simulation() -> list:
    max_pow = ceil(log2(watch_time)) + 1
    sparse = [[0] * max_pow for _ in range(video_count + 1)]
    
    for video in range(1, video_count + 1):
        sparse[video][0] = recommandations[video - 1]
    
    for pow2 in range(1, max_pow):
        for video in range(1, video_count + 1):
            half = sparse[video][pow2 - 1]
            sparse[video][pow2] = sparse[half][pow2 - 1]
    
    result = []
    for video in start_videos:
        current_video = video
        remain_time = watch_time - 1
        bit_pos = 0
        while remain_time:
            if remain_time & 1:
                current_video = sparse[current_video][bit_pos]
            remain_time >>= 1
            bit_pos += 1
        result.append(current_video)
        
    return result


student_count, video_count, watch_time = map(int, input().split())
start_videos = list(map(int, input().split()))
recommandations = list(map(int, input().split()))

result = simulation()
print(*result)

# 25.01.06
# Platinum 1: 2169 > 2169 (+0pts)
# 승급까지 -31 > -31