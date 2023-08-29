T = int(input())
for tc in range(1, T+1):
    # N: 부분집합 내의 원소 개수
    # K: 부분집합의 원소들의 합
    N, K = map(int, input().split())

    A = [_ for _ in range(1, 13)]  # 집합 A

    # 집합 A의 모든 부분집합 만들기
    for i in range(len(A)):
        