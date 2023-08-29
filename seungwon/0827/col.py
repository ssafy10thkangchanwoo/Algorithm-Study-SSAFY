t = int(input())
for tc in range(1,t+1):
    sr,sc,le,he = map(int, input().split())
    visited = [[0]*10 for _ in range(10)]
    num = 1
    for c in range(sc,le+sc):
        for r in range(sr,he+sr):
           visited[r][c] += num
           num+=1

    print(f"#{tc}")
    for i in range(10):
        print(*visited[i])


'''
1
3 4 3 4
5 2 1 5
2 3 4 6

'''