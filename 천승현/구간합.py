T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    text = list(map(int, input().split()))
    for _ in range(0, N):
        for i in range(0, N - 1):
            if text[i] > text[i+1]:
                text[i], text[i+1] = text[i+1], text[i]
    print(text)
    max_nums = 0
    min_nums = 0
    ans = 0

    for i in range(0, M):
        max_nums = max_nums + text[N-1-i]
        min_nums = min_nums + text[i]
    # for i in range(0, M):
    #     min_nums = min_nums + text[i]
    ans = max_nums - min_nums
    print(f"#{tc} {ans}")