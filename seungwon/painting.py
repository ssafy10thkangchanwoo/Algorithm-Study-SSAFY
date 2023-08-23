t = int(input())
for tc in range(1,t+1):
    # 칠할 영역의 개수 n. 상자를 몇개 만들어줄거냐
    n = int(input())
    #10*10의 정방형 구조 2차원 배열을 생성.
    board = [[0] * 10 for _ in range(10)]
    # n의 값이 색칠을 해야하는 영역의 개수를 나타내므로 반복문을 써준다
    for i in range(n):
        # 시작 행열 값과 끝 행렬값 그리고 색깔이 정해진다.
        r1, c1, r2, c2, color = map(int, input().split())
        # 상자의 크기를 색칠하도록 포문 작성
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                # 보드에 color의 값을 추가해준다.
                board[r][c] += color
   # 색칠이 끝난후에 보드판에서 보라색으로 색칠된 범위를 세어주어라
    cnt = 0  
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                cnt += 1

    #결과 값 출력.
    print(f"#{tc} {cnt}")