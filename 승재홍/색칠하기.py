# 색칠하기

# 도화지에서 빨간영역 칠하고, 파란영역 칠하기
# 겹치진 부분 보라색 + 1

# 깨달은 점 : input 값을 활용해서 할 수 있다. 

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    # 도화지 생성
    matrix = [[0]* 10 for _ in range(10)]

    # 보라 영역
    purple_area = 0

    # 색칠 영역 표시
    for _ in range(N):
        r1,c1,r2,c2,color = map(int, input().split())

        for r in range(r1,r2+1):
            for c in range(c1,c2+1):

                # 빨강, 파랑 색칠하기
                if color == 1:
                    matrix[r][c] += 1
                elif color == 2:
                    matrix[r][c] += 2

                # 보라 영역 표시
                if matrix[r][c] == 3:
                    purple_area += 1


    print(f'#{tc} {purple_area}')

    # print(matrix)
    # 이게 왜 될까? : '같은 색인 영역은 겹치지 않는다.' 라는 조건 때문
    # if 같은 색의 영역이 겹친다면? 
    # => 색이 안칠해져 있으면, 칠한다.
    # => 색이 칠해져 있으면 또 칠해야한 보라색 영역이다.
    # if matrix[r][c] == 0:
    #   matrix[r][c] = color
    # else:
    #   purple_area += 1
