# 구간합

T = int(input())
for tc in range(1, T+1):
    n,m = map(int,input().split())
    arr = list(map(int, input().split()))

    # 구간 몇개 ? / 구간 안에 숫자 몇개? / 구간내 숫자합 구해서 최대최소 비교

    max_v = 0
    min_v = 10000 * m # 한 숫자당 10000이하이니까, 구간합은?

    for i in range(n-m+1):
        total = 0
        for j in range(m):
            total += arr[i+j] # i는 구간에서 시작위치 / j는 구간내의 숫자를 도는 것

        max_v = total if max_v < total else max_v
        min_v = total if min_v > total else min_v 
    
    print(f'#{tc} {max_v-min_v}')
