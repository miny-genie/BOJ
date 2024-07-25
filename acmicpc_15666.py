from sys import stdin
input = stdin.readline


def compute_sequence(nums, sequence: list):
    if len(sequence) == pick_count:
        print(*sequence)
        sequences[tuple(sequence)] = True
        return
    
    for num in nums:
        if not sequence or sequence[-1] <= num:
            sequence.append(num)
            if tuple(sequence) not in sequences:
                compute_sequence(nums, sequence)
            sequence.pop()


num_count, pick_count = map(int, input().split())
nums = sorted(map(int, input().split()))
sequences = {}

compute_sequence(nums, [])