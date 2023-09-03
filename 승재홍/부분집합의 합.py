# 부분집합의 합

'''
3
3 6
5 15
5 10

'''

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split()) # N : 부분집합 원소 개수, # K = 부분집합 원소들의 합


    A = [i for i in range(1,13)]
    
    # 조건을 만족하는 부분집합 개수
    cnt = 0


    for i in range(1<<12): # i는 원소 12개의 모든 부분집합들 : 1 ~ 2^12
        sum_subset = 0
        subset = []

        for j in range(12): # j는 원소 개수 12만큼 반복
            if i & (1<<j):  # j번씩 차례대로 밀면서 부분집합 i(정수)에 포함된다면
                subset.append(A[j])     # 부분집합에 원소 추가
                sum_subset += A[j]      # 부분집합 원소들의 합 계산

        if len(subset) == N and sum_subset== K:
            cnt += 1
    
    print(f'#{tc} {cnt}')