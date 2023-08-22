# 연속적인 1의 개수 세기

arr = [0,1,1,0,0,1,0,1,1,1]

cnt = 0 # 연속적인 1의 개수 세기
answer = 0 # 연속적인 1의 최대갯수
for i in range(len(arr)):
    if arr[i] == 1:
        cnt += 1
        answer = cnt if answer < cnt else answer
    else:
         cnt = 0

print(cnt)