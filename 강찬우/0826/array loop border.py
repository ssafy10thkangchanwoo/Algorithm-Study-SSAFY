T = int(input())

for tc in range(1, T+1):

    arr = [[0]*10 for _ in range(10)]

    r, c, k = map(int,input().split())

    for i in range(k):
        arr[r+i][c] = 1
        arr[r][c+i] = 1
        arr[r+k-1][c+i] = 1
        arr[r+i][c+k-1] = 1
    print(f'#{tc}')
    for j in range(10):
        print(*arr[j])
        