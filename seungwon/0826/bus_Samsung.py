t= int(input())
for tc in range(1,t+1):
    # 하나의 정수
    n = int(input())
    # 버스 정류장의 배열이 5000개 까지 주어진다.
    bus_station = [0]*5001
    # ai의 정류장과 bi 의 정류장을 나누어서 받아줄 수 있도록
    for i in range(n):
        a,b = list(map(int, input().split()))
        # a와 b사이를 지나는 버스 정거장을 지나는 버스 정류장 수
        for j in range(a,b+1) :
            # 버스 정거장 번호 위치에 지나 다니는 버스의 수가
            # 카운트 되어 나타난다.
            bus_station[j] += 1

    # p 개의 정류장 수를 알 수 있도록 해주는 정수 입력값
    p = int(input())
    # 순서대로 숫자들이 받아질 변수 만들어주기
    result = ""
    # 정수 범위의 정류장 인덱스에서 몇개의 버스가 지나가는지 확인
    for j in range(p):
        c = int(input())
        result += str(bus_station[c]) + " "

    print(f"#{tc} {result}")


'''
1
2
1 3
2 5
5
1
2
3
4
5
    
'''
