from sys import stdin
input = stdin.readline


def play_music(song_count: int, start_volume: int, max_volume: int, volumes: list) -> int:
    dp = [[False] * (max_volume + 1) for _ in range(song_count + 1)]
    dp[0][start_volume] = True
    
    for cur_idx, cur_vol in enumerate(volumes, 1):
        bef_idx = cur_idx - 1
        mixing_volume = False
        for bef_vol in range(max_volume + 1):
            if dp[bef_idx][bef_vol]:
                if bef_vol + cur_vol <= max_volume:
                    dp[cur_idx][bef_vol + cur_vol] = True
                    mixing_volume = True
                    
                if bef_vol - cur_vol >= 0:
                    dp[cur_idx][bef_vol - cur_vol] = True
                    mixing_volume = True
                
        if not mixing_volume:
            return -1
    
    for idx, volume in enumerate(reversed(dp[-1])):
        if volume:
            return max_volume - idx


song_count, start_volume, max_volume = map(int, input().split())
volumes = list(map(int, input().split()))
last_volume = play_music(song_count, start_volume, max_volume, volumes)
print(last_volume)
