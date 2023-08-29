t = int(input())
for tc in range(1,t+1):
    n = int(input())
    num_list = list(map(int,input().split()))
    min_minus = 9999

    for i in range(1,n-1):
        sum_result = 9999
        for j in range(i+1,n):
            moeum = []
            sum_1,sum_2,sum_3 = sum(num_list[0:i]), sum(num_list[i:j]), sum(num_list[j:])
            moeum.append(sum_1)
            moeum.append(sum_2)
            moeum.append(sum_3)
            sort_num = sorted(moeum)
            result = sort_num[2] - sort_num[0]

            if min_minus > result :
                min_minus = result
    print(f"#{tc} {min_minus}")


'''
1
5
2 6 8 5 -8
5
-2 -2 -5 -8 5
6
1 -5 7 -6 8 3
10
7 -5 -2 0 6 4 9 8 1 -7
'''