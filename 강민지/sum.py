T = 10
for tc in range(1, T+1):
    int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_v = 0

    for r in range(100):
        sum_r = 0  # 각 행의 합(행 바뀌면 초기화)
        for c in range(100):
            sum_r += arr[r][c]

        if max_v < sum_r:
            max_v = sum_r


    for c in range(100):
        sum_c = 0  # 각 열의 합(열 바뀌면 초기화)
        for r in range(100):
            sum_c += arr[r][c]
        
        if max_v < sum_c:
            max_v = sum_c


    # 대각선의 합
    sum_dia1 = sum_dia2 = 0

    for r in range(100):
        for c in range(100):
            if r == c:
                sum_dia1 = arr[r][c]
            
            if r + c == 99:
                sum_dia2 = arr[r][c]
       
    if max_v < sum_dia1:
        max_v = sum_dia1
    if max_v < sum_dia2:
        max_v = sum_dia2

    print(f'#{tc} {max_v}')