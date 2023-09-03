# 특별한 정렬


def special(i,tmp):

    # 종료 조건(10개까지 출력)
    if i == 5:
        return # 마지막 값 찍고 이제 리턴 준비

    # 재귀 호출
    tmp.append(max(arr)) # tmp에 max값 추가 후 arr에서 제거
    arr.remove(max(arr))

    tmp.append(min(arr)) # tmp에 min값 추가 후 arr에서 제거
    arr.remove(min(arr))
    # print(tmp)
    # print(arr)
    special(i+1,tmp) # 반복
    
    # 재귀 탈출
    return tmp 


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    answer = special(0,[])
    print(f'#{tc}', *answer)

