def binarySearch(P, key):  # key: 찾으려는 페이지
    start = 1
    end = P
    cnt = 1  # 탐색 횟수 기본값은 1

    while start == end:
        mid = (start + end) // 2

        if mid == key:  # 중간 페이지가 찾으려는 페이지 일 때
            return cnt  # 탐색 횟수 반환

        elif mid > key:  # 중간이 찾으려는 페이지보다 클 때
            

T = int(input())
for tc in range(1, T+1):
    # P: 전체 책 페이지
    # A: A가 찾아야할 페이지
    # B: B가 찾아야할 페이지
    P, A, B = map(int, input().split())

    Pa = binarySearch(P, A)
    Pb = binarySearch(P, B)

    print(f'#{tc} {}')