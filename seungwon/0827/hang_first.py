t = int(input())

for tc in range(1, t+1):
    sr,sc,lenth = map(int,input().split())
    visited = [[0]*10 for _ in range(10)]
    num = 1
    for r in range(sr, sr+lenth):
        for c in range(sc,sc+lenth):
            visited[r][c] = num
            num += 1

    print(f"#{tc}")
    for i in range(10):

        print(*visited[i])


'''
1
3 4 3
5 5 1
2 3 4

'''
