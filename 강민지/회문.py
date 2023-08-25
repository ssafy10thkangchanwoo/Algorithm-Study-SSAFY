def palindrome(word):
    l = len(word)
    # 주어진 글자의 절반까지가 나머지 절반과 같은지 확인
    for w in range(l//2):  # 절반만 반복하면 됨
        if word[w] != word[l-w-1]:  # w가 커질수록 작아지도록
            return 0
        
    return 1  # 글자 다 확인해서 일치함


T = int(input())
for tc in range(1, T+1):
    # N: 글자판 크기, M: 회문 길이
    N, M = map(int, input().split())
    string = [list(input()) for _ in range(N)]
    ans = ''  # 회문인 문자열(정답)

    # 행 우선 조회하면서 회문 조회할 문자열(가로) 만들기
    for r in range(N):
        for c in range(N-M+1):  # 회문이 갈 수 있는 범위: N -> N-M
            check_r = ''  # 행과 열이 바뀌면 초기화
            
            for k in range(M):  # 회문의 길이만큼 글자 모으기 위해서
                check_r += string[r][c+k]  # 열 기준점이 바뀔때마다 M개 만큼

            if palindrome(check_r):  # 회문일 경우
                ans = check_r
    

    # 열 우선 조회하면서 회문 조회할 문자열(세로) 만들기
    for c in range(N):
        for r in range(N-M+1):
            check_c = ''

            for k in range(M):
                check_c += string[r+k][c]

            if palindrome(check_c):
                ans = check_c

    print(f'#{tc} {ans}')