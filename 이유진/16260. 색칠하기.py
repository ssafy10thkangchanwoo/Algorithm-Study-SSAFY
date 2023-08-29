T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    purple = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if arr[r][c] == 0:
                    arr[r][c] = color
                else:
                    purple += 1
                    
    print(f'#{tc} {purple}')