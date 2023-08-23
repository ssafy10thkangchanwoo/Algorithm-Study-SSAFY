max_v = 0
for i in range(0, N - M + 1):
    sum_num = 0
    for j in range(0, M):
        sum_num = sum_num + text[i+j]
    if max_v < sum_num:
            max_v = sum_num