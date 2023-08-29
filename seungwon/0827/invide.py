t = int(input())

for tc in range(1,t+1):

    n =  int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1,n-1):
        for j in range(i+1, n):

            for k in range()