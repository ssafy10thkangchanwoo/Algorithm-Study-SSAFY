T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 칠할 영역 개수
    paper = [[0] * 10 for _ in range(10)]  # 10*10 격자

    purple_cnt = 0  # 보라색이 된 영역(색이 겹친부분)의 개수

    for _ in range(N):  # 칠할 영역 개수만큼 반복해서 입력 받기
        r1, c1, r2, c2, color = map(int, input().split())

        # 주어진 영역만큼만 순회하며 색칠하기
        for r in range(r1, r2+1):  # r1 -> r2
            for c in range(c1, c2+1):  # c1 -> c2
                paper[r][c] += color

                if paper[r][c] == 3:  # 색칠된 부분의 값이 3이면 두 색깔이 칠해진 부분임
                    purple_cnt += 1

    print(f'#{tc} {purple_cnt}')
