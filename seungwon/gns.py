arr = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

def sort_word(init):
    for j in range(len(arr)):
        for i in range(n):
            if init[i] == arr[j]:
                sort_list[j] += 1
    return  sort_list

t = int(input())
for _ in range(1,t+1):
    tc,n= input().split()
    n = int(n)
    # 리스트로 만들어준다.
    word = input().split()
    # 그 인자 값을 카운팅해주기 위한..? 배열 생성하기
    sort_list = [0] * (n+1)


    result = sort_word(word)
    print(result)