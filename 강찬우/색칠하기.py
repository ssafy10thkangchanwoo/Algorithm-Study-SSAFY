T = int(input())

for tc in range(1, T+1):
    color_count = int(input())
    matrix = [[0]*10 for _ in range(10)]
    
    for _ in range(color_count):
        i, j, k, l, c = map(int, input().split())
        for a_i in range(i, k+1):
            for a_j in range(j, l+1):
                if matrix[a_i][a_j] == 0:
                    matrix[a_i][a_j] = c
                elif matrix[a_i][a_j] == c:
                    matrix[a_i][a_j] = c
                else:
                    matrix[a_i][a_j] = 3
    
    purple = 0 
    for row in matrix:
        for cell in row:
            if cell == 3:
                purple += 1
   
    print(f'#{tc} {purple}')