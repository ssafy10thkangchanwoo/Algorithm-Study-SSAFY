# 함수에 이동가능한 거리 k와 종점 좌표 n을 표시
def moving_point(k,n):
    #마지막으로 충전한 곳에서 멀어진 정류장 세기
    last = 0
    # 버스가 이동가능한 거리
    next = k
    # 충전한 횟수 표시
    charge = 0
    # 이동 가능한 거리가 종점보다 작을떄까지 진행시켜
    while next <n:
        #반복할건데 언제까지냐면?
        while bus_stop[next] ==0:
            #충전기가 없으면 나올때까지 되돌아가라?
            next -=1
            if next ==last


t= int(input())
for tc in range(1,t+1):
    # k - 이동할 수 있는 정류장의 수,n -> 종점 m=> 중전기가 설치된 정류장 번호
    k,n,m = map(int,input().split())
    # 충전기가 설치된 번호.
    charge_point = list(map(int,input().split()))
    # 버스 정류장을 표현해줄 인접배열
    bus_stop = [0] * n+1
    #일단 진행시켜


    #전기 충전소가 있는 정거장표시
    for i in charge_point:
        # 인덱스 번호가 있는 곳에 버스 충전소가 설치되어있음
        bus_stop[i] = 1

