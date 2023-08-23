for tc in range(1,11):
    # 100, 100 의 배열 생성
    n = 100
    ladder = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    dr = [-1,0,0]
    dc = [0,1,-1]
    for c in range(n):
        if ladder[99][c]== 2:
            ec = c
            print(ec)

    #방문했는지 확인하기 위한 visited 행렬 만들기
            d = 0
            r,c = 99, ec
            while r>0:
                if d == 0:
                    #왼쪽으로 갈 수 있을때
                    if c>0 and ladder[r][c-1]:
                        d= 2
                    # 오른쪽으로 갈 수 있을때
                    elif c < 99 and ladder[r][c+1]:
                        d= 1
                else: # 좌 우 방향으로 움직이고 있다면
                    # 위로 올라갈 수 있으면
                    if ladder[r-1][c]:
                        d = 0
                #다음 위치에서 위치를 탐색해야하니
                r += dr[d]
                c += dc[d]

                if ladder[0][c] == 1:
                    result = c
                    break


    print(f"#{tc} {result}")