# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
text = input().rstrip()
FLAG = ""

# 마지막 문자 검사
if text[-1] == ">":
    FLAG = "REMOVE"

# 닫는 꺽새를 기준으로 텍스트 나누기
text = text.split(">")

# tag 온전하게 복구하기
for i in range(len(text)):
    if "<" in text[i]:
        text[i] += ">"

# split으로 마지막에 공백 여부 확인
if FLAG == "REMOVE":
    text.pop()

# 하나씩 순회하면서 뒤집을지 판단
for t in text:

    # tag라면 그대로 출력
    if t[0] == "<":
        print(t, end="")

    # tag 외에 다른 단어가 섞였다면
    else:
        new_list = t.split("<")

        # tag 분할하기
        for i in range(len(new_list)):
            if ">" in new_list[i]:
                new_list[i] = "<" + new_list[i]
            
        # 출력하기    
        for nt in new_list:
            
            # tag인지 확인하기
            if nt[0] == "<":
                print(nt, end="")
            
            # 공백 기준으로 나누기
            else:
                temp = nt.split(" ")
                
                for idx, tmp in enumerate(temp):
                    print(tmp[::-1], end="")
                    
                    # 마지막이 아니라면 공백 추가
                    if idx != (len(temp) - 1):
                        print(" ", end="")