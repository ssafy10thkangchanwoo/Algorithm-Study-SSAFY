# sum
# 행의 합, 열의 합, 대각선 합 중 max값

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    int(input())

    matrix = [list(map(int,input().split())) for _ in range(100)]

    # 각 행, 열, 대각선 max값들 출력
    max_r = 0
    max_c = 0
    max_d1 = 0
    max_d2 = 0

    for r in range(100):
        tot_r = 0
        tot_c = 0
        max_d1 += matrix[r][r]
        max_d2 += matrix[r][99-r]

        for c in range(100):
            tot_r += matrix[r][c] 
            tot_c += matrix[c][r]
        max_r = tot_r if max_r < tot_r else max_r
        max_c = tot_c if max_c < tot_c else max_c

    # 오름차순 정렬 => 가장 마지막 인덱스가 가장 크다.
    result = [max_r,max_c, max_d1,max_d2]
    result.sort()

    print(f'#{tc} {result[-1]}')
    # print(f'#{tc} {max(result)}')
    
    
        