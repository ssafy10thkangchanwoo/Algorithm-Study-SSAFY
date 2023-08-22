# 이진탐색
# 이진탐색으로 책을 살펴 먼저 펼치는 사람이 이김! 비기면 0 출력

# A와 B 따로 이진탐색 돌려야함. => 이진탐색 함수 작성, 
# A,B의 cnt 비교, cnt 적게한 사람이 승리
# 결과값 출력


def binarysearch(page,key):
    l = 1
    r = page
    cnt = 0
    while l <= r:
        middle = int((l+r)//2) # 가운데 찍을 때, cnt + 1
        cnt += 1
        
        if middle == key:
            return cnt
        
        elif middle > key:
            r = middle
            
        else:
            l = middle



import sys
sys.stdin = open('input1.txt','r')

T = int(input())
for tc in range(1, T+1):
    P,A,B = map(int,input().split())

    if binarysearch(P,A) > binarysearch(P,B):
        print(f'#{tc} B')
    elif binarysearch(P,A) < binarysearch(P,B):
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')




