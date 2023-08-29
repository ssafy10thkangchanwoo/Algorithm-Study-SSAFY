# 나중에 생성된 리스트의 값과 비교하여 답을 도출할 딕셔너리
code_search = {"0001101": "0",
              "0011001": "1",
              "0010011": "2",
              "0111101": "3",
              "0100011": "4",
              "0110001": "5",
              "0101111": "6",
              "0111011": "7",
              "0110111": "8",
              "0001011": "9"
              }

t = int(input())
for tc in range(1,t+1):
    #n은 배열의 세로크기, m은 배열의 가로크기
    n,m = map(int,input().split())
    # 지정된 가로 길이 까지만 받아야하는데
    # 가로 길이랑 다르게 나타낸 것이 테케에서 보임
    pass_board = [input()[:m] for _ in range(n)]
    print(pass_board)
    start_moeum = ""
    # pass보드에서 암호를 찾기.
    for r in range(n):
        for c in range(m-1,-1,-1):
            # 뒤에서 0이 아닌 숫자를 찾아라
            if pass_board[r][c] !="0":
                # 코드 모음을 보드에서 찾아 앞에서부터 c까지 담아라
                start_moeum += pass_board[r][0:c+1]
                break
    # print(start_moeum)
    # 암호를 찾아왔으니 그 숫자를 다시 2진수로 변환하기
    num = ""
    for i in start_moeum:
        change = int(i,16)
        for j in range(3,-1,-1):
            num += "1" if change &(1<<j) else "0"

    # 변환했으니까 7자리씩 자르고 비교하기
    slice_num = []
    for i in range(0,len(num),7):
        cut_num = num[i:i+7]
        slice_num.append(cut_num)
    print(slice_num)
    #잘린 기준을 구하는게 안되는 모습을 보임...
    # 배율을 비교해야하는데 그게 안됨..
    # 7개씩 자르고 그것을 확인된 숫자에 추가...
    check_num = []
    for i in slice_num:
        for j in range(len(code_search)):
            if i == code_search[j]:
                check_num.append(j)

    result = check_num
    # 결과 값의 홀수자리 숫자의 합
    hourse = 0
    # 결과 값의 짝수자리 숫자의 합
    bina = 0
    # 짝수와 홀수를 분리하고 검증코드를 빼서 결과 값을 구해줘라
    for i in range(len(result)-1):
        if i % 2 == 0:
            hourse += result[i]
        else:
            bina += result[i]
    # 제시하는 조건처럼 홀수의 3배와 짝수, 검증코드를 더해준다
    sum_value = (hourse * 3) + (bina) + result[-1]
    # 더해진 값이 10으로 나누었을때 0인지 확인
    if sum_value % 10 == 0:
        #맞다면 홀수, 짝수 총합 프린트
        print(f"#{tc} {hourse + bina + result[-1]}")
    # 나누어 떨어지지 않는것
    else:
        print(f"#{tc} {0}")





"""
1
16 26
00000000000000000000000000
00000000000000000000000000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
00000000000000000000000000
00000000000000000000000000

"""