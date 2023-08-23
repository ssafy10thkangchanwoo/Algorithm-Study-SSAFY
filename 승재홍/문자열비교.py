
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    target = input()
    text = input()

    cnt = 0
    for i in range(len(text)):
        
        for j in range(len(target)):
            if text[i] == target[j]:
                
                for k in range(len(target)):

                    if text[i:i+k] == target[j:j+k]:
                        cnt = 1
                    else:
                        cnt = 0
                            
    
    print(f'#{tc} {cnt}')
                        