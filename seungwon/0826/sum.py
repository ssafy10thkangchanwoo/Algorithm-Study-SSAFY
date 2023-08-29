t =  int(input())
for tc in range(1,t+1):
    # n개의 정수, k 번째로 작은수
    n,k = map(int,input().split())
    Search_List = list(map(int, input().split()))
    Mouem_List = []

    for i in Search_List:
        if i not in Mouem_List:
            Mouem_List.append(i)

    for i in range(len(Mouem_List)):
        for j in range(i + 1, len(Mouem_List)):
            if Mouem_List[i] > Mouem_List[j]:
                Mouem_List[i], Mouem_List[j] = Mouem_List[j], Mouem_List[i]
    print(f"#{tc} {Mouem_List[k-1]}")

'''
3
7 5
1 3 5 6 4 4 6
10 5
1 3 4 2 3 7 1 6 9 2
10 5
4 7 5 5 1 5 4 4 3 3
'''
