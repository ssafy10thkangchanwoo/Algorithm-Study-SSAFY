t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    max_cnt = 0
    for r in range(n):
        for c in range(n):
            sum_cnt = 0
            for lr in range(r,m+r):
                for lc in range(c,m+c):
                    if 0<=lr<n and 0<=lc <n:
                        sum_cnt += board[lr][lc]

            if max_cnt<sum_cnt:
                max_cnt = sum_cnt

    print(f"#{tc} {max_cnt}")