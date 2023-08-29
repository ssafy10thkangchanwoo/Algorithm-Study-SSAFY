t = int(input())
for tc in range(1,t+1):
    n = int(input())
    RCL = [list(map(int, input().split())) for _ in range(n)]
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    max_sum = 0
    for r in range(n):
        for c in range(n):
            here_sum = RCL[r][c]
            for k in range(4):
                for l in range(1,n):
                    nr = r + dr[k] * l
                    nc = c + dc[k] * l
                    if 0<= nr < n and 0<= nc <n :
                        here_sum += RCL[nr][nc]
            if max_sum < here_sum :
                max_sum = here_sum
    print(f"#{tc} {max_sum}")0