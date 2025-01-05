from sys import stdin, setrecursionlimit
setrecursionlimit(1_000_000)
input = stdin.readline

COPS_1_INIT_IDX = X = 0
COPS_2_INIT_IDX = Y = 1
INIT = -1
EVENT_LEN = 1000 + 2 # maximum event count(1000) + initial cops pos(2)


def move_cost(s_event_idx: int, e_event_idx: int) -> int:
    x_diff = abs(events[s_event_idx][X] - events[e_event_idx][X])
    y_diff = abs(events[s_event_idx][Y] - events[e_event_idx][Y])
    return x_diff + y_diff


def min_total_dist(cops1_idx: int, cops2_idx: int) -> int:
    # Already processing
    if dp[cops1_idx][cops2_idx] != INIT:
        return dp[cops1_idx][cops2_idx]
    
    nxt_event_idx = max(cops1_idx, cops2_idx) + 1
    
    # None of the following events
    if nxt_event_idx == event_count + 2:
        return 0
    
    # Calculate cops 1 time cost(assigned and move)
    cops1_assigned = min_total_dist(nxt_event_idx, cops2_idx)
    cops1_move = move_cost(cops1_idx, nxt_event_idx)
    cops1_time = cops1_assigned + cops1_move
    
    # Calculate cops 2 time cost(assigned and move)
    cops2_assigned = min_total_dist(cops1_idx, nxt_event_idx)
    cops2_move = move_cost(cops2_idx, nxt_event_idx)
    cops2_time = cops2_assigned + cops2_move
    
    # Compare
    if cops1_time < cops2_time:
        dp_trace[cops1_idx][cops2_idx] = 1
        dp[cops1_idx][cops2_idx] = cops1_time
    else:
        dp_trace[cops1_idx][cops2_idx] = 2
        dp[cops1_idx][cops2_idx] = cops2_time
    
    return dp[cops1_idx][cops2_idx]


def trace_assignment(cops1_idx: int, cops2_idx: int) -> list[int]:
    trace = []
    for i in range(2, event_count + 2):
        assigned = dp_trace[cops1_idx][cops2_idx]
        trace.append(assigned)
        if assigned == 1:
            cops1_idx = i
        else:
            cops2_idx = i
    return trace


n = int(input())
event_count = int(input())
events = [[1, 1], [n, n]]
events.extend([list(map(int, input().split()))for _ in range(event_count)])

dp = [[INIT] * EVENT_LEN for _ in range(EVENT_LEN)]
dp_trace = [[INIT] * EVENT_LEN for _ in range(EVENT_LEN)]

total_dist = min_total_dist(COPS_1_INIT_IDX, COPS_2_INIT_IDX)
print(total_dist)

trace = trace_assignment(COPS_1_INIT_IDX, COPS_2_INIT_IDX)
print(*trace, sep="\n")

# 25.01.05
# Platinum 1: 2167 > 2169 (+2pts)
# 승급까지 -33 > -31