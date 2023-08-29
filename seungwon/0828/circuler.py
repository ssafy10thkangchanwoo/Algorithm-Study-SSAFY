for tc in range(1,3):
    # 회문의 길이
    n = int(input())
    # 보드 판의 크기
    board = [list(input()) for _ in range(8)]
    # 보드판의 행과 열 탐색
    cnt = 0
    # 탐색하는 위치만큼 구간으로 나누기, 파리잡기처럼 상자가 움직이게
    for r in range(8):
        for c in range(8-n+1):
            # 보드판안에서 움직일 단어상자
            row_word = ""
            col_word = ""
            for i in range(n):
                # 행 우선 탐색
                row_word += board[r][c+i]
                # 열 우선탐색
                col_word += board[c+i][r]
            # c의 위치가 변하기 전에 현재 자리에서 조건을 만족하는 것 탐색
            for w in range(len(row_word)//2):
                # 인덱스 자리와 인덱스
                if row_word[w] != row_word[-w-1]:
                    break
            else:
                cnt+=1
            for w in range(len(col_word)//2):
                if col_word[w] != col_word[-w-1]:
                    break
            else:
                cnt+=1

    print(f"#{tc} {cnt}")