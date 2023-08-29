# 가장빠른 문자열 타이핑
t = int(input())
for tc in range(1,t+1):
    a,b = map(str,input().split())
    # 패턴이 나온 횟수 조회
    pattern = 0
    a_search = 0
    b_search = 0
    # 전체 문자열을 다 돌아보기 전까지는 반복하겠다.
    while a_search<len(a) :
        # a의 인덱스와 b의 인덱스의 값이 같다면
        if a[a_search] == b[b_search]:
            #인덱스 값을 증가시켜줘라!
            a_search += 1
            b_search += 1
            # 만약 패턴이 만들어졌다면
            if b_search == len(b):
                # 패턴 횟수를 증가시켜주고 b인덱스를 초기화해줘라
                pattern += 1
                b_search = 0
        # a인덱스값과 b의 인덱스 값이 같지 않다면
        else:
            # 이전위치의 +1인덱스에서 다시 탐색을 이어가라
            a_search = a_search- b_search +1
            b_search = 0
    #이제 카운트 값이 다 정해졋으면 값을 구해라
    #전체 길이에서 패턴이 나온 횟수의 길이를 빼주고 카운트 된 횟수를 더해줘라
    ans = len(a) - len(b)*pattern + pattern
    print(f"#{tc} {ans}")

