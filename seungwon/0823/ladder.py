import sys
sys.stdin = open("input (27).txt","r")

for tc in range(1,11):
    t = int(input())
    # 100, 100 의 배열 생성
    n = 100
    ladder = [list(map(int, input().split())) for _ in range(n)]

    # 위 우 좌 순서
    dr = [0,0,-1]
    dc = [1,-1,0]
    for i in range(n):
        if ladder[99][i]== 2:
            ec = i


    sr,sc = 99, ec



    #방문했는지 확인하기 위한 visited 행렬 만들기

    while sr>0:
        for d in range(3):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0<= nr <n and 0<= nc <n and ladder[nr][nc]==1:
                ladder[sr][sc] =0
                sr = nr
                sc = nc
                break

    print(f"#{tc} {sc}")



    # if d == 0:
    #     #왼쪽으로 갈 수 있을때
    #     if c>0 and ladder[r][c-1]:
    #         d= 2
    #     # 오른쪽으로 갈 수 있을때
    #     elif c < 99 and ladder[r][c+1]:
    #         d= 1
    # else: # 좌 우 방향으로 움직이고 있다면
    #     # 위로 올라갈 수 있으면
    #     if ladder[r-1][c]:
    #         d = 0
    # #다음 위치에서 위치를 탐색해야하니
    # r += dr[d]
    # c += dc[d]
    # #d==0  위 d==1  우 d ==2 좌
    #
    # if ladder[0][c] == 1:
    #     result = c
    #     break


