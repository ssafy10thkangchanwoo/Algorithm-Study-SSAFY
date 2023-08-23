# 현재 내 풀이(못품)
def winner(pA, pB):
    if pA > pB:
        return 'B'
    elif pA < pB:
        return 'A'
    else:
        return 0
T = int(input())

for tc in range(1, T+1):
    # 페이지 수, A목표 페이지, B 목표 페이지 
    page, A, B = map(int,input().split())
    # 턴 수
    count_A = 0
    count_B = 0
    # A의 제일 왼쪽/오른쪽
    page_L_A = 1
    page_R_A = page
    page_L_B = 1
    page_R_B = page
    # 얼마나 찾아야 하는지 모르므로 while
    # while A != page: 왜 이건 안될까요?
    while page_L_A<=page_R_A:
        count_A += 1
        # 페이지 중앙보다 찾을 A의 페이지 값이 클 경우 중앙페이지부터 재탐색
        if A > int((page_L_A+page_R_A)/2):
            page_L_A = int((page_L_A+page_R_A)/2)
        else:
            page_R_A = int((page_L_A+page_R_A)/2)

    while page_L_B<=page_R_B:
        count_B += 1
        # 페이지 중앙보다 찾을 B의 페이지 값이 클 경우 중앙페이지부터 재탐색
        if B > int((page_L_B+page_R_B)/2):
            page_L_B = int((page_L_B+page_R_B)/2)
        else:
            page_R_B = int((page_L_B+page_R_B)/2)

    print(f'#{tc} {winner(count_A,count_B)}')

# 과거의 풀이...
# T = int(input())

# for tc in range(1, T+1):
#     p, a, b = map(int,(input().split()))
#     count_a = 0
#     count_b = 0
#     start_p = 1
#     end_p = p
#     winner = 0
#     while start_p <= end_p:
#         if (start_p+end_p)//2 == a:
#             count_a += 1
#             break
#         elif (start_p+end_p)//2 > a:
#             count_a += 1
#             end_p = (start_p+end_p)//2
#         else: 
#             count_a += 1
#             start_p = (start_p+end_p)//2


#     start_p = 1
#     end_p = p
#     while start_p <= end_p:
#         if (start_p+end_p)//2 == b:
#             count_b += 1
#             break
#         elif (start_p+end_p)//2 > b:
#             count_b += 1
#             end_p = (start_p+end_p)//2
#         else: 
#             count_b += 1
#             start_p = (start_p+end_p)//2
    
#     if count_a > count_b:
#         winner = "B"
#     elif count_a < count_b:
#         winner = "A"
#     else: 
#         winner = "0"

#     print(f'#{tc} {winner}')