# 회문

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,M  = map(int, input().split()) # matrix n*n / 패턴 길이가 m
    matrix = [list(input()) for _ in range(N)]


    answer = ''
    
    # 행 우선
    for r in range(N):
        for c in range(N-M+1):  # 회문 검사 자릿수 계산
            word_row = ''
            for k in range(M): # 회문 길이만큼 text입력
                word_row += matrix[r][c+k]
            
            rotate = 1
            for v in range(M//2):
                if word_row[v] != word_row[M-1-v]:  # 다르면 회문 아님!
                    rotate = 0
                    break
            else:   # break 작동 안된 것들은 회문임!
                rotate = 1
                answer = word_row
                
    # 열 우선
    for c in range(N):
        for r in range(N-M+1):
            word_col = ''
            for k in range(M):
                word_col += matrix[r+k][c]
            
            rotate = 1
            for v in range(M//2):
                if word_col[v] != word_col[M-1-v]:
                    rotate = 0
                    break
            else:
                rotate = 1
                answer = word_col
    
    print(f'#{tc} {answer}')