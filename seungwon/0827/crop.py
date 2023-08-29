# 농작물 수확

T = int(input())

for t in range(T):
    N = int(input())
    field = [list(map(int, input().split())) for i in range(N)]

    li_one, li_two, li_three, li_other = [], [], [], []

    for vl in range(N):
        for hl in range(N):
            one, two, three, other = 0, 0, 0, 0
            for col in range(N):
                for row in range(N - vl):
                    three += field[col][row + vl]

            li_three.append(three)

            for col in range(hl):
                for row in range(vl):
                    one += field[col][row]
            li_one.append(one)

            for col in range(N - hl):
                for row in range(vl):
                    two += field[col + hl][row]

            li_two.append(two)

    li_sigma = []
    zip_field = list(zip(li_three, li_one, li_two))
    for i in zip_field:
        tot = 0
        for j in i:
            tot += ((sum(i) / 3) - j) ** 2
            sigma = tot / 3
        li_sigma.append(sigma)

    sigma_index = li_sigma.index(min(li_sigma))

    answer = max(zip_field[sigma_index]) - min(zip_field[sigma_index])

    print("#" + str(t + 1), answer)