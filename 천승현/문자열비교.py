T = int(input())
 
for tc in range(1, 1 + T):
    num1 = input()
    num2 = input()
    cnt = 0
    ans = 0

    for i in range(0, len(num2)):
        for j in range(0, len(num1)):
            cnt = 0
            for k in range(0, len(num1)):
                if i+k <= len(num2) and j+k <= len(num1):
                    if num1[i+k] == num2[j+k]:
                        cnt = cnt + 1
                        
                    if cnt == len(num1):
                        ans = 1
    
    print(f"#{tc} {ans}")
            
            
    
