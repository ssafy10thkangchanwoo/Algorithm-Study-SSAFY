T = int(input())
for tc in range(1, T+1):
    pattern = input()  # 패턴
    str1 = input()  # 확인할 문자열
    
    pi = si = 0  # 패턴과 문자열의 인덱스 시작 위치

    ans = 0  # 문자열 일치하는지 여부

    # 문자열 인덱스가 확인할 문자열의 끝까지 갈때까지 반복
    # 패턴도 마찬가지
    while si < len(str1) and pi < len(pattern):
        # 문자열과 패턴의 글자가 일치하면
        if str1[si] == pattern[pi]:
            # 다음 인덱스로 넘어가서 확인 반복
            si += 1
            pi += 1
        
        else:  # 글자 일치하지 않으면
            si = si - pi + 1  # 되돌아와서 그 바로 옆자리부터 다시 확인
            pi = 0  # 패턴의 0번 인덱스부터 다시 확인
    
        if pi == len(pattern):  # 패턴의 인덱스가 패턴 끝까지 갔으면 => 문자열 일치
            ans = 1
            break  # while문 반복 종료
    
    print(f'#{tc} {ans}')
