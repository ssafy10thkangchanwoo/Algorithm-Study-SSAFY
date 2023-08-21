# 왜 오류가 날까...?

T = 10
for tc in range(1, T+1):
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점 찾아서 출발지점까지 거슬러 올라가기
    r = 99
    c = -1

    for i in range(100):
        if ladder[r][i] == 2:
            c = i
    
    # 사다리 탐색 방향 순서(좌우상)
    dr = [0,0,-1]
    dc = [-1,1,0]

    while r > 0:  # 출발지점 행에 도착하기 전까지 반복
    
        for d in range(3):
            # 다음 방향 탐색
            nr = r + dr[d]
            nc = c + dc[d]

            # 다음 방향이 갈 수 있는 곳인지 확인
            if 0 <= nr < 100 and 0 <= nc < 100 and ladder[nr][nc] == 1:
                r, c = nr, nc  # 위치 갱신
                ladder[r][c] = 0  # 갔던 곳 다시 안 보게 값 바꾸기
                break

    print (f'#{tc} {c}')