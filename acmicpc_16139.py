
# ------------------------------Using Python3 ------------------------------
# ---------- Import ----------
import sys, string
input = sys.stdin.readline

# ---------- Main ----------
text = input().rstrip()

tmp = {}
for i in string.ascii_lowercase:
    tmp[i] = 0
dict = {}
dict[-1] = tmp

# 초기화: 0번째 dict 요소에 0번쨰 text 글자 세기
for i, v in enumerate(text):
    dict[i] = dict[i - 1].copy()
    dict[i][text[i]] += 1
    
# 
for i in range(int(input())):
    alphabet, start, end = input().split()
    start, end = int(start), int(end)
    
    print(dict[end][alphabet] - dict[start - 1][alphabet])
    

# # ------------------------------ Using Pypy3 ------------------------------
# # ---------- Import ----------
# import sys, string
# input = sys.stdin.readline

# # ---------- Main ----------
# text = input().rstrip()
# lst = [ [0] * len(text) for _ in range(26) ]

# # 각 대응하는 알파벳 위치 초기화, ord('a') == 97
# for i in range(len(text)):
#     lst[ord(text[i]) - 97][i] += 1
    
# # 나머지 2차원 배열 누적합 연산
# for row in range(26):
#     for column in range(1, len(text)):
#         lst[row][column] += lst[row][column - 1]
        
# # 실제 연산
# for _ in range(int(input())):
#     alphabet, start, end = input().split()
#     alphabet, start, end = ord(alphabet) - 97, int(start), int(end)

#     ans = lst[alphabet][end] - lst[alphabet][start]
#     if text[start] is chr(alphabet+97): ans += 1
#     print(ans)
    
# # ---------- Comment ----------
# # end - start를 하면 end는포함하지만 start는 포함하지 않는다.
# # 띠라서 text의 start 위치와 alphabet이 같다면 1을 더해주는 것(L27)