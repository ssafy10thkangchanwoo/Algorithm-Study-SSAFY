T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 카드 장수
    card = list(map(int, input()))
 
    count = [0] * 10  # 카드 0~9번 몇 장인지 세기 위한 카운팅 배열
 
    for i in range(N):
        # 카운트배열의 인덱스는 카드의 번호
        count[card[i]] += 1
 
    # 카운트 배열에서 가장 높은 숫자 찾기
    max_idx = 0  # 카운트배열의 0번 인덱스가 가장 크다고 가정
    for c in range(1, 10):  # 카운트배열의 1번 인덱스부터 9번 인덱스까지
        if count[max_idx] <= count[c]:  # 장수 같을 경우 숫자 큰 걸 출력하므로 (뒤의 인덱스값이 더 큰 숫자카드)
            max_idx = c  # 값 갱신
 
    print(f'#{tc} {max_idx} {count[max_idx]}')