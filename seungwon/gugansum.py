# tc의 개수를 정수로 입력받았어요
t = int(input())
# 입력받은 개수를 이용해서 tc를 반복하는 반복문을 만들어요
for tc in range(1,t+1):
    #정수의 개수  n 과 구간의 개수 m
    n,m = map(int,input().split())
    # n개의 정수들이 담겨잇는 리스트
    ai = list(map(int,input().split()))
    #최댓값과 최솟값의 범위를 확인하고 기입해줬어요 
    min_val = 10000
    max_val = 0
    # 구간합은 인덱스의 범위로 가기때문에 인덱스 값을 잘 계산해서
    for i in range(n-m+1):
        # 값을 비교하기위해 값을 저장할 수 있는 변수를 만들어요
        sum_thing = 0
        # 이구간을 거치는 동안 의 합을 구할거예요
        # 범위가 (i,i+m)이 되는 이유는
        # 위의 전체범위의 구간에서 아래 포문이 움직이니까
        # i값의 변화량에 따라 m의 값도 변화하게 만들어줘야해요
        # j가 가 돌때까지의 합을 구해서 최대 최솟 값을 구할거예요
        for j in range(i,i+m):
            sum_thing += ai[j]

        # sumthing과 같은 라인에 있어야 포문이 다 돌고난 이후의 값을
        # 얻어올 수 있어요
        if sum_thing <min_val:
            min_val = sum_thing

        if sum_thing > max_val:
            max_val = sum_thing
    # 최대 최솟값이 구해진 후에 합산값을 구해요 
    sum_val = max_val - min_val
    #조건에 맞게 답을 출력해줘요
    print(f"#{tc} {sum_val}")

