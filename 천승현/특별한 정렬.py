T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    text = list(map(int, input().split()))
    list1 = []

    for i in range(N):
        for j in range(0, N-i-1):
            if text[j] > text[j+1]:
                text[j], text[j+1] = text[j+1], text[j]

    while text:
        list1.append(max(text))
        text.pop()
        list1.append(min(text))
        text.pop(0)
    print(f"#{tc}" , end = " ")
    for i in list1:
        print(i, end = " ")
    print()