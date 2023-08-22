T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 정수 개수
    numbers = list(map(int, input().split()))
    
    for i in range(10):  # 정렬은 10개까지만
        # 최댓값, 최솟값의 위치 찾기
        max_idx = min_idx = i

        # 짝수 자리는 큰 수부터 내림차순
        if i % 2 == 0:
            for j in range(i+1, N):
                if numbers[max_idx] < numbers[j]:
                    max_idx = j  # 최대값 위치 갱신
            # numbers 안의 최대값 찾은 후 자리 배치 (맨 앞으로)
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

        # 홀수 자리는 작은 수부터 오름차순
        else:
            for j in range(i+1, N):
                if numbers[min_idx] > numbers[j]:
                    min_idx = j  # 최소값 위치 갱신

            #numbers 안의 최솟값 찾은 후 자리 배치
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    print(f'#{tc}', end = ' ')

    # 10개까지만 뽑아내야 해서
    for _ in range(10):
        print(numbers[_], end = ' ')
    print()