# 문자열 비교

# text안에 pattern이 있냐?
# 있으면 1, 없으면 0 출력

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    pattern = input() # 찾는 것
    text = input() # 문자열

    ti = pi = 0 # 패턴, text의 idx

    answer = 1

    while ti < len(text) and pi < len(pattern):

        if text[ti] == pattern[pi]:
            ti += 1
            pi += 1
        
        else:
            ti = ti - pi + 1
            pi = 0
    if pi == len(pattern):
        answer = 1
    else:
        answer = 0
    
    print(f'#{tc} {answer}')
                        