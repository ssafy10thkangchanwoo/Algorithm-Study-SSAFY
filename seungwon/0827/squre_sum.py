t = int(input())
for tc in range(1,t+1):
    #n 은 정수의 크기 m은 박수의 갯수
    n,m = map(int,input().split())
    # 박스의 합을 구해줄 배열의 상태
    arr = [list(map(int,input().split())) for _ in range(n)]
    # 다른 상자와 비교하기 위해 방문했다는걸 표시
    visited = [[0]*n for _ in range(n)]
    all_sum = 0
    # 박스의 갯수만큼 반복한다.
    for i in range(m):
        # 정사각 행렬들의 크기와 초기 값을 받아줄 것들
        s,e,l = map(int,input().split())
        # 더해지는 값들을 정해줄 것들
        sum = 0
        for r in range(s, s+l):
            for c in range(e,e+l):
                if 0<=r<n and 0<=c<n and not visited[r][c] == 1:
                    sum += arr[r][c]
                    visited[r][c] += 1
        all_sum+= sum

    print(f"#{tc} {all_sum}")




