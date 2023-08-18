# view

# 건물 하나씩 검사
# 층 수 올라가면서 검사

import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    n = int(input())
    height = list(map(int, input().split()))


    # 조망권
    cnt = 0

    for i in range(n):  # 빌딩 갯수 세기
        for j in range(1, height[i]+1): # 빌딩 층 수 세기
            if j > height[i-1] and j > height[i-2] and j > height[i+1] and j > height[i+2]:
                cnt += 1

    print(f'#{tc} {cnt}') 
                

    

