T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 양수 개수
    numbers = list(map(int, input().split()))
 
    max_idx = min_idx = 0  # 최대값/최소값의 인덱스 0으로 가정하고 시작
    max_value = min_value = 0  # 구해야 할 최대값/최소값의 값 정의
 
    # numbers의 길이인 N만큼 반복하면서 최대/최소값 찾기
    for n in range(1, N):  # 1번째 인덱스부터 N-1번째 인덱스까지
        # max_idx에 있는 값보다 n번째 인덱스에 있는 값이 더 크다면
        if numbers[max_idx] < numbers[n]:
            max_value = numbers[n]  # 최대값 갱신
            max_idx = n  # 최대값 인덱스 갱신
 
        # min_idx에 있는 값보다 n번째 인덱스에 있는 값이 더 작다면
        if numbers[min_idx] > numbers[n]:
            min_value = numbers[n]  # 최소값 갱신
            min_idx = n  # 최소값 인덱스 갱신
 
    # 최대값/최소값 찾았으면 둘의 차이 구하기
    ans = max_value - min_value
 
    print(f'#{tc} {ans}')