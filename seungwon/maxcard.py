t = int(input())
for tc in range(1,t+1):
    # 첫줄에 주어지는 카드 장수
    n = int(input())
    # 띄어쓰기 없이 주어진 숫자들
    ai = list(map(int,input()))
    # 숫자를 세어줄 인접 리스트
    # ai 중에서 가장 큰수만큼 만들면 되는데 0자리가 포함되므로 +1 만큼
    cnt = [0] * (max(ai)+1)
    # ai 에 들어있는 리스트 중에서 숫자를 카운드 해줘야하니까
    for i in range(len(ai)):
        # ai 의 i 번째 리스트에 있는 숫자가 cnt에 있는지 확인
        # cnt[] 의 ai[i]의 값을 늘려주겠다.
        cnt[ai[i]] += 1

    max_card = 0
    max_cnt = 0
    for i in range(len(cnt)):
        # i의 값이 1부터 증가하므로 인덱스의 값이 더 크다면 최댓값을 바꾸어줘라
        # 그럼 가장 만많이 세어준 값도 인덱스 값으로 바꾸어줘러
        if cnt[i]>=max_cnt:
            max_cnt = cnt[i]
            max_card = i

    print(f"#{tc} {max_card} {max_cnt}")