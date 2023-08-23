T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input()
    card_list = [0] * 10
    for i in cards:
        card_list[int(i)] = card_list[int(i)] + 1

    ans = 0
    max_counts = 0
    for i in range(0, 10):
        if max_counts <= card_list[i]:
            max_counts = card_list[i]
            ans = i
    
    print(f"#{tc} {ans} {max_counts}")