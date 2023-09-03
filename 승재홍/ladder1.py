# ladder1
# 시작점 -> 도착점

# 도착점 지정
def end_point():
    for c in range(100):
        if matrix[99][c] == 2:
            return 99,c


import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1,11):
    int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]

    # 동서북
    dr = [0,0,-1]
    dc = [1,-1,0]

    # 도착점부터 거슬러 올라감
    r,c = end_point()

    # 첫 행(시작점)에 도착할 때까지 반복
    while r > 0:
        # 좌,우,북 3방향 탐색
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]
            # 새롭게 탐색한 위치가 유효하고, 길이 있으면 간다. 
            if 0<= nr < 100 and 0 <= nc < 100 and matrix[nr][nc] == 1:
                r = nr
                c = nc
                matrix[r][c] = 0 # 지나온 자리 벽 표시 -> 다시 못가게 끔

    print(f'#{tc} {c}')   


   
