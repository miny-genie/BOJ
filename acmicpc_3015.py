from sys import stdin
input = stdin.readline

LAST, HEIGHT, SCORE = -1, 0, 1


def solution(heights: list) -> int:
    stack = []
    answer = 0
    
    for height in heights:
        while stack and stack[LAST][HEIGHT] < height:
            answer += stack.pop()[SCORE]
            
        # stack is empty
        if not stack:
            stack.append([height, 1])
            continue
        
        # maintain DESC state, except same elements
        if stack[LAST][HEIGHT] == height:
            answer += stack[LAST][SCORE]
            stack[LAST][SCORE] += 1
            
            # Existing left person taller than current height 
            if len(stack) > 1: answer += 1
          
        # unless all condition
        else:
            stack.append([height, 1])
            answer += 1
    
    return answer


heights = [int(input()) for _ in range(int(input()))]
answer = solution(heights)
print(answer)