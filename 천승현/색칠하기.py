T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(0, N)]
    color = [[0] * 10 for _ in range(0, 10)]
    
    
    for r in range(arr[0][1], arr[0][3]-1):
        for c in range(arr[0][2], arr[0][4]-1):
            color[r][c] = 1
    
    cnt = 0
    for i in range(1, N):
        for r in range(arr[i][1], arr[i][3]-1):
            for c in range(arr[i][2], arr[i][4]-1):
                if color[r][c] == 1:
                    cnt = cnt + 1
    
    # cnt = 0
    # for r in range(arr[1][1], arr[1][3]-1):
    #     for c in range(arr[1][2], arr[1][4]-1):
    #         if color[r][c] == 1:
    #             cnt = cnt + 1
    
    print(f"#{tc} {cnt}")
    # cnt = 0
    # for r in range(0, 10):
    #     for c in range(0, 10):
    #         if color[r][c] == 2:
    #             cnt = cnt + 1