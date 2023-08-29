t = int(input())
for tc in range(1,t+1):
    n = int(input())
    solve_num = list(map(int, input().split()))
    for i in range(n-2):
        for j in range(i+1,n-1):

            for k in range(j+1, n):


