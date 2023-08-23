# 전기버스

# 종점에 도달할 때, 충전 최소 갯수
# 정류장 + 충전소 표시(-1)
# 버스 현재위치 + 이동거리 <= 최대 이동가능거리 and 충전기가 있으면 == 충전

# 경우 : 이동거리를 뒤에서부터 세기


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    k,n,m = map(int, input().split()) # k : 1번 충전 최대 이동 / n : 종점 정류장 / m : 충전기 설치 정류장 개수
    charge_idx = list(map(int, input().split()))

    # 정류장 + 충전소 표시(-1) <= 카운팅 배열
    c = [0] * (n+1)
    for i in range(len(charge_idx)):
        c[charge_idx[i]] -= 1
    print(c)


    cnt = 0 # 충전 횟수
    bus_now = 0 # 버스 현재 위치

    # 종점 도착할 때까지 계속
    while bus_now < n:
        if (bus_now + k) >= n:
            break
        for distance in range(k,0,-1): # distance : 버스이동거리 # 이동거리를 뒤에서부터 세는 이유는 불필요하게 충전안해도 되는데, 충전하는 경우 방지 
            if c[bus_now + distance] == -1: # 현재위치 + 이동거리 내에서 충전소 발견
                cnt += 1 # 충전하고
                bus_now = bus_now + distance # 버스 위치를 충전한 곳으로 초기화
                break

        else:
            cnt = 0 # 안되는 경우 0 출력
            break
       
    
    print(f'#{tc} {cnt}')




    

