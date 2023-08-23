# 숫자카드
# 가장 많은 카드에 적힌 숫자, 그 카드가 몇 장인지? 
# => 카운팅 배열을 만들어서
# 0~9까지 각각 숫자 카운트하고 최대 카운트 몇 ?
# 카운팅 배열에서 가장 많은 숫자의 인덱스 ==> 가장 많은 카드에 적힌 숫자


# 카운팅 정렬 : 카운팅정렬의 인덱스, cnt+1

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input()))

    # 카운팅 배열 만들기
    c = [0]* 10 


    # 각 숫자 카운트 + 최대 카운트
    max_cnt = 0
    for i in range(n): # arr배열(input값) 탐색
        c[arr[i]] += 1
        max_cnt = c[arr[i]] if max_cnt < c[arr[i]] else max_cnt
    # print(c) # 중간확인용
    

    # 인덱스 구하기
    idx = 0
    for j in range(10): # 카운팅 배열 탐색
        if max_cnt == c[j]:
            idx = j


    print(f'#{tc} {idx} {max_cnt}')
    