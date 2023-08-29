T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    cnt = 0  # 패턴과 일치하는 횟수
    ans = len(A)  # 가장 적은 타이핑 횟수(기본은 A 길이)

    ai = bi = 0

    while ai < len(A):
        if A[ai] == B[bi]:
            ai += 1
            bi += 1

            if bi == len(B):
                cnt += 1
                bi = 0  # A의 길이가 아직 안 끝났을 경우 뒤에 패턴 더 있는지 확인하려고
        
        else:
            ai = ai - bi + 1
            bi = 0
            

    # 글자열 모두 확인한 후
    if cnt > 0:  # 일치하는 문자열이 하나라도 있다면
        ans = len(A) - (len(B)*cnt) + cnt*1
        # cnt*1 을 하는 이유?
    
    print(f'#{tc} {ans}')