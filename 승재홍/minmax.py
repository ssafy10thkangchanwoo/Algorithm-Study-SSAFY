T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
 
    max_v = 0
    min_v = 1000000
 
    for i in arr:
        max_v = i if max_v < i else max_v
        min_v = i if min_v > i else min_v 
     
    print(f'#{tc} {max_v-min_v}')