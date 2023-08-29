t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    visited = [[0]*n for _ in range(n)]
    # 폭탄의 갯수만큼 반복
    all_sum = 0
    for i in range(m):
        st,ed,lenth = map(int,input().split())
        result = 0
        if visited[st][ed] == 0 :
            all_sum += arr[st][ed]
            visited[st][ed] +=1

        boom_sum = 0
        for j in range(1,lenth+1):
            for k in range(4):
                nr = st + dr[k] *j
                nc = ed + dc[k] *j
                if 0 <= nr < n and 0 <= nc <n and visited[nr][nc] !=1 :

                    boom_sum += arr[nr][nc]
                    visited[nr][nc] += 1

        all_sum += boom_sum
    print(f"#{tc} {all_sum}")

    '''
1
4 1
0 2 1 3
1 0 0 1
2 0 2 0
3 2 2 2
1 1 2
    
    '''