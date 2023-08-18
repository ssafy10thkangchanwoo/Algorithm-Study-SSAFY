# 테스트 케이스의 갯수
t = int(input())
#테스트 케이스의 갯수만큼 반복하는 반복문
for tc in range(1,t+1):
    # ai리스트에 들어가는 정수의 개수
    n = int(input())
    # 제시된 다섯개의 숫자가 들어갈 리스트
    ai = list(map(int,input().split()))
    # 문제에서 제시되어진 맥스값
    min_val = 1000000
    # ai의 갯수만큼 반복해라
    for i in range(len(ai)):
        #ai 리스트의 i번째 인덱스값이 min_val작으면
        #min_val 값을 작은값으로 바꾸어줘라
        if ai[i] < min_val:
            min_val = ai[i]
    #최댓값을 구하는 것이니 시작은 0부터
    max_val = 0

    for i in range(len(ai)):
        if ai[i]>max_val:
            max_val = ai[i]

    minus_value  = max_val - min_val
    print(f"#{tc} {minus_value}")