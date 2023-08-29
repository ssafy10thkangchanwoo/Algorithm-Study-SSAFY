def electronicBus(K, N):
    next = K  # 다음에 갈 정류장 번호(최대로 갈 수 있는 거리로 설정)
    last = 0  # 마지막으로 출발한 정류장 번호 (첫 시작은 0번)
    cnt = 0  # 충전 횟수

    # 반복 횟수 모르니까 종점에 도착하기 전까지로 설정 (K의 최소는 1이므로)
    while next < N:
        if stop[next]:  # 최대 거리로 갔는데 정류장에 충전기가 있으면
            last += next  # 마지막 출발 정류장 번호 갱신
            next += K
            cnt += 1  # 충전 횟수 카운트

        # 충전기 없으면
        else:
            next -= 1  # 다음에 가야할 거리를 1 감소

            if next == last:  # 돌아오다가 마지막으로 출발한 정류장이 되면 충전기가 제대로 설치 안됐다는 뜻
                return 0

    return cnt


T = int(input())
for tc in range(1, T + 1):
    # K: 한 번에 갈 수 있는 거리
    # N: 가야 하는 거리 (= 종점)
    # M: 충전기 개수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))  # 충전기 설치된 정류장 번호 정보
    stop = [0] * N

    for c in charge:
        # 충전기 설치된 정류장 표시
        stop[c] = 1

    print(f'#{tc} {electronicBus(K, N)}')