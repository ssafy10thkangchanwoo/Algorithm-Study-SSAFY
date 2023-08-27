T = int(input())

for tc in range(1, T+1):

    arr = [[0]*10 for _ in range(10)]

    r, c, k = map(int,input().split())

    for i in range(k):
        arr[r+i][c+i] = 1 ## 대각선
        arr[r+k-1-i][c+i] = 1
    print(f'#{tc}')
    for j in range(10):
        print(*arr[j])
        