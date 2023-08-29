t = int(input())

for tc in range(1,t+1):
    #땅의 크기 n
    n = int(input())
    #땅의 배열
    arr = [list(map(int,input().split())) for _ in range(n)]

    min_result = 9999
    #땅에서 움직일 범위 설정
    for r in range(1,n):
        for c in range(1,n):

            temp_1 = 0
            for r_1 in range(0,r):
                for c_1 in range(0,c):
                    temp_1 += arr[r_1][c_1]
            temp_2 = 0
            for r_2 in range(r,n):
                for c_2 in range(0,c):
                    temp_2 += arr[r_2][c_2]
            temp_3 = 0
            for r_3 in range(0,n):
                for c_3 in  range(c,n):
                    temp_3 += arr[r_3][c_3]
            result = [temp_1,temp_2,temp_3]
            max_cnt = max(result)
            min_cnt = min(result)

            result = max_cnt - min_cnt
            if min_result >result :
                min_result = result
    print(f"#{tc} {min_result}")

