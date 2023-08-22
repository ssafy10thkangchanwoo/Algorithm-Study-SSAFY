def binarySearch(P, key):  # key: 찾으려는 페이지
    start = 1  # 시작 페이지
    end = P  # 마지막 페이지 = 책 전체 페이지
    cnt = 1  # 탐색 횟수 기본값은 1

    while start <= end:  # 시작 페이지가 마지막까지 가면 탐색 끝
        mid = (start + end) // 2

        if mid == key:  # 중간 페이지가 찾으려는 페이지 일 때
            return cnt  # 탐색 횟수 반환

        elif mid > key:  # 중간 페이지가 찾으려는 페이지보다 클 때
            end = mid  # 마지막 페이지 값 갱신
            cnt += 1
        
        else:  # 중간 페이지가 찾으려는 페이지보다 작을 때
            start = mid  # 시작 페이지 값 갱신
            cnt += 1

    return cnt
            

T = int(input())
for tc in range(1, T+1):
    # P: 전체 책 페이지
    # A: A가 찾아야할 페이지
    # B: B가 찾아야할 페이지
    P, A, B = map(int, input().split())

    Pa = binarySearch(P, A)
    Pb = binarySearch(P, B)
    ans = 0

    if Pa > Pb:
        ans = 'B'
    elif Pa < Pb:
        ans = 'A'
    else:
        ans = 0

    print(f'#{tc} {ans}')