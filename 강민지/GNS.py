T = int(input())
number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    test, lenght = input().split()
    data = list(input().split())

    print(f'#{tc}')
    for n in range(10):  # 0 ~ 9까지 순회하면서
        for d in data:  # 입력받은 데이터 값 하나씩 보기
            if d == number[n]:  # 데이터 요소 중 n번째 값과 일치할 때 출력
                print(d, end = ' ')

