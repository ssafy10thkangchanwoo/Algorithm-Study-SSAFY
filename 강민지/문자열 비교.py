T = int(input())
for tc in range(1, T+1):
    pattern = input()  # 패턴
    str1 = input()  # 확인할 문자열
    M = len(str1)
    N = len(pattern)  # 확인할 구간 길이

    ans = 0  # 문자열 일치하는지 여부

    for i in range(M):
        for j in range(i, i+N):  # 패턴의 첫 시작인덱스 0 -> i+N-1까지 가능
            if pattern[j] != str1[i]:
                break  # 문자열의 다음 글자부터 다시 확인

