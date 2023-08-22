T = 10
for tc in range(1, T+1):
    dump = int(input())
    box = list(map(int, input().split()))

    # 최대 높이/최저 높이의 위치 찾기
    max_idx = min_idx = 0

    for 