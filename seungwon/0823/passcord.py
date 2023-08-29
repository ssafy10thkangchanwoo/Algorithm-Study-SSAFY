maching = {"0001101" : 0,"0011001":1, "0010011":2,
            "0111101" : 3 , "0100011":4, "0110001":5,
            "0101111":6, "0111011":7, "0110111":8,"0001011":9 }
# 딕셔너리를 탐ㅁ색해서 그 자리에 있으면 밸류값을 가져와라
def maching_result(init):
    for j in maching:
        for i in range(len(mouem)):
            if init[i] == j:
                init[i] = maching[j]
    return init


t = int(input())
for tc in range(1,t+1):
    # 배열의 세로와 배열의 가로를 나누어 받는다
    n,m = map(int, input().split())
    # 암호의 배열을 입력받는다
    pass_cord = [list(map(int,input())) for _ in range(n)]
    #행열 탐색을 돌아라
    for r in range(n):
        for c in range(m-1 ,-1,-1):
            # 인덱스 위치를 찾아라
            if pass_cord[r][c] ==1:
                sr,sc = r,c
                break
    # 슬라이싱을 해서 그것을 변수에 담아주고
    pass_list = pass_cord[sr][sc-55:sc+1]
    # 리스트로 되어있으니 문자열로 변환시켜주어야 다음에 실행이 가능
    joy = ""
    for i in range(len(pass_list)):
        c =  pass_list[i]
        # 인덱스 값이 정수로 받아졌으니 c를 문자열로 변환
        joy += str(c)


    l_pass = len(pass_list)
    # 7개씩 슬라이싱한 것이 들어갈 리스트
    mouem = []
    for i in range(0,l_pass,7):
        pass_word =joy[i:i+7]
        mouem.append(pass_word)
    # 정의 함수를 돌고 나온 결과 값
    result = maching_result(mouem)
    # 홀수인데 인덱스가 아닌 그냥 그 자리 홀수
    hourse = 0
    # 인덱스가 아닌 그자리 짝수
    bina = 0
    # 짝수와 홀수를 분리해서 결과 값을 구해줘라
    for i in range(len(result)):
        if i % 2 ==0:
            hourse += result[i]
        else:
            bina +=result[i]
    # 최종 결과를 위해 문제에서 요구하는 조건을 맞추어주어라
    sum_value = (hourse*3)+(bina)
    # 나머지가 0 이면 10으로 나누어떨어지는것
    if sum_value%10 == 0 :
        print(f"#{tc} {hourse+bina}")
    # 나누어 떨어지지 않는것
    else :
        print(f"#{tc} {0}")

