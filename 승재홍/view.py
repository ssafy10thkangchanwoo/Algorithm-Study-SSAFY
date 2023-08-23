# view

# 건물 하나씩 검사
# 층 수 올라가면서 검사

import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    n = int(input())
    height = list(map(int, input().split())) # 빌딩 높이


    # 조망권
    cnt = 0

    for i in range(n):  # 빌딩 갯수 세기
        for j in range(1, height[i]+1): # 빌딩 층 수 세기
            if j > height[i-1] and j > height[i-2] and j > height[i+1] and j > height[i+2]:
                cnt += 1

    print(f'#{tc} {cnt}') 

    # 현재 i번째 건물의 층수 j
    # j층에서 양쪽 2칸을 확인한 다음 조망권이 있으면 count를 1씩 증
    # 왼쪽 -1,-2 건물의 높이 확인, 오른쪽 +1, +2 건물의 높이 확인
    # 현재 j층이 왼쪽과 오른쪽 건물의 높이보다 높아야 조망권 ok
    # 왼쪽 -1 => buildings[i-1]
    # i-2. i+1, i+2
                

    

