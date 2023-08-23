T = int(input())

for tc in range(1, T+1):
    case_num, numbers = input().split()
    numbers = int(numbers)
    arr = input().split()
    GNS = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = 0
    vacant_GNS = [0]*10

    for i in range(0, numbers):
        for j in range(10):
            if arr[i] == GNS[j]:
                vacant_GNS[j] += 1
    vacant = ''
    for i in range(10):
        vacant += (GNS[i] + " ")*vacant_GNS[i]

    print(f'#{tc} \n{vacant}')
