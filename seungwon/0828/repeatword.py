#반복문자 지우기

t = int(input())
for tc in range(1, t + 1):
    # 문자열 받기
    word = input()
    t = -1
    w_ex = [0] * (len(word))
    t += 1
    w_ex[t] = 0

    #입력받은 word에서 비교한다.
    for i in word:
        # 만약 t인덱스랑 글자 값이 다르면 인덱스를 증가시켜주고 거기에 글자값을 넣어줘라
        if w_ex[t] != i:
            t +=1
            w_ex[t] = i
        # 같은게 나오면 인덱스 값을 빼버려라
        else:
            t -= 1
    print(f"#{tc} {t}")