#총 10 개의 테스트 케이스가 주어진다.
t = 10
# 테스트 케이스의 갯수만큼 반복해서 값을 구하겠다.
for tc in range(1,t+1):
    #각 테스트 케이스의 첫줄에는 건물의 개수 n 이 주어진다.
    n = int(input())
    # 그 다음줄에는 n개의 건물 높이가 주어진다.
    # n_list = 건물의 갯수 n_list[i] = 건물의 높이
    n_list = list(map(int,input().split()))
    # 그냥 크면 다 세어야 하니까 포문바깥에 둬서 전체 수를 다 비교할 수 있게
    cnt = 0
    #양옆의 두개가 빠져야하니까 범위는 2,n-2
    for i in range(2, n-2):
        # 높이를 나타내 줘야하니까 변수를 설정해서 각 위치에서의 높이값 비교.
        #n_list 의 인덱스 값을 받아오는 변수
        height = n_list[i]
        # 아래서 꼭대기까지 거꾸로 한칸씩 비교해보겠다.
        for j in range(height,-1,-1):
            # 조망권이 양옆으로 두칸씩 비교해봐야하므로 if 문 안에 4가지를 비교하는 것
            if j >n_list[i-2] and j>n_list[i-1] and j>n_list[i+1] and j > n_list[i+2]:
                cnt+=1


    #포문이 다 돌고 난 이후의 결과값을 출력해라
    print(f"#{tc} {cnt}")

